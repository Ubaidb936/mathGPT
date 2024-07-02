import pandas as pd
import json
import os
import csv
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import SystemMessage
from langchain_openai import ChatOpenAI
from tqdm import tqdm

#path to the logs folder
log_folder_path = os.path.join(os.getcwd(), 'logs')

# List all files in the logs folder
files = os.listdir(log_folder_path)

json_files = [file for file in files if file.endswith('.json') and file[0].isdigit()]

# Hold json data returned by student_llm
global data

# Reads the responses of the student llm
if len(json_files) > 0:
    json_file = json_files[0]
    json_file_path = os.path.join(log_folder_path, json_file)    
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    # os.remove(json_file_path)
else:
    raise ValueError("Please call the student_llm first")  



student_llm_results = data["samples"]



GRADE_LLM_PROMPT = """
###Task Description:
An instruction (which includes a mathematical problem involving addition, subtraction, multiplication, or division of two numbers), a response to evaluate, a reference answer, and a score rubric representing the evaluation criteria are given.
1. Write a detailed feedback that assesses the quality of the response strictly based on the given score rubric and mathematical knowledge, not evaluating in general.
2. After writing a feedback, write either "Correct" or "Incorrect" based on the score rubric.
3. The output format should look as follows: "Feedback: {{write a feedback for criteria}} [RESULT] {{Correct/Incorrect}}"
4. Please do not generate any other opening, closing, and explanations. Be sure to include [RESULT] in your output.

###The instruction to evaluate:
{instruction}

###Response to evaluate:
{response}

###Reference Answer:
{reference_answer}

###Score Rubrics:
[Is the response correct, accurate, and factual based on the reference answer and mathematical knowledge?]
Score: The response is either "Correct" or "Incorrect".

###Feedback:
"""
grade_llm_prompt_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="You are a fair evaluator language model."),
        HumanMessagePromptTemplate.from_template(GRADE_LLM_PROMPT),
    ]
)
grade_llm = ChatOpenAI(model="gpt-4-turbo", temperature=0)






def grader_llm(student_llm_results, grade_llm_prompt_template, grade_llm):
    evaluations = []
    
    for sample in tqdm(student_llm_results, desc="Grading responses"):
        question = sample["input"]
        response = sample["output"]["choices"][0]["message"]["content"]
        reference_answer = sample["target"]
    
        eval_prompt = grade_llm_prompt_template.format_messages(
            instruction=question,
            response=response,
            reference_answer=reference_answer,
        )
        try:
            eval_result = grade_llm.invoke(eval_prompt)
            feedback, score = [item.strip() for item in eval_result.content.split("[RESULT]")]
            evaluations.append(
                {
                    "input": question,
                    "target": reference_answer,
                    "student_llm_answer": response,
                    "grade_llm_score": score,
                    "grade_llm_feedback": feedback,
                }
            )
            df = pd.DataFrame.from_dict(evaluations)
            df.to_csv("logs/scores.csv", index=False)
        except Exception as e:
            print(f"Error processing sample: {e}")
            continue
        
    
grader_llm(student_llm_results, grade_llm_prompt_template, grade_llm)
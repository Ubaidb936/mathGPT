# Flow for the TaleCrafter Chatbot

![Cute kitten](https://github.com/Ubaidb936/TaleCrafter/blob/main/story_developing_pipeline.png)


# Agent 1

```python
GENERATION_PROMPT = """
A story is provided below. Your task is to read through the story and generate a single idea that will help enhance and develop the story further. 
This idea should provide insight into what additional elements or directions can be added to create a more compelling and complete narrative.

Provide your response in the following format:

Output:::
Idea: (Idea to develop a good story)

Now, here is the story.

Story: {story}

Output:::
"""

GENERATION_PROMPT = ChatPromptTemplate.from_template(GENERATION_PROMPT)
prompt_generating_llm_agent = jobDescription_summary_generation_prompt | chat_model
```

# Agent 2
```python
INPUT_INCORPORATING_PROMPT = """
You are provided with a story and a user input. 
Your task is to incorporate the user input into the story to enhance and develop it further, creating a cohesive and compelling narrative.

Provide your response in the following format:

Output:::
Story: (Story with user input incorporated)

Now, here is the story and user input.

Story: {story}
User Input: {input}

Output:::
"""

INPUT_INCORPORATING_PROMPT = ChatPromptTemplate.from_template(INPUT_INCORPORATING_PROMPT)
input_incorporating_llm_agent = INPUT_INCORPORATING_PROMPT | chat_model
```

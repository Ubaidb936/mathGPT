# Math Evaluations

![Cute kitten](https://github.com/Ubaidb936/mathGPT/blob/main/arch.png)


### Running the project on your local system:

1. clone the repository: `git clone https://github.com/Ubaidb936/mathGPT.git`
2. Cd into chatWithDocs:  `cd mathGPT`
3. create a new virtual env using this command `python3 -m venv myenv` for linux/mac and activate it using `source myenv/bin/activate`
4. run `pip install -r requirements.txt` to install dependencies.
5. run `export OPENAI_API_KEY= {your_key}`(required)
6. run `python question_gereration.py`. This command generates Arithmetic questions and stores them in logs folder.
7. run `inspect eval student_llm.py --model openai/gpt-4`. Uses Inspect AI solver(only generate() used) to solve the questions and JSON file is stored in the logs file.
8. run `python grader_llm.py`. this commands grades the student llm answers and stores a scores.csv file in logs folder.
   
### Checkout the graded sample:
[Huggingface_dataset_link](https://huggingface.co/datasets/Ubaidbhat/evaluations?row=1)


### Improvements:
1. Use change of thought to evaluate the approach of the student LLM as well.
2. Include other math problems as well.

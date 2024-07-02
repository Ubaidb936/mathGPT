from inspect_ai import Task, task
import pandas as pd
import os
from inspect_ai.dataset import csv_dataset
from inspect_ai.solver import (               
 generate 
) 

if os.path.exists("logs/arithematic_questions.csv"):
  arithematic_dataset = csv_dataset("logs/arithematic_questions.csv")
else:
  raise FileNotFoundError(f"Please generate arithematic question first...")
                                          
@task
def student_llm():
    return Task(
        dataset=arithematic_dataset[:10],
        plan=[
          generate()
        ]
    )
import pandas as pd
import random
import operator
from tqdm import tqdm

import os

# Removes all the previous logs
log_folder_path = os.path.join(os.getcwd(), 'logs')
files = os.listdir(log_folder_path)
for file in files:
    file_path = os.path.join(log_folder_path, file) 
    os.remove(file_path)



# Generates arithmetic problems
def generate_operations():
    operations = []
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    
    for _ in tqdm(range(50), desc="Generating arithematic questions"):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        op = random.choice(list(ops.keys()))
        if op == '/' and num2 == 0:
            num2 = random.randint(1, 100)  # Ensure no division by zero
        
        answer = ops[op](num1, num2)
        operation_dict = {
            'input': f"{num1} {op} {num2}",
            'target': round(answer, 2)
        }
        operations.append(operation_dict)
    
    return operations

# Generate operations and save to CSV
operation_list = generate_operations()

generated_questions = pd.DataFrame.from_dict(operation_list)
generated_questions.to_csv("logs/arithematic_questions.csv", index=False)

"""
File: weekday_calculator.py
Authors: Weijian(David)
Date: 2025-01-25
Description: 
Use Deepseek to return the logic statement, and create the truth table
Puzzle website:
https://philosophy.hku.hk/think/logic/knights.php
"""
import re
from openai import OpenAI


def deepseek(user_input):
    """
    function name: deepseek
    input: user_input-->str
    output: return message-->str
    Call deepseek API
    """

    client = OpenAI(api_key="sk-48b305a73fe14ff2bb9f06f05c78f2ae", base_url="https://api.deepseek.com")
    prompt = """
    1. 转化成只使用or and not的公式
    2. not前面一定要加() 
    3. or and not一定要用小写
    4. 必须只有1行
    5. 不要使用xor!
    6. 使用单字母而不是名字
    7. 要考虑所有人说的是真话或假话的情况

    请注意只输出结果本身，不要输出任何其他东西，多一次词也不要!!!!
    ------------------
    output举例1
    ((Z and (not M)) and ((not Z) or M))
    output举例2
    ((A and (not R)) and (R and (not B)) and (B and (A or B)))
    """
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content":prompt },
            {"role": "user", "content": user_input},
        ],
        stream=False
    )
    infor = response.choices[0].message.content
    return infor

def truth_table(expression_str, variable_l):
    """
    input: expression, variable_list
    output: a dict with truth table
    print the truth table
    """
    num_variables = len(variable_l)
    num_rows = 2 ** num_variables  #row of the truth table
    truth_table_data = []  # List to hold each row of the truth table

    for i in range(num_rows):
        row = []
        for j in range(num_variables):
            row.append(bool((i // (2 ** (num_variables - j - 1))) & 1))
        # 动态赋值，输出每个变量的值
        for idx, var_name in enumerate(variable_l):
            globals()[var_name] = row[idx]
        # 判断条件
        expression = eval(expression_str)
        truth_table_row = ", ".join(f"{var_name}={globals()[var_name]}" for var_name in variable_l)
        print(f"{truth_table_row}, the statement of S = {expression}")
        row.append(expression)
        truth_table_data.append(row)
    return truth_table_data


def main():
    """
    input: expression, variable_list
    output:none
    """
    input_user=input("please fillin the puzzle: \n")
    formula = deepseek(input_user)
    variables = re.findall(r'\b[A-Z]\b', formula)
    unique_variables = list(dict.fromkeys(variables))
    variable_num = len(unique_variables)
    print(f"The formular(S) is {formula}")
    print(f"There are {variable_num} objects, and they are {unique_variables}.")
    #output the truth_table and result
    truth_table_data = truth_table(formula, unique_variables)
    print("----------------------------------")
    print(truth_table_data)


if __name__ == "__main__":
    main()

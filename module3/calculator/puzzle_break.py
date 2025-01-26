"""
File: weekday_calculator.py
Authors: Weijian(David)
Date: 2025-01-25
Description: 
Use Deepseek to return the logic statement, and create the truth table
"""
import re
from openai import OpenAI
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

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
    6. 使用字母而不是名字

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
        print(truth_table_row,f", the statement of S = {expression}")
        row.append(expression)
        values = dict(zip(variable_l, row))
    return values

@app.route('/')
def index():
    # HTML content embedded directly into the Python code
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Logic Puzzle Calculator</title>
        <script>
            async function calculate() {
                const userInput = document.getElementById("userInput").value;
                const response = await fetch('/calculator', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ input: userInput })
                });
                const result = await response.json();
                const output = result.output.map(row => {
                    return Object.entries(row).map(([key, value]) => `${key}=${value}`).join(', ');
                }).join('\\n');
                document.getElementById("result").innerText = output;
            }
        </script>
    </head>
    <body>
        <h1>Logic Puzzle Calculator</h1>
        <label for="userInput">Enter your logical formula:</label><br>
        <textarea id="userInput" name="userInput" rows="8" cols="50"></textarea><br>
        <button onclick="calculate()">Submit</button>
        <h2>Result:</h2>
        <pre id="result"></pre>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route('/calculator', methods=['POST'])
def calculate():
    """
    input: expression, variable_list
    output:none
    """
    data = request.get_json()
    user_input = data.get('input')

    # Call deepseek to get the formula
    formula = deepseek(user_input)

    # Find the unique variables in the formula
    variables = re.findall(r'\b[A-Z]\b', formula)
    unique_variables = list(dict.fromkeys(variables))

    # Generate the truth table
    truth_table_result = truth_table(formula, unique_variables)

    # Return the result as a JSON response
    return jsonify({"output": truth_table_result})


if __name__ == '__main__':
    app.run(debug=True)

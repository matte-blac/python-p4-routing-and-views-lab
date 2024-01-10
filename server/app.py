#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/math/<int:num1>/<operation>/<int:num2>', methods=['GET'])
def math(num1, operation, num2):
    # perform the appropriate operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid Operation!'
    
    return f'{result}'

@app.route('/print/<string>', methods=['GET'])
def print_string(string):
    # print the string in the console
    print(string)
    # display the string in the web browser
    return string

@app.route('/count/<int:n>', methods=['GET'])
def count(n):
    # create a string with all numbers in the range
    numbers = '\n'.join(str(i) for i in range(n))

    # add a newline at the end
    numbers += '\n'

    return numbers

if __name__ == '__main__':
    app.run(port=5555, debug=True)

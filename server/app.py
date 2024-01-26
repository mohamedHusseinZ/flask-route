from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>zakis trial</h1>'

@app.route('/print/<string:parameter>')
def print_parameter(parameter):
    return f'<h2>print for {parameter}</h2>'
@app.route('/count/<int:parameter>')
def count(parameter):
    result = '\n'.join(str(a) for a in range(parameter + 1))
    return f'<pre>{result}</pre>'



@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "/":
            result = num1 / num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "%":
            result = num1 % num2
        else:
            return 'Invalid operation'
        
        return f'Result: {result}'
    except ValueError:
        return 'Invalid input, please provide valid numbers.'

if __name__ == '__main__':
    app.run(port=5555, debug=True)



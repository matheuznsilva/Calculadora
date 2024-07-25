from flask import Flask, request, jsonify, send_from_directory
import math

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data['expression']
    try:
        result = eval(expression)
    except Exception as e:
        result = str(e)
    return jsonify(result=result)

@app.route('/sqrt', methods=['POST'])
def sqrt():
    data = request.get_json()
    expression = data['expression']
    try:
        result = math.sqrt(float(expression))
    except Exception as e:
        result = str(e)
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)

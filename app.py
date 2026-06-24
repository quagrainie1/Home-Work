from flask import Flask, request, jsonify

app = Flask(__name__)

# basic math functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


@app.route('/add')
def route_add():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = add(a, b)
        return jsonify({
            "a": a,
            "b": b,
            "operation": "addition",
            "result": result
        }), 200
    except TypeError:
        return jsonify({"error": "please provide both a and b"}), 400
    except ValueError:
        return jsonify({"error": "a and b must be numbers"}), 400


@app.route('/subtract')
def route_subtract():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = subtract(a, b)
        return jsonify({
            "a": a,
            "b": b,
            "operation": "subtraction",
            "result": result
        }), 200
    except TypeError:
        return jsonify({"error": "please provide both a and b"}), 400
    except ValueError:
        return jsonify({"error": "a and b must be numbers"}), 400


@app.route('/multiply')
def route_multiply():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = multiply(a, b)
        return jsonify({
            "a": a,
            "b": b,
            "operation": "multiplication",
            "result": result
        }), 200
    except TypeError:
        return jsonify({"error": "please provide both a and b"}), 400
    except ValueError:
        return jsonify({"error": "a and b must be numbers"}), 400


@app.route('/divide')
def route_divide():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        # cant divide by zero
        if b == 0:
            return jsonify({"error": "cannot divide by zero"}), 400
        result = divide(a, b)
        return jsonify({
            "a": a,
            "b": b,
            "operation": "division",
            "result": result
        }), 200
    except TypeError:
        return jsonify({"error": "please provide both a and b"}), 400
    except ValueError:
        return jsonify({"error": "a and b must be numbers"}), 400


if __name__ == '__main__':
    app.run(port=5000, debug=True)

from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/soma', methods=['POST'])
def soma():
    """
    Soma dois números
    ---
    parameters:
      - in: body
        name: payload
        required: true
        schema:
          type: object
          properties:
            a:
              type: number
            b:
              type: number
    responses:
      200:
        description: A soma dos números
    """
    data = request.get_json()
    return jsonify({'resultado': data['a'] + data['b']})

@app.route('/multiplicacao', methods=['POST'])
def multiplicacao():
    """
    Multiplica dois números
    ---
    parameters:
      - in: body
        name: payload
        required: true
        schema:
          type: object
          properties:
            a:
              type: number
            b:
              type: number
    responses:
      200:
        description: O produto dos números
    """
    data = request.get_json()
    return jsonify({'resultado': data['a'] * data['b']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

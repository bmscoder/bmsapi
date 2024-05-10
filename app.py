import os
from numpy import matmul
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
    return "BMS – #2 Basic Matrix System"

@app.route('/multiplication', methods=['GET'])
def api():
    # Get the message from the query parameter
    matrix_A = request.args.get('A')
    matrix_B = request.args.get('B')

    try:
        # Check if the message exists
        if matrix_A and matrix_B:
            A = json.loads(matrix_A)
            B = json.loads(matrix_B)
            if len(A[0]) == len(B):
                res = matmul(A, B).tolist()
                # Create a response dictionary
                response = {'status': 'ok', 'A': str(A), 'B': str(B), 'result': str(res)}
                return jsonify(response)
            else:
                return jsonify({'error': 'A matritsa ustunlari bilan B matritsa satrlari soni teng emas!'})
        else:
            return jsonify({'error': 'Matrix parameters is missing'})
    except Exception as e:
        return jsonify({'error': "Something went wrong: " + str(e)})

if __name__ == '__main__':
    app.run(debug=False, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4445)))

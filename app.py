from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/get-env', methods=['GET'])
def get_env():
    value = os.getenv('MY_VARIABLE', 'Not set')
    return jsonify({"MY_VARIABLE": value})

@app.route('/set-env', methods=['POST'])
def set_env():
    data = request.json
    if 'value' in data:
        os.environ['MY_VARIABLE'] = data['value']
        print(f"MY_VARIABLE set to: {data['value']}")
        return jsonify({"message": "Variable set"}), 200
    else:
        return jsonify({"error": "No value provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)

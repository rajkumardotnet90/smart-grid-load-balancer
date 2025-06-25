
from flask import Flask, request
import requests

app = Flask(__name__)

LOAD_BALANCER_URL = "http://load_balancer_service:6000/route"

@app.route('/charge', methods=['POST'])
def handle_charge():
    data = request.get_json()
    response = requests.post(LOAD_BALANCER_URL, json=data)
    return response.text, response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

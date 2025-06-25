
from flask import Flask, request
import requests

app = Flask(__name__)
SUBSTATIONS = ["substation1:8000", "substation2:8000", "substation3:8000"]

def get_load(substation):
    try:
        resp = requests.get(f"http://{substation}/metrics")
        for line in resp.text.splitlines():
            if "substation_load" in line:
                return float(line.split()[-1])
    except Exception:
        return float('inf')
    return float('inf')

@app.route('/route', methods=['POST'])
def route_charge():
    loads = {s: get_load(s) for s in SUBSTATIONS}
    target = min(loads, key=loads.get)
    try:
        r = requests.post(f"http://{target}/charge", json=request.get_json())
        return r.text, r.status_code
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)

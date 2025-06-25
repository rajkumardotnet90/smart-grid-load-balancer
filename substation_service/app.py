
from flask import Flask
from prometheus_client import start_http_server, Gauge
import threading, time

app = Flask(__name__)
current_load = 0
load_metric = Gauge('substation_load', 'Current charging load')

@app.route('/charge', methods=['POST'])
def charge():
    global current_load
    current_load += 1
    load_metric.set(current_load)
    time.sleep(5)
    current_load -= 1
    load_metric.set(current_load)
    return "Charging complete", 200

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)

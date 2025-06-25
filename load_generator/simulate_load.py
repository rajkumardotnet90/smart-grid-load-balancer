
import requests
import threading
import time

def send_request():
    try:
        requests.post('http://localhost:5001/charge', json={"vehicle_id": "EV-001"})
    except Exception as e:
        print("Error:", e)

threads = []
for _ in range(30):  # simulate 30 EVs
    t = threading.Thread(target=send_request)
    threads.append(t)
    t.start()
    time.sleep(0.1)

for t in threads:
    t.join()
print("Rush hour simulation complete.")

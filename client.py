# client.py

import requests

out_data = {"name": "Michael Larbie",
            "hdl_value": 150}
r = requests.get("http://127.0.0.1:500/info", json=out_data)
print(r.status_code)
print(r.text)

out_data = {"a": 10,
            "b": 50}
r = requests.get("http://127.0.0.1:500/info", json=out_data)
print(r.status_code)
print(r.text)

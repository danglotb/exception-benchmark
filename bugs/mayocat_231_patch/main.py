#!/bin/python

import requests

s = requests.Session()

r = s.get("http://172.17.0.1:8080")
print(r.status_code)
r = s.post("http://172.17.0.1:8080/cart/add", {"product": "product"})
print(r.status_code)
r = s.get("http://172.17.0.1:8080")
print(r.status_code)
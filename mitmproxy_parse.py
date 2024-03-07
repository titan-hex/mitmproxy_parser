#!/usr/bin/env python3
import sys
from mitmproxy.io import FlowReader

if len(sys.argv) != 2:
  print(f"Usage: {sys.argv[0]} <flows.mitm>")
  exit()

filename = sys.argv[1]
with open(filename, 'rb') as fp:
  reader = FlowReader(fp)
  for flow in reader.stream():
    print(f"method: {flow.request.method}\nurl: {flow.request.url}")
    print("request headers:")
    for k,v in dict(flow.request.headers).items():
      print(f" {k}: {v}")

    print(f"request data:\n{flow.request.text}")
    
    try:
      print(f"response code: {flow.response.status_code}")
      print("response headers:")
      for k,v in dict(flow.response.headers).items():
        print(f" {k}: {v}")

      print(f"response data:\n{flow.response.text}")
    except:
      pass

    print("\n\n")

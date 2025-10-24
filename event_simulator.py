import json, time, subprocess, os
from lambda_function import lambda_handler

print("Simulating network event: route table inconsistency...")
# show initial state
with open("mock_vpc_routes.json") as f:
    data = json.load(f)
print("Initial route tables:")
print(json.dumps(data, indent=2))
time.sleep(1)
print("\nTriggering mitigation handler...")
result = lambda_handler()
print("\nResult:")
print(result)
time.sleep(1)
print("\nPost-run route tables:")
with open("mock_vpc_routes.json") as f:
    data = json.load(f)
print(json.dumps(data, indent=2))

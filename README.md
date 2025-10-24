# Automated Network Event Mitigation (Mock)

This is a simplified, local mock of an AWS Lambda-based network event mitigation system.
It detects simple "blackhole/unreachable" routes in a mock VPC route table JSON and "remediates" them.

## Files
- `lambda_function.py` : Main handler (callable as a Lambda or local script).
- `mock_vpc_routes.json` : Mock route table data.
- `event_simulator.py` : Script to run a simulation of detection and remediation.
- `README.md` : This file.

## How to run locally
1. Ensure you have Python 3.8+ installed.
2. Run: `python event_simulator.py`
3. You will see the initial route tables, detection, remediation, and final state printed.

## Notes
- This is a simplified demo (no real AWS APIs or credentials).
- The remediation logic is intentionally basic to demonstrate the pattern for auto-remediation.
- <img width="730" height="632" alt="1" src="https://github.com/user-attachments/assets/7c8a32f4-e46e-40d3-afa3-73988b0288db" />
<img width="1351" height="640" alt="2" src="https://github.com/user-attachments/assets/7aad579c-0b52-4129-b27d-fe4c97eee003" />
<img width="543" height="331" alt="3" src="https://github.com/user-attachments/assets/b742563d-f306-463e-aaf0-5f9943f78966" />


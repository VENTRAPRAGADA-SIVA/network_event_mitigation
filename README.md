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

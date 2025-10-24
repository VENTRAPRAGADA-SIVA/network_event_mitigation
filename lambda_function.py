import json
import logging
import time

logger = logging.getLogger('net-mitigation')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
logger.addHandler(handler)

ROUTE_FILE = "mock_vpc_routes.json"

def load_routes():
    with open(ROUTE_FILE) as f:
        return json.load(f)

def detect_inconsistencies(routes):
    # Simple rule: any route with 'destination_cidr' overlapping a 'blackhole' -> inconsistency
    inconsistencies = []
    for rt in routes.get("route_tables", []):
        for r in rt.get("routes", []):
            if r.get("state") == "blackhole" or r.get("target") == "unreachable":
                inconsistencies.append({"route_table": rt["id"], "route": r})
    return inconsistencies

def remediate(inconsistencies, routes):
    # Mock remediation: change state to 'active' and set target to 'local'
    fixed = []
    for inc in inconsistencies:
        rt_id = inc["route_table"]
        route = inc["route"]
        for rt in routes["route_tables"]:
            if rt["id"] == rt_id:
                for r in rt["routes"]:
                    if r["destination_cidr"] == route["destination_cidr"] and r["state"] == route["state"]:
                        r["state"] = "active"
                        r["target"] = "local"
                        fixed.append({"route_table": rt_id, "destination_cidr": r["destination_cidr"]})
    return fixed

def lambda_handler(event=None, context=None):
    logger.info("Starting network event mitigation run...")
    routes = load_routes()
    inconsistencies = detect_inconsistencies(routes)
    if not inconsistencies:
        logger.info("No inconsistencies detected. System healthy.")
        return {"status": "ok", "fixed": 0}
    logger.info(f"Detected {len(inconsistencies)} inconsistency(ies): {inconsistencies}")
    fixed = remediate(inconsistencies, routes)
    # write back to file to simulate change
    with open(ROUTE_FILE, "w") as f:
        json.dump(routes, f, indent=2)
    logger.info(f"Remediated {len(fixed)} route(s): {fixed}")
    return {"status": "fixed", "fixed": len(fixed)}

if __name__ == '__main__':
    # For local run simulation
    print(lambda_handler())

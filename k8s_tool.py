import subprocess
import json

def get_pods():
    output = subprocess.check_output(
        ["kubectl", "get", "pods", "-o", "json"]
    )

    data = json.loads(output)

    running = sum(
        1 for p in data["items"]
        if p["status"]["phase"] == "Running"
    )

    return {"running_pods": running}

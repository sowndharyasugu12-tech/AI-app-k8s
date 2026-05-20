import subprocess

def get_pods():

    result = subprocess.run(
        ["kubectl","get","pods"],
        capture_output=True,
        text=True
    )

    return result.stdout

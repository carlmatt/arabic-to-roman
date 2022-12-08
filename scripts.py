import subprocess


def test():
    """Run mypy and pytest tests"""
    subprocess.run(
        ["python", "-u", "-m", "mypy", "."]
    )
    subprocess.run(
        ["python", "-u", "-m", "pytest"]
    )
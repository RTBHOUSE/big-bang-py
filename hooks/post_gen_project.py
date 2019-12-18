import subprocess
from typing import List, NoReturn, Optional


def run_with_message(command: List[str]) -> Optional[NoReturn]:
    print("»", " ".join(command))
    result = subprocess.run(command)
    if result.returncode != 0:
        exit(result.returncode)


run_with_message(["make", "dotenv"])
run_with_message(["make", "requirements"])

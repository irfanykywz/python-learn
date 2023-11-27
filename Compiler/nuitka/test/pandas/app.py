import time

import pandas as pd

SLEEP_SEC = 5

while True:
    now = pd.Timestamp.utcnow()
    print(f"{now=}")

    print(f"Sleep for {SLEEP_SEC} seconds")
    time.sleep(SLEEP_SEC)
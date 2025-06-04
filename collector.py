import asyncio
import pandas as pd
from datetime import datetime
import os

FILENAME = "data.csv"

async def main():
    while True:
        now = datetime.utcnow()
        data = {
            "timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
            "value": round(now.timestamp() % 100, 2)
        }

        df = pd.DataFrame([data])
        file_exists = os.path.exists(FILENAME)

        if file_exists:
            df.to_csv(FILENAME, mode="a", header=False, index=False)
        else:
            df.to_csv(FILENAME, index=False)

        print(f"[{now}] записано значение: {data['value']}")
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())

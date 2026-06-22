import requests
import pandas as pd
from pathlib import Path

funds = {
    "hdfc_top100": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_largecap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

output_folder = Path("data/raw")
output_folder.mkdir(parents=True, exist_ok=True)

for name, code in funds.items():
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        nav_df.to_csv(
            output_folder / f"{name}_nav.csv",
            index=False
        )

        print(f"Saved {name}_nav.csv")

    else:
        print(f"Failed for {name}")
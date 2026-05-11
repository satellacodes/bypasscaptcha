from pathlib import Path

import pandas as pd

SUCCESS_FILE = "success.xlsx"
FAILED_FILE = "failed.xlsx"


def append_excel(file_name, data):
    df = pd.DataFrame([data])

    if Path(file_name).exists():
        existing = pd.read_excel(file_name)
        df = pd.concat([existing, df], ignore_index=True)

    df.to_excel(file_name, index=False)


def save_success(row):
    append_excel(SUCCESS_FILE, row.to_dict())


def save_failed(row, reason):
    data = row.to_dict()
    data["reason"] = reason

    append_excel(FAILED_FILE, data)

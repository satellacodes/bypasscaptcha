import asyncio

import pandas as pd
from loguru import logger

logger.add(
    "logs/bot.log",
    rotation="10 MB",
    retention="7 days",
)

from utils.excel import save_failed, save_success
from utils.profile import fill_profile
from utils.register import register_user

EXCEL_FILE = "accounts.xlsx"


async def process_user(row):
    browser = None

    try:
        result = await register_user(row)

        if not result["success"]:
            save_failed(row, result["reason"])
            return

        page = result["page"]
        browser = result["browser"]

        profile_result = await fill_profile(page, row)

        if profile_result:
            save_success(row)
            logger.success(f"SUCCESS => {row['fullname']}")
        else:
            save_failed(row, "profile_failed")

    except Exception as e:
        logger.exception(e)
        save_failed(row, str(e))

    finally:
        if browser:
            await browser.close()


async def main():
    df = pd.read_excel(EXCEL_FILE)

    for _, row in df.iterrows():
        await process_user(row)


if __name__ == "__main__":
    asyncio.run(main())

from loguru import logger
from utils.helpers import human_delay


async def fill_profile(page, row):
    try:
        await page.wait_for_load_state("networkidle")

        await human_delay()

        await page.locator('input[name="born_date"]').fill(str(row["born_date"]))

        await human_delay()

        await page.locator('textarea[name="produced"]').fill(str(row["produced"]))

        await human_delay()

        await page.locator('textarea[name="business_address"]').fill(
            str(row["business_address"])
        )

        await human_delay()

        await page.locator('select[name="business_sector"]').select_option("7")

        await human_delay()

        await page.locator('select[name="province"]').select_option("33")

        await human_delay(1000, 2000)

        await page.locator('select[name="regency"]').select_option("3305")

        await human_delay(1000, 2000)

        await page.locator('select[name="subdistrict"]').select_option("3305120")

        await human_delay(1000, 2000)

        await page.locator('select[name="village"]').select_option("3305120011")

        await human_delay(1000, 2000)

        await page.locator('select[name="postal_code"]').select_option("36497")

        await human_delay()

        await page.locator('button[type="submit"]').click()

        await page.wait_for_timeout(5000)

        logger.success("PROFILE SUCCESS")

        return True

    except Exception as e:
        logger.exception(e)
        return False

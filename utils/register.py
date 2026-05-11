from loguru import logger

from utils.browser import create_browser
from utils.captcha import solve_captcha
from utils.helpers import human_delay

REGISTER_URL = "your-address-webite/register"


async def register_user(row):
    playwright, browser, page = await create_browser()

    try:
        await page.goto(REGISTER_URL)

        await human_delay()

        await page.locator('input[name="fullname"]').type(
            str(row["fullname"]),
            delay=40,
        )

        await human_delay()

        await page.locator('input[name="phone_number"]').type(
            str(row["phone_number"]),
            delay=40,
        )

        await human_delay()

        await page.locator('input[name="id_number"]').type(
            str(row["id_number"]),
            delay=40,
        )

        await human_delay()

        await page.locator('input[name="password"]').type(
            str(row["password"]),
            delay=40,
        )

        await human_delay()

        await page.locator('input[name="password_retype"]').type(
            str(row["password"]),
            delay=40,
        )

        captcha_img = page.locator('img[src*="capctha_mantri"]')

        await captcha_img.screenshot(path="captcha/current.png")

        captcha_text = solve_captcha("captcha/current.png")

        logger.info(f"Captcha => {captcha_text}")

        await page.locator('input[name="kode_captcha"]').fill(captcha_text)

        await human_delay()

        await page.locator(".l-regist").click()

        await page.wait_for_timeout(5000)

        current_url = page.url

        if "register" in current_url:
            return {
                "success": False,
                "reason": "captcha_failed",
            }

        return {
            "success": True,
            "browser": browser,
            "page": page,
        }

    except Exception as e:
        logger.exception(e)

        return {
            "success": False,
            "reason": str(e),
        }

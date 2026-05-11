from playwright.async_api import async_playwright


async def create_browser():
    playwright = await async_playwright().start()

    browser = await playwright.chromium.launch(
        headless=False,
        args=[
            "--disable-blink-features=AutomationControlled",
            "--disable-dev-shm-usage",
            "--no-sandbox",
            "--disable-setuid-sandbox",
        ],
    )

    context = await browser.new_context(viewport={"width": 1400, "height": 900})

    page = await context.new_page()

    return playwright, browser, page

import asyncio
import random


async def human_delay(min_ms=500, max_ms=1500):
    delay = random.randint(min_ms, max_ms)
    await asyncio.sleep(delay / 1000)

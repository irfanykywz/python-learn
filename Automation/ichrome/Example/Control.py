# https://clericpy.github.io/ichrome/quickstart/
import asyncio
import json

from ichrome import AsyncChromeDaemon, AsyncChrome

host = '127.0.0.1'
port = 9222

async def chromeLaunch():
    async with AsyncChromeDaemon(host=host,
                                 port=port,
                                 headless=False,
                                 on_startup=False,
                                 on_shutdown=False,
                                 clear_after_shutdown=True) as chromed:
        await chromed.run_forever()

loop = asyncio.new_event_loop()
loop.run_until_complete(chromeLaunch())
loop.close()

#  after chrome launch use Control2.py to control chrome..
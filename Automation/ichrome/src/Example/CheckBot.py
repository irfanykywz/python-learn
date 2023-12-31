import asyncio
import json

from ichrome import AsyncChromeDaemon, AsyncChrome

async def chromeLaunch():
	async with AsyncChromeDaemon(
	host='127.0.0.1',
	port=9222,
	headless=False,
	on_startup=False,
	on_shutdown=False,
	clear_after_shutdown=True) as chromed:

		async with chromed.connect_tab(index=0, auto_close=False) as tab:

			await tab.goto('https://pixelscan.net/')
			await chromed.run_forever()


loop = asyncio.new_event_loop()
loop.run_until_complete(chromeLaunch())
loop.close()
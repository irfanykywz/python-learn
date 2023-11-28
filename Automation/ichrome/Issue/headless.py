import asyncio
from ichrome import AsyncChromeDaemon, AsyncChrome


async def test_examples():
    async with AsyncChromeDaemon(host='127.0.0.1',
                                 port=9222,
                                 headless=True,
                                 extra_config=['--enable-javascript']
                                 clear_after_shutdown=True) as chromed:
    	async with chromed.connect_tab(auto_close=True) as tab:
       
	        await tab.goto("https://google.com", timeout=5)
	        title = await tab.title
	        print(title)

loop = asyncio.new_event_loop()
loop.run_until_complete(test_examples())
loop.close()
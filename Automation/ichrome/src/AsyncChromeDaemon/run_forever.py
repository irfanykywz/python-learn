# https://clericpy.github.io/ichrome/reference/AsyncChromeDaemon/
import asyncio
from ichrome import AsyncChromeDaemon, AsyncChrome


async def test_examples():
    async with AsyncChromeDaemon(host='127.0.0.1',
                                 port=9222,
                                 headless=False,
                                 clear_after_shutdown=True) as chromed:

        # dont close chrome after finish command
        await chromed.run_forever()



loop = asyncio.new_event_loop()
loop.run_until_complete(test_examples())
loop.close()
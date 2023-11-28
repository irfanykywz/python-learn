# https://clericpy.github.io/ichrome/reference/AsyncChromeDaemon/
import asyncio
from ichrome import AsyncChromeDaemon, AsyncChrome


async def test_examples():
    async with AsyncChromeDaemon(host='127.0.0.1',
                                 port=9222,
                                 headless=False,
                                 clear_after_shutdown=True) as chromed:


        # current tab
        async with chromed.connect_tab(index=0, auto_close=False) as tab:
            pass

        # about blank new tab
        async with chromed.connect_tab(index=None, auto_close=False) as tab:
            pass

        # connect to AsyncTab class (use this method if want to multiple processing at same time)
        async with chromed.connect_tab(index='https://google.com', auto_close=False) as tab:
            pass

        await chromed.run_forever()




loop = asyncio.new_event_loop()
loop.run_until_complete(test_examples())
loop.close()
import asyncio
from ichrome import AsyncChromeDaemon, AsyncChrome


async def test_examples():
    async with AsyncChromeDaemon(host='127.0.0.1',
                                 port=9222,
                                 headless=False,
                                 clear_after_shutdown=True) as chromed:

        # # check if chrome has opened
        # print(await chromed.check_chrome_ready())

        # # check connection
        # print(await chromed.check_connection())


        # # close browser
        # await chromed.close_browser()

        # # restart
        # await chromed.restart()

        # # shutdown
        # await chromed.shutdown()

        
        

        # connect to AsyncTab class as incognite
       async with chromed.incognito_tab() as tab:
            await tab.goto("https://pixelscan.net/")
            await chromed.run_forever()

        # ???
        # print(await chromed.create_context())

        # # get free port
        # print(await chromed.get_free_port())




loop = asyncio.new_event_loop()
loop.run_until_complete(test_examples())
loop.close()
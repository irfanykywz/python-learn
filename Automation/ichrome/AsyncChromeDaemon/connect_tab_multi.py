# https://clericpy.github.io/ichrome/reference/AsyncChromeDaemon/
# https://github.com/ClericPy/ichrome/issues/87
import asyncio
from ichrome import AsyncChromeDaemon, AsyncChrome


async def test_connect_tab(cd, url):
    async with cd.connect_tab(None) as tab:
        await tab.goto(url)
        await tab.wait_tag('body')
        title = await tab.title
        print(title)
        # await tab.close()



async def jobs():
    async with AsyncChromeDaemon(host='127.0.0.1',
                                 port=9222,
                                 headless=False,
                                 clear_after_shutdown=True) as chromed:

        list = [
        'https://google.com',
        'https://tiktok.com',
        'https://youtube.com',        
        'https://gmail.com',        
        ]        

        tasks = [asyncio.create_task(test_connect_tab(chromed, url)) for url in list]
        await asyncio.wait(tasks)


        # dont close chrome
        await chromed.run_forever()




asyncio.run(jobs())
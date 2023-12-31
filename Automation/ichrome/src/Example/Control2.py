# https://clericpy.github.io/ichrome/quickstart/
import asyncio
import json

from ichrome import AsyncChrome

import ichrome

host = '127.0.0.1'
port = 9222
# test control
async def control():
    async with AsyncChrome(host=host, port=port) as chrome:
        memory = chrome.get_memory()
        print(memory)
        async with chrome.connect_tab(index=0, auto_close=False) as tab:
            await tab.goto('https://google.com')


checkprocess = ichrome.base.get_proc(port=port, host=host)

if len(checkprocess) > 0:
    asyncio.run(control())

# print(checkprocess[0].pid)
# print(checkprocess[0].name())
# print(checkprocess[0].status())
# print(checkprocess[0].is_running())
# print(checkprocess[0].create_time())
# print(dir(checkprocess[0]))
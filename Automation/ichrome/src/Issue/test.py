import asyncio

import traceback
from ichrome import AsyncChrome, AsyncTab

doings = {}


async def watchdog_callback(browser: AsyncTab, data: dict):
    # 这里会看到很多 Network 事件
    print(data)


async def daemon(tab_id, chrome: AsyncChrome):
    try:
        async with chrome.connect_tab(tab_id) as tab:
            # 假设我这里把每一个新建的 tab 都跳转到 bing.com
            await tab.goto('http://bing.com')
            # 然后我这里打印请求事件
            await tab.enable('Network')
            tab.default_recv_callback.append(watchdog_callback)
            await asyncio.sleep(1000)
    except Exception:
        traceback.print_exc()


async def callback(browser: AsyncTab, data: dict):
    # print(browser, data, flush=True)
    if data.get('method') == 'Target.targetCreated':
        tab_id = data['params']['targetInfo']['targetId']
        if tab_id not in doings:
            print('[标签页新建]:',
                  tab_id,
                  data['params']['targetInfo']['title'],
                  data['params']['targetInfo']['url'],
                  flush=True)
            task = asyncio.create_task(daemon(tab_id, chrome=browser.chrome))
            doings[tab_id] = task
        # 这里可以创建一个守护协程监听这个 Tab 做点事情, 比如 fetch iter
    elif data.get('method') == 'Target.targetDestroyed':
        tab_id = data['params']['targetId']
        print('[标签页关闭]:', tab_id, flush=True)
        # 这里可以把之前监听的 Task 给 cancel 掉
        task = doings.pop(tab_id, None)
        if task:
            task.cancel()
            await asyncio.sleep(0)


async def main():
    async with AsyncChrome(port=9222) as chrome:
        memory = chrome.get_memory()
        print(memory)
        # await chrome.browser.send('Target.setDiscoverTargets', discover=True)
        # chrome.browser.default_recv_callback.append(callback)
        # # print(await chrome.browser.send('Target.getTargets'))
        # # await chrome.browser.wait_event('Target.targetCreated')
        # await asyncio.sleep(1000)


if __name__ == "__main__":
    asyncio.run(main())
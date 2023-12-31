import asyncio

from ichrome import AsyncChromeDaemon


async def main():
    async with AsyncChromeDaemon(clear_after_shutdown=True,
                                 headless=False) as cd:
        async with cd.connect_tab(0, auto_close=True) as tab:
            async with tab.iter_fetch(handleAuthRequests=True) as f:
                await tab.goto('https://httpbin.org/basic-auth/user/password',
                               timeout=0.1)
                async for event in f:
                    print(event, flush=True)
                    if event['method'] == 'Fetch.requestPaused':
                        await f.continueRequest(event)
                    elif event['method'] == 'Fetch.authRequired':
                        await f.continueWithAuth(
                            event,
                            'ProvideCredentials',
                            'user',
                            'password',
                        )
                        await tab.wait_loading(3)
                        print('HTML:', await tab.html)


if __name__ == "__main__":
    asyncio.run(main())

# =========================


import asyncio

from ichrome import AsyncChromeDaemon


async def main():
    async with AsyncChromeDaemon(clear_after_shutdown=True,
                                 headless=False) as cd:
        async with cd.connect_tab(0, auto_close=True) as tab:
            async with tab.iter_events(['Network.requestWillBeSentExtraInfo']) as f:
                await tab.goto('https://httpbin.org/basic-auth/user/password',
                               timeout=0.1)
                async for event in f:
                    if 'authorization' in str(event).lower():
                        print(event)
                        break


if __name__ == "__main__":
    asyncio.run(main())
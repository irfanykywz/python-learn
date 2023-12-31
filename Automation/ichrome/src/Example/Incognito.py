import asyncio

from ichrome import AsyncChromeDaemon


async def main():
    async with AsyncChromeDaemon() as cd:
        proxy = None
        async with cd.incognito_tab(proxyServer=proxy) as tab:
            # This tab will be created in the given BrowserContext
            await tab.goto('http://httpbin.org/ip', timeout=10)
            # print and watch your IP changed
            print(await tab.html)
            await cd.run_forever()


asyncio.run(main())

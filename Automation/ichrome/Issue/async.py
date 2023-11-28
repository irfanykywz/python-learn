from ichrome import ChromeDaemon, AsyncChrome
import asyncio


async def main():
    with ChromeDaemon(port=9222) as chromed:
        chromed.run_forever()
        # `async with` usage will be fixed after version 0.2.7
        # chrome = AsyncChrome(port=9222)
        # await chrome.connect()
        # tab = (await chrome.tabs)[0]
        # async with tab():
        #     print(await tab.current_url)
        #     # about:blank
        # await chrome.close()


if __name__ == "__main__":
    asyncio.run(main())
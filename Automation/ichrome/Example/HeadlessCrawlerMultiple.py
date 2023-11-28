# https://github.com/ClericPy/ichrome/blob/master/use_cases.py

"""crawl a page with headless chrome"""
import asyncio
import re

from ichrome import AsyncChrome, AsyncChromeDaemon

# WARNING: Chrome has a limit of 6 connections per host name, and a max of 10 connections.
# Read more: https://blog.bluetriangle.com/blocking-web-performance-villain

async def main():
    # crawl 3 urls in 3 tabs
    timeout = 3

    async def crawl(url):
        async with chrome.connect_tab(url, True) as tab:
            await tab.wait_loading(timeout=timeout)
            html = await tab.html
            result = re.search('<h1>(.*?)</h1>', html).group(1)
            print(result)
            await asyncio.sleep(5)
            assert result == 'Herman Melville - Moby-Dick'
            
    # multi-urls concurrently crawl
    test_urls = ['http://httpbin.org/html'] * 5
    async with AsyncChromeDaemon(headless=True):
        async with AsyncChrome() as chrome:
            tasks = [asyncio.ensure_future(crawl(url)) for url in test_urls]
            await asyncio.wait(tasks)
            await asyncio.sleep(2)


asyncio.run(main())
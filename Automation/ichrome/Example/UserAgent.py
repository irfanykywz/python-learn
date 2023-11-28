"""crawl a page with headless chrome"""
import asyncio
import re

from ichrome import AsyncChrome, AsyncTab, AsyncChromeDaemon

# WARNING: Chrome has a limit of 6 connections per host name, and a max of 10 connections.
# Read more: https://blog.bluetriangle.com/blocking-web-performance-villain
test_url = 'http://httpbin.org/user-agent'

async def main():
    # crawl url with custom UA
    timeout = 3

    #  set custom usera gent on deamon
    async with AsyncChromeDaemon(headless=True, user_agent='jancuk koe hahaha'):
        async with AsyncChrome() as chrome:
            async with (await chrome[0])() as tab:
                tab: AsyncTab
                await tab.set_url(test_url, timeout=timeout)
                html = await tab.html
                result = re.search('("user-agent".*)', html).group(1)
                print(result)
                assert result == '"user-agent": "jancuk koe hahaha"'

asyncio.run(main())

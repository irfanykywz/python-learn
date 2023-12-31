# https://github.com/ClericPy/ichrome/issues/41
# https://github.com/ClericPy/ichrome/issues/86

import asyncio

from ichrome import AsyncChromeDaemon


async def main():
    async with AsyncChromeDaemon(
    							# proxy='50.227.121.35:80',
                                extra_config=[
                                f'--proxy-server=https=50.227.121.35:80;http=50.227.121.35:80'
                                ],
                                clear_after_shutdown=True,
                                headless=False
                                ) as cd:
        async with cd.connect_tab() as tab:
            # await tab.pass_auth_proxy('user', 'pwd')
            print('ahihihi')
            await tab.goto('https://httpbin.org/ip', timeout=2)
            print(await tab.html)

            await cd.run_forever()


asyncio.run(main())
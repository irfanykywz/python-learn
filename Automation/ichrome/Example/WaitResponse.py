# https://clericpy.github.io/ichrome/quickstart/
import asyncio
import json

from ichrome import AsyncChromeDaemon


async def main():
    async with AsyncChromeDaemon() as cd:
        async with cd.connect_tab() as tab:

            async with tab.wait_response_context(
                        filter_function=lambda r: tab.get_data_value(
                            r, 'params.response.url') == 'https://httpbin.org/get',
                        timeout=5,
                ) as r:
                    await tab.goto('https://httpbin.org/get')
                    result = await r
                    if result:
                        print(result['data'])

        await cd.run_forever()     


if __name__ == "__main__":
    asyncio.run(main())                                        
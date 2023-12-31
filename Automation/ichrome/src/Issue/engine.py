# https://github.com/ClericPy/ichrome/issues/55

import asyncio

from ichrome.pool import ChromeEngine


def test_chrome_engine_connect_tab():

    async def _test_chrome_engine_connect_tab():

        async with ChromeEngine(port=9234, headless=True,
                                disable_image=True) as ce:
            async with ce.connect_tab(port=9234) as tab:
                await tab.goto('http://pypi.org')
                title = await tab.title
                return title

    loop = asyncio.get_event_loop()
    get_future = asyncio.ensure_future(_test_chrome_engine_connect_tab())
    loop.run_until_complete(get_future)
    return get_future.result()


if __name__ == "__main__":
    title = test_chrome_engine_connect_tab()
    print(title)
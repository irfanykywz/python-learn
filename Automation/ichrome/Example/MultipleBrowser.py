import asyncio
import json
import socket

from ichrome import *

# python -m ichrome --window-size=480,640

# C:\Windows\system32\cmd.exe /c ""C:/Program Files/Google/Chrome/Application/chrome.exe" --remote-debugging-address=127.0.0.1 --remote-debugging-port=9998 --user-data-dir=C:/Users/WIN10/ichrome_user_data/chrome_9998 --disable-gpu --no-first-run --app=https://mobile.facebook.com"

async def test(ports):
    async with AsyncChromeDaemon(
        chrome_path=None,
        host="127.0.0.1",
        port=ports,
        headless=False,
        user_agent=None,
        proxy=None,
        user_data_dir=None,
        disable_image=False,
        start_url="--app=https://mobile.facebook.com",
        extra_config=None,
        max_deaths=1,
        daemon=True,
        block=False,
        timeout=3,
        debug=False,
        proc_check_interval=5,
        on_startup=None,
        on_shutdown=None,
        before_startup=None,
        after_shutdown=None,
        clear_after_shutdown=False,
        ) as cd:
        # create a new tab
        async with cd.connect_tab(index=0) as tab:
            # await tab.goto('https://github.com/ClericPy/ichrome', timeout=5)
            await tab.alert('Now will input some text and search the issues.')
            await tab.mouse_click_element_rect('#m_login_email')
            await tab.keyboard_send(string='chromium')
             await tab.mouse_click_element_rect('#m_login_password')
            await tab.keyboard_send(string='chromium')
            print(await tab.title)          


async def main():
    await asyncio.gather(
        test(9999),
        test(9998),
        test(9997)
    )

x = asyncio.run(main())
print(x)
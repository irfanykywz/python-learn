首先, ichrome 启动的 chrome 用的不是默认的 User dir, 所以和你的那个 Default Profile 可能不一样, 你可以考虑先启动 ichrome 的浏览器在里面设置语言
当然也可以对单个 Tab 设置, 见下面代码
还有就是启动的时候加命令行参数, --lang=locale, 或者 --accept-lang=en-US 这个东西放到 extra_config 参数里就行了
还有就是系统环境变量 LANGUAGE=en, 没试过
# 模拟地理位置=美国
await tab.send('Emulation.setLocaleOverride',
                locale='en_US')
# 设置地理坐标
await tab.send('Emulation.setGeolocationOverride',
                kwargs={
                    'accuracy': 100,
                    'latitude': 39.11884413294521,
                    'longitude': -77.33412341617008,
                })
# America/Chicago 时区
await tab.send('Emulation.setTimezoneOverride',
                timezoneId='America/Chicago')
# 模拟 UserAgent, 然后接受语言 en
await tab.send('Emulation.setUserAgentOverride',
                userAgent=UA,
                acceptLanguage='en')
await tab.send('Network.setExtraHTTPHeaders',
                headers={'Accept-Language': 'en'})







==================


import asyncio
import json

from ichrome import AsyncChromeDaemon


async def main():
    async with AsyncChromeDaemon() as cd:
        async with cd.connect_tab() as tab:
            async with tab.iter_fetch(timeout=5) as f:
                await tab.goto('http://httpbin.org/get', timeout=0)
                async for request in f:
                    print(json.dumps(request))
                    await f.continueRequest(request)


if __name__ == "__main__":
    asyncio.run(main())


    ================

 print(await tab.send('Input.dispatchMouseEvent',
                                 type="mouseWheel",
                                 timeout=2,
                                 x=0,
                                 y=0,
                                 deltaX=0,
                                 deltaY=100))



=============


https://github.com/ClericPy/ichrome/issues/54                                 
# https://clericpy.github.io/ichrome/quickstart/
import asyncio
import json

from ichrome import AsyncChromeDaemon


async def main():
    async with AsyncChromeDaemon() as cd:
        async with cd.connect_tab() as tab:
   
            # 2. disable image requests
            url = 'https://www.bing.com'
            RequestPatternList = [
                {
                    'urlPattern': '*',
                    'resourceType': 'Image',  # could be other types
                    'requestStage': 'Request'
                },
                {
                    'urlPattern': '*',
                    'resourceType': 'Stylesheet',
                    'requestStage': 'Request'
                },
                {
                    'urlPattern': '*',
                    'resourceType': 'Script',
                    'requestStage': 'Request'
                },
            ]
            # listen 5 seconds
            async with tab.iter_fetch(RequestPatternList, timeout=5) as f:
                await tab.goto(url, timeout=0)
                # handle all the matched requests
                async for event in f:
                    if f.match_event(event, RequestPatternList[0]):
                        print('abort request image:',
                              tab.get_data_value(event, 'params.request.url'),
                              flush=True)
                        await f.failRequest(event, 'Aborted')
                    elif f.match_event(event, RequestPatternList[1]):
                        print('abort request css:',
                              tab.get_data_value(event, 'params.request.url'),
                              flush=True)
                        await f.failRequest(event, 'ConnectionRefused')
                    elif f.match_event(event, RequestPatternList[2]):
                        print('abort request js:',
                              tab.get_data_value(event, 'params.request.url'),
                              flush=True)
                        await f.failRequest(event, 'AccessDenied')
                await asyncio.sleep(5)     


if __name__ == "__main__":
    asyncio.run(main())                
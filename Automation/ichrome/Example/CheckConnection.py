# https://clericpy.github.io/ichrome/quickstart/
import asyncio
import json

from ichrome import AsyncChromeDaemon


async def main():
    async with AsyncChromeDaemon() as cd:
        async with cd.connect_tab() as tab:
            url = 'https://blogger.com/'
            # 1. listen request/response network
            RequestPatternList = [{
                'urlPattern': '*blogger.com/*',
                'requestStage': 'Response'
            }]
            status = None
            async with tab.iter_fetch(RequestPatternList) as f:
                await tab.goto(url, timeout=0)
                # only one request could be catched
                event = await f
                print(event)
                if 'responseStatusCode' in event['params']:
                  status = event['params']['responseStatusCode']

                response = await f.get_response(event, timeout=5)
                print(response)
                # print(response['params']['response']['status'])   
            
            # await tab.alert(status) 
            if status == None:
              print('no connection')
            elif status in [301,302]:
              print('redirect')

            # await tab.goto('https://google.com')

            # check by tag
            # if contain class offline on html its a no connection
            await tab.html # this code must include for detect html class offline
            check = await tab.findone(regex='offline' ,cssselector='html[class=offline]')
            check2 = await tab.findone(regex='main-frame-error')
            print(check)
            print(check2)
            if check or check2:
              print('connection disconnect')
            else:
              print('connection connected')


            await cd.run_forever()     


if __name__ == "__main__":
    asyncio.run(main())                
# https://github.com/ClericPy/ichrome/blob/master/use_cases.py

"""network flow sniffer

    1. run the function.
    2. change url of chrome's tab.
    3. watch the console logs.
"""
import asyncio
from ichrome import AsyncChrome, AsyncTab, AsyncChromeDaemon
import json

get_data_value = AsyncTab.get_data_value

def filter_function(r):
    req = json.dumps(get_data_value(r, 'params.request'),
                     ensure_ascii=0,
                     indent=2)
    req_type = get_data_value(r, 'params.type')
    req_type = get_data_value(r, 'params.type')
    doc_url = get_data_value(r, 'params.documentURL')
    print(f'{doc_url} - {req_type}\n{req}', end=f'\n{"="*40}\n')
    # print(r)

async def main():
    async with AsyncChromeDaemon():
        async with AsyncChrome() as chrome:
            async with chrome.connect_tab(0) as tab:
                await tab.wait_request(filter_function=filter_function,
                                       timeout=60)


asyncio.run(main()) 
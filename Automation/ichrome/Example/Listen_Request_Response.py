# https://clericpy.github.io/ichrome/quickstart/
import asyncio
import json

from ichrome import AsyncChromeDaemon


async def main():
    async with AsyncChromeDaemon() as cd:
        async with cd.connect_tab() as tab:
            url = 'http://httpbin.org/ip'
            # 1. listen request/response network
            RequestPatternList = [{
                'urlPattern': '*httpbin.org/ip*',
                'requestStage': 'Response'
            }]
            async with tab.iter_fetch(RequestPatternList) as f:
                await tab.goto(url, timeout=0)
                # only one request could be catched
                event = await f
                print('request event:', json.dumps(event), flush=True)
                """
                {
                  "method": "Fetch.requestPaused",
                  "params": {
                    "requestId": "interception-job-1.0",
                    "request": {
                      "url": "http://httpbin.org/ip",
                      "method": "GET",
                      "headers": {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                        "Upgrade-Insecure-Requests": "1",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
                      },
                      "initialPriority": "VeryHigh",
                      "referrerPolicy": "strict-origin-when-cross-origin"
                    },
                    "frameId": "D1539BE3188C44313176FB65D66BAA57",
                    "resourceType": "Document",
                    "responseStatusCode": 200,
                    "responseStatusText": "OK",
                    "responseHeaders": [
                      {
                        "name": "Date",
                        "value": "Fri, 03 Nov 2023 18:59:32 GMT"
                      },
                      {
                        "name": "Content-Type",
                        "value": "application/json"
                      },
                      {
                        "name": "Content-Length",
                        "value": "33"
                      },
                      {
                        "name": "Connection",
                        "value": "keep-alive"
                      },
                      {
                        "name": "Server",
                        "value": "gunicorn/19.9.0"
                      },
                      {
                        "name": "Access-Control-Allow-Origin",
                        "value": "*"
                      },
                      {
                        "name": "Access-Control-Allow-Credentials",
                        "value": "true"
                      }
                    ],
                    "networkId": "01685DD067680156C1B630F410B48D0E"
                  },
                  "sessionId": "1179753196AB9D5C111002ECBFB6393B"
                }
                """

                response = await f.get_response(event, timeout=5)
                print('response body:', response)
                """
                {
                  'method': 'Network.responseReceived',
                  'params': {
                    'requestId': '86B058B670C3BD66652500CCB1C3E498',
                    'loaderId': '86B058B670C3BD66652500CCB1C3E498',
                    'timestamp': 254500.309033,
                    'type': 'Document',
                    'response': {
                      'url': 'http://httpbin.org/ip',
                      'status': 200,
                      'statusText': 'OK',
                      'headers': {
                        'Access-Control-Allow-Credentials': 'true',
                        'Access-Control-Allow-Origin': '*',
                        'Connection': 'keep-alive',
                        'Content-Length': '33',
                        'Content-Type': 'application/json',
                        'Date': 'Fri, 03 Nov 2023 19:01:07 GMT',
                        'Server': 'gunicorn/19.9.0'
                      },
                      'mimeType': 'application/json',
                      'connectionReused': False,
                      'connectionId': 55,
                      'remoteIPAddress': '54.90.18.68',
                      'remotePort': 80,
                      'fromDiskCache': False,
                      'fromServiceWorker': False,
                      'fromPrefetchCache': False,
                      'encodedDataLength': 229,
                      'timing': {
                        'requestTime': 254499.523305,
                        'proxyStart': -1,
                        'proxyEnd': -1,
                        'dnsStart': 0,
                        'dnsEnd': 45.666,
                        'connectStart': 45.666,
                        'connectEnd': 53.614,
                        'sslStart': -1,
                        'sslEnd': -1,
                        'workerStart': -1,
                        'workerReady': -1,
                        'workerFetchStart': -1,
                        'workerRespondWithSettled': -1,
                        'sendStart': 55.194,
                        'sendEnd': 55.404,
                        'pushStart': 0,
                        'pushEnd': 0,
                        'receiveHeadersStart': 781.678,
                        'receiveHeadersEnd': 781.748
                      },
                      'responseTime': 1699038074350.912,
                      'protocol': 'http/1.1',
                      'alternateProtocolUsage': 'unspecifiedReason',
                      'securityState': 'insecure'
                    },
                    'hasExtraInfo': True,
                    'frameId': '06247407310BFE9CBCFC2C8C6585F20C'
                  },
                  'sessionId': 'B310E0CDCD9C47D9085F92655A715EB2',
                  'data': '{\n  "origin": "103.253.24.248"\n}\n'
                }
                """                


if __name__ == "__main__":
    asyncio.run(main())                
from fastapi import FastAPI
from ichrome import AsyncChromeDaemon
from starlette.responses import Response
from base64 import b64decode
import asyncio
app = FastAPI()


async def restart_job():
    while 1:
        if getattr(app, 'chrome', None):
            await app.chrome.shutdown()
        app.chrome = await AsyncChromeDaemon(headless=True).__aenter__()
        await asyncio.sleep(8 * 60)


@app.on_event("startup")
async def startup_event():
    asyncio.ensure_future(restart_job())


@app.get('/screenshot')
async def screenshot(url):
    async with app.chrome.connect_tab(index=None, auto_close=True) as tab:
        await tab.set_url(url)
        await tab.wait_tag('[data-testid="Keycommand_wrapper_feed_story"]')
        # await asyncio.sleep(5)
        image = await tab.screenshot()
        return Response(b64decode(image or b''))


if __name__ == "__main__":
    from uvicorn import run
    run(app)
# http://127.0.0.1:8000/screenshot?url=https%3A%2F%2Fwww.facebook.com%2Fads%2Fapi%2Fpreview_iframe.php%3Fd%3DAQJEfPAy4afAB60wOmfaUWylbt8x1HH0G5-d1GBmoVf8tSLkRTRZiU1qJQFtbm0OC3pCB_MrYyC9Pube0sfAiGaK5g2cpbYgd1-QCPTQrJyDGG6pVIZW06ETtjy76xuF3x9S62Flq4HM4z8o8t2ubqZwjNp7IibhPnce3riTqj4_x7UwUjkDFvkIRr0TfhNStRiM-KC8z5YF3jfLvohCWXeH5Ncv6-1_KxmDUo_nBBHMfKqzPt7kP0dz5cGX6OsLWvtNQklJTOBcVQ8rm4XXVBe8lGO9iq_9RogAXuuA8ePlqaZ-1Rt7uCmbTFWR_6l0PNzzTD8YL87DRLmjmkg9UecY%26t%3DAQKo6Fq5kHbz5Mf6WNA
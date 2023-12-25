import asyncio
import httpx
from tqdm import tqdm

async def download(url: str, filename: str):
    with open(filename, 'wb') as f:
        async with httpx.AsyncClient() as client:
            async with client.stream('GET', url) as r:
                r.raise_for_status()
                total = int(r.headers.get('content-length', 0))

                tqdm_params = {
                    'desc': url,
                    'total': total,
                    'miniters': 1,
                    'unit': 'B',
                    'unit_scale': True,
                    'unit_divisor': 1024,
                }
                with tqdm(**tqdm_params) as pb:
                    downloaded = r.num_bytes_downloaded
                    async for chunk in r.aiter_bytes():
                        pb.update(r.num_bytes_downloaded - downloaded)
                        f.write(chunk)
                        downloaded = r.num_bytes_downloaded

async def main():
    """
    Downloading three large files simultaneously.
    Each file has its own progress bar.
    """
    loop = asyncio.get_running_loop()
    urls = [
        ('https://speed.hetzner.de/100MB.bin', '100MB.bin'),
        ('https://speed.hetzner.de/1GB.bin', '1GB.bin'),
        ('http://ipv4.download.thinkbroadband.com/50MB.zip', '50MB.zip'),
    ]
    tasks = [loop.create_task(download(url, name)) for url, name in urls]
    await asyncio.gather(*tasks, return_exceptions=True)


asyncio.run(main())
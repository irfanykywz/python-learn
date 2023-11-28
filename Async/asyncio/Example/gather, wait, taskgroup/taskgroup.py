# https://stackoverflow.com/questions/42231161/asyncio-gather-vs-asyncio-wait-vs-asyncio-taskgroup

import asyncio
import random


# Python 3.11+ ONLY!
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(some_coro(...))
        task2 = tg.create_task(another_coro(...))
    print("Both tasks have completed now.")
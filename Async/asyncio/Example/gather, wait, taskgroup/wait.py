# https://stackoverflow.com/questions/42231161/asyncio-gather-vs-asyncio-wait-vs-asyncio-taskgroup

import asyncio
import random


async def coro(tag):
    print(">", tag)
    await asyncio.sleep(random.uniform(5, 10))
    print("<", tag)
    return tag


loop = asyncio.new_event_loop()

tasks = [coro(i) for i in range(1, 11)]

print("Get first result:")
finished, unfinished = loop.run_until_complete(
    asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED))

for task in finished:
    print(task.result())
print("unfinished:", len(unfinished))

print("Get more results in 2 seconds:")
finished2, unfinished2 = loop.run_until_complete(
    asyncio.wait(unfinished, timeout=2))

for task in finished2:
    print(task.result())
print("unfinished2:", len(unfinished2))

print("Get all other results:")
finished3, unfinished3 = loop.run_until_complete(asyncio.wait(unfinished2))

for task in finished3:
    print(task.result())

loop.close()
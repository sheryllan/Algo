import asyncio
from time import sleep

async def cora_a():
    print("I am coro_a(). Hi!")
    await asyncio.sleep(5)
    print("I am coro_a(). Done!")


async def cora_b(sec=0):
    print("I am coro_b(). Hi!")
    sleep(sec)
    print("I am coro_b(). Done!")


async def main():
    task_0 = asyncio.create_task(cora_b())
    task_a = asyncio.create_task(cora_a())
    for _ in range(3):
        await asyncio.create_task(cora_b())

    print("wonderful")
    print("amazing")
    print("brilliant")

    await task_a
    await task_0
    print("next")


asyncio.run(main())


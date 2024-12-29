import asyncio

arr = ["red", "yellow", "green"]
interval = 3

def light_logic(x):
    if x == "red":
        print("stop...")
    elif x == "green":
        print("go...")
    else:
        print("ready..")


async def random_call():
    for i in range(len(arr)):
        light_logic(arr[i])
        await asyncio.sleep(interval)
    await random_call()

async def main():
    await random_call()

asyncio.run(main())
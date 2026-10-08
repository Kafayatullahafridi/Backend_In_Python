# # import time


# # def task(name):
# #     print(f"{name} started")
# #     time.sleep(2)
# #     print(f"{name} finished")


# # start = time.time()

# # task("Task 1")
# # task("Task 2")
# # task("Task 3")

# # end = time.time()

# # print(f"Total time: {end - start:.2f} seconds")









# import asyncio


# async def task(name):
#     print(f"{name} started")
#     await asyncio.sleep(2)
#     print(f"{name} finished")


# async def main():
#     await task("Task 1")
#     await task("Task 2")
#     await task("Task 3")


# asyncio.run(main())

import asyncio

async def database(name):
    await asyncio.sleep(1)
    return f"{name} completed"


async def payment(name):
    await asyncio.sleep(1)
    return f"{name} completed"

async def notification(name):
    await asyncio.sleep(1)
    return f"{name} completed"
@app.get('/process')
async def process(name:str):
     return await asyncio.gather(
        notification(name),payment(name),database(name)
    )
    
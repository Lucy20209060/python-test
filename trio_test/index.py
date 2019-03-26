#!/usr/bin/python
# -*- coding: UTF-8 -*-

import trio

async def trio_test():
    print("start")
    await  trio.sleep(1)
    print("end")

# async def parent():
#     async with trio.open_nursery() as nursery:
#         nursery.start_soon(trio_test)
 
trio.run(trio_test)
from asyncio import sleep, get_event_loop


async def f():
    await sleep(2)
    print(64)
    await sleep(12)
    print(67)


async def g():
    print(1)
    await sleep(8)
    print(2)


async def dispatch():
    main_loop.create_task(f())
    main_loop.create_task(g())


try:
    main_loop = get_event_loop()
    main_loop.run_until_complete(dispatch())
    main_loop.run_forever()
except KeyboardInterrupt:
    print('до свидания')

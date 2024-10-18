from collections.abc import AsyncIterator
import complete
import asyncio


async def my_async_iterator() -> AsyncIterator[str]:
    coros = (complete.complete(s) for s in ("hello", "world", "test"))
    results = await asyncio.gather(*coros)
    for result in results:
        yield result

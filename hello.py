import my_dep
import complete


async def main():
    await complete.complete("hello")
    my_nodes = my_dep.my_async_iterator()
    print([result async for result in my_nodes])

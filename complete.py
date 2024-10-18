import openai
import nest_asyncio
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from openai.types import chat

nest_asyncio.apply() # pyright: ignore[reportUnknownMemberType]


async def complete(prompt: str) -> str:
    client = openai.AsyncOpenAI(
        base_url="",
    )
    message: chat.chat_completion_message_param.ChatCompletionMessageParam = {
        "role": "user",
        "content": prompt,
    }

    response = await client.chat.completions.create(
        model="MY_MODEL",
        messages=[message],
    )
    return str(response.choices[0].message.content)

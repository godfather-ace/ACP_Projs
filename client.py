import nest_asyncio
nest_asyncio.apply()
import asyncio
from acp_sdk.client import Client
from acp_sdk.models import Message, MessagePart

async def acp_client() -> None:
    async with Client(base_url="http://localhost:8000") as client:
        run = await client.run_sync(agent="research_agent", input=[Message(parts=[MessagePart(content="Explain Agentic AI in less than 100 words?")])])
        print(run)

if __name__ == "__main__":
    asyncio.run(acp_client())
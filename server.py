from collections.abc import AsyncGenerator
from acp_sdk.models import Message, MessagePart
from acp_sdk.server import Context, RunYield, RunYieldResume, Server
from smolagents import ToolCallingAgent, ToolCollection, CodeAgent, DuckDuckGoSearchTool, LiteLLMModel, VisitWebpageTool
import nest_asyncio
nest_asyncio.apply()
import logging 

server = Server()

model = LiteLLMModel(
    model_id="ollama_chat/qwen3:4b",
    api_base="http://localhost:11434",
    num_ctx=4096,
)

@server.agent()
async def research_agent(input: list[Message], context: Context) -> AsyncGenerator[RunYield, RunYieldResume]:
    "This is a ResearchAgent which assists users in understanding topics with ease."
    agent = CodeAgent(tools=[DuckDuckGoSearchTool(), VisitWebpageTool()], model=model)
    prompt = input[0].parts[0].content
    response = agent.run(prompt)
    yield Message(parts=[MessagePart(content=str(response))])

if __name__ == "__main__":
    server.run()
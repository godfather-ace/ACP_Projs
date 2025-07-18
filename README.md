### Step 1: Environment Setup 
Initialise a uv project, create and activate a virtual environment, and install the required libraries using the commands provided below (in a terminal) - 
```
mkdir ACP_projs  
cd ACP_projs 
uv init 
uv venv 
source .venv/bin/activate
uv add acp_sdk load_dotenv nest-asyncio 'smolagents[litellm]' duckduckgo-search
```

### Step 2: Ollama Setup and LLM Download 
Make sure you have Ollama application up and running so that qwen3:4b model can be pulled and used in our implementation. Use the following commands to download qwen3:4b model and check if it’s download properly (in a terminal) - 
```
ollama pull qwen3:4b
ollama list
```

### Step 3: Server and Client Setup
We will create two python scripts server.py and client.py for using ACP to create, run our agent and interact with it using HTTP requests. 

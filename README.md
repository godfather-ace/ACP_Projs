sachintripathi@Sachins-MacBook-Air Py_files % mkdir ACP_projs   
sachintripathi@Sachins-MacBook-Air Py_files % cd ACP_projs
sachintripathi@Sachins-MacBook-Air ACP_projs % uv init
Initialized project `acp-projs`
sachintripathi@Sachins-MacBook-Air ACP_projs % uv venv
Using CPython 3.13.3 interpreter at: /opt/homebrew/opt/python@3.13/bin/python3.13
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
sachintripathi@Sachins-MacBook-Air ACP_projs % source .venv/bin/activate
sachintripathi@Sachins-MacBook-Air ACP_projs % uv add acp_sdk load_dotenv nest-asyncio 'smolagents[litellm]' duckduckgo-search 


ollama pull qwen3:4b
ollama list

uv run server.py
uv run client.py


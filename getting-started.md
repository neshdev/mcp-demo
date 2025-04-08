# Getting start guide

clone the repo

## Prereqs
Install the following:
* [uv](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_1)
* [npm](https://screenshot.googleplex.com/7ELY7kaX8xHZiHJ)
## Start the MCP Server

### Cli

Run the following command `mcp dev main.py` or  
Run the following command `uv run mcp dev main.py`

## Using the inspector

On your cloudtop, visit http://127.0.0.1:6274

1. Fill in the following configurations (Ex: https://screenshot.googleplex.com/6acELasoYjDHv4g)
```text
Transport type: STDIO
Command: uv
Arguments: run --active mcp run main.py
```
1. Click Connect
1. View tabs in main section: Resources, prompts, tools. 

## Other Clients

See supported clients:
https://modelcontextprotocol.io/clients

* VSCode - https://code.visualstudio.com/docs/copilot/chat/mcp-servers
* Ryder - https://plugins.jetbrains.com/plugin/26071-mcp-server

## Docs

* https://modelcontextprotocol.io/introduction
* https://modelcontextprotocol.io/introduction#general-architecture
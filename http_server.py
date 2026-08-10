#!/usr/bin/env python3
"""
Streamable HTTP — MCP Server over HTTP.

Runs the 17-API gateway as a public Streamable HTTP MCP endpoint
so AI agents and MCP directories (Smithery, Glama, etc.) can
discover, connect, and use the tools over the network.

Run:  uvicorn http_server:app --host 0.0.0.0 --port 8900
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

from mcp_server import APIS, call_api  # reuse the tool definitions + call logic

# Disable DNS-rebinding host validation so the endpoint works behind
# the Agent37 reverse proxy (which uses its own public Host header).
security = TransportSecuritySettings(
    enable_dns_rebinding_protection=False,
)

# Build a FastMCP wrapping the same tools
mcp = FastMCP("api-gateway", transport_security=security)

def _make_tool(name: str, api_def: dict):
    """Build a single-tool handler bound to one API definition."""
    async def handler(**kwargs):
        result = await call_api(api_def, kwargs)
        return result
    handler.__name__ = name
    handler.__qualname__ = name
    return handler

for api_id, api_def in APIS.items():
    name = api_def["name"]
    desc = f"{api_def['description']} [Cost: {api_def['pricing']}]"
    tool_fn = _make_tool(name, api_def)
    mcp.tool(name=name, description=desc)(tool_fn)

app = mcp.streamable_http_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8900)

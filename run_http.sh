#!/bin/bash
# Launch the MCP server over Streamable HTTP on port 8900
export WEBSITE_INTEL_KEY="wia_admin_c07351920198c21708653ff7c7c6e81a"
export MARKETING_BUNDLE_KEY="mab_mcp_admin_2e8f94c1a73b"
cd /home/node/.minions/workspace/api-mcp-server
exec /home/node/.minions/workspace/marketing-api-bundle/venv/bin/python3 -m uvicorn http_server:app --host 0.0.0.0 --port 8900

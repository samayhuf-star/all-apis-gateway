#!/bin/bash
# Launch the MCP server over Streamable HTTP on port 8900.
# API keys are read from the environment (set WEBSITE_INTEL_KEY / MARKETING_BUNDLE_KEY).
# Do NOT hardcode secrets here.
cd "$(dirname "$0")"
exec /home/node/.minions/workspace/marketing-api-bundle/venv/bin/python3 -m uvicorn http_server:app --host 0.0.0.0 --port 8900

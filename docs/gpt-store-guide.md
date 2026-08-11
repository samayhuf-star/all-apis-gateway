# OpenAI GPT Store Registration Guide

Your 17 APIs are already AI-agent discoverable via `.well-known/ai-plugin.json` on both droplets. To register them as **GPT Actions** in the OpenAI GPT Store:

## Step 1 — Create a GPT Action for Website Intelligence

1. Go to **https://chatgpt.com/gpts/editor**
2. Click **Create a GPT** → **Configure**
3. Under **Actions**, click **Add action**
4. Import from URL:
   ```
   https://momentumbysamay.online/api/website-intel/openapi.json
   ```
5. Set **Authentication**: `API Key` → Header name: `X-API-Key`
6. Paste in the admin key from your deployment's admin endpoint (see README / env.example)
7. Set **Privacy Policy URL**: `https://momentumbysamay.online/api/website-intel/privacy` (or your own)
8. Save GPT

## Step 2 — Create a GPT Action for Marketing Bundle

1. Create another GPT from the GPT editor
2. Import OpenAPI from:
   ```
   https://momentumbysamay.online/api/marketing/openapi.json
   ```
3. **Authentication**: `API Key` → `X-API-Key`
4. Use the marketing bundle admin key from your deployment (env.example)
5. Save GPT

## Step 3 — Publish to GPT Store

1. Click **Publish** → **Anyone with a link** (private) or **Public** (Store)
2. Fill description: "17 AI-powered APIs for website intelligence and marketing data extraction"
3. For **Category**: choose "Developer Tools" or "Business"

## Alternative: Direct Agent Registration

Both droplets already serve **AI agent discovery manifests**:

| Droplet | Manifest URL |
|---------|-------------|
| Website Intel | `https://momentumbysamay.online/api/website-intel/.well-known/ai-plugin.json` |
| Marketing Bundle | `https://momentumbysamay.online/api/marketing/.well-known/ai-plugin.json` |

These are auto-discovered by OpenAI GPT Actions, Claude Code, and any MCP-aware agent. Simply point the agent to the `.well-known/ai-plugin.json` URL.

# API Gateway — 17 APIs for AI Agents

**Single MCP server exposing 17 production APIs behind one public domain.**

All APIs are served at **`https://momentumbysamay.online/api/<apiname>`** (DNS →
`167.71.22.95`), a single nginx gateway with Let's Encrypt HTTPS. The
Website Intelligence bundle runs on droplet 1; Marketing, Web Scraper, PDF and
Email Verify are reverse-proxied from droplet 2.

---

## 🚀 What This Is

An **MCP (Model Context Protocol) server** that wraps **17 real, deployed APIs** into MCP tools. Any AI agent with MCP support can discover, call, and pay for these APIs programmatically.

### How AI Agents Use It

1. **Connect** — Agents connect via MCP (stdio or HTTP)
2. **Discover** — Agent calls `list_tools()` → sees 20 tools
3. **Pay** — Agent calls `generate_invoice` + `check_balance` for crypto payment
4. **Use** — Agent calls any API tool, credits auto-deduct

### Revenue Model

| Channel | How It Makes Money | Status |
|---------|-------------------|--------|
| **🤖 AI Agents via MCP** | Agents discover tools → generate invoice → send USDC → use APIs | ✅ LIVE |
| **🤖 AI Agents via `.well-known/ai-plugin.json`** | OpenAI GPT Agents auto-discover APIs | ✅ LIVE |
| RapidAPI Marketplace | $29–$199/mo subscriptions | 📦 Ready — needs RapidAPI provider account |
| **Apify Store** | Per-run pricing | 📦 Ready, not published |
| **api.market** | Global API marketplace | 📦 Ready (Redis issues) |

---

## 📋 API Inventory — 17 APIs + 3 Payment Tools

### 🖥️ Website Intelligence (`/api/website-intel`) — 10 APIs

| # | MCP Tool | API | Description | Price |
|---|----------|-----|-------------|-------|
| 1 | `website_to_markdown` | Website → Markdown | Convert any web page to clean Markdown | $0.0005 |
| 2 | `website_metadata` | Website Metadata | Meta tags, OG, Twitter Cards, headings, images, favicon | $0.0002 |
| 3 | `technology_detector` | Technology Detector | CMS, frameworks, analytics, CDN, server tech | $0.0003 |
| 4 | `contact_extractor` | Contact Extractor | Emails, phones, social links, addresses | $0.0005 |
| 5 | `ai_website_summary` | AI Website Summary | Structured summary + optional AI narrative | $0.002 |
| 6 | `opengraph_extractor` | OpenGraph Extractor | OG tags, Twitter Cards, social preview data | $0.0002 |
| 7 | `robots_txt_parser` | Robots.txt Parser | Crawl rules, disallowed paths, sitemap URLs | $0.0002 |
| 8 | `sitemap_parser` | Sitemap Parser | Discover & parse XML sitemaps | $0.0005 |
| 9 | `ssl_checker` | SSL Checker | Certificate details, expiry, security grade | $0.0002 |
| 10 | `dns_lookup` | DNS Lookup | A, AAAA, MX, NS, CNAME, TXT, subdomain discovery | $0.0002 |

**Payment:** Solana USDC ($USDC on Solana mainnet)

### 📊 Marketing API Bundle (`/api/marketing`) — 7 APIs

| # | MCP Tool | API | Description | Price |
|---|----------|-----|-------------|-------|
| 11 | `marketing_contact_extractor` | Marketing Contact Extractor | Emails, phones, social profiles, address | $0.0005 |
| 12 | `google_maps_reviews` | Google Maps Reviews | Ratings, reviews, business metadata by Place ID or search | $0.001 |
| 13 | `business_metadata` | Business Metadata | Category, founding year, hours, certifications, payments | $0.0003 |
| 14 | `seo_audit` | SEO Audit | On-page SEO analysis with scoring (0–100) | $0.0005 |
| 15 | `ai_company_summary` | AI Company Summary | AI-powered business overview + narrative | $0.002 |
| 16 | `marketing_technology_detector` | Technology Detector | CMS, frameworks, analytics, hosting | $0.0003 |
| 17 | `citation_checker` | Citation Checker | Directory presence across 10+ platforms + NAP scoring | $0.001 |

**Payment:** Solana USDC ($USDC on Solana mainnet)

### 💰 Payment/Management Tools — Free

| # | MCP Tool | Description |
|---|----------|-------------|
| 18 | `get_pricing` | Get current pricing for all APIs |
| 19 | `generate_invoice` | Generate Solana USDC payment invoice |
| 20 | `check_balance` | Check credit balance for an API key |

---

## 🔧 Quick Start

### For AI Agents (MCP-native)

Configure the MCP server in your agent:

```json
{
  "mcpServers": {
    "all-apis-gateway": {
      "command": "python3",
      "args": ["/path/to/mcp_server.py"],
      "env": {
        "WEBSITE_INTEL_BASE": "https://momentumbysamay.online/api/website-intel",
        "WEBSITE_INTEL_KEY": "YOUR_WEBSITE_INTEL_KEY",
        "MARKETING_BUNDLE_BASE": "https://momentumbysamay.online/api/marketing",
        "MARKETING_BUNDLE_KEY": "YOUR_MARKETING_KEY"
      }
    }
  }
}
```

### For Developers (REST APIs directly)

**Website Intelligence:**
```bash
# Get an admin key (one-time)
curl -X POST https://momentumbysamay.online/api/website-intel/api/v1/auth/generate-key \
  -H "Content-Type: application/json" \
  -d '{"name":"my-app","tier":"admin"}'

# Call an API
curl -X POST https://momentumbysamay.online/api/website-intel/api/v1/dns-lookup \
  -H "X-API-Key: *** \
  -H "Content-Type: application/json" \
  -d '{"domain": "example.com"}'

# Get pricing
curl https://momentumbysamay.online/api/website-intel/api/v1/payments/pricing

# Generate payment invoice
curl -X POST https://momentumbysamay.online/api/website-intel/api/v1/payments/invoice \
  -H "Content-Type: application/json" \
  -d '{"api_key": "YOUR_KEY", "amount_usdc": 5.0}'
```

**Marketing Bundle:**
```bash
curl -X POST https://momentumbysamay.online/api/marketing/api/v1/contact-extractor \
  -H "X-API-Key: *** \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

---

## 💳 Crypto Payment Flow

Both API bundles accept **Solana USDC** for AI agents.

```
┌─────────────────────────────────────────────┐
│  Payment Flow                                 │
│                                               │
│  1. Agent: POST /payments/invoice             │
│     → Gets: {wallet_address, memo}            │
│                                               │
│  2. Agent: Send USDC to wallet + memo         │
│     (On Solana mainnet)                       │
│                                               │
│  3. Agent: POST /payments/verify              │
│     → Credits added to API key                │
│                                               │
│  4. Agent: Call any API with X-API-Key        │
│     → Credits auto-deduct per call            │
└─────────────────────────────────────────────┘
```

**Treasury Wallet:** Configured on the droplet (set `TREASURY_WALLET` env var)

**Token:** `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` (Solana USDC)

---

## 📊 Rate Limits

| Plan | Requests/sec | Daily Limit | Price |
|------|-------------|-------------|-------|
| Free | 2 | 100 | $0 |
| Starter | 10 | 5,000 | $29/mo |
| Growth | 30 | 25,000 | $79/mo |
| Enterprise | 100 | 100,000 | $199/mo |

---

## 🏗 Architecture

```
MCP Client (Claude Code, Cline, Hermes, any MCP agent)
    │
    ▼
┌──────────────────────────────┐
│  MCP Server (api-gateway)    │
│  - 20 tools                  │
│  - Auth injection            │
│  - Error handling            │
│  - Pricing/cost display      │
└──────┬───────────────────────┘
       │
       ├──→ momentumbysamay.online/api/website-intel: Website Intelligence (10 APIs + payments)
       │       POST .../api/website-intel/api/v1/{endpoint}
       │       POST .../api/website-intel/api/v1/payments/{invoice,verify,balance,pricing}
       │       GET  .../api/website-intel/.well-known/ai-plugin.json
       │
       └──→ momentumbysamay.online/api/marketing: Marketing API Bundle (7 APIs + payments)
               POST .../api/marketing/api/v1/{endpoint}
               POST .../api/marketing/api/v1/payments/{invoice,verify,balance,pricing}
               GET  .../api/marketing/.well-known/ai-plugin.json
```

---

### 📦 Marketplace Publishing Guides

Ready-to-use docs for registering on each platform:

| Marketplace | Guide | Status |
|------------|-------|--------|
| **OpenAI GPT Store** | [`docs/gpt-store-guide.md`](docs/gpt-store-guide.md) | 📝 Step-by-step |
| **RapidAPI** | [`docs/rapidapi-publish-guide.md`](docs/rapidapi-publish-guide.md) | 📝 Upload-ready spec + copy |
| **Apify Store** | See Apify console links below | 🔴 Needs Store terms accepted |
| **api.market** | Pre-prepared OpenAPI specs at `/home/node/api-market-specs/` | 🔴 Redis outage |

### 🪙 Solana USDC Payments

Docs: [`docs/setup-wallet.md`](docs/setup-wallet.md)

Both bundles accept Solana USDC (token `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`):
- `POST .../api/website-intel/api/v1/payments/invoice` — generate wallet + memo
- `POST .../api/website-intel/api/v1/payments/verify` — verify payment → add credits
- `POST .../api/website-intel/api/v1/payments/balance` — check balance
- `GET .../api/website-intel/api/v1/payments/pricing` — per-endpoint pricing

**Real Solana treasury wallet on BOTH bundles:** `F8tmJqiyEpcSbAbWef3XhsknsnW4gxb2gv6K8ZxEfgE`

## 🌐 AI Agent Discovery Endpoints

Each bundle exposes AI agent discovery files under its domain path:

| Endpoint | Description |
|----------|-------------|
| `.../api/<apiname>/.well-known/ai-plugin.json` | OpenAI GPT Actions manifest |
| `.../api/<apiname>/.well-known/openapi.json` | OpenAPI spec for AI consumption |
| `.../api/<apiname>/api/v1/payments/pricing` | Per-endpoint USDC pricing |
| `.../api/<apiname>/health` | Health check (no auth) |
| `.../api/<apiname>/status` | Component status (no auth) |

---

## 📈 Monitoring

| Endpoint | Description | Auth |
|----------|-------------|------|
| `GET /health` | Service health check | None |
| `GET /status` | Component status (cache, auth, payments) | None |
| `GET /metrics` | Operational metrics (P50/P95/P99, cache hit rate) | Admin key |
| `GET /dashboard` | Usage dashboard HTML | Admin key |

---

## 🔐 Authentication

- **Header:** `X-API-Key: <your-key>` (recommended)
- **Bearer:** `Authorization: Bearer <your-key>`
- **Query param:** `?api_key=<your-key>`

Tiers: `free`, `starter`, `growth`, `enterprise`, `admin`

---

## 📜 License

Private — Samay Vashisht. All APIs and code proprietary.

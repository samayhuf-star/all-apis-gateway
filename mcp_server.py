#!/usr/bin/env python3
"""
MCP Server — Website Intelligence + Marketing API Bundle

Exposes 17 APIs across 2 droplets as MCP tools for AI agents.
Agents discover and use these tools like any MCP tool.

Features:
- Auto-generates MCP tools from API definitions
- Handles auth (API keys, crypto payments)
- Structured error responses
- Includes per-API pricing so agents can estimate costs
"""

import os
import sys
import json
import asyncio
import httpx
from typing import Any, Optional
from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
from mcp.types import (
    Tool,
    TextContent,
    CallToolResult,
)

# =============================================================================
# Configuration
# =============================================================================

# Website Intelligence APIs (167.71.22.95) — 10 APIs + payments
WEBSITE_INTEL_BASE = os.getenv("WEBSITE_INTEL_BASE", "http://167.71.22.95")
WEBSITE_INTEL_KEY = os.getenv("WEBSITE_INTEL_KEY", "")

# Marketing API Bundle (64.227.2.61) — 7 APIs + payments
MARKETING_BUNDLE_BASE = os.getenv("MARKETING_BUNDLE_BASE", "http://64.227.2.61")
MARKETING_BUNDLE_KEY = os.getenv("MARKETING_BUNDLE_KEY", "")

# Admin keys for self-registration
ADMIN_API_KEY = os.getenv("ADMIN_API_KEY", "")

# =============================================================================
# API Definitions — Each API is a tool the MCP exposes
# =============================================================================

APIS = {
    # ── Website Intelligence (167.71.22.95) ──
    "website_to_markdown": {
        "name": "website_to_markdown",
        "description": "Convert any web page to clean, structured Markdown. Returns the page title, description, and full markdown content.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "Website URL (e.g., https://example.com)"}
            },
            "required": ["url"]
        },
        "endpoint": f"{WEBSITE_INTEL_BASE}/api/v1/website-to-markdown",
        "key": WEBSITE_INTEL_KEY,
        "pricing": "$0.0005",
    },
    "website_metadata": {
        "name": "website_metadata",
        "description": "Extract comprehensive metadata from any website: meta tags, OpenGraph, Twitter Cards, headings (H1-H6), images (with counts/SRSet), canonical URL, language, favicon, and structured data.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "Website URL (e.g., https://example.com)"}
            },
            "required": ["url"]
        },
        "endpoint": f"{WEBSITE_INTEL_BASE}/api/v1/website-metadata",
        "key": WEBSITE_INTEL_KEY,
        "pricing": "$0.0002",
    },
    "technology_detector_web": {
        "name": "technology_detector",
        "description": "Detect the technology stack used by any website: CMS, JavaScript frameworks, analytics tools, CDN providers, web servers, and UI libraries. Returns confidence scores per technology.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "Website URL (e.g., https://example.com)"}
            },
            "required": ["url"]
        },
        "endpoint": f"{WEBSITE_INTEL_BASE}/api/v1/technology-detector",
        "key": WEBSITE_INTEL_KEY,
        "pricing": "$0.0003",
    },
    "contact_extractor_web": {
        "name": "contact_extractor",
        "description": "Extract all contact information from a business website: email addresses, phone numbers, social media links (LinkedIn, Twitter, Facebook, Instagram, YouTube, GitHub), and physical addresses. Supports deep crawling of /contact, /about, /team pages.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "Website URL (e.g., https://example.com)"},
                "deep_crawl": {"type": "boolean", "description": "Enable deep crawl of /contact and /about pages for more contacts", "default": False}
            },
            "required": ["url"]
        },
        "endpoint": f"{WEBSITE_INTEL_BASE}/api/v1/contact-extractor",
        "key": WEBSITE_INTEL_KEY,
        "pricing": "$0.0005",
    },
    "ai_website_summary": {
        "name": "ai_website_summary",
        "description": "Generate a structured AI-powered summary of any website: company overview, industry classification, key offerings, target audience. Optionally generate an AI narrative with business analysis. Costs more due to LLM inference.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "Website URL (e.g., https://example.com)"},
                "use_ai": {"type": "boolean", "description": "Generate AI-powered narrative summary (extra cost)", "default": False}
            },
            "required": ["url"]
        },
        "endpoint": f"{WEBSITE_INTEL_BASE}/api/v1/ai-website-summary",
        "key": WEBSITE_INTEL_KEY,
        "pricing": "$0.002 (with AI: $0.005)",
    },
    "opengraph_extractor": {
        "name": "opengraph_extractor",
        "description": "Extract Open Graph (og:) and Twitter Card (twitter:) tags from any website. Returns social preview data: title, description, image, URL, site_name, type, and Twitter-specific tags.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "Website URL (e.g., https://example.com)"}
            },
            "required": ["url"]
        },
        "endpoint": f"{WEBSITE_INTEL_BASE}/api/v1/opengraph-extractor",
        "key": WEBSITE_INTEL_KEY,
        "pricing": "$0.0002",
    },
    "robots_txt_parser": {
        "name": "robots_txt_parser",
        "description": "Fetch and parse robots.txt from any website. Returns crawl rules per user-agent, disallowed/allowed paths, crawl delays, sitemap URLs, and accessibility analysis for key pages.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "Website URL to fetch robots.txt from (e.g., https://example.com)"}
            },
            "required": ["url"]
        },
        "endpoint": f"{WEBSITE_INTEL_BASE}/api/v1/robots-txt-parser",
        "key": WEBSITE_INTEL_KEY,
        "pricing": "$0.0002",
    },
    "sitemap_parser": {
        "name": "sitemap_parser",
        "description": "Discover and parse XML sitemaps from any website. Supports standard sitemap.xml, sitemap index files, and common alternative sitemap paths. Returns all URLs with lastmod dates, change frequency, and priority.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "Website URL to discover sitemaps from (e.g., https://example.com)"}
            },
            "required": ["url"]
        },
        "endpoint": f"{WEBSITE_INTEL_BASE}/api/v1/sitemap-parser",
        "key": WEBSITE_INTEL_KEY,
        "pricing": "$0.0005",
    },
    "ssl_checker": {
        "name": "ssl_checker",
        "description": "Check SSL/TLS certificate details for any domain. Returns: issuer, subject, validity period, days to expiry, cipher suite, protocol (TLS 1.2/1.3), certificate type, security grade (A+ through F), and SANs.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "domain": {"type": "string", "description": "Domain name to check SSL for (e.g., example.com)"}
            },
            "required": ["domain"]
        },
        "endpoint": f"{WEBSITE_INTEL_BASE}/api/v1/ssl-checker",
        "key": WEBSITE_INTEL_KEY,
        "pricing": "$0.0002",
    },
    "dns_lookup": {
        "name": "dns_lookup",
        "description": "Perform comprehensive DNS lookups for any domain: A, AAAA, MX (mail servers), NS (name servers), CNAME, TXT records. Also discovers common subdomains (www, mail, blog, api, etc.) and checks DNSSEC status.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "domain": {"type": "string", "description": "Domain name to look up (e.g., example.com)"}
            },
            "required": ["domain"]
        },
        "endpoint": f"{WEBSITE_INTEL_BASE}/api/v1/dns-lookup",
        "key": WEBSITE_INTEL_KEY,
        "pricing": "$0.0002",
    },

    # ── Marketing API Bundle (64.227.2.61) ──
    "contact_extractor_mkt": {
        "name": "marketing_contact_extractor",
        "description": "[Marketing Bundle] Extract business contact information from any website: email addresses, phone numbers, social media profiles (LinkedIn, Twitter, Facebook, Instagram), and physical address.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "Business website URL (e.g., https://company.com)"},
                "deep_crawl": {"type": "boolean", "description": "Deep crawl for more contacts", "default": False}
            },
            "required": ["url"]
        },
        "endpoint": f"{MARKETING_BUNDLE_BASE}/api/v1/contact-extractor",
        "key": MARKETING_BUNDLE_KEY,
        "pricing": "$0.0005",
    },
    "google_maps_reviews": {
        "name": "google_maps_reviews",
        "description": "[Marketing Bundle] Extract reviews, ratings, and business metadata from Google Maps listings. Search by Place ID or by business name + location. Returns ratings, review counts, top reviews, hours, address, phone, and website.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "place_id": {"type": "string", "description": "Google Maps Place ID (optional — provide if known)"},
                "query": {"type": "string", "description": "Business name or search term (used if place_id not provided)"},
                "location": {"type": "string", "description": "City, state or zip for search"}
            }
        },
        "endpoint": f"{MARKETING_BUNDLE_BASE}/api/v1/google-maps-reviews",
        "key": MARKETING_BUNDLE_KEY,
        "pricing": "$0.001",
    },
    "business_metadata": {
        "name": "business_metadata",
        "description": "[Marketing Bundle] Extract comprehensive business profile metadata from a website: company name, description, founding year, industry, business hours, payment methods, certifications, awards, team size, and social profiles.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "Business website URL"}
            },
            "required": ["url"]
        },
        "endpoint": f"{MARKETING_BUNDLE_BASE}/api/v1/business-metadata",
        "key": MARKETING_BUNDLE_KEY,
        "pricing": "$0.0003",
    },
    "seo_audit": {
        "name": "seo_audit",
        "description": "[Marketing Bundle] Run a comprehensive on-page SEO audit on any website: title tag analysis, meta description, heading structure, keyword density, image alt text, internal/external links, page speed indicators, mobile-friendliness signals, and an overall SEO score (0-100) with actionable recommendations.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "Website URL to audit"}
            },
            "required": ["url"]
        },
        "endpoint": f"{MARKETING_BUNDLE_BASE}/api/v1/seo-audit",
        "key": MARKETING_BUNDLE_KEY,
        "pricing": "$0.0005",
    },
    "ai_company_summary": {
        "name": "ai_company_summary",
        "description": "[Marketing Bundle] Generate an AI-powered business summary: company overview, industry classification, key products/services, target market, competitive positioning. Optionally includes an AI-written narrative analysis.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "Business website URL"},
                "use_ai": {"type": "boolean", "description": "Generate AI narrative summary (extra cost)", "default": False}
            },
            "required": ["url"]
        },
        "endpoint": f"{MARKETING_BUNDLE_BASE}/api/v1/company-summary",
        "key": MARKETING_BUNDLE_KEY,
        "pricing": "$0.002 (with AI: $0.005)",
    },
    "technology_detector_mkt": {
        "name": "marketing_technology_detector",
        "description": "[Marketing Bundle] Detect the technology stack used by any business website: CMS platforms, JavaScript frameworks, analytics tools, advertising networks, CRM systems, CDN providers, and hosting infrastructure.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "Website URL to analyze"}
            },
            "required": ["url"]
        },
        "endpoint": f"{MARKETING_BUNDLE_BASE}/api/v1/technology-detector",
        "key": MARKETING_BUNDLE_KEY,
        "pricing": "$0.0003",
    },
    "citation_checker": {
        "name": "citation_checker",
        "description": "[Marketing Bundle] Check a business's citation presence across 10+ major directories (Yelp, YellowPages, BBB, Facebook, Foursquare, SuperPages, MerchantCircle, HotFrog, Manta, Citysearch). Returns NAP (Name, Address, Phone) consistency score and per-directory status.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "Business website URL to check citations for"},
                "business_name": {"type": "string", "description": "Business name (if URL not provided)"},
                "location": {"type": "string", "description": "City/state location"}
            }
        },
        "endpoint": f"{MARKETING_BUNDLE_BASE}/api/v1/citation-checker",
        "key": MARKETING_BUNDLE_KEY,
        "pricing": "$0.001",
    },

    # ── Cross-droplet Payments API ──
    "get_pricing": {
        "name": "get_pricing",
        "description": "Get current pricing for all APIs across both bundles. Returns per-endpoint cost in USDC (Solana) so agents can estimate call costs before making requests.",
        "inputSchema": {
            "type": "object",
            "properties": {}
        },
        "endpoint": f"{WEBSITE_INTEL_BASE}/api/v1/payments/pricing",
        "key": "",
        "pricing": "free",
    },
    "generate_invoice": {
        "name": "generate_invoice",
        "description": "Generate a Solana USDC payment invoice to prepay for API credits. Provide your API key and optional amount. Returns: treasury wallet address, unique memo, and instructions. Send USDC with the memo to receive credits.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "api_key": {"type": "string", "description": "Your API key to link credits to"},
                "amount_usdc": {"type": "number", "description": "Amount of USDC to send (optional, defaults to any amount)"}
            },
            "required": ["api_key"]
        },
        "endpoint": f"{WEBSITE_INTEL_BASE}/api/v1/payments/invoice",
        "method": "POST",
        "key": "",
        "pricing": "free",
    },
    "check_balance": {
        "name": "check_balance",
        "description": "Check your API credit balance in USDC. Returns current balance and total spent so AI agents can track their spending.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "api_key": {"type": "string", "description": "Your API key to check balance for"}
            },
            "required": ["api_key"]
        },
        "endpoint": f"{WEBSITE_INTEL_BASE}/api/v1/payments/balance",
        "key": "",
        "pricing": "free",
    },
}

# =============================================================================
# HTTP client helpers
# =============================================================================

_client = httpx.AsyncClient(timeout=httpx.Timeout(30.0, connect=10.0))


async def call_api(api_def: dict, args: dict) -> dict:
    """
    Call an API endpoint and return the result.
    Handles auth injection, URL construction, and error parsing.
    """
    endpoint = api_def["endpoint"]
    method = api_def.get("method", "POST")
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    # Inject API key if configured
    api_key = api_def.get("key", "")
    if api_key:
        headers["X-API-Key"] = api_key

    # Prepare request body — filter args to match input schema
    body = {}
    schema = api_def["inputSchema"]
    if schema:
        props = schema.get("properties", {})
        required = schema.get("required", [])
        for key in list(props.keys()):
            if key in args:
                body[key] = args[key]

    try:
        if method == "GET":
            resp = await _client.get(endpoint, params=body, headers=headers)
        else:
            resp = await _client.post(endpoint, json=body, headers=headers)

        result = resp.json()
        if resp.status_code >= 400:
            return {"error": True, "status": resp.status_code, "detail": result}

        return result

    except httpx.TimeoutException:
        return {"error": True, "detail": "Request timed out. The source may be slow or unavailable."}
    except httpx.ConnectError:
        return {"error": True, "detail": "Could not connect to the API service. The backend may be down."}
    except json.JSONDecodeError:
        return {"error": True, "detail": "Invalid response from API (not valid JSON)."}
    except Exception as e:
        return {"error": True, "detail": f"Unexpected error: {str(e)}"}


# =============================================================================
# MCP Server
# =============================================================================

server = Server("api-gateway")


@server.list_tools()
async def list_tools() -> list[Tool]:
    """Return all available API tools."""
    tools = []
    for api_id, api_def in APIS.items():
        tools.append(Tool(
            name=api_def["name"],
            description=f"{api_def['description']} [Cost: {api_def['pricing']}]",
            inputSchema=api_def["inputSchema"],
        ))
    return tools


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Execute an API call when the agent invokes a tool."""
    # Find the API definition
    api_def = None
    for api_id, ad in APIS.items():
        if ad["name"] == name:
            api_def = ad
            break

    if not api_def:
        return [TextContent(
            type="text",
            text=json.dumps({"error": True, "detail": f"Unknown tool: {name}"}, indent=2)
        )]

    # Call the API
    result = await call_api(api_def, arguments)
    return [TextContent(
        type="text",
        text=json.dumps(result, indent=2, default=str)
    )]


async def main():
    """Run the MCP server using stdio transport."""
    from mcp.server.stdio import stdio_server
    async with stdio_server() as (read_stream, write_stream):
        async with await server.run(read_stream, write_stream, server.create_initialization_options()):
            await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())

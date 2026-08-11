# Per-API Documentation — 17 APIs for AI Agents

**Single MCP server exposing 17 production APIs across two droplets:**

| Bundle | Base URL | APIs |
|--------|----------|------|
| **Website Intelligence** | `momentumbysamay.online/api/website-intel` | 10 APIs |
| **Marketing Bundle** | `momentumbysamay.online/api/marketing` | 7 APIs |

---

## Authentication

All endpoints require an `X-API-Key` header (or `Authorization: Bearer <key>`).

```bash
curl -X POST http://DROPLET_IP/api/v1/ENDPOINT \
  -H "X-API-Key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

---

# 📡 Website Intelligence (`/api/website-intel`) — 10 APIs

All endpoints: `POST https://momentumbysamay.online/api/website-intel/api/v1/{slug}`

---

## 1. website_to_markdown

| Field | Value |
|-------|-------|
| **Description** | Convert any web page to clean, structured Markdown. Returns title, description, word count, and full markdown content. |
| **Endpoint** | `POST https://momentumbysamay.online/api/website-intel/api/v1/website-to-markdown` |
| **Pricing** | `$0.0005` |
| **Input Parameters** | `url` (string, required) — Website URL to convert |

**Example curl:**
```bash
curl -X POST https://momentumbysamay.online/api/website-intel/api/v1/website-to-markdown \
  -H "X-API-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

**Example Response:**
```json
{
  "url": "https://example.com",
  "success": true,
  "content_type": "text/markdown",
  "title": "Example Domain",
  "word_count": 20,
  "char_count": 131,
  "markdown": "# Example Domain\n\nThis domain is for use in documentation examples without needing permission. Avoid use in operations.\n\nLearn more"
}
```

---

## 2. website_metadata

| Field | Value |
|-------|-------|
| **Description** | Extract comprehensive metadata: meta tags, OpenGraph, Twitter Cards, headings (H1–H6), images (with counts/SRSet), canonical URL, language, favicon, structured data, and link analysis. |
| **Endpoint** | `POST https://momentumbysamay.online/api/website-intel/api/v1/website-metadata` |
| **Pricing** | `$0.0002` |
| **Input Parameters** | `url` (string, required) — Website URL to analyze |

**Example curl:**
```bash
curl -X POST https://momentumbysamay.online/api/website-intel/api/v1/website-metadata \
  -H "X-API-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

**Example Response:**
```json
{
  "url": "https://example.com",
  "success": true,
  "metadata": {
    "title": "Example Domain",
    "description": null,
    "keywords": null,
    "og": {},
    "twitter": {},
    "canonical": null,
    "robots": null,
    "url": "https://example.com"
  },
  "headings": { "h1": ["Example Domain"], "h2": [], "h3": [], "h4": [], "h5": [], "h6": [] },
  "images": { "total_images": 0, "images_missing_alt": 0, "images_with_lazy_loading": 0 },
  "links": {
    "internal_links": 0,
    "external_links": 1,
    "external_link_list": [{ "url": "https://iana.org/domains/example", "text": "Learn more", "nofollow": false }]
  },
  "contacts": { "emails": [], "phones": [], "social_links": {}, "address": null },
  "language": "en",
  "favicon": "data:,",
  "page_size_bytes": 559,
  "http_status": 200
}
```

---

## 3. technology_detector

| Field | Value |
|-------|-------|
| **Description** | Detect the technology stack: CMS, JavaScript frameworks, analytics tools, CDN providers, web servers, and UI libraries. Returns confidence scores per technology. |
| **Endpoint** | `POST https://momentumbysamay.online/api/website-intel/api/v1/technology-detector` |
| **Pricing** | `$0.0003` |
| **Input Parameters** | `url` (string, required) — Website URL to analyze |

**Example curl:**
```bash
curl -X POST https://momentumbysamay.online/api/website-intel/api/v1/technology-detector \
  -H "X-API-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

**Example Response:**
```json
{
  "url": "https://example.com",
  "success": true,
  "technologies": {},
  "categorized": { "cms": [], "frameworks": [], "analytics": [], "cdn": [], "ecommerce": [], "other": [] },
  "http_headers": { "server": null, "x_powered_by": null },
  "ssl_enabled": true,
  "redirected": false,
  "final_url": "https://example.com",
  "http_status": 200,
  "technology_count": 0
}
```

---

## 4. contact_extractor

| Field | Value |
|-------|-------|
| **Description** | Extract all contact information: email addresses, phone numbers, social media links (LinkedIn, Twitter, Facebook, Instagram, YouTube, GitHub), and physical addresses. Supports deep crawling of `/contact`, `/about`, `/team` pages. |
| **Endpoint** | `POST https://momentumbysamay.online/api/website-intel/api/v1/contact-extractor` |
| **Pricing** | `$0.0005` |
| **Input Parameters** | `url` (string, required) — Website URL; `deep_crawl` (boolean, optional, default: `false`) — Enable deep crawl for more contacts |

**Example curl:**
```bash
curl -X POST https://momentumbysamay.online/api/website-intel/api/v1/contact-extractor \
  -H "X-API-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com", "deep_crawl": false}'
```

**Example Response:**
```json
{
  "url": "https://example.com",
  "success": true,
  "contacts": {
    "emails": [],
    "phones": [],
    "social_links": {},
    "address": null
  },
  "total_contact_points": 0,
  "source_pages": ["https://example.com"]
}
```

---

## 5. ai_website_summary

| Field | Value |
|-------|-------|
| **Description** | Generate a structured AI-powered summary: company overview, industry classification, key offerings, target audience. Optionally generate an AI narrative with business analysis. Costs more due to LLM inference. |
| **Endpoint** | `POST https://momentumbysamay.online/api/website-intel/api/v1/ai-website-summary` |
| **Pricing** | `$0.002` (with AI narrative: `$0.005`) |
| **Input Parameters** | `url` (string, required) — Website URL; `use_ai` (boolean, optional, default: `false`) — Generate AI-powered narrative summary |

**Example curl:**
```bash
curl -X POST https://momentumbysamay.online/api/website-intel/api/v1/ai-website-summary \
  -H "X-API-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com", "use_ai": false}'
```

**Example Response:**
```json
{
  "url": "https://example.com",
  "success": true,
  "title": "Example Domain",
  "description": "This domain is for use in ...",
  "summary": "Example Domain is a ...",
  "ai_generated": false
}
```

---

## 6. opengraph_extractor

| Field | Value |
|-------|-------|
| **Description** | Extract Open Graph (`og:`) and Twitter Card (`twitter:`) tags. Returns social preview data: title, description, image, URL, site_name, type, and Twitter-specific tags with preview quality analysis. |
| **Endpoint** | `POST https://momentumbysamay.online/api/website-intel/api/v1/opengraph-extractor` |
| **Pricing** | `$0.0002` |
| **Input Parameters** | `url` (string, required) — Website URL |

**Example curl:**
```bash
curl -X POST https://momentumbysamay.online/api/website-intel/api/v1/opengraph-extractor \
  -H "X-API-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

**Example Response:**
```json
{
  "url": "https://example.com",
  "success": true,
  "opengraph": {
    "title": null,
    "description": null,
    "type": null,
    "url": "https://example.com",
    "image": null,
    "site_name": null,
    "locale": null,
    "twitter_card": null,
    "twitter_site": null,
    "twitter_creator": null,
    "raw_og": null,
    "raw_twitter": null
  },
  "social_preview": {
    "title": "Example Domain",
    "description": null,
    "image": null,
    "twitter_card": null
  },
  "preview_analysis": {
    "quality": "fair",
    "issues": [
      "Missing description — shared links won't have a summary",
      "Missing Open Graph image — shared links won't show a preview image",
      "Missing og:type — defaults to 'website'"
    ],
    "issue_count": 3
  }
}
```

---

## 7. robots_txt_parser

| Field | Value |
|-------|-------|
| **Description** | Fetch and parse `robots.txt` from any website. Returns crawl rules per user-agent, disallowed/allowed paths, crawl delays, sitemap URLs, and key page accessibility analysis. |
| **Endpoint** | `POST https://momentumbysamay.online/api/website-intel/api/v1/robots-txt-parser` |
| **Pricing** | `$0.0002` |
| **Input Parameters** | `url` (string, required) — Website URL to fetch `robots.txt` from |

**Example curl:**
```bash
curl -X POST https://momentumbysamay.online/api/website-intel/api/v1/robots-txt-parser \
  -H "X-API-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

**Example Response:**
```json
{
  "url": "https://example.com",
  "robots_url": "https://example.com/robots.txt",
  "success": true,
  "exists": true,
  "raw_length": 559,
  "total_rules": 0,
  "user_agents_found": [],
  "rules": [],
  "sitemaps": [],
  "crawl_delay": null,
  "key_page_access": {
    "/": { "label": "Homepage", "allowed": true, "disallowed_reason": null },
    "/contact": { "label": "Contact page", "allowed": true, "disallowed_reason": null },
    "/about": { "label": "About page", "allowed": true, "disallowed_reason": null },
    "/privacy": { "label": "Privacy policy", "allowed": true, "disallowed_reason": null },
    "/terms": { "label": "Terms of service", "allowed": true, "disallowed_reason": null },
    "/admin": { "label": "Admin area", "allowed": true, "disallowed_reason": null },
    "/wp-admin": { "label": "WordPress admin", "allowed": true, "disallowed_reason": null }
  },
  "http_status": 404
}
```

---

## 8. sitemap_parser

| Field | Value |
|-------|-------|
| **Description** | Discover and parse XML sitemaps. Supports standard `sitemap.xml`, sitemap index files, and common alternative paths. Returns all URLs with lastmod dates, change frequency, and priority. |
| **Endpoint** | `POST https://momentumbysamay.online/api/website-intel/api/v1/sitemap-parser` |
| **Pricing** | `$0.0005` |
| **Input Parameters** | `url` (string, required) — Website URL to discover sitemaps from |

**Example curl:**
```bash
curl -X POST https://momentumbysamay.online/api/website-intel/api/v1/sitemap-parser \
  -H "X-API-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

**Example Response:**
```json
{
  "url": "https://example.com",
  "success": true,
  "stats": {
    "total_urls": 0,
    "total_sitemaps": 0,
    "indexed_sitemaps": 0,
    "errors": []
  },
  "url_analysis": {
    "top_level_pages": 0,
    "by_depth": {},
    "by_type": { "pages": 0, "posts": 0, "categories": 0, "products": 0, "images": 0, "other": 0 },
    "average_depth": 0
  },
  "sample_urls": [],
  "all_urls": []
}
```

---

## 9. ssl_checker

| Field | Value |
|-------|-------|
| **Description** | Check SSL/TLS certificate details: issuer, subject, validity period, days to expiry, cipher suite, protocol (TLS 1.2/1.3), certificate type, security grade (A+ through F), and SANs. |
| **Endpoint** | `POST https://momentumbysamay.online/api/website-intel/api/v1/ssl-checker` |
| **Pricing** | `$0.0002` |
| **Input Parameters** | `domain` (string, required) — Domain name to check SSL for (e.g., `example.com`) |

**Example curl:**
```bash
curl -X POST https://momentumbysamay.online/api/website-intel/api/v1/ssl-checker \
  -H "X-API-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": "example.com"}'
```

**Example Response:**
```json
{
  "domain": "example.com",
  "success": true,
  "has_ssl": true,
  "certificate": {
    "subject": { "common_name": "example.com", "organization": "", "country": "" },
    "issuer": { "organization": "SSL Corporation", "common_name": "Cloudflare TLS Issuing ECC CA 3" },
    "serial_number": "0624D0AB311558780B7D5213B9631831",
    "valid_from": "2026-07-29T22:10:08+00:00",
    "valid_to": "2026-10-27T22:17:21+00:00",
    "days_remaining": 78,
    "days_valid_total": 90,
    "pct_validity_elapsed": 12.2,
    "is_expired": false,
    "is_wildcard": true,
    "subject_alt_names": ["example.com", "*.example.com"],
    "cn_matches_domain": true,
    "san_matches_domain": true
  },
  "connection": {
    "protocol": "TLSv1.3",
    "cipher": "TLS_AES_256_GCM_SHA384",
    "cipher_bits": 256,
    "resolved_ip": "104.20.23.154",
    "latency_ms": 17.8
  },
  "security": {
    "score": 100,
    "grade": "A+",
    "problems": [],
    "downgrades": []
  }
}
```

---

## 10. dns_lookup

| Field | Value |
|-------|-------|
| **Description** | Perform comprehensive DNS lookups: A, AAAA, MX (mail servers), NS (name servers), CNAME, TXT records. Also discovers common subdomains (www, mail, blog, api, etc.) and checks DNSSEC status. |
| **Endpoint** | `POST https://momentumbysamay.online/api/website-intel/api/v1/dns-lookup` |
| **Pricing** | `$0.0002` |
| **Input Parameters** | `domain` (string, required) — Domain name to look up (e.g., `example.com`) |

**Example curl:**
```bash
curl -X POST https://momentumbysamay.online/api/website-intel/api/v1/dns-lookup \
  -H "X-API-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": "example.com"}'
```

**Example Response:**
```json
{
  "domain": "example.com",
  "success": true,
  "records": {
    "A": ["104.20.23.154", "172.66.147.243"],
    "AAAA": ["2606:4700:10::6814:179a", "2606:4700:10::ac42:93f3"],
    "MX": [{ "priority": 0, "host": "" }],
    "NS": ["hera.ns.cloudflare.com", "elliott.ns.cloudflare.com"],
    "CNAME": []
  },
  "latency_ms": 145.1,
  "subdomains": { "www": ["172.66.147.243", "104.20.23.154"] },
  "summary": {
    "ip_addresses_resolved": 4,
    "has_ipv6": true,
    "subdomains_found": 1,
    "mx_records_found": 1,
    "nameservers_found": 2
  },
  "ip_info": [
    { "ip": "104.20.23.154", "type": "IPv4", "hint": "Likely cloudflare" },
    { "ip": "172.66.147.243", "type": "IPv4", "hint": "Likely cloudflare" },
    { "ip": "2606:4700:10::6814:179a", "type": "IPv6", "hint": "Unknown" },
    { "ip": "2606:4700:10::ac42:93f3", "type": "IPv6", "hint": "Unknown" }
  ]
}
```

---

# 📊 Marketing API Bundle (`/api/marketing`) — 7 APIs

All endpoints are `POST` under `https://momentumbysamay.online/api/marketing/api/v1/{slug}`. The service runs on port 8001 behind an nginx reverse proxy at `/marketing/`.

**Batch endpoint:** `POST https://momentumbysamay.online/api/marketing/api/v1/batch` — process up to 100 URLs concurrently.

---

## 11. marketing_contact_extractor

| Field | Value |
|-------|-------|
| **Description** | Extract business contact information: email addresses, phone numbers, social media profiles (LinkedIn, Twitter, Facebook, Instagram), and physical address from a business website. Optionally deep-crawls `/contact` and `/about` pages. |
| **Endpoint** | `POST https://momentumbysamay.online/api/marketing/api/v1/contact-extractor` |
| **Pricing** | `$0.0005` |
| **Input Parameters** | `url` (string, required) — Business website URL; `deep_crawl` (boolean, optional, default: `false`) — Deep crawl for more contacts; `proxy` (string, optional) — Proxy URL |

**Example curl:**
```bash
curl -X POST https://momentumbysamay.online/api/marketing/api/v1/contact-extractor \
  -H "X-API-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://httpbin.org", "deep_crawl": false}'
```

**Example Response:**
```json
{
  "url": "https://httpbin.org",
  "success": true,
  "meta": {
    "title": "httpbin.org",
    "description": null,
    "keywords": null,
    "og": {},
    "twitter": {},
    "canonical": null,
    "robots": null,
    "url": "https://httpbin.org"
  },
  "data": {
    "business_name": "httpbin.org",
    "emails": ["me@kennethreitz.org"],
    "email_count": 1,
    "phones": [],
    "phone_count": 0,
    "social_links": {
      "github": ["https://github.com/requests", "https://github.com/rochacbruno"]
    },
    "address": null,
    "deep_crawl_performed": false,
    "scraped_pages": ["https://httpbin.org"]
  }
}
```

---

## 12. google_maps_reviews

| Field | Value |
|-------|-------|
| **Description** | Extract reviews, ratings, and business metadata from Google Maps listings. Search by Place ID or by business name + location. Returns ratings, review counts, top reviews, hours, address, phone, and website. |
| **Endpoint** | `POST https://momentumbysamay.online/api/marketing/api/v1/google-maps-reviews` |
| **Pricing** | `$0.001` |
| **Input Parameters** | `place_id` (string, required) — Google Maps Place ID (e.g., `ChIJN1t_tDeuEmsRUsoyG83frY4`); `proxy` (string, optional) — Proxy URL |

**Example curl:**
```bash
curl -X POST https://momentumbysamay.online/api/marketing/api/v1/google-maps-reviews \
  -H "X-API-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"place_id": "ChIJN1t_tDeuEmsRUsoyG83frY4"}'
```

**Example Response:**
```json
{
  "place_id": "ChIJN1t_tDeuEmsRUsoyG83frY4",
  "success": true,
  "business_name": "Example Business",
  "rating": 4.5,
  "review_count": 342,
  "top_reviews": [
    { "author": "John D.", "rating": 5, "text": "Great place!", "date": "1 month ago" }
  ],
  "address": "123 Main St, New York, NY 10001",
  "phone": "(212) 555-0100",
  "website": "https://example-business.com",
  "hours": { "monday": "9:00 AM – 5:00 PM", "tuesday": "9:00 AM – 5:00 PM" }
}
```

---

## 13. google_maps_search

| Field | Value |
|-------|-------|
| **Description** | Search Google Maps by business name and location. Returns top matching businesses with ratings, addresses, and contact info. |
| **Endpoint** | `POST https://momentumbysamay.online/api/marketing/api/v1/google-maps-search` |
| **Pricing** | `$0.001` |
| **Input Parameters** | `query` (string, required) — Business name or search term; `location` (string, optional) — City, state, or zip code; `proxy` (string, optional) — Proxy URL |

**Example curl:**
```bash
curl -X POST https://momentumbysamay.online/api/marketing/api/v1/google-maps-search \
  -H "X-API-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "pizza", "location": "New York"}'
```

**Example Response:**
```json
{
  "query": "pizza",
  "location": "New York",
  "success": true,
  "results": [
    {
      "name": "Joe's Pizza",
      "rating": 4.6,
      "reviews": 1200,
      "address": "7 Carmine St, New York, NY 10014",
      "phone": "(212) 555-1234",
      "place_id": "ChIJ...",
      "website": "https://joespizza.com"
    }
  ],
  "result_count": 20
}
```

---

## 14. business_metadata

| Field | Value |
|-------|-------|
| **Description** | Extract comprehensive business profile metadata: company name, description, founding year, industry, business hours, payment methods, certifications, awards, team size, social profiles, and contact info. |
| **Endpoint** | `POST https://momentumbysamay.online/api/marketing/api/v1/business-metadata` |
| **Pricing** | `$0.0003` |
| **Input Parameters** | `url` (string, required) — Business website URL; `proxy` (string, optional) — Proxy URL |

**Example curl:**
```bash
curl -X POST https://momentumbysamay.online/api/marketing/api/v1/business-metadata \
  -H "X-API-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://httpbin.org"}'
```

**Example Response:**
```json
{
  "url": "https://httpbin.org",
  "success": true,
  "data": {
    "name": "httpbin.org",
    "description": null,
    "category": null,
    "founding_year": null,
    "employees": null,
    "payment_methods": [],
    "certifications": [],
    "hours": null,
    "price_range": null,
    "contact": {
      "email": "me@kennethreitz.org",
      "phone": null,
      "address": null,
      "all_emails": ["me@kennethreitz.org"],
      "all_phones": []
    },
    "social": {
      "github": ["https://github.com/requests", "https://github.com/rochacbruno"]
    },
    "meta": {
      "title": "httpbin.org",
      "description": null,
      "keywords": null,
      "og": {},
      "twitter": {},
      "canonical": null,
      "robots": null,
      "url": "https://httpbin.org"
    }
  }
}
```

---

## 15. seo_audit

| Field | Value |
|-------|-------|
| **Description** | Run a comprehensive on-page SEO audit: title tag analysis, meta description, heading structure, keyword density, image alt text, internal/external links, schema validation, robots.txt/sitemap check, page speed indicators, and an overall SEO score (0–100) with actionable recommendations. |
| **Endpoint** | `POST https://momentumbysamay.online/api/marketing/api/v1/seo-audit` |
| **Pricing** | `$0.0005` |
| **Input Parameters** | `url` (string, required) — Website URL to audit; `proxy` (string, optional) — Proxy URL |

**Example curl:**
```bash
curl -X POST https://momentumbysamay.online/api/marketing/api/v1/seo-audit \
  -H "X-API-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://httpbin.org"}'
```

**Example Response:**
```json
{
  "url": "https://httpbin.org",
  "success": true,
  "fetch_time_seconds": 0.05,
  "page_size_kb": 9.4,
  "http_status": 200,
  "meta": {
    "title": "httpbin.org",
    "description": null,
    "keywords": null,
    "og": {},
    "twitter": {},
    "canonical": null,
    "robots": null,
    "url": "https://httpbin.org"
  },
  "headings": {
    "h1": [],
    "h2": ["httpbin.org0.9.2", "Other Utilities"],
    "h3": [], "h4": [], "h5": [], "h6": []
  },
  "images": { "total_images": 0, "images_missing_alt": 0, "images_with_lazy_loading": 0 },
  "links": {
    "internal_count": 1,
    "external_count": 3,
    "internal_sample": [{ "url": "https://httpbin.org/forms/post", "text": "HTML form", "nofollow": false }],
    "external_sample": [
      { "url": "https://github.com/requests/httpbin", "text": "[no text]", "nofollow": false },
      { "url": "https://kennethreitz.org", "text": "the developer - Website", "nofollow": false },
      { "url": "https://github.com/rochacbruno/flasgger", "text": "Flasgger", "nofollow": false }
    ]
  },
  "content": {
    "word_count": 44,
    "keyword_density": [
      { "word": "httpbin", "count": 4, "density_pct": 12.1 },
      { "word": "org", "count": 3, "density_pct": 9.1 },
      { "word": "run", "count": 2, "density_pct": 6.1 },
      { "word": "developer", "count": 2, "density_pct": 6.1 }
    ]
  },
  "structured_data": { "jsonld_count": 0, "microdata_count": 0, "has_structured_data": false },
  "infrastructure": {
    "server": "gunicorn/19.9.0",
    "content_type": "text/html; charset=utf-8",
    "compression": false,
    "robots_txt": { "accessible": true, "url": "https://httpbin.org/robots.txt" },
    "sitemap": { "accessible": false, "url": null }
  },
  "score_summary": { "passed": 3, "warnings": 8, "issues": 3, "overall_score": 15 },
  "issues": [
    "Missing meta description",
    "No <h1> tag found (critical for SEO)",
    "Missing viewport meta tag (critical for mobile SEO)"
  ],
  "warnings": [
    "Title tag too short (11 chars, min 30 recommended)",
    "No images found on page",
    "No canonical URL tag",
    "No OpenGraph tags",
    "No Twitter Card tags",
    "No structured data (JSON-LD or Microdata)",
    "No sitemap found",
    "No compression (gzip/brotli) detected"
  ]
}
```

---

## 16. marketing_technology_detector

| Field | Value |
|-------|-------|
| **Description** | Detect the technology stack: CMS platforms, JavaScript frameworks, analytics tools, advertising networks, CRM systems, CDN providers, and hosting infrastructure. Uses HTML signatures, HTTP headers, and script references. |
| **Endpoint** | `POST https://momentumbysamay.online/api/marketing/api/v1/technology-detector` |
| **Pricing** | `$0.0003` |
| **Input Parameters** | `url` (string, required) — Website URL to analyze; `proxy` (string, optional) — Proxy URL |

**Example curl:**
```bash
curl -X POST https://momentumbysamay.online/api/marketing/api/v1/technology-detector \
  -H "X-API-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://httpbin.org"}'
```

**Example Response:**
```json
{
  "url": "https://httpbin.org",
  "success": true,
  "technologies": {
    "google_fonts": "Fonts",
    "jquery": "JavaScript Library"
  },
  "technologies_count": 2,
  "categories": {
    "Fonts": ["Google Fonts"],
    "JavaScript Library": ["Jquery"]
  },
  "server_header": "gunicorn/19.9.0",
  "note": "Detection is based on HTML signatures, HTTP headers, and script references. Results are indicative, not exhaustive."
}
```

---

## 17. citation_checker

| Field | Value |
|-------|-------|
| **Description** | Check a business's citation presence across 10+ major directories (Google Business Profile, Yelp, YellowPages, BBB, Facebook, Foursquare, SuperPages, MerchantCircle, HotFrog, Citysearch, Manta). Returns NAP (Name, Address, Phone) consistency score, per-directory status, and actionable recommendations. |
| **Endpoint** | `POST https://momentumbysamay.online/api/marketing/api/v1/citation-checker` |
| **Pricing** | `$0.001` |
| **Input Parameters** | `url` (string, optional) — Business website URL to extract name from; `business_name` (string, optional) — Business name (if URL not provided); `location` (string, optional) — City/state location; `proxy` (string, optional) — Proxy URL |

**Example curl:**
```bash
curl -X POST https://momentumbysamay.online/api/marketing/api/v1/citation-checker \
  -H "X-API-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://httpbin.org"}'
```

**Example Response:**
```json
{
  "success": true,
  "business_name": "httpbin.org",
  "location": "",
  "source_url": "https://httpbin.org",
  "citation_score": 0,
  "citations_found": 0,
  "directories_checked": 9,
  "nap_consistent": null,
  "directory_results": [
    { "directory": "Google Business Profile", "found": false, "url": null, "status": "skipped", "nap_match": null },
    { "directory": "Yelp", "found": false, "url": null, "status": "http_403", "nap_match": null },
    { "directory": "YellowPages", "found": false, "url": null, "status": "http_403", "nap_match": null },
    { "directory": "Facebook", "found": false, "url": null, "status": "fetch_error", "nap_match": null },
    { "directory": "MapQuest", "found": false, "url": null, "status": "not_found", "nap_match": null },
    { "directory": "Foursquare", "found": false, "url": null, "status": "not_found", "nap_match": null },
    { "directory": "Bing Places", "found": false, "url": null, "status": "fetch_error", "nap_match": null },
    { "directory": "Superpages", "found": false, "url": null, "status": "http_403", "nap_match": null },
    { "directory": "MerchantCircle", "found": false, "url": null, "status": "not_found", "nap_match": null },
    { "directory": "Hotfrog", "found": false, "url": null, "status": "fetch_error", "nap_match": null }
  ],
  "recommendations": [
    "Critical: Your business is missing from most major directories. List your business on Google Business Profile, Yelp, Facebook, and Bing Places immediately.",
    "Ensure NAP (Name, Address, Phone) is identical across all listings — even minor differences hurt local SEO.",
    "Monitor citations quarterly — directories sometimes alter or remove listings without notice."
  ]
}
```

---

## Batch Endpoint

| Field | Value |
|-------|-------|
| **Description** | Process multiple URLs concurrently through any compatible API. Run `contact_extractor`, `business_metadata`, `seo_audit`, `technology_detector`, or `company_summary` against up to 100 URLs in a single request. |
| **Endpoint** | `POST https://momentumbysamay.online/api/marketing/api/v1/batch` |
| **Pricing** | `$0.0005` per URL processed |
| **Input Parameters** | `urls` (array of strings, required, max 100) — URLs to process; `api_type` (string, optional, default: `"contact_extractor"`) — Which API to run; `deep_crawl` (boolean, optional, default: `false`); `use_ai` (boolean, optional, default: `false`); `concurrency` (integer, optional, default: `5`, max: `20`) — Max concurrent requests |

**Example curl:**
```bash
curl -X POST https://momentumbysamay.online/api/marketing/api/v1/batch \
  -H "X-API-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "urls": ["https://httpbin.org", "https://example.com"],
    "api_type": "technology_detector",
    "concurrency": 5
  }'
```

**Example Response:**
```json
{
  "success": true,
  "api_type": "technology_detector",
  "total": 2,
  "processed": 2,
  "failed": 0,
  "elapsed_seconds": 1.2,
  "results": {
    "https://httpbin.org": { "url": "https://httpbin.org", "success": true, "technologies_count": 2, ... },
    "https://example.com": { "url": "https://example.com", "success": true, "technologies_count": 0, ... }
  }
}
```

---

## Payment APIs (Free)

These payment/management endpoints are also available:

| API | Endpoint | Pricing |
|-----|----------|---------|
| **Get Pricing** | `GET /api/v1/payments/pricing` | Free |
| **Generate Invoice** | `POST /api/v1/payments/invoice` | Free |
| **Check Balance** | `POST /api/v1/payments/balance` | Free |
| **Verify Payment** | `POST /api/v1/payments/verify` | Free |
| **Payment History** | `GET /api/v1/payments/history` | Free |

---

## Pricing Summary

| # | API | Price |
|---|-----|-------|
| 1 | website_to_markdown | $0.0005 |
| 2 | website_metadata | $0.0002 |
| 3 | technology_detector (Web Intel) | $0.0003 |
| 4 | contact_extractor (Web Intel) | $0.0005 |
| 5 | ai_website_summary | $0.002 / $0.005 (w/ AI) |
| 6 | opengraph_extractor | $0.0002 |
| 7 | robots_txt_parser | $0.0002 |
| 8 | sitemap_parser | $0.0005 |
| 9 | ssl_checker | $0.0002 |
| 10 | dns_lookup | $0.0002 |
| 11 | marketing_contact_extractor | $0.0005 |
| 12 | google_maps_reviews | $0.001 |
| 13 | google_maps_search | $0.001 |
| 14 | business_metadata | $0.0003 |
| 15 | seo_audit | $0.0005 |
| 16 | marketing_technology_detector | $0.0003 |
| 17 | citation_checker | $0.001 |

---

## Rate Limits

| Plan | Requests/sec | Daily Limit | Price |
|------|-------------|-------------|-------|
| Free | 2 | 100 | $0 |
| Starter | 10 | 5,000 | $29/mo |
| Growth | 30 | 25,000 | $79/mo |
| Enterprise | 100 | 100,000 | $199/mo |

---

## Payment Flow (Solana USDC)

1. **Generate invoice:** `POST /api/v1/payments/invoice` → receive wallet address + memo
2. **Send USDC** to the wallet address with the memo on Solana mainnet
3. **Verify:** `POST /api/v1/payments/verify` → credits added to your API key
4. **Use:** Call any API — credits auto-deduct per request

**Token:** `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` (Solana USDC)

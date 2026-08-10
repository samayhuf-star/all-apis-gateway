# RapidAPI Publishing Guide

Your OpenAPI specs and listing copy are **ready to upload**. Here's what to do:

## Prerequisites

1. Create a **RapidAPI Provider** account at https://rapidapi.com/auth/sign-up
2. Go to **Provider Dashboard** → **Add New API**

## Website Intelligence (10 APIs)

**OpenAPI spec:** 
```
/home/node/.minions/workspace/website-intel-apis/rapidapi/openapi.json
```

**Listing copy:**
```
/home/node/.minions/workspace/website-intel-apis/rapidapi/README.md
```

1. Upload `openapi.json` as your API specification
2. Use `README.md` content as the description
3. Set base URL: `http://167.71.22.95`
4. Auth: `X-API-Key` header
5. Pricing: Free (100 req/mo), Basic $19/mo (5k req), Pro $49/mo (25k req)

## Marketing Bundle (7 APIs)

**OpenAPI spec:**
```
/home/node/.minions/workspace/marketing-api-bundle/rapidapi/openapi.json
```

**Listing copy:**
```
/home/node/.minions/workspace/marketing-api-bundle/rapidapi/README.md
```

1. Upload `openapi.json`
2. Base URL: `http://64.227.2.61/marketing`
3. Auth: `X-API-Key` header
4. Same pricing tiers

## Verification

After publishing, test with RapidAPI's test console:

```bash
curl -X POST "https://rapidapi.com/api/v1/YOUR-API-NAME/dns-lookup" \
  -H "X-RapidAPI-Key: YOUR_RAPIDAPI_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": "example.com"}'
```

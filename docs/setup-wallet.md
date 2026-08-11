# Setting Up Solana USDC Payments

Your APIs already accept Solana USDC (token `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`).

The **live Solana treasury wallet on both bundles is**
`F8tmJqiyEpcSbAbWef3XhsknsnW4gxb2gv6K8ZxEfgE` (verified on `payments/pricing` and
`payments/invoice`). If a deployed bundle's `.env` ever shows a
`8x2z3F4REPLACE...` placeholder, fix it back to the real wallet.

## Set / verify the treasury wallet on a droplet

### Website Intelligence (`/api/website-intel`)

```bash
ssh root@167.71.22.95
# Edit .env
sed -i "s/TREASURY_WALLET=.*/TREASURY_WALLET=F8tmJqiyEpcSbAbWef3XhsknsnW4gxb2gv6K8ZxEfgE/" /opt/website-intel-apis/.env
# Restart service
systemctl restart website-intel-apis
```

### Marketing Bundle (`/api/marketing`)

```bash
ssh root@64.227.2.61
# Edit .env
sed -i "s/TREASURY_WALLET=.*/TREASURY_WALLET=F8tmJqiyEpcSbAbWef3XhsknsnW4gxb2gv6K8ZxEfgE/" /opt/marketing-api-bundle/.env
# Restart service
systemctl restart marketing-api-bundle
```

## Verify

After setting, check payments work:

```bash
# Generate an invoice through the domain gateway
curl -s -X POST https://momentumbysamay.online/api/website-intel/api/v1/payments/invoice \
  -H "X-API-Key: *** \
  -H "Content-Type: application/json" \
  -d '{"amount": 1.0}' | python3 -m json.tool

# Expected: wallet address should match F8tmJqiyEpcSbAbWef3XhsknsnW4gxb2gv6K8ZxEfgE
```

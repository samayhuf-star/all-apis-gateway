# Setting Up Solana USDC Payments

Your APIs already accept Solana USDC (token `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`) but the **treasury wallet is a placeholder**.

## Replace with Your Real Wallet

### Website Intelligence (167.71.22.95)

```bash
ssh root@167.71.22.95
# Edit .env
sed -i "s/TREASURY_WALLET=.*/TREASURY_WALLET=YOUR_REAL_SOLANA_WALLET_ADDRESS/" /opt/website-intel-apis/.env
# Restart service
systemctl restart website-intel-apis
```

### Marketing Bundle (64.227.2.61)

```bash
ssh root@64.227.2.61
# Edit .env
sed -i "s/TREASURY_WALLET=.*/TREASURY_WALLET=YOUR_REAL_SOLANA_WALLET_ADDRESS/" /opt/marketing-api-bundle/.env
# Restart service
systemctl restart marketing-api-bundle
```

## Verify

After setting, check payments work:

```bash
# Generate an invoice
curl -s -X POST http://167.71.22.95/api/v1/payments/invoice \
  -H "X-API-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"amount": 1.0}' | python3 -m json.tool

# Expected: wallet address should match YOUR_REAL_SOLANA_WALLET
```

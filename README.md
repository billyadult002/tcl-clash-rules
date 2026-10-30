# tcl-clash-rules

Private ad-block rule-provider for the TCL TV Clash setup.

- `adblock.yaml` — mihomo rule-provider (behavior: domain), auto-updated daily by GitHub Actions.
- `scripts/gen_adblock.py` — pulls 217heidai/adblockfilters and regenerates adblock.yaml.
- `.github/workflows/update-adblock.yml` — daily cron (03:17 UTC).

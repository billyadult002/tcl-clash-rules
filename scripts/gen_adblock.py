#!/usr/bin/env python3
"""Fetch the upstream ad-block DNS list and emit a mihomo rule-provider
(behavior: domain) file at ../adblock.yaml (repo root).

Runs inside GitHub Actions (full internet) or locally. Only needs stdlib.
"""
import os
import sys
import urllib.request

SRC = ("https://raw.githubusercontent.com/217heidai/adblockfilters/"
       "main/rules/adblockdns.txt")
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "adblock.yaml")


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read().decode("utf-8", "replace")


def main():
    raw = fetch(SRC)
    domains = set()
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("!"):
            continue
        # AdGuard style: ||domain^
        if line.startswith("||") and line.endswith("^"):
            d = line[2:-1].strip().lower()
            if d and " " not in d and "/" not in d:
                domains.add(d)
    lines = [
        "# mihomo rule-provider, behavior: domain",
        "# source: 217heidai/adblockfilters (auto-updated)",
        "payload:",
    ]
    lines += ["  - %s" % d for d in sorted(domains)]
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("wrote %d domains -> %s" % (len(domains), OUT))


if __name__ == "__main__":
    main()

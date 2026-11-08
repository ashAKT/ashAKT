#!/usr/bin/env python3
"""Build a small public threat snapshot from Feodo Tracker's recommended feed.

This is defensive threat-intelligence visualization, not telemetry about attacks
against this GitHub user or repository.
"""
import json
import ipaddress
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

FEED_URL = "https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.json"
OUTPUT = Path("docs/data/threats.json")
MAX_RECORDS = 3000


def main():
    request = urllib.request.Request(
        FEED_URL,
        headers={"User-Agent": "ashAKT-live-threat-map/1.0", "Accept": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        source = json.load(response)

    records = []
    for item in source if isinstance(source, list) else []:
        raw_ip = str(item.get("ip_address", "")).strip()
        try:
            ip = ipaddress.ip_address(raw_ip)
        except ValueError:
            continue
        if ip.version != 4 or not ip.is_global:
            continue
        country = str(item.get("country", "")).upper()
        if len(country) != 2 or not country.isalpha():
            country = "ZZ"
        records.append({
            "ip": str(ip),
            "port": item.get("port"),
            "country": country,
            "malware": str(item.get("malware", "Unknown"))[:80],
            "status": str(item.get("status", "unknown"))[:20],
            "first_seen": str(item.get("first_seen", ""))[:30],
            "last_online": str(item.get("last_online", ""))[:30],
            "asn": item.get("as_number"),
            "as_name": str(item.get("as_name", ""))[:100],
        })

    # Stable deduplication and a bounded payload for a fast static site.
    unique = {r["ip"]: r for r in records}
    records = list(unique.values())[:MAX_RECORDS]
    country_counts = Counter(r["country"] for r in records)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "source": "abuse.ch Feodo Tracker — recommended IP blocklist",
        "source_url": FEED_URL,
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "total": len(records),
        "countries": dict(country_counts),
        "records": records,
        "notice": "Public threat-intelligence indicators; not live attack telemetry or attacks targeting this site.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(records)} unique IPv4 indicators across {len(country_counts)} countries")


if __name__ == "__main__":
    main()

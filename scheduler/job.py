#!/usr/bin/env python3
import os, requests, sys

BASE = os.getenv("BASE")
TOKEN = os.getenv("TOKEN")
if not BASE or not TOKEN:
    print("BASE and TOKEN must be set", file=sys.stderr)
    sys.exit(1)

resp = requests.get(
    f"{BASE}/api/top?type=Movie&limit=5",
    headers={"Authorization": f"Bearer {TOKEN}"}
)
resp.raise_for_status()
movies = resp.json()

for i, m in enumerate(movies, 1):
    print(f"{i}. {m['name']} — {m['playCount']} plays")

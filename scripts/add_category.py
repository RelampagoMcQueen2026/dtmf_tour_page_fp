#!/usr/bin/env python3
import json
from pathlib import Path

def main():
    p = Path("dtmf_tour_data.json")
    data = json.loads(p.read_text(encoding="utf-8"))
    count = 0
    for item in data.get("tour_dates", []):
        if "exclusive_song" not in item:
            item["exclusive_song"] = ""
            count += 1
    if count:
        p.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    print(f"Added 'exclusive_song' to {count} items")

if __name__ == '__main__':
    main()

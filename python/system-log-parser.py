#!/usr/bin/env python3
"""Parse log files for failed login attempts and summarize counts by IP."""

import argparse
import re
from collections import Counter
from pathlib import Path

IPV4_PATTERN = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
FAILED_KEYWORDS = ("failed password", "authentication failure", "invalid user")


def parse_failed_logins(log_path: Path) -> Counter:
    ip_counts: Counter = Counter()

    with log_path.open("r", encoding="utf-8", errors="replace") as file:
        for line in file:
            lowered = line.lower()
            if any(keyword in lowered for keyword in FAILED_KEYWORDS):
                ips = IPV4_PATTERN.findall(line)
                for ip in ips:
                    ip_counts[ip] += 1

    return ip_counts


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Summarize failed login attempts by IP address from a log file."
    )
    parser.add_argument(
        "logfile",
        nargs="?",
        default="/var/log/auth.log",
        help="Path to the log file (default: /var/log/auth.log)",
    )
    args = parser.parse_args()

    log_path = Path(args.logfile)
    if not log_path.is_file():
        print(f"Error: Log file not found -> {log_path}")
        return 1

    results = parse_failed_logins(log_path)
    print(f"Failed login summary for: {log_path}")
    print("-" * 45)

    if not results:
        print("No matching failed login entries found.")
        return 0

    for ip, count in results.most_common():
        print(f"{ip:<18} {count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

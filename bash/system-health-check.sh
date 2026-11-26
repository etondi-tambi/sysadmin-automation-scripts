#!/usr/bin/env bash
set -euo pipefail

echo "=== System Health Check ==="
echo "Date: $(date)"
echo "Hostname: $(hostname)"
echo ""

echo "--- CPU Load Average ---"
uptime

echo ""
echo "--- Memory Usage ---"
free -h

echo ""
echo "--- Disk Usage ---"
df -h --exclude-tmpfs --exclude-devtmpfs

 sysadmin-automation-scripts
A collection of production-ready Python and Bash scripts for automating routine system administration and maintenance tasks.

sysadmin-automation-scripts/
├── README.md
├── bash/
│   ├── system-health-check.sh
│   └── log-backup.sh
└── python/
    └── system-log-parser.py
     SysAdmin Automation & Utility Toolkit

  Project Overview
This repository contains a collection of lightweight, automated tools and scripts built using Bash and Python to streamline routine system administration, server monitoring, and backup workflows in Linux environments.

---

  Script Directory

 1. System Health Checker (`bash/system-health-check.sh`)
 Purpose: Performs a quick diagnostic scan of system resources.
 Checks Performed: CPU utilization, available disk space, active memory usage, and running system services.
 Output: Generates a timestamped terminal report for quick triage.

 2. Automated Log Backup & Rotation (`bash/log-backup.sh`)
 Purpose: Safely compresses, archives, and rotates old system log files to conserve storage space.
 Features: Includes error handling and retention limits to prevent uncontrolled disk bloat.

 3. Log Parser & Threat Indicator Search (`python/system-log-parser.py`)
 Purpose: Parses authentication logs (`auth.log`) to scan for repeated failed login attempts or brute-force patterns.
 Output: Extracts unique malicious IP addresses and summarizes failed attempt counts.

---

 🛡️ Engineering Principles Followed
 Idempotency: Designed to run multiple times without causing redundant file creations or syntax errors.
 Error Handling: Built with error traps and graceful exit codes (`set -e`) to prevent unintended state changes.
 Documentation: Inline commenting explaining parameter logic and usage instructions.

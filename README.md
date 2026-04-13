⚡ PRESTON BREACHER v2.0
Path Discovery & Reconnaissance Framework
Preston Breacher is a high-speed reconnaissance tool designed to identify administrative interfaces and Exposure of Sensitive Information (EAR) vulnerabilities. Optimized for speed and stealth with a modernized terminal interface.

🛠 CORE CAPABILITIES
Parallel Execution: Multi-threaded path discovery for rapid analysis.

Deep Dictionary: Ship-ready with a curated list of 400+ high-value paths.

Extension Filtering: Target specific environments (PHP, ASP, HTML).

Vulnerability Detection: Automated checks for EAR (Execute After Redirect) flaws.

Metadata Analysis: Integrated robots.txt and Urmum.txt intelligence gathering.

Custom Scoping: Inject custom path prefixes for localized directory testing.

🚀 OPERATIONAL USAGE
1. Targeted Extension Discovery
Identify PHP-based entry points:

Bash
python preston.py -u example.com --type php
2. High-Speed Multi-Threaded Scan
Engage threading for faster results on robust targets:

Bash
python preston.py -u example.com --type php --fast
3. Standard Enumeration
Run a default scan across the full payload buffer:

Bash
python preston.py -u example.com
4. Custom Path Prefixing
Scope the discovery to a specific directory (e.g., example.com/assets/admin/):

Bash
python preston.py -u example.com --path /assets
PRO TIP: When using the --type flag, the framework intelligently includes extensionless paths (e.g., /dashboard) alongside your specified format to ensure no entry point is missed.

📺 DEMONSTRATION
⚠️ OPERATIONAL NOTICE
This framework is for authorized security auditing only. Ensure you have explicit permission before initiating path discovery against any target. Use it or lose it. Safe.
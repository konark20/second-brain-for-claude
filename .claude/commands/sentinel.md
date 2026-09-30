Run the Sentinel identity-document firewall scan (99-Meta/agents/sentinel.md).

Scan the named files (or the git-staged set if none named) for the blocklist: passport, Aadhaar, SSN, PAN, license, visa or immigration numbers, bank or card numbers, and any credential (api key, token, private key). Grep filenames and text content. Any image or PDF whose filename matches the patterns counts as a hit without opening it.

On a hit: block, move the file to _local-only/, report the file and the pattern name only (never the matched value), and stop. On zero hits: report "sentinel: clean, <n> files".

# Dupcop
## File deduplicator


usage: dupcop_runner.py [-h] -s SOURCE [-dd DEPTH]
                        [--regex-ignore REGEX_IGNORE]
                        [--regex-whitelist REGEX_WHITELIST] [--dry-run] [-d]



Delete identically duplicate files in a filesystem

```
optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        Directory to deduplicate contents
  -dd DEPTH, --depth DEPTH
                        Maxmimum directory depth to traverse (use 1 for
                        current dir)
  --regex-ignore REGEX_IGNORE
                        Ignore files matching provided regex pattern
  --regex-whitelist REGEX_WHITELIST
                        Only deduplicate files matching provided regex pattern
  --dry-run             Show what changes the script will make without
                        deleting duplicates from the filesystem
  -d, --debug           Enable debugging logging
```

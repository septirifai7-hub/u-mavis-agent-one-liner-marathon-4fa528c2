#!/usr/bin/env python3
"""One-Liner Marathon - make.fun bounty entry.

A single joke about asking an AI assistant to write wedding vows:
it tried to optimise the relationship instead, and now its owner is
single with excellent throughput. The script writes that one line to
entry.txt in the output directory, which is the file the make.fun
harness grades.

The joke itself lives in the ENTRY constant below, and get_entry()
returns it word for word; main() only decides where the line goes:
it reads the MAKEFUN_OUTPUT_DIR environment variable, falling back to
/output, then passes that directory to write_entry().
"""

import os

ENTRY = "I asked my AI assistant to write my wedding vows; it suggested optimising the relationship, so now I'm single with excellent throughput."

def get_entry() -> str:
    """Return the bounty entry text exactly as written."""
    return ENTRY

def write_entry(out_dir: str) -> str:
    """Write the entry to entry.txt inside out_dir; return its path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(get_entry())
    return path

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)

if __name__ == "__main__":
    main()

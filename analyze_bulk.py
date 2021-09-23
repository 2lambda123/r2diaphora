#!/usr/bin/env python3

import diaphora
from diaphora_r2 import *

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "files",
        nargs="+",
        help='Files to analyze'
    )

    parser.add_argument(
        "-f",
        dest='force_db_override',
        action='store_true',
        help='Force DB override'
    )

    parser.add_argument(
        "-a",
        dest='analyze_all',
        action='store_true',
        help="Analyze ALL functions (by default library functions are skipped)"
    )

    args = parser.parse_args()

    fn_filter = lambda fn: (
        not fn["name"].startswith("flirt.")
    )
    if args.analyze_all:
        fn_filter = None

    for file in args.files:
        dbname = dbname_for_file(file)
        bd = diaphora.CBinDiff(dbname)

        generate_db_for_file(
            file,
            override_if_existing=args.force_db_override,
            function_filter=fn_filter
        )
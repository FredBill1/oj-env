#!/usr/bin/env python3
from argparse import ArgumentParser
from pathlib import Path
from shutil import copy, rmtree

START_CHAR = "A"
END_CHAR = "N"

START_NUM = 1
END_NUM = 12

INPUT_FILE = Path("input.txt")

SRC = Path("templates/main.cpp")
DST = Path("src")

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--numbers", action="store_true")
    parser.add_argument("--start", type=str, default=None)
    parser.add_argument("--end", type=str, default=None)
    args = parser.parse_args()

    start, end = args.start, args.end
    if not args.numbers:
        if start is None:
            start = START_CHAR
        if end is None:
            end = END_CHAR
        if len(start) != 1 or len(end) != 1:
            print(f"Invalid characters: {start=} {end=}")
            exit(1)
    else:
        if start is None:
            start = START_NUM
        if end is None:
            end = END_NUM
        try:
            start, end = int(start), int(end)
        except ValueError:
            print(f"Invalid numbers: {start=} {end=}")
            exit(1)

    if DST.exists():
        rmtree(DST)
    DST.mkdir(exist_ok=True)
    INPUT_FILE.touch(exist_ok=True)

    if not args.numbers:
        for c in range(ord(start.upper()), ord(end.upper()) + 1):
            copy(SRC, DST / f"{chr(c)}.cpp")
    else:
        for i in range(int(start), int(end) + 1):
            copy(SRC, DST / f"{i}.cpp")

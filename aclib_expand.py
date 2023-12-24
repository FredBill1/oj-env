#!/usr/bin/env python3
from multiprocessing.pool import ThreadPool
from pathlib import Path
from subprocess import PIPE, Popen
from sys import executable

SRC = Path("src").absolute()
LIB = Path("libraries/ac-library").absolute()
EXPANDER = Path("libraries/ac-library/expander.py").absolute()


def expand_file(path: Path) -> None:
    cmd = [executable, EXPANDER, "-c", "--lib", LIB, path]
    p = Popen(cmd, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    p.wait()
    if p.returncode != 0:
        print(f'"{path}": return code: {p.returncode}\nstdout: "{out.decode().rstrip()}"\nstderr: "{err.decode().rstrip()}"')
    else:
        with open(path, "wb") as f:
            f.write(out)


if __name__ == "__main__":
    with ThreadPool() as pool:
        pool.map(expand_file, SRC.glob("**/*.cpp"))
    print("Done.")

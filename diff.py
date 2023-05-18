#!/usr/bin/env python3
import subprocess

def getDiff(path=".", pathspec=None):
    if pathspec:
            pathspecs = [f"{pathspec}"]
    else:
        pathspecs = []
    try:
        output = subprocess.check_output(["/usr/bin/git", "-C", path, "diff", "--cached"] + pathspecs)
    except subprocess.CalledProcessError as e:
        print(f"Error running git diff command: {e}")
        output = b""
    return output.decode("utf-8")

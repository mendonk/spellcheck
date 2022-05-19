#! /usr/bin/env python3

# Interactively spellcheck all .adoc files

import glob
import subprocess

paths = glob.iglob("modules/**/*.adoc", recursive=True)

for path in paths:
  with open(path) as check_file:
    cmd = ["aspell", "-c", "-p", "./aspell.dict", path]
    result = subprocess.run(cmd)
    print(result)
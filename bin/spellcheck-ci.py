#! /usr/bin/env python3

import glob
import subprocess

paths = glob.iglob("modules/**/*.adoc", recursive=True)
global_exit_code = 0

for path in paths:
  with open(path) as check_file:
    cmd = ["aspell", "list", "-p", "./aspell.dict"]
    result = subprocess.run(cmd, stdin=check_file, text=True, capture_output=True)
    
    if len(result.stdout) > 0:
      global_exit_code = global_exit_code + 1

      print(f"::error file={path}::Misspelled words in {path}")
      print(result.stdout)

exit(global_exit_code)
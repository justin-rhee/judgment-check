#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
python3 tests/test_skills.py
python3 tests/mutation.py

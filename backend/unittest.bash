#!/usr/bin/env bash
find . -name 'test_*.py' -exec echo ">>> Testing: {}" \; -exec python ./{} \;

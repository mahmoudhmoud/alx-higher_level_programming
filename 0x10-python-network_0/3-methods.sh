#!/bin/bash
# wari gaa torak dyalliow
curl -s -I "${1}" | grep "^Allow: .*" | cut -d " " -f 2-

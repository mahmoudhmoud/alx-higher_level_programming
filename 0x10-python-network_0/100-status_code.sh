#!/bin/bash
# talab bachiih ijaja
curl -so /dev/null -w "%{http_code}" "$1"

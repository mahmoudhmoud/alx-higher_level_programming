#!/bin/bash
# maktob kaysift dak ltam
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"

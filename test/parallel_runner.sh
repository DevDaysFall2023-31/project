#!/bin/bash

PROCESSES_NUM=$1
PY_SCRIPT_ARGS="${@:2}"

for i in $(seq 1 $PROCESSES_NUM); do
    python3 script.py $PY_SCRIPT_ARGS >> out.txt 2>&1 &
done
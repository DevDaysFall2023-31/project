#!/bin/bash

PROCESSES_NUM=$1
PY_SCRIPT_ARGS="${@:2}"

if [ -f out.txt ]; then
    > out.txt
fi

for i in $(seq 1 $PROCESSES_NUM); do
    python3 script.py $PY_SCRIPT_ARGS >> out.txt 2>&1 &
done
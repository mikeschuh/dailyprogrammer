#!/bin/bash

if [ $# -ne 1 ]; then
    echo $0: usage: quickadd [CNC]
    exit 1
fi

name=$1

mkdir -p challenges/${name}/
touch challenges/${name}/${name}.md
touch challenges/${name}/${name}.py

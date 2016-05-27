#!/bin/bash

# if no arguments given, display help
if [ $# -ne 1 ]; then
    echo $0: usage: sh setup/quickadd.sh [CNC]
    # ex: sh setup/quickadd.sh 094e
    exit 1
fi

name=$1

mkdir -p challenges/${name}/
#touch challenges/${name}/${name}.md
touch challenges/${name}/${name}.py

# auto fill the common file heading
echo "\nChallenge "${name} 1>> challenges/${name}/${name}.md
echo "====\n" 1>> challenges/${name}/${name}.md

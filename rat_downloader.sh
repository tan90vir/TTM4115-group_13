#!/bin/bash
file="forms-link.txt"
url=$(tail -1 "$file")
url=${url//'/edit?usp=sharing'/}
url=$url"/gviz/tq?tqx=out:csv"
nRat=$(($(cat "$file" | wc -l) -1))
wget "$url" -O "RAT-"$nRat".csv"

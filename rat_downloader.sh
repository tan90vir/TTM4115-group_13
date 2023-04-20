#!/bin/bash
#file="form-links.txt"
#url=$(tail -1 "$file")
#url=${url//'/edit?usp=sharing'/}
#url=$url"/gviz/tq?tqx=out:csv&sheet=$1"
url="https://docs.google.com/spreadsheets/d/19LL73LN_uUWXpZN12LcX6Yikn6XPKuYvcBzpYfuB80I/gviz/tq?tqx=out:csv&sheet=$1"
nRat=$(($(cat "$file" | wc -l) -1))
wget "$url" -O "$1".csv

dir="$( dirname -- "$0"; )"
url="https://docs.google.com/spreadsheets/d/19LL73LN_uUWXpZN12LcX6Yikn6XPKuYvcBzpYfuB80I/gviz/tq?tqx=out:csv&sheet="
while read p; do
  dColl="python3 $dir/DataCollector.py $p"
  nRat=($p)
  nRat=${nRat[0]}
  wget "$url$nRat" -O "$dir/RATs/$nRat".csv
  $dColl
done < "$dir/../dks_webpage/members/ratTimestamps.txt"

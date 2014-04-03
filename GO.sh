# Check argument, print info if none.
if (( $# != 1 )); then
  echo "Usage: ./GO.sh directory_containing_data"
  echo "Example: ./GO.sh example"
  echo "More info at doc/readme.html"
  exit 0
fi

# Stop GO.sh script on first failure.
set -e

# clean 'out/' directory
bin/cleanout.sh

# go to '$1' directory
cd $1

# process all csv in '$1' directory as '$a'
echo "Processing records in" $1 "..."
for a in *.csv
do

  # process '$a', make/append temp file 'out/middle.html'
  python ../bin/column2.py $a

  # create '$a.output' here
  python ../bin/csvtotable.py $a

  # create '$a.html' for record '$a'
  cat ../template/top2.html > ../out/$a.html
  cat $a.output >> ../out/$a.html
  cat ../template/bottom.html >> ../out/$a.html

  # remove '$a.output'
  rm $a.output

  # rename '$a.html'
  rename ".csv" "" ../out/$a.html

done
echo "... done processing."

# go back to ./ (up one level from '$1')
cd ..

# make 'table.html' using 'out/middle.html'
echo Creating table.html
cat template/top.html	>table.html
cat out/middle.html	>>table.html
cat template/bottom.html>>table.html

# remove temporary 'out/middle.html'
rm out/middle.html

echo "View table.html (this directory) to see processed records from ["$1"]"
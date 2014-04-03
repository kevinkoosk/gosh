# check if out/ exists
if [ -d "out" ]; then

  # remove out/ directory
  sudo chmod -R 777 out
  rm -r out
  echo "Deleted old contents of out/ directory"
fi

# create new out/ directory
mkdir out
# get to the right repo
cd DD2480-CI

# compile all with py_compile
python3 -m py_compile src/*.py

[ $? -eq 1 ] && exit 1 || exit 0

# all is well
#exit 0

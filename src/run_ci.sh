# get to the right repo
cd DD2480-CI

# compile all with py_compile
python -m py_compile src/main/*.py
if [$? -eq 1]
then 
    exit 1
fi

# all is well
exit 0
#! /bin/bash

# This script is intended to launch all tests and publish the new version of my texts.

# - no future references in 'frido'
# - no future references in 'mazhe'
# - compile with no errors 'frido'
# - compile with no errors 'mazhe'
# - git status clean


# If everything goes well :
# - publish the results on my website.


rm -rf build_tests
mkdir build_tests
cd build_tests


# making
# git clone .. 
# does not work. So this is an assumption on the directory name in which the
# user is working.
git clone ../../mazhe

cd mazhe

rm .deploy.log
touch .deploy.log

# Frido's compilation is together with everything's verification
# because we want to balance the two threads.

compile_frido ()
{
    pytex lst_frido.py
    pytex lst_everything.py --verif
}

compile_everything ()
{
    pytex lst_everything.py
    pytex lst_frido.py --verif
}

# Poor man's multi-thread
compile_frido&compile_everything

cd ../..
git status >> build_tests/mazhe/.deploy.log

cd build_tests/mazhe


echo "Result : -----------"

cat .deploy.log

echo "--------------------"
echo "Beware that this is the result for build_test/mazhe. I did not compile here."

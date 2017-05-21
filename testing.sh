#! /bin/bash

# This script is intended to launch all tests and publish the new version of my texts.

# - no future references in 'frido'
# - no future references in 'mazhe'
# - compile with no errors 'frido'
# - compile with no errors 'mazhe'
# - the pictures are clean
# - git status clean


# If everything goes well (not yet implemented) :
# - publish the results on my website.
# - git push to github


MAIN_DIR=`pwd`

BUILD_DIR=$MAIN_DIR/build
CLONE_DIR=$BUILD_DIR/build_mazhe

STASH=`git stash list`
if [[ -z $STASH  ]];then
    echo "The git's stash is empty. We can continue"
else
    echo "The stash list is not empty. You should empty it before to launch 'testing.sh'"
    exit
fi

NEW_BRANCH=testing_$RANDOM$RANDOM
CURRENT_BRANCH=`git rev-parse --abbrev-ref HEAD`

# Create a new branch which contains not only the state of the last commit,
# but also the state of the modified files.
# Thus we are testing the current state of the project, not the last commit
# state.

git stash
git checkout -b $NEW_BRANCH
git stash apply
git commit -a -m "The new build-test branch"
git checkout $CURRENT_BRANCH
git stash pop

rm -rf $BUILD_DIR
mkdir $BUILD_DIR
cd $BUILD_DIR

git clone $MAIN_DIR --branch   $NEW_BRANCH   --single-branch  $CLONE_DIR

cd $BUILD_DIR

rm .testing.log
touch .testing.log

# Frido's compilation is together with everything's verification
# because we want to balance the two threads.

compile_frido ()
{
    pytex lst_frido.py --no-external
    pytex lst_everything.py --verif
}

compile_everything ()
{
    pytex lst_everything.py --no-external
    pytex lst_frido.py --verif
}

cd $CLONE_DIR/src_phystricks
./testing.sh


cd $CLONE_DIR
# Poor man's multi-thread
compile_frido&
compile_everything


cd $MAIN_DIR
git status >> $CLONE_DIR/.testing.log

cd $CLONE_DIR


echo "Result : -----------"

cat .testing.log

echo "--------------------"
echo "Beware that this is the result for the branch $1. I did not compile here."

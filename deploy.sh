#! /bin/bash

# This script is intended to launch all tests and publish the new version of my texts.

# - no future references in 'frido'
# - no future references in 'mazhe'
# - compile with no errors 'frido'
# - compile with no errors 'mazhe'
# - git status clean


# If everything goes well (not yet implemented) :
# - publish the results on my website.
# - git push to github

MAIN_DIR=`pwd`

BUILD_DIR=$MAIN_DIR/build
CLONE_DIR=$BUILD_DIR/build_mazhe

NEW_BRANCH=deploy_$RANDOM$RANDOM
CURRENT_BRANCH=`git rev-parse --abbrev-ref HEAD`

echo $NEW_BRANCH
echo $CURRENT_BRANCH


git stash
git checkout -b $NEW_BRANCH
git stash apply
git commit -a -m "The new build-test branch"
git checkout $CURRENT_BRANCH
git stash apply

rm -rf $BUILD_DIR
mkdir $BUILD_DIR
cd $BUILD_DIR

git clone $MAIN_DIR --branch   $NEW_BRANCH   --single-branch  $CLONE_DIR

cd $BUILD_DIR

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

cd $CLONE_DIR

# Poor man's multi-thread
compile_frido
compile_everything

cd $MAIN_DIR
git status >> $CLONE_DIR/.deploy.log

cd $CLONE_DIR


echo "Result : -----------"

cat .deploy.log

echo "--------------------"
echo "Beware that this is the result for build_test/mazhe. I did not compile here."

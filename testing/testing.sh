#! /bin/bash

# This script is intended to launch all tests and publish the new version of my texts.

# - no future references in 'frido'
# - no future references in 'mazhe'
# - compile with no errors 'frido'
# - compile with no errors 'mazhe'
# - the '.pstricks' recompiled from the '.py' are equal to the '.recall'
# - git status clean

# The fact that the '.pstricks' are equal to the '.recall'
# is checked at each compilation in 'lst_frido.py'


# If everything goes well (not yet implemented) :
# - publish the results on my website.
# - git push to github


MAIN_DIR=`pwd`/..

BUILD_DIR=$MAIN_DIR/build
CLONE_DIR=$BUILD_DIR/build_mazhe
SRC_PHYSTRICKS=$CLONE_DIR/src_phystricks
AUTO_PICTURES_TEX=$CLONE_DIR/auto/pictures_tex
LOG_FILE=$BUILD_DIR/.testing.log

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

rm $LOG_FILE
touch  $LOG_FILE

# Frido's compilation is together with everything's verification
# because we want to balance the two threads.

compile_frido ()
{
    pytex lst_frido.py --no-external --output=$LOG_FILE
    pytex lst_frido.py --verif  --output=$LOG_FILE
}

compile_everything ()
{
    pytex lst_everything.py --no-external --output=$LOG_FILE
    pytex lst_everything.py --verif --output=$LOG_FILE
}

cd $SRC_PHYSTRICKS
./testing.sh

cd $CLONE_DIR/testing
./test_recall.py $AUTO_PICTURES_TEX >> $LOG_FILE

cd $CLONE_DIR
# Poor man's multi-thread
#compile_everything&
#compile_frido


cd $MAIN_DIR
git status >> $LOG_FILE

cd $CLONE_DIR


echo "Result : -----------"

cat  $LOG_FILE 

echo "--------------------"
echo "Beware that this is the result for the branch $1. I did not compile here."

# remettre la liste des figures
# remettre les compilations ici

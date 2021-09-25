#!/bin/bash

# This script is intended to launch all tests and publish the new version of my texts.

# - no future references in 'frido'
# - no future references in 'giulietta'
# - compile with no errors 'frido'
# - compile with no errors 'giulietta'
# - the '.pstricks' recompiled from the '.py' are equal to the '.recall' (only if "--full" is given as argument)
# - git status clean

# The fact that the '.pstricks' are equal to the '.recall'
# is checked at each compilation in 'lst_frido.py'
# For that, the directory of 'phystricks' must be in $PYTONPATH,
# see test_recall.py


# If everything goes well (not yet implemented) :
# - publish the results on my website.
# - git push to github



MAIN_DIR=`pwd`/..

BUILD_DIR=$MAIN_DIR/build
CLONE_DIR=$BUILD_DIR/build_giulietta
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

compile_frido ()
{
    cd $CLONE_DIR
    pytex lst_frido.py --no-external --output=$LOG_FILE
    pytex lst_frido.py --verif  --output=$LOG_FILE
}

compile_giulietta ()
{
    cd $CLONE_DIR
    pytex lst_giulietta.py --no-external --output=$LOG_FILE
    pytex lst_giulietta.py --verif --output=$LOG_FILE
}


test_death_links ()
{
    cd $CLONE_DIR/testing
    ./test_dead_links.py $CLONE_DIR --output=$LOG_FILE
}

check_spelling()
{
    # For your information, you can make replacements
    # with
    # sed -i -- 's/foo/bar/g' *

    ag " [LldDcC]es variable " >> $LOG_FILE
    ag " demi [a-z]" >> $LOG_FILE
    ag " d'intersections " >> $LOG_FILE
    ag "boite" >> $LOG_FILE
    ag "est choisit" >> $LOG_FILE
    ag "inclus à" >> $LOG_FILE      # on dit "inclus DANS"
    ag "est a dire" >> $LOG_FILE        # il faut un trait d'union
    ag "corollaire" >> $LOG_FILE        # orthographe réformée
    ag "Corollaire" >> $LOG_FILE        # orthographe réformée
    ag "chaîne" >> $LOG_FILE        # orthographe réformée
    ag "[Qq]uelque [a-zéàçèùôîûê]*s " >> $LOG_FILE
    ag "[Qq]uelque [a-zéàçèùôîûê]*x " >> $LOG_FILE
    ag "ez moi" >> $LOG_FILE        # vient par exemple de "écrivez moi" au lieu de "écrivez-moi".
    ag "[Rr]acine carré " >> $LOG_FILE
    ag "une cas " >> $LOG_FILE
    ag " status " >> $LOG_FILE
    ag " c'est à dire " >> $LOG_FILE # doit être c'est-à-dire
    ag " en terme " >> $LOG_FILE
    ag " paramétrisation " >> $LOG_FILE  # doit être "paramétrage"
    ag " multi-indice " >> $LOG_FILE  # doit être "multiindice"
    ag " semi-norme" >> $LOG_FILE  # doit être "seminorme"
    ag " une ensemble" >> $LOG_FILE  
    ag " s'il " >> $LOG_FILE    # devrait être "s'il", mais je préfère si il.
    ag " S'il " >> $LOG_FILE 
}

test_picture ()
{
    cd $SRC_PHYSTRICKS
    ./testing.sh

    cd $CLONE_DIR/testing
    ./test_recall.py $CLONE_DIR >> $LOG_FILE
    if [ $? -eq 1 ]; then
        echo "test_recall.py had a problem " >> $LOG_FILE
    fi
}

if [[  "$@" == "--pictures"  ]] || [[  "$@" == "--full"  ]]
then
    test_picture
fi

if [[  "$@" == "--dead_links"  ]] || [[  "$@" == "--full"  ]]
then
    test_death_links&
fi

compile_giulietta&
compile_frido
check_spelling

cd $MAIN_DIR

wait

cd $CLONE_DIR



echo "----------------"

cat  $LOG_FILE

echo "--------------------"
echo "Find all the results in $LOG_FILE"

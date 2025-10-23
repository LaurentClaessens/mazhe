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


one_spelling()
{
    wrong=$1
    # echo "Search for $wrong" 
    ag "$wrong" 
}

check_spelling()
{
    # For your information, you can make replacements
    # with
    # sed -i -- 's/foo/bar/g' *

    one_spelling " [LldDcC]es variable " 
    one_spelling " demi [a-z]" 
    one_spelling "boite" 
    one_spelling "est choisit"   # est choisi
    one_spelling "inclus à"       # on dit "inclus DANS"
    one_spelling "est a dire"         # il faut un trait d'union
    one_spelling "corollaire"         # orthographe réformée, doit être corolaire
    one_spelling "Corollaire"         # orthographe réformée
    one_spelling "chaîne"         # orthographe réformée
    one_spelling "[Qq]uelque [a-zéàçèùôîûê]*s " 
    one_spelling "[Qq]uelque [a-zéàçèùôîûê]*x " 
    one_spelling "ez moi"         # vient par exemple de "écrivez moi" au lieu de "écrivez-moi".
    one_spelling "[Rr]acine carré " 
    one_spelling "une cas " 
    one_spelling " status " 
    one_spelling " c'est à dire "  # doit être c'est-à-dire
    one_spelling " en terme " 
    one_spelling " paramétrisation "   # doit être "paramétrage"
    one_spelling " multi-indice "   # doit être "multiindice"
    one_spelling " semi-norme"   # doit être "seminorme"
    one_spelling " une ensemble"   
    one_spelling " Cesaro "  # Cesàro
    one_spelling " la théorème " 
    one_spelling " [Vv]oila " 
    one_spelling " fonction lipscitz " 
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

#compile_giulietta&
#compile_frido
check_spelling

cd $MAIN_DIR

wait

cd $CLONE_DIR



echo "----------------"

cat  $LOG_FILE

echo "--------------------"
echo "Find all the results in $LOG_FILE"

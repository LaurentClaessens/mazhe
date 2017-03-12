#! /bin/bash

# This script is intended to launch all tests and publish the new version of my texts.

# - no future references in 'frido'
# - no future references in 'mazhe'
# - compile with no errors 'frido'
# - compile with no errors 'mazhe'
# - git status clean


# If everything goes well :
# - publish the results on my website.


rm .deploy.log
touch .deploy.log
pytex lst_frido.py
pytex lst_frido.py --verif
pytex lst_everything.py
pytex lst_everything.py --verif

git status >> .deploy.log


echo "Result : -----------"

cat .deploy.log

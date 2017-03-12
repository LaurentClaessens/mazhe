#! /bin/bash

rm .deploy.log
touch .deploy.log
pytex lst_frido.py
pytex lst_frido.py --verif
pytex lst_everything.py
pytex lst_everything.py --verif

git status >> .deploy.log


echo "Result : -----------"

cat .deploy.log

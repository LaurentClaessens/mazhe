#!/usr/bin/env bash
# test-url-in-file
for file in $@; do
    egrep -o "\\url\{([^\}]+)" "$file" | sed s/"\\url{"/""/g | test-all-urls.sh
    egrep -o "\\href\{([^\}]+)" "$file" | sed s/"\\url{"/""/g | test-all-urls.sh
done

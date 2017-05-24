#!/usr/bin/env bash

cd /tmp/
for url in $@; do
    wget --quiet "$url" || echo -e "$url invalide ?"
done

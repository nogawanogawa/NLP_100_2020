#!/bin/sh

cat popular-names.txt | gsed  -e "s/\t/ /g" 

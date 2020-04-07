#!/bin/sh

split -l $(expr $(cat $2 | wc -l) / $1 + 1) $2 

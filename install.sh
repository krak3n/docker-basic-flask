#!/bin/bash

if [ $1 ]
then
    pip install -e .[$1]
else
    pip install -e .
fi

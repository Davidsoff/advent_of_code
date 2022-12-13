#!/bin/bash
YEAR=${PWD##*/}
DAYS="25"
if [ $YEAR -eq "$(date +%Y)" ] && [ "`date +%m`" -eq "12" ]; then
    DAYS=`date +%d`
fi

for i in $(seq -f "%02g" 1 $DAYS)
do 
    if [[ ! -e 'input' ]]; then mkdir 'input'; fi
    file="input/day$i.txt"
    if [[ ! -e $file ]]
    then
        aocd $i $YEAR > $file
    fi
done  
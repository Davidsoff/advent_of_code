#!/bin/bash

YEAR=$1
mkdir -p $YEAR/input

cp template/get_data.sh $YEAR/
cp template/requirements.txt $YEAR/
touch $YEAR/input/test.txt
for i in $(seq -f "%02g" 1 25)
do 
    file="$YEAR/day$i.py"
    if [[ ! -e $file ]]
    then
        sed "s/01/$i/g" template/base.py > $file
    fi
done

VENV_FILE=$YEAR/.venv
if [[ ! -e $VENV_FILE ]]
then
    DIR=${HOME}/.virtualenvs/$YEAR
    python3 -m venv $DIR
    echo $YEAR > $VENV_FILE
    chmod 600 $VENV_FILE
    cd $YEAR
    source $DIR/bin/activate
    pip install -r requirements.txt
    deactivate
fi



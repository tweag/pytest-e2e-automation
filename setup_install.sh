#!/bin/sh

PLATFORM_TYPE=$(command uname)

python ./setup_install.py global

RETCODE=$?
if [ $RETCODE = 0 ]; then
    if [ "$PLATFORM_TYPE" = "Darwin" ]; then
        . $HOME/.qa-venv/bin/activate
    elif [ "$PLATFORM_TYPE" = "Linux" ]; then
        . $HOME/.qa-venv/bin/activate
    else
        . $HOME\\.qa-venv\\Scripts\\activate
    fi
else
    true
fi

python ./setup_install.py venv

RETCODE=$?
if [ $RETCODE = 0 ]; then

    if [ "$PLATFORM_TYPE" = "Windows" ]; then
        echo -e "Please activate virtual environment using command \". $HOME\\.qa-venv\\Scripts\\activate\" while running test cases from new shell. Need not activate now, since it is already activated."
    else
        echo -e "Please activate virtual environment using command \". $HOME/.qa-venv/bin/activate\" while running test cases from new shell. Need not activate now, since it is already activated."
    fi
else
    true
fi

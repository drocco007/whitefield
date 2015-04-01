#!/bin/bash

cd ~/source/whitefield/

# First run
~/.envs/whitefield/bin/py.test -q tests/

# Watch for changes
while ,watch -qr . ;
do
    ~/.envs/whitefield/bin/py.test -q tests/
done

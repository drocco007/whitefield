#!/bin/bash

cd ~/source/whitefield/

while ,watch -qr . ;
do
    ~/.envs/whitefield/bin/py.test -q tests/
done

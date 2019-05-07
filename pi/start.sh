#!/bin/bash

screen -dm -S robot /dev/ttyACM0 9600

mkfifo messages
websocat -s 8080 <> messages &

python stream.py
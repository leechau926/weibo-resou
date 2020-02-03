#!/bin/bash

DATE="`date +'%Y%m%d-%H%M'`"

python3 ~/resou/resou.py | tee ~/resou/wbrs-${DATE}.txt

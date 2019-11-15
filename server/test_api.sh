#!/bin/bash

python3='/escnfs/home/csesoft/2017-fall/anaconda3/bin/python3'

printf "Testing /users/\n"
python3 ./test_users.py

printf "Testing /quotes/\n"
python3 ./test_quotes.py

printf "Testing /movers/\n"
python3 ./test_movers.py

printf "Testing /charts/\n"
python3 ./test_charts.py

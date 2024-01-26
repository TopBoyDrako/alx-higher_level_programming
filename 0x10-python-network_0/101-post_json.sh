#!/bin/bash
# bash script to post json files and a test server
curl -sX POST $1 -H "Content-Type: application/json" -d @$2 -L

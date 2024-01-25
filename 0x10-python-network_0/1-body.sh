#!/bin/bash
# script that takes in a URL, sends a GET request to the url and displays
curl -sX GET $1 -L

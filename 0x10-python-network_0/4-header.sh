#!/bin/bash
# scipt takes in a url , sends a GET request to the url and displays body of the response
curl -sX GET $1 -J "X-School-User-Id: 98" -L

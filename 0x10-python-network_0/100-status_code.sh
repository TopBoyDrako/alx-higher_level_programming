#!/bin/bash
# carries out a task using curl to run commands
curl -L -s -X HEAD -w "%{http_code}" "$1"

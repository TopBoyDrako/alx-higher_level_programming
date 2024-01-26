#!/bin/bash
#script that takes a request that causes the server to respond with a message
curl -o /dev/null -sw "You got me!" 0.0.0.0:5000/catch_me

#!/usr/bin/python3
"""
This python script takes in a url, sends a request to the url
displays the value of the X-Request-Id found in the header
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as r:
        print(dict(r.headers).get("X-Request-Id"))

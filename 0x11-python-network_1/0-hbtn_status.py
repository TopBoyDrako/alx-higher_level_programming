#!/usr/bin/python3
"""
This module fetches a script using the urllib package
"""
import urllib.request


if __name__ == "__main__":

    response = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(response) as request:
        body = request.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))

#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a letter as a parameter."""
import requests
import sys


if __name__ == "__main__":
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]

    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
        json_data = r.json()

        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

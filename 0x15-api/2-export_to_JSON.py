#!/usr/bin/python3
"""
2-export_to_JSON module

This script exports data in the json format
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    id = argv[1]
    usr_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    tds_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)

    u = requests.get(usr_url).json()
    todo = requests.get(tds_url).json()

    with open('{}.json'.format(id), 'w') as f:
        tasks = []
        for t in todo:
            tasks.append({"task": t.get("title"),
                          "completed": t.get("completed"),
                          "username": u.get("username")})
            data = {"{}".format(id): tasks}
        json.dump(data, f)

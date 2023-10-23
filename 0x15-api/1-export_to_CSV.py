#!/usr/bin/python3
"""
1-export_to_CSV module

This script exports data in the CSV format
"""


import csv
import requests
from sys import argv


if __name__ == "__main__":
    id = argv[1]
    usr_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    tds_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)

    u = requests.get(usr_url).json()
    todo = requests.get(tds_url).json()

    with open('{}.csv'.format(id), 'w') as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for t in todo:
            row = [id, u.get("username"), t.get("completed"), t.get("title")]
            row = [str(value) for value in row]
            csv_writer.writerow(row)

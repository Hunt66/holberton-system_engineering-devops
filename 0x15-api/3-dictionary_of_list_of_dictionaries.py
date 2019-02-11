#!/usr/bin/python3
""" exports data of user to json format"""
from requests import get
import sys
import json
from pprint import pprint


if __name__ == '__main__':
    users = get('https://jsonplaceholder.typicode.com/users/').json()
    if users is not None:
        to_do = get('https://jsonplaceholder.typicode.com/todos/').json()
        new_json = {}
        for user in users:
            eid = user.get('id')
            username = user.get('username')
            tsks = []
            for t in to_do:
                if t['userId'] == eid:
                    tsks += [t]
            tskss = []
            for t in tsks:
                tskss += [{"task": t.get('title'),
                           "completed": t.get('completed'),
                           "username": username}]
            new_json[str(eid)] = tskss
        with open("todo_all_employees.json", "w") as f:
            json.dump(new_json, f)

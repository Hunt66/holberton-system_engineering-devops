#!/usr/bin/python3
""" exports info about an employee to csv"""
from requests import get
import sys
import csv


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].isdigit:
        user = get('https://jsonplaceholder.typicode.com/users/' +
                   sys.argv[1]).json()
        if user is not None:
            to_do = get('https://jsonplaceholder.typicode.com/todos/').json()
            eid = user.get('id')
            username = user.get('username')
            tsks = []
            new_csv = []
            for t in to_do:
                if t['userId'] == eid:
                    tsks += [t]
            for t in tsks:
                new_csv += [{"id": eid, "name": username,
                         "completed": t.get('completed'),
                         "title": t.get('title')}]
            kys = ['id', 'name', 'completed', 'title']
            with open(str(eid) + ".csv", "w") as f:
                wr = csv.DictWriter(f, kys, quoting=csv.QUOTE_ALL)
                wr.writerows(new_csv)

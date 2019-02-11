#!/usr/bin/python3
""" returns info about the todo list progress of an employee"""
from requests import get
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].isdigit:
        user = get('https://jsonplaceholder.typicode.com/users/' +
                   sys.argv[1]).json()
        if user is not None:
            to_do = get('https://jsonplaceholder.typicode.com/todos/').json()
            eid = user.get('id')
            name = user.get('name')
            tsks = []
            done = []
            for t in to_do:
                if t['userId'] == eid:
                    tsks += [t]
                    if t.get('completed'):
                        done += [t['title']]
            print("Employee " + name + " is done with tasks(" + str(len(done)) +
                  '/' + str(len(tsks)) + "):")
            print('     ',end='')
            print('\n     '.join(done))

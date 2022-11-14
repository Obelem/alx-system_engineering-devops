#!/usr/bin/python3
''' export data in json format '''
from sys import argv
from requests import get
import json


if __name__ == '__main__':
    endpoint = 'https://jsonplaceholder.typicode.com'
    users = get(endpoint + '/users/').json()
    todos = get(endpoint + '/todos/').json()

    i, records = 0, []
    id, user, all = users[i]['id'], users[i]['username'], {}

    for todo in todos:
        if todo['userId'] != id:
            all[id] = records
            i += 1
            id, user = users[i]['id'], users[i]['username']
            records = []
        records.append({'username': user, 'task': todo['title'],
                        'completed': todo['completed']})

    all[id] = records
    with open('todo_all_employees.json', 'w') as file:
        json.dump(all, file)

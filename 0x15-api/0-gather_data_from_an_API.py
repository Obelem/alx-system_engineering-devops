#!/usr/bin/python3
''' gather data from an API '''
import requests
from sys import argv

if __name__ == '__main__':
    # get employee name
    endpoint = 'https://jsonplaceholder.typicode.com'
    user_res = requests.get(endpoint + '/users/' + argv[1]).json()
    name = user_res['name']

    # get total number of tasks
    todos = requests.get(endpoint + '/todos?userId=' + argv[1]).json()
    all_tasks = len(todos)

    # get number completed tasks and their titles
    titles_done = [todo['title'] for todo in todos if todo['completed']]

    print('Employee {} is done with tasks({}/{}):'
          .format(name, len(titles_done), all_tasks))

    for title in titles_done:
        print('\t {}'.format(title))

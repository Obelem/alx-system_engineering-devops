#!/usr/bin/python3
''' export data in the CSV format '''
from sys import argv
from requests import get
import csv


if __name__ == '__main__':
    endpoint = 'https://jsonplaceholder.typicode.com'
    user_res = get(endpoint + '/users/' + argv[1]).json()
    todos = get(endpoint + '/todos?userId=' + argv[1]).json()
    usr = user_res['username']

    with open('{}.csv'.format(argv[1]), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([argv[1], usr, todo['completed'], todo['title']])

#! /usr/bin/env python3

users = [{'admin': True, 'active': True, 'name': 'Skylar'},
         {'admin': False, 'active': True, 'name': 'Jack'},
         {'admin': True, 'active': True, 'name': 'Shan'},
         {'admin': False, 'active': True, 'name': 'Tom'},
         {'admin': True, 'active': False, 'name': 'Deren'},
         {'admin': False, 'active': False, 'name': 'Bob'}
         ]

for user in users:
    if user['admin'] and user['active']:
        print(f"ACTIVE - (ADMIN) {user['name']}")
    elif user['active']:
        print(f"ACTIVE - {user['name']}")
    elif user['admin']:
        print(f"(ADMIN) {user['name']}")
    else:
        print(f"{user['name']}")

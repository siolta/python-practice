#! /usr/bin/env python3

user = {'admin': True, 'active': True, 'name': 'Skylar'}

if user['admin'] and user['active']:
    print(f"ACTIVE - (ADMIN) {user['name']}")
elif user['active']:
    print(f"ACTIVE - {user['name']}")
elif user['admin']:
    print(f"(ADMIN) {user['name']}")
else:
    print(f"{user['name']}")

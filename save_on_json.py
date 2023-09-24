import requests
import json #библиотека есть в python
from pprint import pprint #

users = requests.get('https://jsonplaceholder.typicode.com/users').json() - #data is taken from this website
print(users)

json_data = []
for user in users:
    name = user['name']
    username = user ['username']
    street = user['address']['street']
    email = user['email']
    json_data.append( {
        'name': name,
        'User':username,
        'Street':street,
        'Email':email

    })

with open ('users.json',mode ='w', encoding = 'UTF-8') as file:
    json.dump(json_data,file, ensure_ascii=False, indent=4)

import json

users = [
    {'name': 'Diego Sousa', 'role':'Designer', 'phone':'(61) 9 9999-9999' },
    {'name':'Thiago', 'role':'Full Stack Developer', 'phone':'(61) 9 7777-7777' },
    {'name':'Filipe', 'role':'Full Stack Developer', 'phone':'(61) 9 8888-8888' }
]

with open('./arquivos/users.json', 'w') as exportFile:
    json.dump(users, exportFile, indent=4)
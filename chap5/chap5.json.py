import json

s = '''
[{  
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
},{
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''

data = json.loads(s)

with open('data.json', 'w') as file:
    file.write(json.dumps(data, indent=2))

import json

x = '{"name" : "helmi","hobby" : "main game", "job" : "developer"}'

y = json.loads(x)
print(y)
print(y['name'])

import json
example = '{"FIRST": "1", "SECOUND": "2", "THREE": "3"}'
y = json.loads(example)
print(type(y))
print(y)
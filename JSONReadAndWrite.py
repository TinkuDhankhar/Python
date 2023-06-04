import json
file = open("data.json", "r");
x = file.read();
data = json.loads(x);
print(data)
print(type(data))
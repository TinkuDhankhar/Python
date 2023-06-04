# json (javascript object notation)
# json is text, written, with javascript object notation
import json
example = {"FIRST": "1", "SECOUND": "2", "THREE": "3"}
to_json = json.dumps(example)
print(to_json)
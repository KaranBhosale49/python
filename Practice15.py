# Python program showing
# use of json package

import json

a = {"name": "John", "age": 31, "Salary": 25000}

b = json.dumps(a)

print(b)

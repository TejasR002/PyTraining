# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

import json

##Json to python
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

#PYTHON TO JSON


x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x) #makes it json


print(y)
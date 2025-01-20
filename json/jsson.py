import json


# #json to python

# # some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
y = json.loads(x)

# # the result is a Python dictionary:
print(y["age"])


# python to json 
x = {
  "name": "Joe",
  "age": 30,
  "city": "nevada"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
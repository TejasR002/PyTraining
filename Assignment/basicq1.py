strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
my_dict = {}

for x in strs:
    k = ''.join(sorted(x))  # Sort the characters in the string and join them back into a string
    if k in my_dict:
        my_dict[k].append(x)
    else:
        my_dict[k] = [x]

# Convert the dictionary values to a list of lists

result = list(my_dict.values())

print(result)
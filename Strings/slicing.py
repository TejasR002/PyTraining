#used for getting the range of character of string

string = "Binoricafe"

# in slicing the end part in not included  in mathematical terms ->   it is [.,.,.,.,.,...)
print(string[2:6]) #for specific range   
print(string[:4]) #from starting to specific ending
print(string[2:]) #from specific start to end

#python suppors negative indexing too .

print(string[-1:-4]) #it prints the empty string cause it goes in the reverse order which doesn't include any .
print(string[-4:-1])
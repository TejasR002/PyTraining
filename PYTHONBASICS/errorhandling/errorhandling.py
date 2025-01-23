try:
  print(x)
except NameError:
  print("Variable x is not defined")
else :
  print("Something else went wrong")


#finally block
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

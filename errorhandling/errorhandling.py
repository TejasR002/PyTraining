try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


#finally block
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

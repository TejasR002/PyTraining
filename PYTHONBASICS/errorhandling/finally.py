#it executes  inrespective of the try has given an error or not 

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
  
  
try:
  f = open("demofile.txt","a")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
    print("Done")
except:
  print("Something went wrong when opening the file")
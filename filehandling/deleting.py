import os
if os.path.exists("create2.txt"):
  os.remove("create2.txt")
else:
  print("The file does not exist")
  

if os.path.exists("deletingfolder"):
    os.rmdir("deletingfolder")
    print("folder removed !")
else : 
    print("folder didnot found")
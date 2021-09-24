myDict = {}
a = int(input("Enter number of Entries"))
for i in range(a):
  key = int(input("Enter data for keys"))
  values = int(input("Enter data for values"))
  myDict.update({key:values})
  print(myDict)

  
def traversedict(Dictionary):
  for key in Dictionary:
    print(key,Dictionary[key])

travsersedict(myDict)

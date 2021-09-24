myDict = {}
a = int(input())
for i in range(a):
  k = input()
  v = input()
  myDict.update({k:v})
  print(myDict)
def searchindict(dictionary,values):
  for key in dicionary:
    if dictionary[key] == values:
      return key,value
    else:
      return "value does not exist"

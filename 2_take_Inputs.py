myDict = {}
a = int(input("Enter the input key and values"))
for i in range(a):
  key = input('enter key')
  value = input('enter value')
  myDict.update({key:value)}
  print(myDict)

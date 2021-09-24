myDict = {}
a = int(input("Enter the values for dictionary"))
for i in range(a):
  k = int(input("Enter key values"))
  v = int(input("Enter value to input"))
  myDict.upadte({k:v})
  print(myDict)

  
  #Method 1:
  myDict.pop("City")
print(myDict)

#Method 2:
myDict.popitem()

#Method 3:
print(myDict.clear())

list = [1,2,3,4]
a= 4
pos=0
flag = 0
for index,item in enumerate(list):
  if (a==item):
    pos = index
    flag = 1
    break

if (flag == 1):
  print("Item is found at position ",pos)
else:
  print("Item is not found")

    
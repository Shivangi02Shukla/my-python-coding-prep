*
**
***
****
*****
****
***
**
*


Sol 1:

n = 5
for i in range(n):
  for j in range(i+1):
    print("*", end = "")
  print()
for i in range(n-1):
  for j in range(n-i-1):
    print("*", end = "")
  print()



Sol 2:

n = 5
for i in range(2*n):
  if i < 5:
    for j in range(i+1):
      print("*", end = "")
    print()
  else:
    for k in range(2*n-i-1):
      print("*", end = "")
    print()
    
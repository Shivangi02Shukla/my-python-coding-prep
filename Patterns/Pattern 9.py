    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *


n = 10
n = int(n/2)
for i in range(n):
  for j in range(n-i-1):
    print(" ", end = "")
  for k in range(2*i+1):
    print("*", end = "")
  print()

for i in range(n, 0, -1):
  for k in range(n-i):
    print(" ", end = "")
  for j in range(2*i-1):
    print("*", end = "")
  print()
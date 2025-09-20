1
01
101
0101
10101


n = 5
a = 1
for i in range(n):
  if i%2 == 0:
    a = 1
  else:
    a = 0
  for j in range(i+1):
    print(a, end = "")
    a = 1 - a
  print()
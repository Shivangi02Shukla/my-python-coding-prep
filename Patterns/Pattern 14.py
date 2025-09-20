A
AB
ABC
ABCD
ABCDE


n = 5
A = 65
for i in range(n):
  A = 65
  for j in range(i+1):
    print(chr(A), end = "")
    A += 1
  print()
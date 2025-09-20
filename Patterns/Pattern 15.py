ABCDE
ABCD
ABC
AB
A


n = 5
A = 65
for i in range(n):
  A = 65
  for j in range(n-i):
    print(chr(A), end = "")
    A += 1
  print()
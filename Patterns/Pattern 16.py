    A
   ABA
  ABCBA
 ABCDCBA


n = 4
for i in range(n):
  A = 65
  for j in range(n-i):
    print(" ", end = "")
  for j in range(i+1):
    print(chr(A), end = "")
    A += 1
  for j in range(i):
    A -= 1
    print(chr(A-1), end = "")
  print()
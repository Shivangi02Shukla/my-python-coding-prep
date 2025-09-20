E
DE
CDE
BCDE
ABCDE


n = 5
E = 69
for i in range(n):
  E -= i
  for j in range(i+1):
    # print(E-i)
    print(chr(E-i), end = "")
    E += 1
  print()
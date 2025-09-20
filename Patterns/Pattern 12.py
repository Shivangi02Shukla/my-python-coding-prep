1      1
12    21
123  321
12344321


n = 5
for i in range(n-1):
  for j in range(i+1):
    print(j+1, end = "")
  for j in range(2*(n-i-2)):
    print(" ", end = "")
  for k in range(i+1, 0, -1):
    print(k, end = "")
  print()
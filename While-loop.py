class Solution:
    def calculateMultiples(self, n):
        count = 10
        while count > 1:
            print(count * n, end = " ")
            count -= 1
        print(n)
    
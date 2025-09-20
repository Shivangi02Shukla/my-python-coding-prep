class Solution:
    def compareNM(self, n : int, m : int) -> str:
        # code here
        if n < m:
            return "lesser"
        elif n > m:
            return "greater"
        else:
            return "equal"
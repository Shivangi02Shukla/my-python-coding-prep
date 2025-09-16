#User function Template for python3
import math

class Solution:
    def switchCase(self, choice, arr):
        # Code here
        match choice:
            case 1:
                return math.pi * arr[0] * arr[0]
            case 2:
                return arr[0] * arr[1]
            # case default:
            #     return -1
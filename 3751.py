# https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/description/

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness = 0
        if num2 < 100: return 0
        for n in range(max(100,num1), num2 + 1):
            digits = []
            c = n 
            while c > 0:
                digits.append(c % 10)
                c = (c - digits[-1]) // 10
            digits = digits[::-1]
            for i in range(1, len(digits) - 1):
                if (digits[i-1] < digits[i] and digits[i] > digits[i+1]) or (digits[i-1] > digits[i] and digits[i] < digits[i+1]):
                    waviness+=1
        return waviness

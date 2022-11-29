class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2147483647
        flag = False
        reverse = 0
        if(x < 0):
            x *= -1
            flag=True

        while(x > 0):
            lastDigit = x % 10
            reverse =(reverse*10) +lastDigit
            x = x // 10

        if (reverse >= INT_MAX):
            return 0
        if flag:
            return (reverse * -1)
        return reverse

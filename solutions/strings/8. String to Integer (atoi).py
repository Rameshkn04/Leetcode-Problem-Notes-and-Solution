class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        num = 0

        #skip leading spaces
        while i < n and s[i] == " ":
            i += 1
        
        #Step 2 Sign
        if i < n and (s[i] == '+' or s[i] == "-"):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        #convert to digits
        while i < n and s[i].isdigit():
            num = num * 10 + (ord(s[i]) - ord('0'))
            # clamp overflow
            if sign * num <= -2**31:
                return -2**31
            if sign * num >= 2**31 - 1:
                return 2**31 - 1
            
            i += 1
        return sign* num

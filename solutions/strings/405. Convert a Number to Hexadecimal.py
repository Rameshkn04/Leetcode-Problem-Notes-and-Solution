class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        if num < 0:
            num &= 0xFFFFFFFF   # convert to 32-bit two’s complement

        hex_chars = "0123456789abcdef"
        res = ""

        while num > 0:
            res = hex_chars[num % 16] + res
            num //= 16

        return res

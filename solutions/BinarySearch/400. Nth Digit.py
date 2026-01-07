class Solution:
    def findNthDigit(self, n: int) -> int:
        digit_length = 1
        count = 9
        start = 1
        
        # Step 1: find the digit-length group
        while n > digit_length * count:
            n -= digit_length * count
            digit_length += 1
            count *= 10
            start *= 10
        
        # Step 2: find the exact number
        number = start + (n - 1) // digit_length
        
        # Step 3: find the digit within the number
        digit_index = (n - 1) % digit_length
        
        return int(str(number)[digit_index])

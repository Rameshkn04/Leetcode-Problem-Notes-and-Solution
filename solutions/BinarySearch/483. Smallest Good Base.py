class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        max_m = n.bit_length() - 1
        
        for m in range(max_m, 1, -1):
            left, right = 2, int(n ** (1 / m)) + 1
            
            while left <= right:
                k = (left + right) // 2
                
                total = 1
                curr = 1
                for _ in range(m):
                    curr *= k
                    total += curr
                    if total > n:
                        break
                
                if total == n:
                    return str(k)
                elif total < n:
                    left = k + 1
                else:
                    right = k - 1
        
        return str(n - 1)

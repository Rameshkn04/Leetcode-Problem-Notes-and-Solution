import bisect

class Solution:
    def findRadius(self, houses, heaters):
        heaters.sort()
        ans = 0
        
        for house in houses:
            idx = bisect.bisect_left(heaters, house)
            
            left_dist = float('inf')
            right_dist = float('inf')
            
            if idx > 0:
                left_dist = house - heaters[idx - 1]
            if idx < len(heaters):
                right_dist = heaters[idx] - house
            
            ans = max(ans, min(left_dist, right_dist))
        
        return ans

import bisect

class Solution:
    def findRightInterval(self, intervals):
        n = len(intervals)
        
        # Store (start, original_index)
        starts = [(intervals[i][0], i) for i in range(n)]
        starts.sort()
        
        result = [-1] * n
        start_values = [s[0] for s in starts]
        
        for i in range(n):
            end = intervals[i][1]
            
            # Binary search for smallest start >= end
            idx = bisect.bisect_left(start_values, end)
            
            if idx < n:
                result[i] = starts[idx][1]
        
        return result

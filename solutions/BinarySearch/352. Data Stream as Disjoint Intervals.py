class SummaryRanges:
    def __init__(self):
        self.intervals = {}

    def addNum(self, val: int) -> None:
        if val in self.intervals:
            return

        start = end = val
        for s in sorted(self.intervals):
            e = self.intervals[s]
            if e + 1 < val:
                continue
            if s - 1 > val:
                break

            start = min(start, s)
            end = max(end, e)
            del self.intervals[s]

        self.intervals[start] = end

    def getIntervals(self) -> List[List[int]]:
        return [[s, self.intervals[s]] for s in sorted(self.intervals)]

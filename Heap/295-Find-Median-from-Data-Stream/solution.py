import heapq

class MedianFinder:
    def __init__(self):
        # max_heap (small half), min_heap (large half)
        self.small = [] # Python's heapq is a min-heap, so we store negative values
        self.large = []

    def addNum(self, num):
        # 1. Add to small (max-heap)
        heapq.heappush(self.small, -num)
        
        # 2. Make sure every num in small is <= every num in large
        if (self.small and self.large and 
            (-self.small[0]) > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # 3. Balance the sizes (size difference max 1)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        elif len(self.large) > len(self.small):
            return float(self.large[0])
        else:
            return (-self.small[0] + self.large[0]) / 2.0

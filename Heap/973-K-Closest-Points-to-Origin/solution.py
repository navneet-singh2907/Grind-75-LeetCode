import heapq

class Solution:
    def kClosest(self, points, k):
        max_heap = []
        
        for x, y in points:
           
            dist = -(x**2 + y**2)
            
           
            if len(max_heap) == k:
                heapq.heappushpop(max_heap, (dist, x, y))
            else:
                heapq.heappush(max_heap, (dist, x, y))
        
        
        return [[x, y] for dist, x, y in max_heap]

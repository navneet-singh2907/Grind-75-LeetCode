import heapq


class Solution:
    def mergeKLists(self, lists):
        min_heap = []
        # Use a counter to handle nodes with the same value
        count = 0 
        
        # 1. Put the head of each list into the min-heap
        for l in lists:
            if l:
                heapq.heappush(min_heap, (l.val, count, l))
                count += 1
        
        dummy = ListNode(0)
        curr = dummy
        
        # 2. Extract min and push next node from that list
        while min_heap:
            val, _, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(min_heap, (node.next.val, count, node.next))
                count += 1
                
        return dummy.next

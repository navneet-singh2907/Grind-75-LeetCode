
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            # Store the next node
            nxt = curr.next
            # Reverse the pointer
            curr.next = prev
            # Advance the pointers
            prev = curr
            curr = nxt
            
        return prev

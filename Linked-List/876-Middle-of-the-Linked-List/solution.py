
class Solution:
    def middleNode(self, head):
        slow = head
        fast = head
        
        # Move fast pointer twice as fast as the slow pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # When fast reaches the end, slow is at the middle
        return slow

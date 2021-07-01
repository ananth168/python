class ListNode:                     #initializing singly linked list
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def ReverseList(self, head):
        pre = None
        cur = head
        suc = None

        while cur:                 #reversing the singly linked list
            suc = cur.next
            cur.next = pre
            pre = cur 
            cur = suc

        head = pre 
        return head



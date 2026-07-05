# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: 
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        str1 = ""
        while l1:
            str1 += str(l1.val)
            l1 = l1.next
        
        str2 = ""
        while l2:
            str2 += str(l2.val)
            l2 = l2.next
        

        total = str(int(str1[::-1]) + int(str2[::-1]))

        reversed_total = total[::-1]


        start = ListNode(0)
        node = start

        for char in reversed_total:
            node.next = ListNode(int(char))
            node = node.next

        return start.next

        
        
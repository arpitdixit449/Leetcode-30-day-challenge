'''
Problem Statement -> Given a non-empty, singly linked list with head node head, return a middle node of linked list.
                     If there are two middle nodes, return the second middle node.
                     
Example 1 -> Input: [1,2,3,4,5]
             Output: Node 3 from this list (Serialization: [3,4,5])
             
Example 2 -> Input: [1,2,3,4,5,6]
             Output: Node 4 from this list (Serialization: [4,5,6])
'''

#Solution : Time O(n), Space O(1)


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None:
            return
        length = 0
        node = head
        while node is not None:
            length += 1
            node = node.next
        
        i = 0
        node = head
        while i != length//2:
            i+=1
            node = node.next
        return node

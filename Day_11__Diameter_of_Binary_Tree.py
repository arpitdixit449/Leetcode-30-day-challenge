'''
Problem Statement -> Given a binary tree, you need to compute the length of the diameter of the
                     tree. The diameter of a binary tree is the length of the longest path
                     between any two nodes in a tree. This path may or may not pass through the root.
                     
Example->Input: 1
               / \
              2   3
             / \     
            4   5    
          Output : Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
'''

#Solution - Using DFS : Time O(n), Space O(log(n))[Recursion Stack]


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        arr = []
        self.helper(root,arr)
        if not len(arr):
            return 0
        return max(arr)
    
    def helper(self,root,arr):
        if root is None:
            return 0
        left = self.helper(root.left,arr)
        right = self.helper(root.right,arr)
        arr.append(left+right)
        return max(left,right)+1
        

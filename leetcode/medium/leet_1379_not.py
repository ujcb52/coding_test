#1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree

# Given two binary trees original and cloned and given a reference to a node target in the original tree.
# The cloned tree is a copy of the original tree.

# Return a reference to the same node in the cloned tree.
# Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

#Follow up: Solve the problem if repeated values on the tree are allowed.

#Example 1:

#Input: tree = [7,4,3,null,null,6,19], target = 3
#Output: 3
#Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.res = None
        def dfs(node):
            if not node or self.res:
                return 
            if node.val == target.val:
                self.res = node
            dfs(node.left)
            dfs(node.right)
        dfs(cloned)
        return self.res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
#         def it(node):
#             if node:
#                 yield node
#                 yield from it(node.left)
#                 yield from it(node.right)
            
#         for n1, n2 in zip(it(original), it(cloned)):
#             if n1 == target:
#                 return n2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        temp = collections.deque()
        if root :
            temp.append(root)

        while temp:
            val = []
            for i in range(len(temp)):
                node = temp.popleft()
                val.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            result.append(val)
        
        return result
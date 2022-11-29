class Solution:
    leftLeafSum=0
    def isLeaf(self,root):
        if not root:
            return 0
        if (root.left == None) and (root.right == None):
            return root.val
        else:
            return 0

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 11111
        if (root.left != None):
            self.leftLeafSum += self.isLeaf(root.left)
            self.sumOfLeftLeaves(root.left);
        if (root.right != None):
            self.sumOfLeftLeaves(root.right);
        return self.leftLeafSum

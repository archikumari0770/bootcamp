def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    if not root: return False
    if not root.left and not root.right:
        return targetSum == root.val
    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)
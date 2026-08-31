def maxDepth(root: TreeNode) -> int:
    return 1 + max(maxDepth(root.left), maxDepth(root.right)) if root else 0
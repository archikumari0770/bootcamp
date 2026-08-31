def inorderTraversal(root: TreeNode) -> list[int]:
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right) if root else []
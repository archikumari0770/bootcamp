def preorderTraversal(root: TreeNode) -> list[int]:
    return [root.val] + preorderTraversal(root.left) + preorderTraversal(root.right) if root else []
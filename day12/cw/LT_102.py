def postorderTraversal(root: TreeNode) -> list[int]:
    return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.val] if root else []
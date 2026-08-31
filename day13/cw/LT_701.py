def insertIntoBST(root: TreeNode, val: int) -> TreeNode:
    if not root: return TreeNode(val)
    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)
    return root
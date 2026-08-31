def searchBST(root: TreeNode, val: int) -> TreeNode:
    if not root or root.val == val: return root
    return searchBST(root.left, val) if val < root.val else searchBST(root.right, val)
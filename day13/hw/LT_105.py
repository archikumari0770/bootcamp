def buildTree(preorder: list[int], inorder: list[int]) -> TreeNode:
    in_map = {val: i for i, val in enumerate(inorder)}
    pre_idx = 0

    def helper(left, right):
        nonlocal pre_idx
        if left > right: return None
        val = preorder[pre_idx]
        pre_idx += 1
        root = TreeNode(val)
        idx = in_map[val]
        root.left = helper(left, idx - 1)
        root.right = helper(idx + 1, right)
        return root

    return helper(0, len(inorder) - 1)
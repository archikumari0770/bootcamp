def buildTree(inorder: list[int], postorder: list[int]) -> TreeNode:
    in_map = {val: i for i, val in enumerate(inorder)}

    def helper(left, right):
        if left > right: return None
        val = postorder.pop()
        root = TreeNode(val)
        idx = in_map[val]
        root.right = helper(idx + 1, right)
        root.left = helper(left, idx - 1)
        return root

    return helper(0, len(inorder) - 1)
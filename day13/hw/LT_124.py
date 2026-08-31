def maxPathSum(root: TreeNode) -> int:
    max_sum = float('-inf')

    def max_gain(node):
        nonlocal max_sum
        if not node: return 0
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)
        max_sum = max(max_sum, node.val + left_gain + right_gain)
        return node.val + max(left_gain, right_gain)

    max_gain(root)
    return max_sum
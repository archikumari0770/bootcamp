from collections import defaultdict

def pathSum(root: TreeNode, targetSum: int) -> int:
    count = 0
    prefix_sums = defaultdict(int)
    prefix_sums[0] = 1

    def dfs(node, curr_sum):
        nonlocal count
        if not node: return
        curr_sum += node.val
        count += prefix_sums[curr_sum - targetSum]
        prefix_sums[curr_sum] += 1
        dfs(node.left, curr_sum)
        dfs(node.right, curr_sum)
        prefix_sums[curr_sum] -= 1

    dfs(root, 0)
    return count
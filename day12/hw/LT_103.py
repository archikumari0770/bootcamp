from collections import deque

def rightSideView(root: TreeNode) -> list[int]:
    if not root: return []
    res, q = [], deque([root])
    while q:
        rightmost = None
        for _ in range(len(q)):
            node = q.popleft()
            rightmost = node.val
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(rightmost)
    return res
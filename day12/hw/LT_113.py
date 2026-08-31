def binaryTreePaths(root: TreeNode) -> list[str]:
    paths = []
    def dfs(node, path):
        if not node: return
        path += str(node.val)
        if not node.left and not node.right:
            paths.append(path)
        else:
            path += "->"
            dfs(node.left, path)
            dfs(node.right, path)
    dfs(root, "")
    return paths
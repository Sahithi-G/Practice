def getSize(node):
    if not node:
        return 0
    return (1 + getSize(node.left) + getSize(node.right))

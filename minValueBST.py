def minValue(root):
    if not root:
        return -1
    if not root.left:
        return root.data
    else:
        return minValue(root.left)

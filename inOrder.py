# RECURSIVE: Return a list containing the inorder traversal of the given tree
def InOrder(root):
    res=[]
    if not root:
        return res
    if root.left:
        res.extend(InOrder(root.left))
    res.append(root.data)
    if root.right:
        res.extend(InOrder(root.right))
    return res
  
  # ITERATIVE: Return a list containing the inorder traversal of the given tree
  

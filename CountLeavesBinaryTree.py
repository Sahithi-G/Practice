'''
Given a Binary Tree of size N , You have to count leaves in it.
https://practice.geeksforgeeks.org/problems/count-leaves-in-binary-tree/1
'''
def countLeaves(root):
    # Code here
    if not root:
        return 0
    if root.right or root.left:
        return(0+countLeaves(root.right)+countLeaves(root.left))
    else:
        return 1

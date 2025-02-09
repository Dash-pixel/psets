# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):

        return f"value {self.val}, left {self.left.val if self.left else 'None'} right {self.right.val if self.right else 'None'}"




def buildTree(preorder, inorder):
    inorder_dict = {value: index for index, value in enumerate(inorder)}
    prev = TreeNode(val = preorder[0])
    parent_stack = [prev]

    for value in preorder[1:]:
        node = TreeNode(val = value)

        if inorder_dict[value] < inorder_dict[parent_stack[-1].val]:
            parent_stack[-1].left = node
            parent_stack.append(node)
        else:
            # search for the left parent of the node?
            while parent_stack and inorder_dict[value] > inorder_dict[parent_stack[-1].val]:
                parent = parent_stack.pop()
            
            parent.right = node
            parent_stack.append(node)
    


    return prev
    




#Tree
                                   1
                                /     \
                              2         3
                           /    \     /    \
                          4      5   6      7
#Traversal techniques for Tree                                  
class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
def Preorder(root):
    if root==None:
        return
    print(root.value,end=' ')
    Preorder(root.left)
    Preorder(root.right)
def Inorder(root):
    if root==None:
        return
    Inorder(root.left)
    print(root.value,end=' ')
    Inorder(root.right)
def Postorder(root):
    if root==None:
        return
    Postorder(root.left)
    Postorder(root.right)
    print(root.value,end=' ')
if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(3)
    root.left.left=node(4)
    root.left.right=node(5)
    root.right.left=node(6)
    root.right.right=node(7)
    print('Preorder')
    Preorder(root)
    print('\nInorder')
    Inorder(root)
    print('\nPostorder')
    Postorder(root)

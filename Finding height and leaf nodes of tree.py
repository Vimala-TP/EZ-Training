#Tree
'''                           1
                     2                5
              (L)3       4                 6
                      9               7         8(L)
                         10              11
                      14(L)          12
                                        13(L)'''
class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
#Function to find height of the tree
def Height(root):
    if root==None:
        return 0
    LH=Height(root.left)
    RH=Height(root.right)
    H=max(LH,RH)+1
    return H
#Function to print Leaf nodes
def Leaf_nodes(root):
    if root==None:
        return 0
    else:
        if root.left==None and root.right==None:
            print(root.value,end=' ')
    Leaf_nodes(root.left)
    Leaf_nodes(root.right)
if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(5)
    root.left.left=node(3)
    root.left.right=node(4)
    root.right.right=node(6)
    root.left.right.left=node(9)
    root.right.right.left=node(7)
    root.right.right.right=node(8)
    root.left.right.left.right=node(10)
    root.right.right.left.right=node(11)
    root.left.right.left.right.left=node(14)
    root.right.right.left.right.left=node(12)
    root.right.right.left.right.left.right=node(13)
    H=Height(root)
    print('\nHeaight of Tree =',H)
    print('Leaf nodes')
    Leaf_nodes(root)
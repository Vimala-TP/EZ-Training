#Printing Left view and Right view of tree
'''                           1
                     2                5
              (L)3       4                 6
                      9               7         8(L)
                         10              11
                     14(L)           12
                                        13(L)'''
class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
def Left_View(root):
    Q=[root]
    Q.append(None)
    print(root.value,end=' ')
    while len(Q)>0:
        cur=Q.pop(0)
        if cur==None:
            if len(Q)==0:
                break
            else:
                print(Q[0].value,end=' ')
                Q.append(None)
        else:
            if cur.left!=None:
                Q.append(cur.left)
            if cur.right!=None:
                Q.append(cur.right)
def Right_View(root):
    Q=[root]
    Q.append(None)
    while len(Q)>0:
        cur=Q.pop(0)
        if cur==None:
            if len(Q)==0:
                break
            else:
                Q.append(None)
        else:
            if Q[0]==None:
                print(cur.value,end=' ')
            if cur.left!=None:
                Q.append(cur.left)
            if cur.right!=None:
                Q.append(cur.right)
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
    print('Left View elements')
    Left_View(root)
    print('\nRight View elements')
    Right_View(root)
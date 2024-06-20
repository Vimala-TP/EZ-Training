#Top View and Botthom View
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
class node_data:
    def __init__(self,node,HKey):
        self.node=node
        self.Hkey=HKey
def Top_View_Bottom_View(root):
    temp=node_data(root,0)
    Key_dic_T={}
    Key_dic_B={}
    Q=[temp]
    Q.append(None)
    while len(Q)!=0:
        cur=Q.pop(0)
        if cur==None:
            if len(Q)==0:
                break
            else:
                Q.append(None)
        else:
            if cur.Hkey not in Key_dic_T.keys():
                Key_dic_T[cur.Hkey]=cur.node.value
            Key_dic_B[cur.Hkey]=cur.node.value
            if cur.node.left!=None:
                temp=node_data(cur.node.left,cur.Hkey-1)
                Q.append(temp)
            if cur.node.right!=None:
                temp=node_data(cur.node.right,cur.Hkey+1)
                Q.append(temp)
    print('Top View Elements')
    for i in sorted(Key_dic_T):
        print(Key_dic_T[i],end=' ')
    print('\nBottom View Elements')
    for i in sorted(Key_dic_B):
        print(Key_dic_B[i],end=' ')
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
    Top_View_Bottom_View(root)
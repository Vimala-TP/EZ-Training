#Bellman's Ford Algorithm
print('-----Bellman-Ford Algorithm---')
g=[[  0  ,  6  ,  4  ,  5  ,False,False],
   [False,  0  ,False,False, -1  ,False],
   [False, -2  ,  0  ,False,  3  ,False],
   [False,False, -2  ,  0  ,False, -1  ],
   [False,False,False,False,  0  ,  3  ],
   [False,False,False,False,False,  0  ]]
d={0:'A',
   1:'B',
   2:'C',
   3:'D',
   4:'E',
   5:'F'}
el=[]
for i in range(len(g)):
    for j in range(len(g[i])):
        if g[i][j]!=False and g[i][j]!=0:
            el.append(tuple((i,j)))
print('\nEdges of the Graph are')
print(el)
dist={}
for i in range(len(g)):
    dist[i]=float("Inf")
dist[0]=0
for i in range(len(g)-1):
    for j in el:
        new_dist=dist[j[0]]+g[j[0]][j[1]]
        if dist[j[1]]>new_dist:
            dist[j[1]]=new_dist
print('\nMinimum cost from vertex 0 (A) to all the sources are')
print(dist)
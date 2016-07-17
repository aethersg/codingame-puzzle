x,y,j,k=[int(i) for i in raw_input().split()]
d={(-1,1):'SW',(0,1):'S',(1,1):'SE',(-1,0):'W',(0,0):None,(1,0):'E',(-1,-1):'NW',(0,-1):'N',(1,-1):'NE'}
while j!=x or k!=y:
    l,m=map(lambda a:(a[0]>a[1])-(a[0]<a[1]),((x,j),(y,k)))
    j+=l
    k+=m
    print d.get((l,m))
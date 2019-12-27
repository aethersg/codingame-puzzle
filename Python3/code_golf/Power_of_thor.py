x,y,j,k=map(int,input().split())
d={(-1,1):'SW',(0,1):'S',(1,1):'SE',(-1,0):'W',(1,0):'E'}
while 1:
 l,m=map(lambda a:(a[0]>a[1])-(a[0]<a[1]),((x,j),(y,k)))
 j+=l
 k+=m
 print(d.get((l,m)))
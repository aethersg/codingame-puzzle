def factors(n):
    t=n*n
    f=[]
    for i in range(1,n+1):
        if t %i==0:
            f.append(i)
    return f

n=int(input())
denominator_list=[]
t=n*n
factor_list=factors(n)
for f in factor_list:
    x=t//f
    xx = x+n
    yy = f+n
    denominator_list.append((xx,yy))
for xx,yy in denominator_list:
    print('1/%s = 1/%s + 1/%s'%(n,xx,yy))

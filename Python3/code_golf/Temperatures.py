n,t = int(input()),input()
if n==0:
    print(0)
else:
    mt=None
    nt=[int(x) for x in t.split()]
    for t in nt:
        if(mt is None)or(abs(t)<abs(mt))or(t==-mt) and (t>0):
            mt=t
    print(mt)
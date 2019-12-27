n,w,r,f,p,nc,ae,ne=[int(i) for i in input().split()]
m = {f:p}
for i in range(ne):
    ef, ep=[int(j) for j in input().split()]
    m[ef]=ep
def l(a,b,c):
    v=a-b.get(c)
    return"LEFT"if v>0 else"RIGHT"if v<0 else"N"
while 1:
    cf,cp,d=input().split()
    cf=int(cf)
    cp=int(cp)
    print("WAIT") if(not(-1in[cp,cf])and d!="N")and l(cp,m,cf)in[d,"N"]else print("BLOCK")
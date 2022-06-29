n=int(input())
m=int(input())
for i in range(n,m+1):
    t=i
    s=0
    while t:
        r=t%10
        s=s*10+r
        t=t//10
    if s==i:
        print(i,end=' ')
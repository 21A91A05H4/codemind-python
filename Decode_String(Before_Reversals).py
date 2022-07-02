t=int(input())
for k in range(t):
    a,b=map(int,input().split())
    s=input()
    for i in range(b):
        r=s[:b-i]
        s=r[::-1]+s[b-i:]
    print(s)
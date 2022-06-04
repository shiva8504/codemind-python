def rev(n):
    s=0
    while(n):
        d=n%10
        s=s*10+d
        n=n//10
    return s
n=int(input())
t=n**2
f=rev(n)
d=f**2
s=rev(d)
if(s==t):
    print(True)
else:
    print(False)
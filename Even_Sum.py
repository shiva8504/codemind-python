_=int(input())
s=list(map(int,input().split()))
sh=0
for h in s:
    if h%2==0:
        sh+=h
print(sh)
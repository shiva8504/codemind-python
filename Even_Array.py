_=int(input())
sh=list(map(int,input().split()))
for i in sh:
    if i%2!=0:
        print('False')
        break
else:
    print('True')
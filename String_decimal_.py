for l in range(0,int(input())):
    r=0
    v=input()
    for k in range(0,len(v)):
        if(ord(v[k])>=48 and ord(v[k])<=57):
            r+=1
    if r==len(v):
        print('True',end='
')
    else:
        print('False',end='
')
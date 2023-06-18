def anag(x,y,n,m):
    f ={}
    if n != m:
        return False
    for i in x:
        if i in f:
            f[i]+=1
        else:
            f[i] =1
    for i in y:
        if i in f:
            f[i]-=1
        else:
            f[i] =1
    for i in f.keys():
        if f[i]!=0:
            return False
    return True


if __name__ == "__main__":
    x = input()
    y = input()
    n = len(x)
    m = len(y)
    print(anag(x,y,n,m))
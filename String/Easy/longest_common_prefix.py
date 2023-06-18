def prefix(x,n):
    pre =""
    c=0
    for i in x:
        p = i[c]
        for j in range(1, n):
            if p == x[j][c]:
                continue
            else:
                break
        pre+=p
        c+=1
    return pre


#Driver Code
if __name__ == "__main__":
    x = [item for item in input().split(',')]
    n = len(x)
    print(prefix(x,n))
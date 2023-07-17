
def cons_ones(arr,n):
    maxone=0
    one=0
    for x in arr:
        if x==1:
            one+=1
            maxone= max(maxone, one)
        else:
            one=0
    return maxone

if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n= len(arr)
    print(cons_ones(arr,n))
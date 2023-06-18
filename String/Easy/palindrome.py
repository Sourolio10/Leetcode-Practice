def palin(x,n):
    low=0
    high = n-1
    while low<=high:
        if x[low] == x[high]:
            low+=1
            high-=1
            continue
        else:
            return False
    return True


#Driver Code
if __name__ == "__main__":
    x = input()
    n = len(x)
    print(palin(x,n))
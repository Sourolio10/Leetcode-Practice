def iso(x,y,n):
    d ={}
    for key, value in zip(x,y):
        d[key] = value
    for i in range(n):
        if d[x[i]] == y[i]:
            continue
        else:
            return False
    return True


#Driver Code
if __name__ == "__main__":
    x = input()
    y = input()
    n = len(x)
    print(iso(x,y,n))
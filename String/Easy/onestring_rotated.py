def rotatated(x,y,n):
    rot = y
    for i in range(n):
        if x == rot:
            return True
        else:
            rot = rot[1:n]+rot[0]
    return False

#Driver Code
if __name__ == "__main__":
    x = input()
    y = input()
    n = len(x)
    print(rotatated(x,y,n))
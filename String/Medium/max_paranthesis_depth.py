def paran(x,n):
    max_d=0
    c=0
    for i in x:
        if i == '(':
            c+=1
            max_d = max(max_d,c)
        elif i == ')':
            c-=1
            
    return max_d



if __name__ == "__main__":
    arr=[]
    x = input()
    n = len(x)
    print(paran(x,n))
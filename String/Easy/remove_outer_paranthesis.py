def paran(x,n):
    new_str =""
    c=0
    for i in x:
        if c==0 and i == '(':
            c+=1
            continue
        elif c==1 and i == ')':
            c-=1
            continue
        elif i == '(':
            c+=1
            new_str+=i
        elif i == ')':
            c-=1
            new_str+=i
    return new_str

#Driver Code
if __name__ == "__main__":
    arr=[]
    x = input()
    n = len(x)
    print(paran(x,n))
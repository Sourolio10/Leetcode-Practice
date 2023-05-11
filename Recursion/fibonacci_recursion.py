def fibo(n):
    if n<=1:
        return n
    
    l = fibo(n-1)
    sl = fibo(n-2)
    return l + sl

# Driver Code
if __name__ == "__main__":
    a=[]
    n = int(input())
    for i in range(n+1):
        print(fibo(i), end=" ")
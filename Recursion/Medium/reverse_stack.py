def  helper(i,n,st):
        if i > n: 
            return 
        
        st[i],st[n] = st[n],st[i]
        helper(i+1,n-1,st)
        
def reverse(st): 
    #code here
    n = len(st)
    helper(0,n-1,st)
    return st

# Driver Code
if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    print(reverse(arr))
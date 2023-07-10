def subseq(k,s,n):
    if n == k:
        print(*s[:n], sep = "", end = " ")
        return
    
    if s[n-1] == '1':
        s[n] ='0'
        subseq(k,s,n+1)

    if s[n-1] == '0':
        s[n] ='0'
        subseq(k,s,n+1)
        s[n] ='1'
        subseq(k,s,n+1)

if __name__ == "__main__":
    n = int(input())
    s=[0]*n
    s[0]='0'
    subseq(n,s,1)
    s[0]='1'
    subseq(n,s,1)

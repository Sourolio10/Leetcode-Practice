
def long_sub(s,k):
    l=0
    max_len=0
    d={}
    count=0
    for  r in range(len(s)):
        if s[r] not in d:
            d[s[r]]=0
        d[s[r]]+=1
        count = r-l+1
        if count - max(d.values()) <= k:
            max_len =  max(max_len, count)
    return max_len


if __name__ == "__main__":
    
    s= input()
    k = int(input())
    print(long_sub(s,k))
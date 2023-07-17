def long_sub(s):
    n= len(s)
    l=0
    le = 0
    a= set()
    for r in range(n):
        while l<r and s[r] in a:
            a.remove(s[l])
            l+=1
        a.add(s[r])
        le = max(le, r-l+1)
    return le

if __name__ == "__main__":
    
    s= input()
    print(long_sub(s))
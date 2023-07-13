
def helper(s,n):
    ans = []
    ser = []
    def paliin_part(ind):
        if ind == n:
            ans.append(ser[:])
            return
        for i in range(ind, n):
            if palindrome(s, ind, i):
                ser.append(s[ind: i+1])
                paliin_part(i+1)
                ser.pop()

    def palindrome(s, start, end):
        while start<=end:
            if s[start] != s[end]:
                return False
            start+=1
            end-=1
        return True

    paliin_part(0)
    return ans



# Driver Code
if __name__ == "__main__":
    s = input()
    n= len(s)
    x = helper(s,n)
    print(*x)
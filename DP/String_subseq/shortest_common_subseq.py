def lcsUtil(s1, s2, ind1, ind2, dp):
    if ind1 == 0 or ind2 == 0:
        return 0
    if dp[ind1][ind2] != 0:
        return dp[ind1][ind2]
    if s1[ind1-1] == s2[ind2-1]:
        dp[ind1][ind2] = 1 + lcsUtil(s1, s2, ind1 - 1, ind2 - 1, dp)
    else:
        dp[ind1][ind2] = 0 + max(lcsUtil(s1, s2, ind1, ind2 - 1, dp), lcsUtil(s1, s2, ind1 - 1, ind2, dp))
    return dp[ind1][ind2]

def lcs(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for j in range(m+1)] for i in range(n+1)]
    k = lcsUtil(s1, s2, n, m, dp)
    i = n
    j = m

    index = k-1
    ans = ""

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            ans += s1[i - 1]
            index -= 1
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            ans += s1[i - 1]
            i -= 1
        else:
            ans += s2[j - 1]
            j -= 1
    #Adding Remaing Characters - Only one of the below two while loops will run 
    while i > 0:
        ans += s1[i - 1]
        i -= 1
    while j > 0:
        ans += s2[j - 1]
        j -= 1

    ans=ans[::-1]
    return ans

def main():
    s1 = "brute"
    s2 ="groot"
    print("TheShortest Common Subsequence is", lcs(s1, s2))

if __name__ == '__main__':
    main()
def lcsUtil(s1, s2, ind1, ind2, dp):
    if ind1 < 0 or ind2 < 0:
        return 0
    if dp[ind1][ind2] != -1:
        return dp[ind1][ind2]
    if s1[ind1] == s2[ind2]:
        dp[ind1][ind2] = 1 + lcsUtil(s1, s2, ind1 - 1, ind2 - 1, dp)
    else:
        dp[ind1][ind2] = 0 + max(lcsUtil(s1, s2, ind1, ind2 - 1, dp), lcsUtil(s1, s2, ind1 - 1, ind2, dp))
    return dp[ind1][ind2]

def lcs(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[-1 for j in range(m)] for i in range(n)]
    k = lcsUtil(s1, s2, n - 1, m - 1, dp)
    return n+m- 2*k

def main():
    s1 = "bbabcbcab"
    s2 ="babcbbc"
    print("The Length of Longest Palindromic Subsequence is", lcs(s1, s2))

if __name__ == '__main__':
    main()
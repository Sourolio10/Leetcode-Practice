import sys
def cutRodUtil(price, ind, N, dp):
    if ind == 0:
        return N * price[0]

    if dp[ind][N] != -1:
        return dp[ind][N]

    notTaken = 0 + cutRodUtil(price, ind - 1, N, dp)

    taken = -sys.maxsize
    rodLength = ind + 1
    if rodLength <= N:
        taken = price[ind] + cutRodUtil(price, ind, N - rodLength, dp)

    dp[ind][N] = max(notTaken, taken)
    return dp[ind][N]


def cutRod(price, N):
    dp = [[-1 for j in range(N + 1)] for i in range(N)]
    return cutRodUtil(price, N - 1, N, dp)


def main():
    price = [2, 6, 7, 8, 10]
    n = len(price)
    print("The Maximum price generated is", cutRod(price, n))


if __name__ == "__main__":
    main()
def uniquePaths(m,n):
        def countPaths(i, j, n, m):
            if i == (n - 1) and j == (m - 1):
                return 1
            if i >= n or j >= m:
                return 0
            else:
                return countPaths(i + 1, j, n, m) + countPaths(i, j + 1, n, m)


        return countPaths(0, 0, m, n)




if __name__ == "__main__":
    m= int(input())
    n= int(input())
    totalCount = uniquePaths(m,n)
    print("The total number of Unique Paths are ", totalCount)
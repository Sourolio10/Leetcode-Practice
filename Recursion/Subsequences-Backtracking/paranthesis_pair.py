def dfs(left, right, s,n):
    if len(s) == n * 2:
        print(*s, sep = "", end = " ")
        return 

    if left < n:
        dfs(left + 1, right, s + '(',n)

    if right < left:
        dfs(left, right + 1, s + ')',n)

if __name__ == "__main__":
    n = int(input())
    dfs(0, 0, '',n)
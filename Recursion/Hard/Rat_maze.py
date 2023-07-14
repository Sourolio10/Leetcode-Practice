# Driver Code
def solve(i, j, board, vis, n, ans, move):
    if i==n-1 and j== n-1:
        ans.append(move)
        return
    
    #down
    if i+1<n and not vis[i+1][j] and board[i+1][j]==1:
        vis[i][j] = 1
        solve(i+1, j, board, vis, n, ans, move + 'D')
        vis[i][j] = 0

    #right
    if j+1<n and not vis[i][j+1] and board[i][j+1]==1:
        vis[i][j] = 1
        solve(i, j+1, board, vis, n, ans, move + 'R')
        vis[i][j] = 0

    #left
    if j-1>=0 and not vis[i][j-1] and board[i][j-1]==1:
        vis[i][j] = 1
        solve(i, j-1, board, vis, n, ans, move + 'L')
        vis[i][j] = 0

    if i-1>=0 and not vis[i-1][j] and board[i-1][j]==1:
        vis[i][j] = 1
        solve(i-1, j, board, vis, n, ans, move + 'U')
        vis[i][j] = 0
    


if __name__ == "__main__":
    n = int(input())
    board = [[1, 0, 0, 0], 
             [1, 1, 1, 1], 
             [0, 0, 0, 1], 
             [1, 1, 1, 1]]
    vis =[[0 for _ in range(n)] for _ in range(n)]
    ans = []
    solve(0,0, board, vis, n, ans, "")
    print(ans)
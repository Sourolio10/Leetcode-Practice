def checkQueens(row, col, board, n):
    temp_col=col
    temp_row = row

    while row>=0 and col>=0:
        if board[row][col] == 'Q':
            return False
        row-=1
        col-=1
    
    row = temp_row
    col = temp_col

    while col>=0:
        if board[row][col] == 'Q':
            return False
        col-=1

    row = temp_row
    col = temp_col
    while row<n and col>=0:
        if board[row][col] == 'Q':
            return False
        row+=1
        col-=1    

    return True

def solve(col, board, ans, n):
    if col == n:
        ans.append(list(board))
        return
    for row in range(n):
        if checkQueens(row, col, board, n):
            board[row] = board[row][:col] + 'Q' + board[row][col+1:]
            solve(col+1, board, ans, n)
            board[row] = board[row][:col] + '.' + board[row][col+1:]


# Driver Code
if __name__ == "__main__":
    n = int(input())
    board = ['.'*n for _ in range(n)]
    ans=[]
    solve(0, board, ans, n)
    print(ans)
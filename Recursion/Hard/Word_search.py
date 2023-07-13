
def search(board, word):
    m = len(board)
    n = len(board[0])
    
    for i in range(m):
        for j in range(n):
            if word[0] == board[i][j]:
                if board_search(word, board, i,j , 0 , m,n):
                    return True
    return False

def board_search(word, board, i,j , ind, m,n):
    if ind == len(word):
        return True
    
    if i<0 or j<0 or i==m or j==n or board[i][j] != word[ind] or board[i][j] == '!':
        return False
    

    # VERY IMPORTANT PART - LOGIC!!!!
    c= board[i][j]
    board[i][j] = '!'

    top = board_search(word, board, i-1,j , ind+1, m,n)
    right = board_search(word, board, i,j+1 , ind+1, m,n)
    bottom = board_search(word, board, i+1,j , ind+1, m,n)
    left = board_search(word, board, i,j-1 , ind+1, m,n)
    
    board[i][j] = c

    return top or right or bottom or left

# Driver Code
if __name__ == "__main__":
    rows = int(input())
    columns = int(input())

    # Initialize an empty matrix
    board = []
    for i in range(rows):
        row = []
        for j in range(columns):
            element = input(f"Enter element at position ({i+1}, {j+1}): ")
            row.append(element)
        board.append(row)
    
    word = input()
    x = search(board, word)
    print(x)
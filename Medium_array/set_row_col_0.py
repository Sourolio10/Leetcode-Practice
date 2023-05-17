def zero(arr, n, m):
    row=[0]*n
    col=[0]*m
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                row[i] = 1
                col[j] = 1
    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                arr[i][j] = 0
    return arr

# Driver Code
if __name__ == "__main__":
    rows = int(input())
    columns = int(input())

    # Initialize an empty matrix
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)
    print(zero(matrix, rows, columns))
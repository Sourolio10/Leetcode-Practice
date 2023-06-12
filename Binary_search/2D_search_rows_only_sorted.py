def binary(arr,n, m, x):
    for i in range(n):
        row = arr[i]
        low=0
        high = m - 1
        while low<=high:
            mid = (low+high)//2
            if row[mid]== x:
                return True
            elif row[mid]< x:
                low=mid+1
            else:
                high = mid-1
    return False

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
    x = int(input())
    print(binary(matrix,rows, columns, x))
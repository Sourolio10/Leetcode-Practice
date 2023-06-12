def countlessthanmid(arr,n,mid):
    l =0
    h= n-1
    while l<=h:
        m = (l+h)//2
        if arr[m] <= mid:
            l= m+1
        else:
            h= m-1
    return l



def binary(arr,n, m):
    l=0 
    h= 1e9
    while l<=h:
        mid = (l+h) //2
        c =0
        for i in range(n):
            c += countlessthanmid(arr[i],m,mid)
        if c<= (n*m)//2:
            l= mid+1
        else:
            h = mid-1
    return l
        


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
    print(binary(matrix,rows, columns))
def binary(mat, n,m):
    L, H = 0, len(mat) - 1
    #as long as we have at least one row left to consider, continue binary search!
    while L <= H:
        mid = (L + H) // 2
        mid_row = mat[mid]
        #initialize max_pos and store column pos later!
        max_pos = None
        max_val = -10000000
        #iterate linearly through the row since it's not sorted and find the maximum element as well
        #as its position!
        for j in range(len(mid_row)):
            if(mid_row[j] > max_val):
                max_val = mid_row[j]
                max_pos = j
                continue
        #once we have max_pos, then we have to compare relative to top and bottom neighbors!
        top_val = -1 if mid - 1 < 0 else mat[mid-1][max_pos]
        bottom_val = -1 if mid + 1 >= len(mat) else mat[mid+1][max_pos]
        #then it's a peak!
        if(top_val < max_val and bottom_val < max_val):
            return [mid, max_pos]
        #top neighboring element is bigger! -> it has better chance to be peak element!
        if(top_val >= max_val):
            H = mid - 1 
            continue
        if(bottom_val >= max_val):
            L = mid + 1
            continue


        

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
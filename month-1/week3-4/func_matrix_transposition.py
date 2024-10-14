# Matrix Transposition

# Description: Write a function transpose(matrix) that transposes a matrix (list of lists).
# Example: transpose([[1, 2, 3], [4, 5, 6]]) should return [[1, 4], [2, 5], [3, 6]].


def transpose(li):
    rows = len(li)
    cols = len(li[0]) if rows > 0 else 0

    # Create an empty matrix with transposed dimensions
    li1 = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            li1[j][i] = li[i][j]  

    return li1



li_str=input("enter list of list e,g [[1, 2, 3], [4, 5, 6]]: ")
li=eval(li_str)

matrix_transpose=transpose(li)

print(f"Transposed matrix: {matrix_transpose}")
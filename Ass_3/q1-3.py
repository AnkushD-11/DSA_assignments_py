#.Q1. Sum of diagonal elements using python:
def DiagonalSum(mat, n):
 
    principle = 0
    for i in range(0, n):
        principle += mat[i][i]
         
    print("Principle Diagonal:", principle)
 
# Driver code

a = [[ 1, 2, 3, 4 ],
     [ 5, 6, 7, 8 ],
     [ 9, 10, 11, 12 ],
     [ 13, 14, 15, 16 ]]

DiagonalSum(a, 4)

# Q2. Write a program to store following numbers ( 1 to 9) in a matrix in spiral manner.

def spiral(matrix):
    sol = []
    
    if(len(matrix)==0):
        return sol

    m = len(matrix)
    n = len(matrix[0])
    seen = [[0 for i in range(n)] for j in range(m)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    x = 0
    y = 0
    di = 0
 
    # Iterate from 0 to R * C - 1
    for i in range(m * n):
        sol.append(matrix[x][y])
        seen[x][y] = True
        cr = x + dr[di]
        cc = y + dc[di]
 
        if (0 <= cr and cr < m and 0 <= cc and cc < n and not(seen[cr][cc])):
            x = cr
            y = cc
        else:
            di = (di + 1) % 4
            x += dr[di]
            y += dc[di]
    return sol
 
 
# Driver code
if __name__ == "__main__":
    a = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]
 
    # Function call
    for x in spiral(a):
        print(x, end=" ")
    print()
    
# q3. Rotate matrix by 90

def rotate90Clockwise(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp
 
# Function to print the matrix
def printMatrix(A):
    N = len(A[0])
    for i in range(N):
        print(A[i])
 
# Driver code
A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
rotate90Clockwise(A)
printMatrix(A)
    

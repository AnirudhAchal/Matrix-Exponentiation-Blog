def get_fibonacci(n):

    if n <= 0: return -1 # throw error

    if n == 1: return 0
    if n == 2: return 1

    dp = [0] * (n + 1) # Initializing Array

    # Setting base case
    dp[1] = 0 
    dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

def power(x, n):

    result = 1

    while n > 0:

        if n % 2 != 0:
            result *= x

        n = n // 2
        x = x * x

    return result		

def matrix_power(P, n):
    m = len(P)
    R = [[1 if i == j else 0 for i in range(m)] for j in range(m)] # Initializing identity m x m matrix

    while n > 0:

        if n % 2 != 0:
            R = matrix_multiply(P, R)

        n = n // 2
        P = matrix_multiply(P, P)

    return R
 
def matrix_multiply(A, B):

    n = len(A)
    m = len(A[0])
    q = len(B)
    r = len(B[0])

    if m != q:
        return -1

    R = [[0 for i in range(r)] for j in range(n)]

    for i in range(n):
        for j in range(r):
            for k in range(m):
                R[i][j] += A[i][k] * B[k][j]

    return R

print(matrix_power([[2, 3],[2, 4]], 10))

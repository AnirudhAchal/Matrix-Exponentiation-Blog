def get_fibonacci(n):

    if n <= 0: return -1 # Throw error : Invalid value of n

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

    # Initializing identity m x m matrix
    R = [[1 if i == j else 0 for i in range(m)] for j in range(m)] 

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
        return -1 # Throw error : Incompatible
    # Initialzing m x m zero matrix
    R = [[0 for i in range(r)] for j in range(n)] 

    for i in range(n):
        for j in range(r):
            for k in range(m):
                R[i][j] += A[i][k] * B[k][j]

    return R

def get_fibonacci_matrix_exp(n):
    if n <= 0: return -1 # Throw error
    if n == 1: return 0
 
    F2 = [[1],
		  [0]]
 
    P = [[1, 1],
		 [1, 0]]
 
    Pn_2 = matrix_power(P, n - 2) # Calculating P^(n-2)
    Fn = matrix_multiply(Pn_2, F2) # Fn = P^(n-2) * F2

    return Fn[0][0] 

def get_tiling_count_dp(n):
    if n == 1: return 0
    if n == 2: return 0

    dp = [0] * (n + 1)
    dp[3] = 2
    
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 3]

    return dp[n]
 
def get_tiling_count(n):
    if n <= 0: return -1 # Throw error : Invalid value of n
    if n == 1: return 0
    if n == 2: return 0
 
    DP3 = [[2],
           [0],
           [0]]
 
    P = [[1, 0, 1],
         [1, 0, 0],
         [0, 1, 0]]
 
    Pn_3 = matrix_power(P, n - 3) # Calculating P^(n-3)
    DPn = matrix_multiply(Pn_3, DP3) # DPn = P^(n-3) * DP3

    return DPn[0][0] 

for i in range(1, 10000000):
    print(get_tiling_count(i), get_tiling_count_dp(i))

---
 layout: post
 title: "An introduction to Matrix Exponentiation"
 author_github: AnirudhAchal
 date: 2021-01-06
 image: '/assets/img/'
 description: 'Introductory post to Matrix Exponentiation'
 tags:
 - IEEE NITK
 - CompSoc
 - DP
 - Matrix Exponentiation
 - Competitive Programming
 categories:
 - Compsoc
 github_username: 'AnirudhAchal'
 ---
 
 Matrix Exponentiation is one of the most used techniques in advanced competitive programming. The concept of matrix exponentiation in its most general form is very useful in solving questions that involve calculating the nth term of a linear recurrence relation in time of the order of log(n). It is especially useful in converting a linear O(n) dynamic programming solution into a O(log(n)) solution. 
 
To understand this better, let us consider a very simple example of finding the nth Fibonacci number. This problem can be very easily solved using a linear recurrence. As we all know, by definition of the fibonacci series, F<sub>n</sub> = F<sub>n - 1</sub> + F<sub>n - 2</sub>. Consider the code below that calculates the nth fibonacci number. 

``` python
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

```

This solution is an iterative dp that runs in linear time ie. O(n). Note that this solution has a space complexity of O(n), but it can be easily converted into O(1) space. 


Now at first there does not seem to be any straightforward way to improve the time complexity of this solution. This is where matrix exponentiation comes into the picture. Our goal is to obtain a recurrence relation of the form F<sub>n</sub> = P * F<sub>n - 1</sub>  where P is a constant matrix and F<sub>n</sub> and F<sub>n - 1</sub> are respectively matrices.  Let us see what happens if we obtain such a relation. 

F<sub>2</sub> = P * F<sub>1</sub> 

F<sub>3</sub> = P * F<sub>2</sub> \
F<sub>3</sub> = P * P * F<sub>1</sub> \
F<sub>3</sub> = P<sup>2</sup> * F<sub>1</sub> 

F<sub>4</sub> = P * F<sub>3</sub> \
F<sub>4</sub> = P * P<sup>2</sup> * F<sub>1</sub> \
F<sub>4</sub> = P<sup>3</sup> * F<sub>1</sub> 

.\
.\
.

Fn = P^(n - 1) * F1

This is a very helpful relation. We have got the nth term of the series in terms of the base matrix F<sub>1</sub>. <b>Note:</b> This base matrix need not always be n = 1. 

You must already be knowing that x<sup>n</sup> can be calculated in O(log(n)) time using binary exponentiation where x and n are integers. Refer to the code below in case you need a refresher on how that is done. If you have never heard of binary exponentiation, go through [this](https://cp-algorithms.com/algebra/binary-exp.html) article before continuing.

``` python
def power(x, n):

    result = 1

    while n > 0:

        if n % 2 != 0:
            result *= x

        n = n // 2
        x = x * x

    return result			
```

A very similar function can be implemented to calculate P<sup>n</sup> in O(log(n) * m<sup>3</sup>) time where P is a square matrix and n is an integer and m is the dimension of P (ie. P is an m x m matrix).  

``` python
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

```

'matrix_multiply' is a function that runs in O(n<sup>3</sup>). Considering that, the overall time complexity of calculating P<sup>n</sup> is O(log(n) * m<sup>3</sup>).

Now let us get back to the original question. That is calculating the nth fibonacci number. What we need to do is to get the matrices F<sub>n</sub> and P. 

We consider F<sub>n</sub> to be:

```
|  fn  | 
| fn_1 |
where fn is the nth fibonacci number and fn_1 is the (n-1)th fibonacci number.
```

# Matrix-Exponentiation-Blog
Matrix Exponentiation Blog for IEEE


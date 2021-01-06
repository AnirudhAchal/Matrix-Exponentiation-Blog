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

 
# Matrix-Exponentiation-Blog
Matrix Exponentiation Blog for IEEE

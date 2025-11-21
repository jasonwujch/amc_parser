# 2009 AIME II Problem 4

## Problem

A group of children held a grape-eating contest. When the contest was over, the winner had eaten $n$ grapes, and the child in $k$ -th place had eaten $n+2-2k$ grapes. The total number of grapes eaten in the contest was $2009$ . Find the smallest possible value of $n$ .

## Solution
### Resolving the ambiguity
The problem statement is confusing, as it can be interpreted in two ways: Either as "there is a $k>1$ such that the child in $k$ -th place had eaten $n+2-2k$ grapes", or "for all $k$ , the child in $k$ -th place had eaten $n+2-2k$ grapes".
The second meaning was apparently the intended one. Hence we will restate the problem statement in this way:
A group of $c$ children held a grape-eating contest. When the contest was over, the following was true: There was a $n$ such that for each $k$ between $1$ and $c$ , inclusive, the child in $k$ -th place had eaten exactly $n+2-2k$ grapes. The total number of grapes eaten in the contest was $2009$ . Find the smallest possible value of $n$ .

## Solution 1
The total number of grapes eaten can be computed as the sum of the arithmetic progression with initial term $n$ (the number of grapes eaten by the child in $1$ -st place), difference $d=-2$ , and number of terms $c$ . We can easily compute that this sum is equal to $c(n-c+1)$ .
Hence we have the equation $2009=c(n-c+1)$ , and we are looking for a solution $(n,c)$ , where both $n$ and $c$ are positive integers, $n\geq 2(c-1)$ , and $n$ is minimized. (The condition $n\geq 2(c-1)$ states that even the last child had to eat a non-negative number of grapes.)
The prime factorization of $2009$ is $2009=7^2 \cdot 41$ . Hence there are $6$ ways how to factor $2009$ into two positive terms $c$ and $n-c+1$ :
- $c=1$ , $n-c+1=2009$ , then $n=2009$ is a solution.
- $c=7$ , $n-c+1=7\cdot 41=287$ , then $n=293$ is a solution.
- $c=41$ , $n-c+1=7\cdot 7=49$ , then $n=89$ is a solution.
- In each of the other three cases, $n$ will obviously be less than $2(c-1)$ , hence these are not valid solutions.
The smallest valid solution is therefore $c=41$ , $n=\boxed{089}$ .

## Solution 2
If the first child ate $n=2m$ grapes, then the maximum number of grapes eaten by all the children together is $2m + (2m-2) + (2m-4) + \cdots + 4 + 2 = m(m+1)$ . Similarly, if the first child ate $2m-1$ grapes, the maximum total number of grapes eaten is $(2m-1)+(2m-3)+\cdots+3+1 = m^2$ .
For $m=44$ the value $m(m+1)=44\cdot 45 =1980$ is less than $2009$ . Hence $n$ must be at least $2\cdot 44+1=89$ . For $n=89$ , the maximum possible sum is $45^2=2025$ . And we can easily see that $2009 = 2025 - 16 = 2025 - (1+3+5+7)$ , hence $2009$ grapes can indeed be achieved for $n=89$ by dropping the last four children.
Hence we found a solution with $n=89$ and $45-4=41$ kids, and we also showed that no smaller solution exists. Therefore the answer is $\boxed{089}$ .

## Solution 3 (similar to solution 1)
If the winner ate n grapes, then 2nd place ate $n+2-4=n-2$ grapes, 3rd place ate $n+2-6=n-4$ grapes, 4th place ate $n-6$ grapes, and so on. Our sum can be written as $n+(n-2)+(n-4)+(n-6)\dots$ . If there are x places, we can express this sum as $(x+1)n-x(x+1)$ , as there are $(x+1)$ occurrences of n, and $(2+4+6+\dots)$ is equal to $x(x+1)$ . This can be factored as $(x+1)(n-x)=2009$ . Our factor pairs are (1,2009), (7,287), and (41,49). To minimize n we take (41,49). If $x+1=41$ , then $x=40$ and $n=40+49=\boxed{089}$ . (Note we would have come upon the same result had we used $x+1=49$ .) ~MC413551
### See Also
These problems are copyrighted © by the Mathematical Association of America.
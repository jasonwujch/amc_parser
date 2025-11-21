# 2016 AMC 10A Problem 14

## Problem

How many ways are there to write $2016$ as the sum of twos and threes, ignoring order? (For example, $1008\cdot 2 + 0\cdot 3$ and $402\cdot 2 + 404\cdot 3$ are two such ways.)

$\textbf{(A)}\ 236\qquad\textbf{(B)}\ 336\qquad\textbf{(C)}\ 337\qquad\textbf{(D)}\ 403\qquad\textbf{(E)}\ 672$

## Solution 1
The amount of twos in our sum ranges from $0$ to $1008$ , with differences of $3$ because $2 \cdot 3 = \operatorname{lcm}(2, 3)$ .
The possible amount of twos is $\frac{1008 - 0}{3} + 1 \Rightarrow \boxed{\textbf{(C)} 337}$ .

## Solution 2
You can also see that you can rewrite the word problem into an equation $2x + 3y$ = $2016$ . Therefore the question is just how many multiples of $3$ subtracted from 2016 will be an even number. We can see that $x = 1008$ , $y = 0$ all the way to $x = 0$ , and $y = 672$ works, with $y$ being incremented by $2$ 's.Therefore, between $0$ and $672$ , the number of multiples of $2$ is $\boxed{\textbf{(C)}337}$ .

## Solution 3
We can utilize the stars-and-bars distribution technique to solve this problem. We have 2 "buckets" in which we will distribute parts of our total sum, 2016. By doing this, we know we will have $\binom{2016-1}{2-1}$ "total" answers. We want every third x and second y, so we divide our previous total by 6, which will result in $2015/6$ . We have to round down to the nearest integer, and we have to add 2 because we did not consider the 2 solutions involving x or y being 0. So, $2015/6\implies335\implies335+2=\boxed{\textbf{(C)}337}$ .

## Solution 4
Another idea that one might get is to try and figure out the nature of how many ways there are to write for any even number X as the sum of twos and threes. We might be able to spot a pattern and apply it to a larger number such as 2016. Let's try the first six evens from zero: 2, 4, 6, 8, 10, and 12. There is 1 way for 2, 1 way for 4, 2 ways for 6, 2 ways for 8, 2 ways for 10, and 3 ways for 12. Notice that the number of ways goes up every time an even number is divisible by 3. Notice also that 2016 is divisible by 3. This means if we can find a pattern for every even number that is divisible by 3, we can find the answer for 2016. The first three even numbers that are divisible by 3 from zero are 6, 12, and 18. There are 2 ways for 6, 3 ways for 12, and 4 ways for 18 (5 for 24, 6 for 30, and 7 for 36). The pattern here is that the number of ways for any even number X that is divisible by 36 is X/6 + 1. It turns out this pattern holds for every X number. So, take 2016 and divide it by 6 and add 1 which gives 337.
-- danfanLOL

## Solution 5
Note that $2016 = 6 \cdot 336$ . In other words, we can write $2016$ as the sum of $336$ sixes.
In turn, we can express each $6$ as either $2 + 2 + 2$ or $3 + 3$ .
Therefore, we can write $2016$ as $n (2 + 2 + 2) + (336 - n) (3 + 3)$ , where $n$ is an integer between $0$ and $336$ , inclusive. Since each value of $n$ corresponds to a unique way to write the sum, we get $336 + 1 = \boxed{\textbf{(C)}337}$
~jd9

## Solution 6 (Generalized)
Note that we can formalize the idea of Solution 2 and Solution 4 into a general solution of the simplest Diophantine equation; given a special solution \((A, B)\) to the equation \(ax+by=c\), the general integer solution is given by \((A-bk, B+ak)\) for all \(k \in \mathbb{Z}\) iff \(\gcd (a, b) = 1\). For this particular equation, it is easy to see that the general solution is \((2k, 1008-3k)\). Given the restrictions, \(k = 0, 1, 2, ..., 336\). Therefore we get \(\boxed{\textbf{(C)}337}\) solutions.
~abghim

## Video Solution (CREATIVE THINKING)
https://youtu.be/0Uc3oWL7V38
~Education, the Study of Everything

## Video Solution
https://youtu.be/dHY8gjoYFXU?t=1058
~IceMatrix
https://youtu.be/99wDp0JcSUE
~savannahsolver

## Video Solution by OmegaLearn
https://youtu.be/ZhAZ1oPe5Ds?t=2959
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
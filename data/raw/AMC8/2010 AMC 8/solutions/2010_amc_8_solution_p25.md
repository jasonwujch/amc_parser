# 2010 AMC 8 Problem 25

## Problem

Everyday at school, Jo climbs a flight of $6$ stairs. Jo can take the stairs $1$ , $2$ , or $3$ at a time. For example, Jo could climb $3$ , then $1$ , then $2$ . In how many ways can Jo climb the stairs?

$\textbf{(A)}\ 13 \qquad\textbf{(B)}\ 18\qquad\textbf{(C)}\ 20\qquad\textbf{(D)}\ 22\qquad\textbf{(E)}\ 24$

## Solution 1
A dynamics programming approach is quick and easy. The number of ways to climb one stair is $1$ . There are $2$ ways to climb two stairs: $1$ , $1$ or $2$ . For 3 stairs, there are $4$ ways: ( $1$ , $1$ , $1$ ) ( $1$ , $2$ ) ( $2$ , $1$ ) ( $3$ )
For four stairs, consider what step they came from to land on the fourth stair. They could have hopped straight from the 1st, done a double from #2, or used a single step from #3. The ways to get to each of these steps are $1+2+4=7$ ways to get to step 4. The pattern can then be extended: $4$ steps: $1+2+4=7$ ways. $5$ steps: $2+4+7=13$ ways. $6$ steps: $4+7+13=24$ ways.
Thus, there are $\boxed{\textbf{(E) } 24}$ ways to get to step $6.$

## Solution 2 (Generating a Function)
We first start by doing some simple casework to try and find the number of ways we can get to the 1st, 2nd, and 3rd Stairs. The number of ways to climb one stair is $1$ . There are $2$ ways to climb two stairs: $1$ , $1$ or $2$ . For 3 stairs, there are $4$ ways: ( $1$ , $1$ , $1$ ) ( $1$ , $2$ ) ( $2$ , $1$ ) ( $3$ )
Next we must try to generalize a recursive function to find the number of ways to climb the stairs. We start out with $f(n)$ , which denotes the number of ways to climb the stairs. Then we must realize, To reach the nth stair, Jeff must take a 1 step from the $f(n-1)$ th stair, a double step from the $f(n-2)$ th stair, or a triple step from the $f(n-3)$ th stair. Therefore, the number of ways of reaching the nth step is the number of ways of reaching the $f(n-1)$ th plus the number of ways of reaching the $f(n-2)$ th plus the number of ways of reaching the $f(n-3)$ th. stair. So we have our generalized recursive function: \[f(n)=f(n-1)+f(n-2)+f(n-3)\]
Now that we have the function and a few of the values we can try to find $f(6)$
\[f(1)=1\] \[f(2)=2\] \[f(3)=f(3-1)+f(3-2)+f(3-3)=f(2)+f(1)+f(0)=2+1+1=4\] \[f(4)=f(4-1)+f(4-2)+f(4-3)=f(3)+f(2)+f(1)=4+2+1=7\] \[f(5)=f(5-1)+f(5-2)+f(5-3)=f(4)+f(3)+f(2)=7+4+2=13\] \[f(6)=f(6-1)+f(6-2)+f(6-3)=f(5)+f(4)+f(3)=13+7+4=24\]
Thus there are 24 ways to get to the 6th stair so the answer is $\boxed{\textbf{(E) } 24}$
~ algebraic_algorithmic
https://youtu.be/5UojVH4Cqqs?t=4560
~ pi_is_3.14
### Video by MathTalks
https://youtu.be/mSCQzmfdX-g
### See Also
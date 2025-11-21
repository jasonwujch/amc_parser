# 2008 AMC 8 Problem 22

## Problem

For how many positive integer values of $n$ are both $\frac{n}{3}$ and $3n$ three-digit whole numbers?

$\textbf{(A)}\ 12\qquad \textbf{(B)}\ 21\qquad \textbf{(C)}\ 27\qquad \textbf{(D)}\ 33\qquad \textbf{(E)}\ 34$

## Solution 1
Instead of finding n, we find $x=\frac{n}{3}$ . We want $x$ and $9x$ to be three-digit whole numbers. The smallest three-digit whole number is $100$ , so that is our minimum value for $x$ , since if $x \in \mathbb{Z^+}$ , then $9x \in \mathbb{Z^+}$ . The largest three-digit whole number divisible by $9$ is $999$ , so our maximum value for $x$ is $\frac{999}{9}=111$ . There are $12$ whole numbers in the closed set $\left[100,111\right]$ , so the answer is $\boxed{\textbf{(A)}\ 12}$ .
- ColtsFan10

## Solution 2
We can set the following inequalities up to satisfy the conditions given by the question, $100 \leq \frac{n}{3} \leq 999$ , and $100 \leq 3n \leq 999$ . Once we simplify these and combine the restrictions, we get the inequality, $300 \leq n \leq 333$ . Now we have to find all multiples of 3 in this range for $\frac{n}{3}$ to be an integer. We can compute this by setting $\frac{n} {3}=x$ , where $x \in \mathbb{Z^+}$ . Substituting $x$ for $n$ in the previous inequality, we get, $100 \leq x \leq 111$ , and there are $111-100+1$ integers in this range giving us the answer, $\boxed{\textbf{(A)}\ 12}$ .
- kn07

## Solution 3
We can create a list of the positive integers $n$ that fulfill the requirement of $\frac {n}{3}$ and $3n$ are three-digit whole numbers. The first number of this list must be $300$ since $\frac {300}{3} = 100$ is the smallest positive integer that satisfies this requirement. The last number of this list must be $333$ since $3 \cdot 333 = 999$ is the largest positive integer that satisfies this requirement. Since the problem requires $\frac {n}{3}$ and $3n$ must be whole numbers, the other numbers must be multiples of 3 (just like 300 and 333), so the list would look like this:
To put this list in to a countable form we must put it in a form similar to $1,2,3, . . ., n$ . So, we manipulate it as follows:
Now we can tell that there are 12 positive integers which satisfies the two requirements, so the answer is $\boxed{\textbf{(A)}\ 12}$ .
~julia333

## Solution 4
We have to find the range for all numbers first. We can first find the smallest digit in which $\frac {n}{3}$ is a 3 digit number that 3n is a 3 digit number which is $\frac {300}{3}$ = 100, then we find the biggest number in which $\frac {n}{3}$ is a 3 digit number and 3n is a 3 digit number which is $\frac {333}{3}$ = 111. Now we know that all integers from 100 to 111 are possible values and the amount of integer values in that range is $\boxed{\textbf{(A)}\ 12}$ (note I divided the numbers by 3 for convenience)
~twinotter

## Video Solution by OmegaLearn
https://youtu.be/rQUwNC0gqdg?t=230
### See Also
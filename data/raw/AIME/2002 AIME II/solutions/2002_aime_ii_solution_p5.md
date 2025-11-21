# 2002 AIME II Problem 5

## Problem

Find the sum of all positive integers $a=2^n3^m$ where $n$ and $m$ are non-negative integers, for which $a^6$ is not a divisor of $6^a$ .

## Solution 1
Substitute $a=2^n3^m$ into $a^6$ and $6^a$ , and find all pairs of non-negative integers (n,m) for which $(2^n3^m)^{6}$ is not a divisor of $6^{2^n3^m}$
Simplifying both expressions:
$2^{6n} \cdot 3^{6m}$ is not a divisor of $2^{2^n3^m} \cdot 3^{2^n3^m}$
Comparing both exponents (noting that there must be either extra powers of 2 or extra powers of 3 in the left expression):
$6n > 2^n3^m$ OR $6m > 2^n3^m$
Using the first inequality $6n > 2^n3^m$ and going case by case starting with n $\in$ {0, 1, 2, 3...}:
n=0: $0>1 \cdot 3^m$ which has no solution for non-negative integers m
n=1: $6 > 2 \cdot 3^m$ which is true for m=0 but fails for higher integers $\Rightarrow (1,0)$
n=2: $12 > 4 \cdot 3^m$ which is true for m=0 but fails for higher integers $\Rightarrow (2,0)$
n=3: $18 > 8 \cdot 3^m$ which is true for m=0 but fails for higher integers $\Rightarrow (3,0)$
n=4: $24 > 16 \cdot 3^m$ which is true for m=0 but fails for higher integers $\Rightarrow (4,0)$
n=5: $30 > 32 \cdot 3^m$ which has no solution for non-negative integers m
There are no more solutions for higher $n$ , as polynomials like $6n$ grow slower than exponentials like $2^n$ .
Using the second inequality $6m > 2^n3^m$ and going case by case starting with m $\in$ {0, 1, 2, 3...}:
m=0: $0>2^n \cdot 1$ which has no solution for non-negative integers n
m=1: $6>2^n \cdot 3$ which is true for n=0 but fails for higher integers $\Rightarrow (0,1)$
m=2: $12>2^n \cdot 9$ which is true for n=0 but fails for higher integers $\Rightarrow (0,2)$
m=3: $18>2^n \cdot 27$ which has no solution for non-negative integers n
There are no more solutions for higher $m$ , as polynomials like $6m$ grow slower than exponentials like $3^m$ .
Thus there are six numbers corresponding to (1,0), (2,0), (3,0), (4,0), (0,1), and (0,2). Plugging them back into the original expression, these numbers are 2, 4, 8, 16, 3, and 9, respectively. Their sum is $\framebox{042}$ .

## Solution 2 (faster and more concise)
Notice that the condition is equivalent to saying
\[v_2(a^6) \geq v_2(6^a) \implies 6n \geq a\] \[v_3(a^6) \geq v_3(6^a) \implies 6m \geq a.\]
Notice that we cannot have both expressions to be equality state, as that would result in $a^6 = 6^a.$ Testing, we see the possible pairs $(n, m)$ are $(1, 0), (2, 0), (3, 0), (4, 0), (0, 1), (0, 2).$ Since the $a$ grows much faster than the left-hand side of the above inequalities, these are all possible solutions. Adding, we get $\framebox{042}$ .
~Solution by Williamgolly
These problems are copyrighted © by the Mathematical Association of America.
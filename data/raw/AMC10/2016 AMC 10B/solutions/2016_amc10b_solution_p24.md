# 2016 AMC 10B Problem 24

## Problem

How many four-digit integers $abcd$ , with $a \neq 0$ , have the property that the three two-digit integers $ab<bc<cd$ form an increasing arithmetic sequence? One such number is $4692$ , where $a=4$ , $b=6$ , $c=9$ , and $d=2$ .

$\textbf{(A)}\ 9\qquad\textbf{(B)}\ 15\qquad\textbf{(C)}\ 16\qquad\textbf{(D)}\ 17\qquad\textbf{(E)}\ 20$

## Solution
The numbers are $10a+b, 10b+c,$ and $10c+d$ . Note that only $d$ can be zero, the numbers $ab$ , $bc$ , and $cd$ cannot start with a zero, and $a\le b\le c$ .
To form the sequence, we need $(10c+d)-(10b+c)=(10b+c)-(10a+b)$ . This can be rearranged as $10(c-2b+a)=2c-b-d$ . Notice that since the left-hand side is a multiple of $10$ , the right-hand side can only be $0$ or $10$ . (A value of $-10$ would contradict $a\le b\le c$ .) Therefore we have two cases: $a+c-2b=1$ and $a+c-2b=0$ .
Case 1: $2c-b-d=10$
If $c=9$ , then $b+d=8,\ 2b-a=8$ , so $5\le b\le 8$ . This gives $2593, 4692, 6791, 8890$ . If $c=8$ , then $b+d=6,\ 2b-a=7$ , so $4\le b\le 6$ . This gives $1482, 3581, 5680$ . If $c=7$ , then $b+d=4,\ 2b-a=6$ , so $b=4$ , giving $2470$ . There is no solution for $c=6$ . Added together, this gives us $8$ answers for Case 1.
Case 2: $2c-b-d=0$
This means that the digits themselves are in an arithmetic sequence, as $a+c-2b=0 \Rightarrow a-b=b-c.$ This gives us $9$ answers, \[1234, 1357, 2345, 2468, 3456, 3579, 4567, 5678, 6789.\] Adding the two cases together, we find the answer to be $8+9=$ $\boxed{\textbf{(D) }17}$ .

## Solution 2 (Brute Force, when you have lots of time)
Looking at the answer options, all the numbers are pretty small so it is easy to make a list.
$12|23|34 \rightarrow 1234$
$13|35|57 \rightarrow 1357$
$14|48|82 \rightarrow 1482$
$23|34|45 \rightarrow 2345$
$24|46|68 \rightarrow 2468$
$24|47|70 \rightarrow 2470$
$25|59|93 \rightarrow 2593$
$34|45|56 \rightarrow 3456$
$35|57|79 \rightarrow 3579$
$35|58|81 \rightarrow 3581$
$45|56|67 \rightarrow 4567$
$46|69|92 \rightarrow 4692$
$56|67|78 \rightarrow 5678$
$56|68|80 \rightarrow 5680$
$67|78|89 \rightarrow 6789$
$67|79|91 \rightarrow 6791$
$88|89|90 \rightarrow 8890$
Counting all the cases we get our answer of $17$ which is $\boxed{D}$ -srisainandan6

## Solution 3
Let $x$ be the difference between the numbers $ab$ , $bc$ , and $cd$ . We then have \[10a + b = 10b + c - x\] and \[10b + c = 10c + d - x.\]
Subtracting the second equation from the first and then simplifying, we are left with: \[10a + 8c + d = 19b.\]
Notice that $b > c$ . Because the values of $a$ and $d$ are irrelevant compared to the other numbers, we can just find pairs of $(b, c)$ such that $a > 0$ . Trying out each value of $b$ from $2$ to $9$ and summing the number of pairs yields $1 + 2 + 4 + 4 + 3 + 2 + 1 + 0 = \boxed{\textbf{(D) }17}$
- cappucher

## Video Solution
https://www.youtube.com/watch?v=UhPxvZ6V4Zs
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
# 2015 AMC 10A Problem 23

## Problem

The zeroes of the function $f(x)=x^2-ax+2a$ are integers. What is the sum of the possible values of $a?$

$\textbf{(A)}\ 7\qquad\textbf{(B)}\ 8\qquad\textbf{(C)}\ 16\qquad\textbf{(D)}\ 17\qquad\textbf{(E)}\ 18$

## Solution 1
By Vieta's Formula, $a$ is the sum of the integral zeros of the function, and so $a$ is integral.
Because the zeros are integral, the discriminant of the function, $a^2 - 8a$ , is a perfect square, say $k^2$ . Then adding 16 to both sides and completing the square yields \[(a - 4)^2 = k^2 + 16.\] Therefore $(a-4)^2 - k^2 = 16$ and \[((a-4) - k)((a-4) + k) = 16.\] Let $(a-4) - k = u$ and $(a-4) + k = v$ ; then, $a-4 = \dfrac{u+v}{2}$ and so $a = \dfrac{u+v}{2} + 4$ . Listing all possible $(u, v)$ pairs (not counting transpositions because this does not affect ( $u + v$ )), $(2, 8), (4, 4), (-2, -8), (-4, -4)$ , yields $a = 9, 8, -1, 0$ . These $a$ sum to $16$ , so our answer is $\boxed{\textbf{(C) }16}$ .

## Solution 2
Let $r_1$ and $r_2$ be the integer zeroes of the quadratic. By Vieta's Formulas , \[r_1 + r_2 = a\text{ and }r_1r_2 = 2a.\]
Plugging the first equation in the second, \[r_1r_2 = 2 (r_1 + r_2).\]
Rearranging gives \[r_1r_2 - 2r_1 - 2r_2 = 0 \implies (r_1 - 2)(r_2 - 2) = 4.\]
These factors $(f_1,f_2)$ (ignoring order, because we want the sum of factors), can be $(1, 4), (-1, -4), (2, 2),$ or $(-2, -2)$ .
The sum of distinct $a = r_1 + r_2 = (f_1+2) + (f_2+2)$ , and these factors give \[\sum_a a = (5+4) + (-5+4) + (4+4) + (-4+4) = \boxed{\textbf{(C) }16}\] .

## Video Solution by Richard Rusczyk
https://artofproblemsolving.com/videos/amc/2015amc10a/397

## Solution 3
Let the roots be $r$ and $s$ . By Vieta's we have that $r+s = a$ , and $rs = 2a$ . So by Simon's Favorite Factoring Trick: \[2r+2s = rs \Longrightarrow rs-2r-2s = 0 \Longrightarrow (r-2)(s-2) = 4.\] Now, we test out values of $r$ and $s$ to see which work. Lets say that $r-2 = 1$ , and $s-2 = 4$ . This implies that $(r,s) = (3,6)$ , so $a = 9$ . Now, we let $r-2 = 2$ , and $s-2 = 2$ , this gives us $(r,s) = (4,4)$ , which gives us a value for $a$ of $8$ . Now, we circle an answer of $17$ and move onto the next problem. Yike! They didn't say that $a$ can't be negative! This is where many people would go wrong. Let $r-2 = -1$ , and $s-2 = -4$ . This gives us that $(r,s) = (1,-2)$ . This results in a value of $-1$ for $a$ . Now, we let $r-2 = -2$ , and $s-2 = -2$ . This gives $a = 0$ . Now, we are done. Our total sum is $9+8-1 = \boxed{\textbf{(C) }16}$ .
-jb2015007 - minor edits by mathlover1205 and PojoDotCom

## Video Solution
https://youtu.be/RQ4ZCttwmA4
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
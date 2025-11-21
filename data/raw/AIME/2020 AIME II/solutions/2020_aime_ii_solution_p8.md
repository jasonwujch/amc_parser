# 2020 AIME II Problem 8

## Problem

Define a sequence recursively by $f_1(x)=|x-1|$ and $f_n(x)=f_{n-1}(|x-n|)$ for integers $n>1$ . Find the least value of $n$ such that the sum of the zeros of $f_n$ exceeds $500,000$ .

## Solution 1 (Official MAA)
First it will be shown by induction that the zeros of $f_n$ are the integers $a, {a+2,} {a+4,} \dots, {a + n(n-1)}$ , where $a = n - \frac{n(n-1)}2.$
This is certainly true for $n=1$ . Suppose that it is true for $n = m-1 \ge 1$ , and note that the zeros of $f_m$ are the solutions of $|x - m| = k$ , where $k$ is a nonnegative zero of $f_{m-1}$ . Because the zeros of $f_{m-1}$ form an arithmetic sequence with common difference $2,$ so do the zeros of $f_m$ . The greatest zero of $f_{m-1}$ is \[m-1+\frac{(m-1)(m-2)}2 =\frac{m(m-1)}2,\] so the greatest zero of $f_m$ is $m+\frac{m(m-1)}2$ and the least is $m-\frac{m(m-1)}2$ .
It follows that the number of zeros of $f_n$ is $\frac{n(n-1)}2+1=\frac{n^2-n+2}2$ , and their average value is $n$ . The sum of the zeros of $f_n$ is \[\frac{n^3-n^2+2n}2.\] Let $S(n)=n^3-n^2+2n$ , so the sum of the zeros exceeds $500{,}000$ if and only if $S(n) > 1{,}000{,}000 = 100^3\!.$ Because $S(n)$ is increasing for $n > 2$ , the values $S(100) = 1{,}000{,}000 - 10{,}000 + 200 = 990{,}200$ and $S(101)=1{,}030{,}301 - 10{,}201 + 202 = 1{,}020{,}302$ show that the requested value of $n$ is $\boxed{101}$ .

## Solution 2 (Same idea, easier to see)
Starting from $f_1(x)=|x-1|$ , we can track the solutions, the number of solutions, and their sum:
\[\begin{array}{c|c|c|c} n&Solutions&number&sum\\ 1&1&1&1\\ 2&1,3&2&4\\ 3&0,2,4,6&4&12\\ 4&-2,0,2...10&7&28\\ 5&-5,-3,-1...15&11&55\\ \end{array}\]
It is clear that the solutions form arithmetic sequences with a difference of 2, and the negative solutions cancel out all but $n$ of the $1+\frac{n(n-1)}{2}$ solutions. Thus, the sum of the solutions is $n \cdot [1+\frac{n(n-1)}{2}]$ , which is a cubic function. (Side Note: Gergor-Newton Interpolation Formula is applicable here)
$n \cdot [1+\frac{n(n-1)}{2}]>500,000$
Multiplying both sides by $2$ ,
$n \cdot [2+n(n-1)]>1,000,000$
1 million is $10^6=100^3$ , so the solution should be close to $100$ .
100 is slightly too small, so $\boxed{101}$ works.
~ dragnin

## Video Solution
https://youtu.be/g13o0wgj4p0
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
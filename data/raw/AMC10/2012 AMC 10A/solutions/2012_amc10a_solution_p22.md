# 2012 AMC 10A Problem 22

## Problem

The sum of the first $m$ positive odd integers is $212$ more than the sum of the first $n$ positive even integers. What is the sum of all possible values of $n$ ?

$\textbf{(A)}\ 255\qquad\textbf{(B)}\ 256\qquad\textbf{(C)}\ 257\qquad\textbf{(D)}\ 258\qquad\textbf{(E)}\ 259$

## Solution 1
The sum of the first $m$ odd integers is given by $m^2$ . The sum of the first $n$ even integers is given by $n(n+1)$ .
Thus, $m^2 = n^2 + n + 212$ . Since we want to solve for n, rearrange as a quadratic equation: $n^2 + n + (212 - m^2) = 0$ .
Use the quadratic formula: $n = \frac{-1 + \sqrt{1 - 4(212 - m^2)}}{2}$ . Since $n$ is clearly an integer, $1 - 4(212 - m^2) = 4m^2 - 847$ must be not only a perfect square, but also an odd perfect square for $n$ to be an integer.
Let $x = \sqrt{4m^2 - 847}$ ; note that this means $n = \frac{-1 + x}{2}$ . It can be rewritten as $x^2 = 4m^2 - 847$ , so $4m^2 - x^2 = 847$ . Factoring the left side by using the difference of squares, we get $(2m + x)(2m - x) = 847 = 7\cdot11^2$ .
Our goal is to find possible values for $x$ , then use the equation above to find $n$ . The difference between the factors is $(2m + x) - (2m - x) = 2m + x - 2m + x = 2x.$ We have three pairs of factors, $847\cdot1, 121\cdot 7,$ and $77\cdot 11$ . The differences between these factors are $846$ , $114$ , and $66$ - those are all possible values for $2x$ . Thus the possibilities for $x$ are $423$ , $57$ , and $33$ .
Now plug in these values into the equation $n = \frac{-1 + x}{2}$ , so $n$ can equal $211$ , $28$ , or $16$ , hence the answer is $\boxed{\textbf{(A)}\ 255}$ .
~Edits by BakedPotato66

## Solution 2
As above, start off by noting that the sum of the first $m$ odd integers $= m^2$ and the sum of the first $n$ even integers $= n(n+1)$ . Clearly $m > n$ , so let $m = n + a$ , where $a$ is some positive integer. We have:
$(n+a)^2 = n(n+1) + 212$ . Expanding, grouping like terms and factoring, we get: $n = \frac{(212 - a^2)}{(2a - 1)}$ .
We know that $n$ and $a$ are both positive integers, so we need only check values of $a$ from $1$ to $14$ ( $14^2 = 196 < 212 < 15^2 = 225$ ). Plugging in, the only values of $a$ that give integral solutions are $1, 4,$ and $6$ . These gives $n$ values of $211, 28,$ and $16$ , respectively. $211 + 28 + 16 = 255$ . Hence, the answer is $\boxed{\textbf{(A)}\ 255}$ .

## Solution 3
Using the closed forms for the sums, we get $m^2=n(n+1)+212$ , or $m^2=n^2+n+212$ . We would like to factor this equation, but the current expressions don't allow for this. So we multiply both sides by 4 to let us complete the square. Our equation is now $4m^2=4n^2+4n+848$ . Complete the square on the right hand side: $4m^2=(4n^2+4n+1)+848-1=(2n+1)^2+847$ . Move over the $(2n+1)^2$ and factor to get $(2m-2n-1)(2m+2n+1)=847=7\cdot11\cdot11$ . The second factor is clearly greater than the first, and the only possible factor pairs are $1$ and $847$ , $7$ and $121$ , $11$ and $77$ . In each of these cases, solve for $m$ and $n$ and we find the solutions $(m,n)=(212,211), (32,28), (22,16)$ . The sum of all possible values of $n$ is $211+28+16=\boxed{\textbf{(A)}\ 255}$ .

## Video Solution by Richard Rusczyk
https://artofproblemsolving.com/videos/amc/2012amc10a/252
~dolphin7
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
# 2015 AIME I Problem 14

## Problem

For each integer $n \ge 2$ , let $A(n)$ be the area of the region in the coordinate plane defined by the inequalities $1\le x \le n$ and $0\le y \le x \left\lfloor \sqrt x \right\rfloor$ , where $\left\lfloor \sqrt x \right\rfloor$ is the greatest integer not exceeding $\sqrt x$ . Find the number of values of $n$ with $2\le n \le 1000$ for which $A(n)$ is an integer.

## Solution 1
Let $n\ge 2$ and define $a(n) = \left\lfloor \sqrt n \right\rfloor$ . For $2\le n \le 1000$ , we have $1\le a(n)\le 31$ .
For $a^2 \le x < (a+1)^2$ we have $y=ax$ . Thus $A(n+1)-A(n)=a(n+\tfrac 12) = \Delta_n$ (say), and $\Delta_n$ is an integer if $a$ is even; otherwise $\Delta_n$ is an integer plus $\tfrac 12$ .
If $a=1$ , $n\in \{1,2,3\}$ and $\Delta_n$ is of the form $k(n)+\tfrac 12$ so $A(n)$ is an integer when $n$ is even.
If $a=2$ , $n\in\{4,\ldots , 8\}$ and $\Delta_n$ is an integer for all $n$ . Since $A(3)$ is not an integer, so $A(n)$ is not an integer for any $n$ .
If $a=3$ , $n\in\{9,\ldots , 15\}$ and $\Delta_n$ is of the form $k(n)+\tfrac 12$ . Since $A(8)$ is of the form $k+\tfrac 12$ so $A(n)$ is an integer only when $n$ is odd.
If $a=4$ , $n\in\{16,\ldots , 24\}$ and $\Delta_n$ is an integer for all $n$ . Since $A(15)$ is an integer so $A(n)$ is an integer for all $n$ .
Now we are back to where we started; i.e., the case $a=5$ will be the same as $a=1$ and so on. Thus, \begin{align} a(n)\equiv 1\pmod 4 \qquad &\Longrightarrow \qquad A(n) \in \mathbb{Z} \textrm{ for even } n, \\ a(n)\equiv 2\pmod 4 \qquad &\Longrightarrow \qquad A(n) \not\in \mathbb{Z} \textrm{ for any } n, \\ a(n)\equiv 3\pmod 4 \qquad &\Longrightarrow \qquad A(n) \in \mathbb{Z} \textrm{ for odd } n, \\ a(n)\equiv 0\pmod 4 \qquad &\Longrightarrow \qquad A(n) \in \mathbb{Z} \textrm{ for all } n. \end{align}
For each $a$ there are $2a+1$ corresponding values of $n$ : i.e., $n\in \{a^2, \ldots , (a+1)^2-1\}$ .
Thus, the number of values of $n$ corresponding to $(4)$ (i.e., $a(n)\equiv 0\pmod 4$ ) is given by \[\sum_{\substack{a=4k \\ a\le 31}}(2a+1) = \sum_{k=1}^7 (8k+1)=231.\]
The cases $(1)$ and $(3)$ combine to account for half the values of $n$ corresponding to odd values of $a(n)$ ; i.e., \[\frac 12 \cdot \sum_{\substack{a=2k+1 \\ a\le 31}} (2a+1) = \sum_{k=0}^{15} (2k+\tfrac 32) = 264\] However, this also includes the odd integers in $\{1001, \ldots , 1023\}$ . Subtracting $12$ to account for these, we get the number of values of $n$ corresponding to cases $(1)$ and $(3)$ to be $264-12=252$ .
Adding the contributions from all cases we get our answer to be $231+252= \boxed{483}$ .

## Solution 2
By considering the graph of this function, it is shown that the graph is composed of trapezoids ranging from $a^2$ to $(a+1)^2$ with the top made of diagonal line $y=ax$ . The width of each trapezoid is $3, 5, 7$ , etc. Whenever $a$ is odd, the value of $A(n)$ increases by an integer value, plus $\frac{1}{2}$ . Whenever $a$ is even, the value of $A(n)$ increases by an integer value. Since each trapezoid always has an odd width, every value of $n$ is not an integer when $a \pmod{4} \equiv 2$ , and is an integer when $a \pmod{4} \equiv 0$ . Every other value is an integer when $a$ is odd. Therefore, it is simply a matter of determining the number of values of $n$ where $a \pmod{4} \equiv 0$ ( $(5^2-4^2)+(9^2-8^2)+...+(29^2-28^2)$ ), and adding the number of values of $n$ where $a$ is odd ( $\frac{(2^2-1^2)+(4^2-3^2)+...+(30^2-29^2)+(1000-31^2)}{2}$ ). Adding the two values gives $231+252=\boxed{483}$ .

## "Step" Solution
First, draw a graph of the function. Note that it is just a bunch of line segments. Since we only need to know whether or not $A(n)$ is an integer, we can take the area of each piece from some $x$ to $x+1$ (mod 1), aka the piece from $2$ to $3$ has area $\frac{1}{2} (\mod 1)$ . There are some patterns. Every time we increase $n$ starting with $2$ , we either add $0 (\mod 1)$ or $\frac{1}{2} (\mod 1)$ . We look at $\lfloor \sqrt{x} \rfloor$ for inspiration. Every time this floor (which is really the slope) is odd, there is always an addition of $\frac{1}{2} (\mod 1)$ , and whenever that slope is even, that addition is zero.
Take a few cases. For slope $=1$ , we see that only one value satisfies. Because the last value, $n=4$ , fails, and the numbers $n$ which have a slope of an even number don't change this modulus, all these do not satisfy the criterion. The pattern then comes back to the odds, and this time $\lfloor \frac{7}{2} \rfloor + 1 = 4$ values work. Since the work/fail pattern alternates, all the $n$ s with even slope, $[17, 25]$ , satisfy the criterion. This pattern is cyclic over period 4 of slopes.
Even summation of working cases: $9+17+25+...+57 = 231$ . Odd summation: $1+4+5+8+9+12...+29$ and plus the $20$ cases from $n=[962, 1000]$ : $252$ . Answer is $\boxed{483}$ .

## Video Solution
https://youtu.be/tup11-90Bqw
~MathProblemSolvingSkills.com
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
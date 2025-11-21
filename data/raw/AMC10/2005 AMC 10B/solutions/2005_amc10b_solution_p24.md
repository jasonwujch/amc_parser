# 2005 AMC 10B Problem 24

## Problem

Let $x$ and $y$ be two-digit integers such that $y$ is obtained by reversing the digits of $x$ . The integers $x$ and $y$ satisfy $x^2 - y^2 = m^2$ for some positive integer $m$ . What is $x + y + m$ ?

$\textbf{(A) } 88 \qquad \textbf{(B) } 112 \qquad \textbf{(C) } 116 \qquad \textbf{(D) } 144 \qquad \textbf{(E) } 154$

## Solution 1
Let $x = 10a+b, y = 10b+a$ . The given conditions imply $x>y$ , which implies $a>b$ , and they also imply that both $a$ and $b$ are nonzero.
Then, $x^2 - y^2 = (x-y)(x+y) = (9a - 9b)(11a + 11b) = 99(a-b)(a+b) = m^2$ .
Since this must be a perfect square, all the exponents in its prime factorization must be even. $99$ factorizes into $3^2 \cdot 11$ , so $11|(a-b)(a+b)$ . However, the maximum value of $a-b$ is $9-1=8$ , so $11|a+b$ . The maximum value of $a+b$ is $9+8=17$ , so $a+b=11$ .
Then, we have $33^2(a-b) = m^2$ , so $a-b$ is a perfect square, but the only perfect squares that are within our bound on $a-b$ are $1$ and $4$ . We know $a+b=11$ , and, for $a-b=1$ , adding equations to eliminate $b$ gives us $2a=12 \Longrightarrow a=6, b=5$ . Testing $a-b=4$ gives us $2a=15 \Longrightarrow a=\frac{15}{2}, b=\frac{7}{2}$ , which is impossible, as $a$ and $b$ must be digits. Therefore, $(a,b) = (6,5)$ , and $x+y+m=\boxed{\textbf{(E) }154}$ .

## Solution 2
The first steps are the same as Solution 1. Let $x = 10a+b, y = 10b+a$ , where we know that a and b are digits (whole numbers less than $10$ ).
Like Solution 1, we end up getting $(9a - 9b)(11a + 11b) = 99(a-b)(a+b) = m^2$ . This is where the solution diverges.
We know that the left side of the equation is a perfect square because $m$ is an integer. If we factor $99$ into its prime factors, we get $3^2\cdot 11$ . In order to get a perfect square on the left side, $(a-b)(a+b)$ must make both prime exponents even. Because the a and b are digits, a simple guess would be that $(a+b)$ (the bigger number) equals $11$ while $(a-b)$ is a factor of nine (1 or 9). The correct guesses are $a = 6, b = 5$ causing $x = 65, y = 56,$ and $m = 33$ . The sum of the numbers is $\boxed{\textbf{(E) }154}$

## Solution 3
Once again, the solution is quite similar as the above solutions. Since $x$ and $y$ are two digit integers, we can write $x = 10a+b, y = 10b+a$ and because $x^2 - y^2 = (x-y)(x+y)$ , substituting and factoring, we get $99(a+b)(a-b) = m^2$ .
Therefore, $(a+b)(a-b) = \frac{m^2}{99}$ and $\frac{m^2}{99}$ must be an integer. A quick strategy is to find the smallest such integer $m$ such that $\frac{m^2}{99}$ is an integer. We notice that 99 has a prime factorization of $3^2 \cdot 11.$
Let $m^2 = n.$ Since we need a perfect square and 3 is already squared, we just need to square 11. So $3^2 \cdot 11^2$ gives us 1089 as $n$ and $m = \sqrt{1089} = 33.$ We now get the equation $(x-y)(x+y) = 33^2$ , which we can also write as $(x-y)(x+y) = 11^2 \cdot 3^2$ .
A very simple guess assumes that $x-y=3^2$ and $x+y=11^2$ since $x$ and $y$ are positive. Finally, we come to the conclusion that $x=65$ and $y=56$ , so $x+y+m$ $=$ $\boxed{\textbf{(E) }154}$ .
Note that all of the solutions used $a+b$ or $a-b$ as part of their solution.

## Solution 4
Continue the same as Solution $3$ until we get $33$ . Knowing that $33^2 = 1089$ , we have narrowed down our Pythagorean triples. We know that the $2$ other squares should be larger than $33^2$ , so we can start testing.
If we start testing the $40$ s, it is fruitless since the closest to $33^2$ would be $33 - 45 - 54$ which is not a Pythagorean triple. We can start by testing out the $50$ s, and it turns our that $33 - 56 - 65$ is a Pythagorean triple. Therefore, our answer is $33+56+65$ = $\boxed{\textbf{(E) }154}$ .
~Arcticturn

## Video Solution
https://www.youtube.com/watch?v=7Y7OX5uVPac ~David
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
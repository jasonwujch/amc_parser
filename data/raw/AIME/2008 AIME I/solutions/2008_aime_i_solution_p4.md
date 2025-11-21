# 2008 AIME I Problem 4

## Problem

There exist unique positive integers $x$ and $y$ that satisfy the equation $x^2 + 84x + 2008 = y^2$ . Find $x + y$ .

## Solution 1
Completing the square , $y^2 = x^2 + 84x + 2008 = (x+42)^2 + 244$ . Thus $244 = y^2 - (x+42)^2 = (y - x - 42)(y + x + 42)$ by difference of squares .
Since $244$ is even, one of the factors is even. A parity check shows that if one of them is even, then both must be even. Since $244 = 2^2 \cdot 61$ , the factors must be $2$ and $122$ . Since $x,y > 0$ , we have $y - x - 42 = 2$ and $y + x + 42 = 122$ ; the latter equation implies that $x + y = \boxed{080}$ .
Indeed, by solving, we find $(x,y) = (18,62)$ is the unique solution.

## Solution 2
We complete the square like in the first solution: $y^2 = (x+42)^2 + 244$ . Since consecutive squares differ by the consecutive odd numbers, we note that $y$ and $x+42$ must differ by an even number. We can use casework with the even numbers, starting with $y-(x+42)=2$ . \begin{align*}2(x+42)+1+2(x+42)+3&=244\\ \Leftrightarrow x&=18\end{align*}
Thus, $y=62$ and the answer is $\boxed{080}$ .

## Solution 3
We see that $y^2 \equiv x^2 + 4 \pmod{6}$ . By quadratic residues , we find that either $x \equiv 0, 3 \pmod{6}$ . Also, $y^2 \equiv (x+42)^2 + 244 \equiv (x+2)^2 \pmod{4}$ , so $x \equiv 0, 2 \mod{4}$ . Combining, we see that $x \equiv 0 \mod{6}$ .
Testing $x = 6$ and other multiples of $6$ , we quickly find that $x = 18, y = 62$ is the solution. $18+62=\boxed{080}$

## Solution 4
We solve for x: $x^2 + 84x + 2008-y^2 = 0$
$x=\dfrac{-84+\sqrt{84^2-4\cdot 2008+4y^2}}{2}=-42+\sqrt{y^2-244}$
So $y^2-244$ is a perfect square. Since 244 is even, the difference $\sqrt{y^2-244} -y^2$ is even, so we try $y^2-244=(y-2)^2$ : $-244=-4y+4$ , $y=62$ .
Plugging into our equation, we find that $x=18$ , and $(x,y)=(18,62)$ indeed satisfies the original equation. $x+y=\boxed{080}$

## Solution 5
Let $y=x+d$ for some $d>0$ , substitute into the original equation to get $84x + 2008 = 2xd + d^2$ .
All terms except for the last one are even, hence $d^2$ must be even, hence let $d=2e$ . We obtain $21x + 502 = xe + e^2$ . Rearrange to $502-e^2 = x(e-21)$ .
Obviously for $0<e<21$ the right hand side is negative and the left hand side is positive. Hence $e\geq 21$ . Let $e=21+f$ , then $f\geq 0$ .
We have $502 - (21+f)^2 = xf$ . Left hand side simplifies to $61 - 42f + f^2$ . As $x$ must be an integer, $f$ must divide the left hand side. But $61$ is a prime, which only leaves two options: $f=1$ and $f=61$ .
Option $f=61$ gives us a negative $x$ . Option $f=1$ gives us $x=61/f - 42 + f = 18$ , and $y = x + d= x + 2e = x + 2(21+f) = 18 + 44 = 62$ , hence $x+y=\boxed{080}$ .

## Solution 6
First complete the square to get $y^2 = (x+42)^2 + 244$ . Remember that squares are the sums of consecutive odd integers, so when the difference between the two squares is 244, the two squares must be an even number of odd integers apart. However, there is only one distinct solution, as the problem states, and very quickly you will realize that only two odd integers work. When there are four, then the numbers are not odd, and when it is any other even integer it does not divide. So we need two consecutive odd integers that sum to 244. Easily we find 121 and 123. 121 is the 61st odd integer and 123 is the 62nd odd integer, so $(x+42)^2$ is the sum of the first 60 odd integers, or $(60)^2$ , while $y^2$ is $62^2$ for the same reasons. That way we get $x=12$ , $y=62$ , hence $x+y=\boxed{080}$ .
-jackshi2006

## Video Solution by OmegaLearn
https://youtu.be/euz1azVKUYs?t=424
~ pi_is_3.14
These problems are copyrighted © by the Mathematical Association of America.
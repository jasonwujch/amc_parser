# 2005 AIME I Problem 6

## Problem

Let $P$ be the product of the nonreal roots of $x^4-4x^3+6x^2-4x=2005.$ Find $\lfloor P\rfloor.$

## Solution 1
The left-hand side of that equation is nearly equal to $(x - 1)^4$ . Thus, we add 1 to each side in order to complete the fourth power and get $(x - 1)^4 = 2006$ .
Let $r = \sqrt[4]{2006}$ be the positive real fourth root of 2006. Then the roots of the above equation are $x = 1 + i^n r$ for $n = 0, 1, 2, 3$ . The two non-real members of this set are $1 + ir$ and $1 - ir$ . Their product is $P = 1 + r^2 = 1 + \sqrt{2006}$ . $44^2 = 1936 < 2006 < 2025 = 45^2$ so $\lfloor P \rfloor = 1 + 44 = \boxed{045}$ .

## Solution 2
Starting like before, $(x-1)^4= 2006$ This time we apply differences of squares. $(x-1)^4-2006=0$ so $((x-1)^2+\sqrt{2006})((x-1)^2 -\sqrt{2006})=0$ If you think of each part of the product as a quadratic, then $((x-1)^2+\sqrt{2006})$ is bound to hold the two non-real roots since the other definitely crosses the x-axis twice since it is just $x^2$ translated down and right. Therefore $P$ is the product of the roots of $((x-1)^2+\sqrt{2006})$ or $P=1+\sqrt{2006}$ so
$\lfloor P \rfloor = 1 + 44 = \boxed{045}$ .

## Solution 3
If we don't see the fourth power, we can always factor the LHS to try to create a quadratic substitution. Checking, we find that $x=0$ and $x=2$ are both roots. Synthetic division gives $(x^2-2x)(x^2-2x+2)=2005$ . We now have our quadratic substitution of $y=x^2-2x+1=(x-1)^2$ , giving us $(y-1)(y+1)=2005$ . From here we proceed as in Solution 1 to get $\boxed{045}$ .

## Solution 4
Realizing that if we add 1 to both sides we get $x^4-4x^3+6x^2-4x+1=2006$ which can be factored as $(x-1)^4=2006$ . Then we can substitute $(x-1)$ with $y$ which leaves us with $y^4=2006$ . Now subtracting 2006 from both sides we get some difference of squares $y^4-2006=0 \rightarrow (y-\sqrt[4]{2006})(y+\sqrt[4]{2006})(y^2+\sqrt{2006})=0$ . The question asks for the product of the complex roots so we only care about the last factor which is equal to zero. From there we can solve $y^2+\sqrt{2006}=0$ , we can substitute $(x-1)$ for $y$ giving us $(x-1)^2+\sqrt{2006}=0$ , expanding this we get $x^2-2x+1+\sqrt{2006}=0$ . We know that the product of a quadratics roots is $\frac{c}{a}$ which leaves us with $\frac{1+\sqrt{2006}}{1}=1+\sqrt{2006}\approx\boxed{045}$ .

## Solution 5
As in solution 1, we find that $(x-1)^4 = 2006$ . Now $x-1=\pm \sqrt[4]{2006}$ so $x_1 = 1+\sqrt[4]{2006}$ and $x_2 = 1-\sqrt[4]{2006}$ are the real roots of the equation. Multiplying, we get $x_1 x_2 = 1 - \sqrt{2006}$ . Now transforming the original function and using Vieta's formula, $x^4-4x^3+6x^2-4x-2005=0$ so $x_1 x_2 x_3 x_4 = \frac{-2005}{1} = -2005$ . We find that the product of the nonreal roots is $x_3 x_4 = \frac{-2005}{1-\sqrt{2006}} \approx 45.8$ and we get $\boxed{045}$ .
Note: $\frac{2005}{\sqrt[4]{2006}-1}=\frac{2005(1+\sqrt[4]{2006})}{2005} = 1+\sqrt[4]{2006}.$

## Solution 6 (De Moivre's Theorem)
As all the other solutions, we find that $(x-1)^4 = 2006$ . Thus $x=\sqrt[4]{2006}+1$ . Thus $x= \sqrt[4]{2006}(\cos(\frac{2\pi(k)}{4}+i\sin(\frac{2\pi(k)}{4}))+1$ when $k=0,1,2,3$ . The complex values of $x$ are the ones where $i\sin(\frac{2\pi(k)}{4})$ does not equal 0. These complex roots are $1+\sqrt[4]{2006}(i)$ and $1-\sqrt[4]{2006}(i)$ . The product of these two nonreal roots is ( $1+\sqrt[4]{2006}(i)$ )( $1-\sqrt[4]{2006}(i)$ ) which is equal to $1+\sqrt {2006}$ . The floor of that value is $\boxed{045}$ .
Video Solution https://www.youtube.com/watch?v=LbHg1Su2Rmg
These problems are copyrighted © by the Mathematical Association of America.
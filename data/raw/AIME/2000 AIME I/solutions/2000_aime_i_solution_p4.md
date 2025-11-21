# 2000 AIME I Problem 4

## Problem

The diagram shows a rectangle that has been dissected into nine non-overlapping squares . Given that the width and the height of the rectangle are relatively prime positive integers, find the perimeter of the rectangle.

[asy]draw((0,0)--(69,0)--(69,61)--(0,61)--(0,0));draw((36,0)--(36,36)--(0,36)); draw((36,33)--(69,33));draw((41,33)--(41,61));draw((25,36)--(25,61)); draw((34,36)--(34,45)--(25,45)); draw((36,36)--(36,38)--(34,38)); draw((36,38)--(41,38)); draw((34,45)--(41,45));[/asy]

## Solution 1
Call the squares' side lengths from smallest to largest $a_1,\ldots,a_9$ , and let $l,w$ represent the dimensions of the rectangle.
The picture shows that \begin{align*} a_1+a_2 &= a_3\\ a_1 + a_3 &= a_4\\ a_3 + a_4 &= a_5\\ a_4 + a_5 &= a_6\\ a_2 + a_3 + a_5 &= a_7\\ a_2 + a_7 &= a_8\\ a_1 + a_4 + a_6 &= a_9\\ a_6 + a_9 &= a_7 + a_8.\end{align*}
Expressing all terms 3 to 9 in terms of $a_1$ and $a_2$ and substituting their expanded forms into the previous equation will give the expression $5a_1 = 2a_2$ .
We can guess that $a_1 = 2$ . (If we started with $a_1$ odd, the resulting sides would not be integers and we would need to scale up by a factor of $2$ to make them integers; if we started with $a_1 > 2$ even, the resulting dimensions would not be relatively prime and we would need to scale down.) Then solving gives $a_9 = 36$ , $a_6=25$ , $a_8 = 33$ , which gives us $l=61,w=69$ . These numbers are relatively prime, as desired. The perimeter is $2(61)+2(69)=\boxed{260}$ .

## Solution 1.2 (more detail)
We can just list the equations: \begin{align*} s_3 &= s_1 + s_2 \\ s_4 &= s_3 + s_1 \\ s_5 &= s_4 + s_3 \\ s_6 &= s_5 + s_4 \\ s_7 &= s_5 + s_3 + s_2 \\ s_8 &= s_7 + s_2 \\ s_9 &= s_8 + s_2 - s_1 \\ s_9 + s_8 &= s_7 + s_6 + s_5 \end{align*} We can then write each $s_i$ in terms of $s_1$ and $s_2$ as follows \begin{align*} s_4 &= 2s_1 + s_2 \\ s_5 &= 3s_1 +2s_2 \\ s_6 &= 5s_1 + 3s_2 \\ s_7 &= 4s_1 + 4s_2 \\ s_8 &= 4s_1 + 5s_2 \\ s_9 &= 3s_1 + 6s_2 \\ \end{align*} Since $s_9 + s_8 = s_7 + s_6 + s_5 \implies (3s_1 + 6s_2) + (4s_1 + 5s_2) = (4s_1 + 4s_2) + (5s_1 + 3s_2) + (3s_1 + 2s_2),$ \[2s_2 = 5s_1 \implies \frac{2}{5}s_2 = s_1.\] Since the side lengths of the rectangle are relatively prime, we can see that $s_1 = 2$ and $s_2 = 5.$ Therefore, $2(2s_9 + s_6 + s_8) = 30s_1 + 40s_2 = \boxed{260}.$ ~peelybonehead

## Solution 2 Length-chasing (Angle-chasing but for side lengths)
We set the side length of the smallest square to 1, and set the side length of square $a_4$ in the previous question to a. We do some "side length chasing" and get $4a - 4 = 2a + 5$ . Solving, we get $a = 4.5$ and the side lengths are $61$ and $69$ . Thus, the perimeter of the rectangle is $2(61 + 69) = \boxed{260}.$
These problems are copyrighted © by the Mathematical Association of America.
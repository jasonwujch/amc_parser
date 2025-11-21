# 2023 AMC 10A Problem 4

## Problem

A quadrilateral has all integer sides lengths, a perimeter of $26$ , and one side of length $4$ . What is the greatest possible length of one side of this quadrilateral?

$\textbf{(A) }9\qquad\textbf{(B) }10\qquad\textbf{(C) }11\qquad\textbf{(D) }12\qquad\textbf{(E) }13$

## Solution 1
Let's use the triangle inequality. We know that for a triangle, the sum of the 2 shorter sides must always be longer than the longest side. This is because if the longest side were to be as long as the sum of the other sides, or longer, we would only have a line.
Similarly, for a convex quadrilateral, the sum of the shortest 3 sides must always be longer than the longest side. Thus, the answer is $\frac{26}{2}-1=13-1=\boxed {\textbf{(D) 12}}$
~zhenghua
Sidenote: If there weren't a restriction on integer side lengths, the answer would be the decimal just less than 13, so the sum of the other 3 sides could be just more than 13. That would make the longest side 12.99999..., stopping at who knows how many 9's.
~sidenote by mihikamishra

## Solution 2
Say the chosen side is $a$ and the other sides are $b,c,d$ .
By the Generalised Polygon Inequality, $a<b+c+d$ . We also have $a+b+c+d=26\Rightarrow b+c+d=26-a$ .
Combining these two, we get $a<26-a\Rightarrow a<13$ .
The largest length that satisfies this is $a=\boxed {\textbf{(D) 12}}$
~not_slay
~slight edits by e___

## Solution 3
This is an AMC 10 problem 4, so there is no need for any complex formulas. The largest singular side length from a quadrilateral comes from a trapezoid. So we can set the $2$ sides of the trapezoid equal to $4$ . Next we can split the trapezoid into $5$ triangles, where each base length of the triangle equals $4$ . So the top side equals $8$ , and the bottom side length equals $4+4+4$ $=$ $\boxed {\textbf{(D) 12}}$ ~ kabbybear
[asy] size(120); draw((0,0)--(2,6),red); draw((2,6)--(5,6),red); draw((5,6)--(7,0),red); draw((0,0)--(7,0),red); draw((2,6)--(2.67,0),red); draw((2.67,0)--(3.5,6),red); draw((3.5,6)--(4.67,0),red); draw((4.67,0)--(5,6),red); [/asy]

## Video Solution by Little Fermat
https://youtu.be/h2Pf2hvF1wE?si=3Dc3LOUcyY0QLrPs&t=507 ~little-fermat

## Video Solution by Math-X (First understand the problem!!!)
https://youtu.be/GP-DYudh5qU?si=ZOEgPD6mg6z9b02s&t=677

## Video Solution by CosineMethod [🔥Fast and Easy🔥]
https://www.youtube.com/watch?v=UDhZqXI2A6Y

## Video Solution
https://youtu.be/HCUAbodk_NA
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=Iu0AJ2rof7k

## Video Solution (easy to digest) by Power Solve
https://youtu.be/Od1Spf3TDBs

## Video Solution (Fast and Easy) by Dr.Google (YT: Pablo's Math)
https://youtu.be/S3LquYpHrsY
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
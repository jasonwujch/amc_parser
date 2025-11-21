# 2012 AIME II Problem 2

## Problem

Two geometric sequences $a_1, a_2, a_3, \ldots$ and $b_1, b_2, b_3, \ldots$ have the same common ratio, with $a_1 = 27$ , $b_1=99$ , and $a_{15}=b_{11}$ . Find $a_9$ .

## Solution 1
Call the common ratio $r.$ Now since the $n$ th term of a geometric sequence with first term $x$ and common ratio $y$ is $xy^{n-1},$ we see that $a_1 \cdot r^{14} = b_1 \cdot r^{10} \implies r^4 = \frac{99}{27} = \frac{11}{3}.$ But $a_9$ equals $a_1 \cdot r^8 = a_1 \cdot (r^4)^2=27\cdot {\left(\frac{11}{3}\right)}^2=27\cdot \frac{121} 9=\boxed{363}$ .

## Solution 2
Let the ratio be \( r \). From \( \frac{a_{15}}{b_{11}} = \frac{a_{15}}{b_{11}} \):
\( a_1 r^{14} = b_1 r^{10} \implies a_1 r^4 = b_1 \).
Notice how \( a_5 = a_1 r^4 = b_1 \).
Then
\( a_9 = a_5 r^4 = b_1 r^4 = \frac{b_1^2}{a_1} \).
Plug in \( a_1 = 27, b_1 = 99 \):
\( a_9 = \frac{99^2}{27} = 363 \).
$\boxed{363}$
~Pinotation

## Video Solution
https://youtu.be/V2X9hz6DuUw
~Lucas
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
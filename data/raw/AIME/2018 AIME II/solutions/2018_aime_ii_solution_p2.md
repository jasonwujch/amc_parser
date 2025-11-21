# 2018 AIME II Problem 2

## Problem

Let $a_{0} = 2$ , $a_{1} = 5$ , and $a_{2} = 8$ , and for $n > 2$ define $a_{n}$ recursively to be the remainder when $4$ ( $a_{n-1}$ $+$ $a_{n-2}$ $+$ $a_{n-3}$ ) is divided by $11$ . Find $a_{2018} \cdot a_{2020} \cdot a_{2022}$ .

## Solution 1
When given a sequence problem, one good thing to do is to check if the sequence repeats itself or if there is a pattern.
After computing more values of the sequence, it can be observed that the sequence repeats itself every 10 terms starting at $a_{0}$ .
$a_{0} = 2$ , $a_{1} = 5$ , $a_{2} = 8$ , $a_{3} = 5$ , $a_{4} = 6$ , $a_{5} = 10$ , $a_{6} = 7$ , $a_{7} = 4$ , $a_{8} = 7$ , $a_{9} = 6$ , $a_{10} = 2$ , $a_{11} = 5$ , $a_{12} = 8$ , $a_{13} = 5$
We can simplify the expression we need to solve to $a_{8}\cdot a_{10} \cdot a_{2}$ .
Our answer is $7 \cdot 2 \cdot 8$ $= \boxed{112}$ .

## Solution 2 (Overkill)
Notice that the characteristic polynomial of this is $x^3-4x^2-4x-4\equiv 0\pmod{11}$
Then since $x\equiv1$ is a root, using Vieta's formula, the other two roots $r,s$ satisfy $r+s\equiv3$ and $rs\equiv4$ .
Let $r=7+d$ and $s=7-d$ .
We have $49-d^2\equiv4$ so $d\equiv1$ . We found that the three roots of the characteristic polynomial are $1,6,8$ .
Now we want to express $a_n$ in an explicit form as $a(1^n)+b(6^n)+c(8^n)\pmod{11}$ .
Plugging in $n=0,1,2$ we get
$(*)$ $a+b+c\equiv2,$
$(**)$ $a+6b+8c\equiv5,$
$(***)$ $a+3b+9c\equiv8$
$\frac{(***)-(*)}{2}$ $\implies b+4c\equiv3$ and $(***)-(**)$ $\implies -3b+c\equiv3$
so $a\equiv6,$ $b\equiv1,$ and $c\equiv6$
Hence, $a_n\equiv 6+(6^n)+6(8^n)\equiv(2)^{-n\pmod{10}}+(2)^{3n-1\pmod{10}}-5\pmod{11}$
Therefore
$a_{2018}\equiv4+8-5=7$
$a_{2020}\equiv1+6-5=2$
$a_{2022}\equiv3+10-5=8$
And the answer is $7\times2\times8=\boxed{112}$
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
# 2004 AIME II Problem 9

## Problem

A sequence of positive integers with $a_1=1$ and $a_9+a_{10}=646$ is formed so that the first three terms are in geometric progression , the second, third, and fourth terms are in arithmetic progression , and, in general, for all $n\ge1,$ the terms $a_{2n-1}, a_{2n}, a_{2n+1}$ are in geometric progression, and the terms $a_{2n}, a_{2n+1},$ and $a_{2n+2}$ are in arithmetic progression. Let $a_n$ be the greatest term in this sequence that is less than $1000$ . Find $n+a_n.$

## Solution 1
Let $x = a_2$ ; then solving for the next several terms, we find that $a_3 = x^2,\ a_4 = x(2x-1),\ a_5$ $= (2x-1)^2,\ a_6$ $= (2x-1)(3x-2)$ , and in general, $a_{2n} = f(n-1)f(n)$ , $a_{2n+1} = f(n)^2$ , where $f(n) = nx - (n-1)$ . [1]
From \[a_9 + a_{10} = f(4)^2 + f(4)f(5) = (4x-3)(9x-7) = 646 = 2\cdot 17 \cdot 19\] , we find that by either the quadratic formula or trial-and-error/modular arithmetic that $x=5$ . Thus $f(n) = 4n+1$ , and we need to find the largest $n$ such that either $f(n)^2\, \mathrm{or}\, f(n)f(n-1) < 1000$ . This happens with $f(7)f(8) = 29 \cdot 33 = 957$ , and this is the $2(8) = 16$ th term of the sequence.
The answer is $957 + 16 = \boxed{973}$ .
^ We can show this by simultaneous induction : since \begin{align*}a_{2n} &= 2a_{2n-1} - a_{2n-2} = 2a_{2(n-1)+1} - a_{2(n-1)} \\ &= 2f(n-1)^2 - f(n-2)f(n-1) \\ &= f(n-1)[2f(n-1) - f(n-2)] \\ &= f(n-1)[(2n-2-n+2)x-(2n-4-n+3)] \\ &= f(n-1)f(n) \end{align*} and \begin{align*}a_{2n+1} &= \frac{a_{2n}^2}{a_{2n-1}} = \frac{f(n-1)^2f(n)^2}{f(n-1)^2} = f(n)^2 \\ \end{align*}

## Solution 2
Let $x = a_2$ . It is apparent that the sequence grows relatively fast, so we start trying positive integers to see what $x$ can be. Finding that $x = 5$ works, after bashing out the rest of the terms we find that $a_{16} = 957$ and $a_{17} = 1089$ , hence our answer is $957 + 16 = \boxed{973}$ .

## Solution 3
We can find the value of $a_{9}$ by its bounds using three conditions:
1. $0<a_{8} = 2a_{9}-a_{10}$
1. $a_{10} < a_{11}$ (note that the sequence must be increasing on all terms, not monotonically increasing) $a_{10} < \frac{a_{10}^2}{a_{9}} \rightarrow a_{9} < a_{10}$
1. $a_{11} = \frac{a_{10}^2}{a_{9}} = \frac{(646-a_{9})^2}{a_{9}}$ , so necessarily $a_{9}$ is a factor of $646^2$ , which factorizes to $2^2\cdot 17^2 \cdot 19^2$
Rearranging conditions 1 and 2, we get:
\[\frac{646}{3} < a_{9} < \frac{646}{2}\]
trying all the terms from the third condition, it is clear that $a_9 = 289$ is the only solution. Then we can calculate the next few terms from there since we have $a_{10}$ as well, to find that $a_{16} = 957$ and $a_{17} = 1089$ , thus we have our answer of $957 + 16 = \boxed{973}$ .
~KafkaTamura

## Solution 4 (quadratic)
Let $a_2 = x$ . We will write the first 10 terms in terms of $x$ (this will require some rigorous polynomial division):
The problem tells us that $a_9 + a_{10} = 646,$ so we can write a quadratic and solve for $x$ :
\[(16x^2 - 24x + 9) + (20x^2 - 31x + 12) = 646\] \[36x^2 - 55x + 21 = 646\] \[36x^2 - 55x - 625 = 0.\] \[x = \frac {-(-55) \pm \sqrt{(-55)^2 - 4(36)(-625)}}{2(36)}\] \[x = \frac {55 \pm \sqrt{3025 + 90000}}{72}\] \[x = \frac {55 \pm \sqrt{93025}}{72}\] $x = \frac {55 \pm 305}{72} = \xcancel{-\frac{125}{36}}, 5.$
Since every number in the series has to be a positive integer, $x$ must be $5$ . Using $x=5$ we can find $a_9$ and $a_{10}$ : \[a_9 = 16(5)^2 - 24(5) + 9 = 16(25) - 120 + 9 = 400 - 120 + 9 = 289.\] \[a_{10} = 20(5)^2 - 31(5) + 12 = 20(25) - 155 + 12 = 500 - 155 + 12 = 357.\]
Notice that our arithmetic differences are increasing by 16: $20 \rightarrow 36 \rightarrow 52 \rightarrow 68...$ So following this pattern, the next differences will be $84, 100, 116$ .
The geometric ratios follow a pattern of adding $4$ to the numerator and denominator: $\frac{9}{5} \rightarrow \frac{13}{9} \rightarrow \frac{17}{13}$ . The next ratios will be $\frac{21}{17}, \frac{25}{21}, \frac{29}{25}.$
We have everything we need to calculate the next few terms:
$a_{11} = 357 \cdot \frac{21}{17} = 441,$ $a_{12} = 441 + 84 = 525,$ $a_{13} = 525 \cdot \frac{25}{21} = 625,$ $a_{14} = 625 + 100 = 725,$ $a_{15} = 725 \cdot \frac{29}{25} = 841,$ $a_{16} = 841 + 116 = 957.$ We stop here because it's clear the next term will exceed 1000. Since $a_{16} = 957,$ the answer is $957 + 16 = \boxed{973}.$
~ grogg007
### See Also
These problems are copyrighted © by the Mathematical Association of America.
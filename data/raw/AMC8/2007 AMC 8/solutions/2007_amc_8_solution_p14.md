# 2007 AMC 8 Problem 14

## Problem

The base of isosceles $\triangle ABC$ is $24$ and its area is $60$ . What is the length of one of the congruent sides?

$\mathrm{(A)}\ 5 \qquad \mathrm{(B)}\ 8 \qquad \mathrm{(C)}\ 13 \qquad \mathrm{(D)}\ 14 \qquad \mathrm{(E)}\ 18$

## Solution 1
The area of a triangle is shown by $\frac{1}{2}bh$ . We set the base equal to $24$ , and the area equal to $60$ , and we get the triangle's height, or altitude, to be $5$ . In this isosceles triangle, the height bisects the base, so by using the Pythagorean Theorem, $a^2+b^2=c^2$ , we can solve for one of the legs of the triangle (it will be the hypotenuse, $c$ ). $a = 12$ , $b = 5$ , $c = 13$ . The answer is $\boxed{\textbf{(C)}\ 13}$ .

## Solution 2 (Heron's Formula)
According to Heron's Formula , setting side $a$ as $24$ , we have \[\sqrt{s(s-24)(s-b)(s-c)}=60\] where $s$ is the triangle's semiperimeter (i.e. $\frac{a+b+c}{2}$ ). Since the triangle is isosceles, $b=c$ , so we can rewrite $s$ as $\frac{24+2b}{2}=12+b$ . Substituting and solving the equation and taking the positive solution for $b$ , \[\sqrt{(12+b)(-12+b)(12)(12)}=60\] \[\sqrt{144(144-b^2)}=60\] \[144(144-b^2)=3600\] \[-b^2=-169\] \[b=\boxed{\textbf{(C)}\ 13}\]
~megaboy6679

## Video Solution by WhyMath
https://youtu.be/9sVdsKcpJ9U
~savannahsolver

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=omFpSGMWhFc

## Video Solution by AliceWang
https://youtu.be/U8v4XVPXr18
### See Also
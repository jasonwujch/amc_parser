# 1999 AMC 8 Problem 25

## Problem

Points $B$ , $D$ , and $J$ are midpoints of the sides of right triangle $ACG$ . Points $K$ , $E$ , $I$ are midpoints of the sides of triangle $JDG$ , etc. If the dividing and shading process is done 100 times (the first three are shown) and $AC=CG=6$ , then the total area of the shaded triangles is nearest

[asy] draw((0,0)--(6,0)--(6,6)--cycle); draw((3,0)--(3,3)--(6,3)); draw((4.5,3)--(4.5,4.5)--(6,4.5)); draw((5.25,4.5)--(5.25,5.25)--(6,5.25)); fill((3,0)--(6,0)--(6,3)--cycle,black); fill((4.5,3)--(6,3)--(6,4.5)--cycle,black); fill((5.25,4.5)--(6,4.5)--(6,5.25)--cycle,black); label("$A$",(0,0),SW); label("$B$",(3,0),S); label("$C$",(6,0),SE); label("$D$",(6,3),E); label("$E$",(6,4.5),E); label("$F$",(6,5.25),E); label("$G$",(6,6),NE); label("$H$",(5.25,5.25),NW); label("$I$",(4.5,4.5),NW); label("$J$",(3,3),NW); label("$K$",(4.5,3),S); label("$L$",(5.25,4.5),S); [/asy]

$\text{(A)}\ 6 \qquad \text{(B)}\ 7 \qquad \text{(C)}\ 8 \qquad \text{(D)}\ 9 \qquad \text{(E)}\ 10$

## Solution 1
Since $\triangle FGH$ is fairly small relative to the rest of the diagram, we can make an underestimate by using the current diagram. All triangles are right-isosceles triangles.
\[CD = \frac {CG}{2} = 3, DE = \frac{CD}{2} = \frac{3}{2}, EF = \frac{DE}{2} = \frac{3}{4}\] \[CB = CD = 3, DK = DE = \frac{3}{2}, EL = EF = \frac{3}{4}\] \[[CBD] = \frac{1}{2}3^2 = \frac{9}{2}\] \[[DKE] = \frac{1}{2}(\frac{3}{2})^2 = \frac{9}{8}\] \[[ELF] = \frac{1}{2}(\frac{3}{4})^2 = \frac{9}{32}\]
The sum of the shaded regions is $\frac{9}{2} + \frac{9}{8} + \frac{9}{32} = \frac{189}{32} \approx 5.9$
$5.9$ is an underestimate, as some portion (but not all) of $\triangle FGH$ will be shaded in future iterations.
If you shade all of $\triangle FGH$ , this will add an additional $\frac{9}{32}$ to the area, giving $\frac{198}{32} \approx 6.2$ , which is an overestimate.
Thus, $\boxed{\text{(A)}\ 6}$ is the only answer that is both over the underestimate and under the overestimate.

## Solution 2
In iteration $1$ , congruent triangles $\triangle ABJ, \triangle BDJ,$ and $\triangle BDC$ are created, with one of them being shaded.
In iteration $2$ , three more congruent triangles are created, with one of them being shaded.
As the process continues indefinitely, in each row, $\frac{1}{3}$ of each triplet of new congruent triangles will be shaded. The "fourth triangle" at the top ( $\triangle FGH$ in the diagram) will gradually shrink,
leaving about $\frac{1}{3}$ of the area shaded. This means $\frac{1}{3}\left(\frac{1}{2}6\cdot 6\right) = 6$ square units will be shaded when the process goes on indefinitely, giving $\boxed{A}$ .

## Solution 3
Using Solution 1 as a template, note that the sum of the areas forms a geometric series :
$\frac{9}{2} + \frac{9}{8} + \frac{9}{32} + \frac{9}{128} + ...$
This is the sum of a geometric series with first term $a_1 = \frac{9}{2}$ and common ratio $r = \frac{1}{4}$ This is the easiest way to do this problem.
The sum of an infinite geometric series with $|r|<1$ is shown by the formula. $S_{\infty} = \frac{a_1}{1 - r}$ Insert the values to get $\frac{\frac{9}{2}}{1 - \frac{1}{4}} = \frac{9}{2}\cdot\frac{4}{3} = 6$ , giving an answer of $\boxed{A}$ .

## Solution 4
Find the area of the bottom triangle, which is 4.5. Notice that the area of the triangles is divided by 4 every time. 4.5*5/4≈5.7, and 5.7+(1/4)≈5.9. We can clearly see that the sum is approaching answer choice $\boxed{A}$ .

## Solution 5
The area of $DBC$ is clearly $\frac{1}{3}$ of $AJDC$ , the area of $DEK$ is $\frac{1}{3}$ of $JIED$ , if the progress is going to infinity, the shaded triangles will be $\frac{1}{3}$ of the triangle $ACG$ . However, 100 times is much enough. The answer is $\frac{1}{3}\times 6\times 6\times \frac{1}{2} = \boxed{(A)6}$ .

## Solution 6
Because all of the triangles are isosceles, this gives us the area of one triangle with side length $s$ , $A = \frac{1}{2}s^2$ . Logically, $s$ keeps on getting $\frac{1}{2}$ as small as the previous one ( $3, \frac{3}{2}, \frac{3}{4}$ , etc) Meaning for triangle number $n, s = 3(\frac{1}{2})^n$ . Putting this into our original equation, $A = \frac{1}{2}(3(\frac{1}{2})^n)^2 = \frac{9}{2}(\frac{1}{2})^{2n} = 9(\frac{1}{2})^{2n+1}$ This means the total area is $9\sum^{\infty}_{n=1} \frac{1}{2}^{2n+1}$ , using exponent laws, we can simplify this to $\frac{9}{2} \sum^{\infty}_{n=1} \frac{1}{4}^n$ .
The formula for a geometric series like this is $\sum^{\infty}_{n=1} a*r^n = \frac{a}{1-r}$ . Using this, we get $\frac{\frac{9}{2}}{\frac{4}{4}-\frac{1}{4}} = \frac{9}{2}\times\frac{4}{3} = 3\times2 = \boxed{(A)6}$ .
~RandomMathGuy500

## Solution 7
Notice how you can fit $\triangle KDE$ into the top right corner of square $BCDJ$ ? Repeat this process by putting smaller triangles into the corner of the square and eventually, you should see that this converges to just $\frac{1}{4}$ of the square. $\triangle BCD$ is $\frac{1}{2}$ of the square and rest of the triangles make $\frac{1}{4}$ which totals to $\frac{3}{4}$ of the square. Square $BCDJ$ has side length $3$ so it's area is $9$ , and $\frac{3}{4}$ of $9$ is $\boxed{(A)6}$ .
~RandomMathGuy500

## Solution 8
As in Solution 3, the area form the geometric series $\frac{9}{2} + \frac{9}{8} + \frac{9}{32} + \frac{9}{128} + ...$ . If this is $x$ , than 4 $x$ is 18 + $\frac{9}{2} + \frac{9}{8} + \frac{9}{32} + \frac{9}{128} + ...$ .Than we take away $x$ to get 3 $x$ = 18. When we solve for $x$ we get $x$ = 6, so the correct answer is $\boxed{A}$ .

## Video Solution 1 by CosineMethod
https://www.youtube.com/watch?v=sZabsoMIf2I
### See Also
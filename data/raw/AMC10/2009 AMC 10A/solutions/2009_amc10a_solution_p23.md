# 2009 AMC 10A Problem 23

## Problem

Convex quadrilateral $ABCD$ has $AB = 9$ and $CD = 12$ . Diagonals $AC$ and $BD$ intersect at $E$ , $AC = 14$ , and $\triangle AED$ and $\triangle BEC$ have equal areas. What is $AE$ ?

$\textbf{(A)}\ \frac {9}{2}\qquad \textbf{(B)}\ \frac {50}{11}\qquad \textbf{(C)}\ \frac {21}{4}\qquad \textbf{(D)}\ \frac {17}{3}\qquad \textbf{(E)}\ 6$

## Solution 1
Let $[ABC]$ denote the area of triangle $ABC$ . $[AED] = [BEC]$ , so $[ABD] = [AED] + [AEB] = [BEC] + [AEB] = [ABC]$ . Since triangles $ABD$ and $ABC$ share a base, they also have the same height and thus $\overline{AB}||\overline{CD}$ and $\triangle{AEB}\sim\triangle{CED}$ with a ratio of $3: 4$ . $AE = \frac {3}{7}\times AC$ , so $AE = \frac {3}{7}\times 14 = 6\ \boxed{\textbf{(E)}}$ .

## Solution 2 (Trigonometry)
Using the sine area formula AREA= absinc/2 on triangles $AED$ and $BEC$ , as $\angle AED = \angle BEC$ , we see that
Since $\angle AEB = \angle DEC$ , triangles $AEB$ and $DEC$ are similar. Their ratio is $\frac {AB}{CD} = \frac {3}{4}$ . Since $AE + EC = 14$ , we must have $EC = 8$ , so $AE = 6\ \textbf{(E)}$ .

## Solution 3 (Fakesolve)
The easiest way for the areas of the triangles to be equal would be if they were congruent [1] . A way for that to work would be if $ABCD$ were simply an isosceles trapezoid! Since $AC = 14$ and $AE:EC = 3:4$ (look at the side lengths and you'll know why!), $\boxed{AE = 6}$

## Solution 4 (Easiest Way)
Using the fact that $[AED] = [BEC]$ and the fact that $\triangle AEB \sim \triangle EDC$ (which should be trivial given the two equal triangles) we have that
\[\frac{AE}{DC} = \frac{BE}{EC} = \frac{9}{12}\]
We know that $DC=EC,$ so we have
\[\frac{AE}{EC} = \frac{BE}{EC} = \frac{3}{4}\]
Thus
\[\frac{AE}{EC} = \frac{3}{4}\]
But $EC = 14 - AE$ so we have
\[\frac{AE}{14 - AE} = \frac{3}{4}\]
Simplifying gives $AE = \boxed{6}.$
~mathboy282
### Note
The two triangles that are equal in area imply that $AB$ is parallel to $DC$ which implies that $\angle{EAB} = \angle{CDE}$ and $\angle{EBA} = \angle{DCE}.$ Furthermore, since $\angle{AEB} = \angle{DEC}$ (vertical angles). By AAA similarity, $\triangle AEB \sim \triangle EDC.$
~mathboy282
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
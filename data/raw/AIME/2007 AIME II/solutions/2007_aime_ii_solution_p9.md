# 2007 AIME II Problem 9

## Problem

Rectangle $ABCD$ is given with $AB=63$ and $BC=448.$ Points $E$ and $F$ lie on $AD$ and $BC$ respectively, such that $AE=CF=84.$ The inscribed circle of triangle $BEF$ is tangent to $EF$ at point $P,$ and the inscribed circle of triangle $DEF$ is tangent to $EF$ at point $Q.$ Find $PQ.$

## Solution

## Solution 1
Several Pythagorean triples exist amongst the numbers given. $BE = DF = \sqrt{63^2 + 84^2} = 21\sqrt{3^2 + 4^2} = 105$ . Also, the length of $EF = \sqrt{63^2 + (448 - 2\cdot84)^2} = 7\sqrt{9^2 + 40^2} = 287$ .
Use the Two Tangent Theorem on $\triangle BEF$ . Since both circles are inscribed in congruent triangles, they are congruent; therefore, $EP = FQ = \frac{287 - PQ}{2}$ . By the Two Tangent theorem, note that $EP = EX = \frac{287 - PQ}{2}$ , making $BX = 105 - EX = 105 - \left[\frac{287 - PQ}{2}\right]$ . Also, $BX = BY$ . $FY = 364 - BY = 364 - \left[105 - \left[\frac{287 - PQ}{2}\right]\right]$ .
Finally, $FP = FY = 364 - \left[105 - \left[\frac{287 - PQ}{2}\right]\right] = \frac{805 - PQ}{2}$ . Also, $FP = FQ + PQ = \frac{287 - PQ}{2} + PQ$ . Equating, we see that $\frac{805 - PQ}{2} = \frac{287 + PQ}{2}$ , so $PQ = \boxed{259}$ .

## Solution 2
By the Two Tangent Theorem , we have that $FY = PQ + QF$ . Solve for $PQ = FY - QF$ . Also, $QF = EP = EX$ , so $PQ = FY - EX$ . Since $BX = BY$ , this can become $PQ = FY - EX + (BY - BX)$ $= \left(FY + BY\right) - \left(EX + BX\right) = FB - EB$ . Substituting in their values, the answer is $364 - 105 = 259$ .

## Solution 3
Call the incenter of $\triangle BEF$ $O_1$ and the incenter of $\triangle DFE$ $O_2$ . Draw triangles $\triangle O_1PQ,\triangle PQO_2$ .
Drawing $BE$ , We find that $BE = \sqrt {63^2 + 84^2} = 105$ . Applying the same thing for $F$ , we find that $FD = 105$ as well. Draw a line through $E,F$ parallel to the sides of the rectangle, to intersect the opposite side at $E_1,F_1$ respectively. Drawing $\triangle EE_1F$ and $FF_1E$ , we can find that $EF = \sqrt {63^2 + 280^2} = 287$ . We then use Heron's formula to get:
\[[BEF] = [DEF] = 11 466\] .
So the inradius of the triangle-type things is $\frac {637}{21}$ .
Now, we just have to find $O_1Q = O_2P$ , which can be done with simple subtraction, and then we can use the Pythagorean Theorem to find $PQ$ .

## Solution 4
Why not first divide everything by its greatest common factor, $7$ ? Then we're left with much simpler numbers which saves a lot of time. In the end, we will multiply by $7$ .
From there, we draw the same diagram as above (with smaller numbers). We soon find that the longest side of both triangles is 52 (64 - 12). That means:
$A = rs$ indicating $26(9)=r(54)$ so $r = 13/3$ .
Now, we can start applying the equivalent tangents. Calling them $a$ , $b$ , and $c$ (with $c$ being the longest and a being the shortest),
$a+b+c$ is the semi perimeter or $54$ . And since the longest side (which has $b+c$ ) is $52$ , $a=2$ .
Note that the distance $PQ$ we desired to find is just $c - a$ . What is $b$ then? $b = 13$ . And $c$ is $39$ . Therefore the answer is $37$ ... $NOT.$
Multiply by $7$ back again (I hope you remembered to write this in $huge$ letters on top of the scrap paper!), we actually get $259$ .

## Solution 5
Scaling everything by 7, we have that $AE = 12, AB = 9, BF = 52$ . Note that if the perpendicular of $F$ dropped down to $ED$ is $X$ , then $EX = 52-12 = 40$ . But $FX = 9$ and so we have a $9-40-41$ right triangle with $EFX$ meaning $EF = 41$ . Now, by symmetry, we know that $EP = QF = a$ meaning $PF = 41-a$ . If the tangent of the circle inscribed in $BEF$ is tangent to $BE$ at $Y$ , then if $BY = b$ we have a system of equations. $a+b = 15, b+41-a = 52$ . We can then solve for $a$ , and since $PQ = 41-2a$ , the rest follows.
These problems are copyrighted © by the Mathematical Association of America.
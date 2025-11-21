# 2011 AIME I Problem 2

## Problem

In rectangle $ABCD$ , $AB = 12$ and $BC = 10$ . Points $E$ and $F$ lie inside rectangle $ABCD$ so that $BE = 9$ , $DF = 8$ , $\overline{BE} \parallel \overline{DF}$ , $\overline{EF} \parallel \overline{AB}$ , and line $BE$ intersects segment $\overline{AD}$ . The length $EF$ can be expressed in the form $m \sqrt{n} - p$ , where $m$ , $n$ , and $p$ are positive integers and $n$ is not divisible by the square of any prime. Find $m + n + p$ .

### Diagram

[asy] pair A,B,C,D,E,F; A=(0,10); B=(12,10); C=(12,0); D=(0,0); E=(4.722,4.7); F=(6.469,4.7); draw(A--B--C--D--A); draw(D--F--E--B); label("$A$",A,NW); label("$B$",B,NE); label("$C$",C,SE); label("$D$",D,SW); label("$E$",E,W); label("$F$",F,SE); [/asy]

~Kscv

## Solution 1
Let us call the point where $\overline{EF}$ intersects $\overline{AD}$ point $G$ , and the point where $\overline{EF}$ intersects $\overline{BC}$ point $H$ . Since angles $FHB$ and $EGA$ are both right angles, and angles $BEF$ and $DFE$ are congruent due to parallelism, right triangles $BHE$ and $DGF$ are similar. This implies that $\frac{BH}{GD} = \frac{9}{8}$ . Since $BC=10$ , $BH+GD=BH+HC=BC=10$ . ( $HC$ is the same as $GD$ because they are opposite sides of a rectangle.) Now, we have a system:
$\frac{BH}{GD}=\frac{9}8$
$BH+GD=10$
Solving this system (easiest by substitution), we get that:
$BH=\frac{90}{17}$
$GD=\frac{80}{17}$
Using the Pythagorean Theorem, we can solve for the remaining sides of the two right triangles:
$\sqrt{9^2-\left(\frac{90}{17}\right)^2}$ and $\sqrt{8^2-\left(\frac{80}{17}\right)^2}$
Notice that adding these two sides would give us twelve plus the overlap $EF$ . This means that:
$EF= \sqrt{9^2-\left(\frac{90}{17}\right)^2}+\sqrt{8^2-\left(\frac{80}{17}\right)^2}-12=3\sqrt{21}-12$
Since $21$ isn't divisible by any perfect square, our answer is:
$3+21+12=\boxed{36}$

## Solution 2
Extend lines $BE$ and $CD$ to meet at point $G$ . Draw the altitude $GH$ from point $G$ to line $BA$ extended.
$GE=DF=8,$ $GB=17$
In right $\bigtriangleup GHB$ , $GH=10$ , $GB=17$ , thus by Pythagoras Theorem we have: $HB=\sqrt{17^2-10^2}=3\sqrt{21}$
$HA=EF=3\sqrt{21}-12$
Thus our answer is: $3+21+12=\boxed{36}$

## Solution 3 (Similar triangles, Algebra)
We notice that since $\overline{BE}||\overline{DF}$ , $\overline{EF}$ is the diagonal of a rectangle. Now, let us extend the width lines to intersect with $\overline{BE}$ and $\overline{DF}$ , respectively, to form this rectangle. Let us call the length of $\overline{EF}$ $d$ , the perpendicular distance between $\overline{EF}$ and $\overline{AD}$ $k$ , and the perpendicular distance between $\overline{EF}$ and $\overline{CD}$ $x$ . We now can begin the similar triangles. When drawing the diagram (where $E$ is closer to $\overline{AD}$ than $F$ ), we put the similar right triangles in the same position so that we can begin solving for our variables and finding ratios. Since all of these triangles are similar, we find that $\frac{dx}{8}=\frac{10d-dx}{9}$ , which solves for $x=\frac{80}{17}$ . Completing the same thing for $k$ , we see $\frac{12d-dk}{9}=\frac{dk+d^2}{8}$ , which solves for $k=\frac{96-9d}{17}$ . We are now ready to find both the length and the width of the rectangle. We find these to be $\frac{10d}{17}$ and $\frac{12d+d^2}{17}$ . Now let us use the Pythagorean to solve for $d$ . We square the length and the width and multiply both sides by 289 (the denominator of the LHS) to reach the equation $(12+d^2)^2+100d^2=289d^2$ . Expanding and simplifying, we find that $d^4+24d^3=45d^2$ . Dividing both sides by $d^2$ and moving everything to the LHS, we see that $d^2+24d-45=0$ . Applying the quadratic formula, $d=\frac{-24\pm \sqrt{756}}{2}=-12\pm \sqrt{189}$ . Since $d>0$ , $d=\sqrt{189}-12=3\sqrt{21}-12$ . Finally, $m+n+p=3+21+12=\boxed{036}$ . -Gideontz

## Video Solution
https://www.youtube.com/watch?v=_znugFEst6E&t=919s
~Shreyas S
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
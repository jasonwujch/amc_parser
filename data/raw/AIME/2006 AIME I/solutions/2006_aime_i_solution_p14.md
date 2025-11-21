# 2006 AIME I Problem 14

## Problem

A tripod has three legs each of length $5$ feet. When the tripod is set up, the angle between any pair of legs is equal to the angle between any other pair, and the top of the tripod is $4$ feet from the ground. In setting up the tripod, the lower 1 foot of one leg breaks off. Let $h$ be the height in feet of the top of the tripod from the ground when the broken tripod is set up. Then $h$ can be written in the form $\frac m{\sqrt{n}},$ where $m$ and $n$ are positive integers and $n$ is not divisible by the square of any prime. Find $\lfloor m+\sqrt{n}\rfloor.$ (The notation $\lfloor x\rfloor$ denotes the greatest integer that is less than or equal to $x.$ )

## Solution 1
We will use $[...]$ to denote volume (four letters), area (three letters) or length (two letters).
Let $T$ be the top of the tripod, $A,B,C$ are end points of three legs. Let $S$ be the point on $TA$ such that $[TS] = 4$ and $[SA] = 1$ . Let $O$ be the center of the base equilateral triangle $ABC$ . Let $M$ be the midpoint of segment $BC$ . Let $h$ be the distance from $T$ to the triangle $SBC$ ( $h$ is what we want to find).
We have the volume ratio $\frac {[TSBC]}{[TABC]} = \frac {[TS]}{[TA]} = \frac {4}{5}$ .
So $\frac {h\cdot [SBC]}{[TO]\cdot [ABC]} = \frac {4}{5}$ .
We also have the area ratio $\frac {[SBC]}{[ABC]} = \frac {[SM]}{[AM]}$ .
The triangle $TOA$ is a $3-4-5$ right triangle so $[AM] = \frac {3}{2}\cdot[AO] = \frac {9}{2}$ and $\cos{\angle{TAO}} = \frac {3}{5}$ .
Applying Law of Cosines to the triangle $SAM$ with $[SA] = 1$ , $[AM] = \frac {9}{2}$ and $\cos{\angle{SAM}} = \frac {3}{5}$ , we find:
Putting it all together, we find $h = \frac {144}{\sqrt {5\cdot317}}$ .

## Solution 2
We note that $AO=3$ . From this we can derive that the side length of the equilateral is $3\sqrt{3}$ . We now use 3D coordinate geometry. \[A = (0,0,0)\] \[B = (3\sqrt{3},0,0)\] \[C = (\frac{3\sqrt{3}}{2}, \frac{9}{2}, 0)\] \[T = (\frac{3\sqrt{3}}{2}, \frac{3}{2}, 4)\] \[S= (\frac{3\sqrt{3}}{10}, \frac{3}{10}, \frac{4}{5})\] We know three points of plane $SCB$ hence we can write out the equation for the plane. Plane $SCB$ can be expressed as \[4\sqrt{3}x+4y+39z-36=0.\]
Applying the distance between a point and a plane formula.
\[\frac{ax+by+cz+d}{\sqrt{a^{2}+b^{2}+c^{2}}} = \frac{4\sqrt{3} \cdot \frac{3\sqrt{3}}{2} + 4\cdot \frac{3}{2} + 39 \cdot 4 -36}{\sqrt{(4\sqrt{3})^2+4^2+39^2}} = \frac{144}{\sqrt{1585}}\]
\[\lfloor m+\sqrt{n}\rfloor = \lfloor 144+\sqrt{1585}\rfloor = 183\]
Solution by SimonSun

## Solution 3 (Cosine Law & Pythagorean Bash)
Diagram borrowed from Solution 1
Apply Pythagorean Theorem on $\bigtriangleup TOB$ yields \[BO=\sqrt{TB^2-TO^2}=3\] Since $\bigtriangleup ABC$ is equilateral, we have $\angle MOB=60^{\circ}$ and \[BC=2BM=2(OB\sin MOB)=3\sqrt{3}\] Apply Pythagorean Theorem on $\bigtriangleup TMB$ yields \[TM=\sqrt{TB^2-BM^2}=\sqrt{5^2-(\frac{3\sqrt{3}}{2})^2}=\frac{\sqrt{73}}{2}\] Apply Law of Cosines on $\bigtriangleup TBC$ we have \[BC^2=TB^2+TC^2-2(TB)(TC)\cos BTC\] \[(3\sqrt{3})^2=5^2+5^2-2(5)^2\cos BTC\] \[\cos BTC=\frac{23}{50}\] Apply Law of Cosines on $\bigtriangleup STB$ using the fact that $\angle STB=\angle BTC$ we have \[SB^2=ST^2+BT^2-2(ST)(BT)\cos STB\] \[SB=\sqrt{4^2+5^2-2(4)(5)\cos BTC}=\frac{\sqrt{565}}{5}\] Apply Pythagorean Theorem on $\bigtriangleup BSM$ yields \[SM=\sqrt{SB^2-BM^2}=\frac{\sqrt{1585}}{10}\] Let the perpendicular from $T$ hits $SBC$ at $P$ . Let $SP=x$ and $PM=\frac{\sqrt{1585}}{10}-x$ . Apply Pythagorean Theorem on $TSP$ and $TMP$ we have \[TP^2=TS^2-SP^2=TM^2-PM^2\] \[4^2-x^2=(\frac{\sqrt{73}}{2})^2-(\frac{\sqrt{1585}}{10}-x)^2\] Cancelling out the $x^2$ term and solving gets $x=\frac{181}{2\sqrt{1585}}$ .
Finally, by Pythagorean Theorem, \[TP=\sqrt{TS^2-SP^2}=\frac{144}{\sqrt{1585}}\] so $\lfloor m+\sqrt{n}\rfloor=\boxed{183}$
~ Nafer
These problems are copyrighted © by the Mathematical Association of America.
# 2014 AMC 10B Problem 19

## Problem

Two concentric circles have radii $1$ and $2$ . Two points on the outer circle are chosen independently and uniformly at random. What is the probability that the chord joining the two points intersects the inner circle?

$\textbf{(A)}\ \frac{1}{6}\qquad \textbf{(B)}\ \frac{1}{4}\qquad \textbf{(C)}\ \frac{2-\sqrt{2}}{2}\qquad \textbf{(D)}\ \frac{1}{3}\qquad \textbf{(E)}\ \frac{1}{2}\qquad$

## Solution
Let the center of the two circles be $O$ . Now pick an arbitrary point $A$ on the boundary of the circle with radius $2$ . We want to find the range of possible places for the second point, $A'$ , such that $AA'$ passes through the circle of radius $1$ . To do this, first draw the tangents from $A$ to the circle of radius $1$ . Let the intersection points of the tangents (when extended) with circle of radius $2$ be $B$ and $C$ . Let $H$ be the foot of the altitude from $O$ to $\overline{BC}$ . Then we have the following diagram.
[asy] scale(200); pair A,O,B,C,H; A = (0,1); O = (0,0); B = (-.866,-.5); C = (.866,-.5); H = (0, -.5); draw(A--C--cycle); draw(A--O--cycle); draw(O--C--cycle); draw(O--H,dashed+linewidth(.7)); draw(A--B--cycle); draw(B--C--cycle); draw(O--B--cycle); dot("$A$",A,N); dot("$O$",O,NW); dot("$B$",B,W); dot("$C$",C,E); dot("$H$",H,S); label("$2$",O--(-.7,-.385),N); label("$1$",O--H,E); draw(circle(O,.5)); draw(circle(O,1)); [/asy]
We want to find $\angle BOC$ , as the range of desired points $A'$ is the set of points on minor arc $\overarc{BC}$ . This is because $B$ and $C$ are part of the tangents, which "set the boundaries" for $A'$ . Since $OH = 1$ and $OB = 2$ as shown in the diagram, $\triangle OHB$ is a $30-60-90$ triangle with $\angle BOH = 60^\circ$ . Thus, $\angle BOC = 120^\circ$ , and the probability $A'$ lies on the minor arc $\overarc{BC}$ is thus $\dfrac{120}{360} = \boxed{\textbf{(D)}\: \dfrac13}$ .
### Comment
This problem is exactly the Bertrand paradox! I feel sorry for students who took 2014 AMC 10B :-( The answers (E) 1/2, (D) 1/3, and (B) 1/4 are all correct, depending on what kind of uniform you choose. (1) If you choose angle uniform, the probability is 1/3. (2) If you choose the center of the chord is uniformly distributed in the big circle, the probability is 1/4. (3) If you choose the center of the chord is uniformly distributed along a radius (i.e. 0 to 2 from the center of the big circle), the probability is 1/2.
-EUCLID_2003
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
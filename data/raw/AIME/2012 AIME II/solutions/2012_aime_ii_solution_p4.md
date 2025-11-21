# 2012 AIME II Problem 4

## Problem

Ana, Bob, and Cao bike at constant rates of $8.6$ meters per second, $6.2$ meters per second, and $5$ meters per second, respectively. They all begin biking at the same time from the northeast corner of a rectangular field whose longer side runs due west. Ana starts biking along the edge of the field, initially heading west, Bob starts biking along the edge of the field, initially heading south, and Cao bikes in a straight line across the field to a point $D$ on the south edge of the field. Cao arrives at point $D$ at the same time that Ana and Bob arrive at $D$ for the first time. The ratio of the field's length to the field's width to the distance from point $D$ to the southeast corner of the field can be represented as $p : q : r$ , where $p$ , $q$ , and $r$ are positive integers with $p$ and $q$ relatively prime. Find $p+q+r$ .

## Solution 1 (bash)
[asy]draw((1.2,0)--(0,0)--(0,1.4)--(6,1.4)--(6,0)--(1.2,0)--(6,1.4)); label("$D$", (1.2,0),dir(-90)); dot((6,1.4)); dot((1.2,0)); label("$a$", (0.6,0),dir(-90)); label("$b$", (3.6,0),dir(-90)); label("$c$", (6,0.7),dir(0));[/asy]
Let $a,b,c$ be the labeled lengths as shown in the diagram. Also, assume WLOG the time taken is $1$ second.
Observe that $\dfrac{2a+b+c}{8.6}=1$ or $2a+b+c=8.6$ , and $\dfrac{b+c}{6.2}=1$ or $b+c=6.2$ . Subtracting the second equation from the first gives $2a=2.4$ , or $a=1.2$ .
Now, let us solve $b$ and $c$ . Note that $\dfrac{\sqrt{b^2+c^2}}{5}=1$ , or $b^2+c^2=25$ . We also have $b+c=6.2$ .
We have a system of equations: \[\left\{\begin{array}{l}b+c=6.2\\ b^2+c^2=25\end{array}\right.\]
Squaring the first equation gives $b^2+2bc+c^2=38.44$ , and subtracting the second from this gives $2bc=13.44$ . Now subtracting this from $b^2+c^2=25$ gives $b^2-2bc+c^2=(b-c)^2=11.56$ , or $b-c=3.4$ . Now we have the following two equations:
\[\left\{\begin{array}{l}b+c=6.2\\ b-c=3.4\end{array}\right.\]
Adding the equations and dividing by two gives $b=4.8$ , and it follows that $c=1.4$ .
The ratios we desire are therefore $1.4:6:4.8=7:30:24$ , and our answer is $7+30+24=\boxed{061}$ .
Note that in our diagram, we labeled the part of the bottom $b$ and the side $c$ . However, these labels are interchangeable. We can cancel out the case where the side is $4.8$ and the part of the bottom is $1.4$ by noting a restriction of the problem: "...a rectangular field whose longer side runs due west." If we had the side be $4.8$ , then the entire bottom would be $1.2+1.4=2.6$ , clearly less than $4.8$ and therefore violating our restriction.

## Solution 2 (uglier bash)
Let P, Q, and R be the east-west distance of the field, the north-south distance, and the distance from the southeast corner to point D, respectively.
Ana's distance to point D = $P + Q + (P - R) = 2P + Q - R$
Bob's distance to point D = $Q + R$
Cao's distance to point D = $\sqrt{Q^2 + R^2}$
Since they arrive at the same time, their distance/speed ratios are equal, so:
\[\frac{2P + Q - R}{8.6} = \frac{Q + R}{6.2} = \frac{\sqrt{Q^2 + R^2}}{5}\]
\[\frac{2P + Q - R}{43} = \frac{Q + R}{31} = \frac{\sqrt{Q^2 + R^2}}{25}\]
Looking at the last two parts of the equation:
\[\frac{Q + R}{31} = \frac{\sqrt{Q^2 + R^2}}{25}\]
\[25 (Q + R) = 31 \sqrt{Q^2 + R^2}\]
\[625 Q^2 + 1250 QR + 625 R^2 = 961 Q^2 + 961 R^2\]
\[336 Q^2 - 1250 QR + 336 R^2 = 0\]
\[168 (\frac{Q}{R})^2 - 625 \frac{Q}{R}+ 168 = 0\]
\[\frac{Q}{R} = \frac{625 \pm \sqrt{625^2 - 4 \cdot 168^2}}{336}\]
\[\frac{Q}{R} = 24/7\;or\;7/24\]
Looking at the first two parts of the equation above:
\[\frac{2 P + Q - R}{43} = \frac{Q + R}{31}\]
\[62 P + 31 Q - 31 R = 43 Q + 43 R\]
\[P = \frac{6}{31}Q + \frac{37}{31} R\]
If $\frac{Q}{R} = \frac{24}{7}$ :
\[R = \frac{7}{24} Q\]
\[P = \frac{6}{31} Q + \frac{37}{31} \cdot \frac{7}{24} Q = \frac{13}{24} Q\]
However, this makes P < Q, but we are given that P > Q. Therefore, $\frac{Q}{R} = \frac{7}{24}$ , and:
\[R = \frac{24}{7} Q\]
\[P = \frac{6}{31} Q + \frac{37}{31} \cdot \frac{24}{7} Q = \frac{30}{7} Q\]
\[P : Q : R = 30 : 7 : 24\]
The solution is $P + Q + R = \framebox{061}$ .
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
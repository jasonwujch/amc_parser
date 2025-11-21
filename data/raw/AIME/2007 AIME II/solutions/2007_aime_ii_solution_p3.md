# 2007 AIME II Problem 3

## Problem

Square $ABCD$ has side length $13$ , and points $E$ and $F$ are exterior to the square such that $BE=DF=5$ and $AE=CF=12$ . Find $EF^{2}$ . [asy]unitsize(0.2 cm); pair A, B, C, D, E, F; A = (0,13); B = (13,13); C = (13,0); D = (0,0); E = A + (12*12/13,5*12/13); F = D + (5*5/13,-5*12/13); draw(A--B--C--D--cycle); draw(A--E--B); draw(C--F--D); dot("$A$", A, W); dot("$B$", B, dir(0)); dot("$C$", C, dir(0)); dot("$D$", D, W); dot("$E$", E, N); dot("$F$", F, S);[/asy]

1 Problem

- 1 Problem

- 2 Solution 2.1 Solution 1 2.2 Solution 2 2.3 Solution 3 2.4 Solution 4 2.5 Solution 5 (Ptolemy's Theorem) 2.6 Solution 6 (Coordinate Bash) 2.7 Solution 7 (Trig Bash)

- 3 See also

- 2.1 Solution 1

- 2.2 Solution 2

- 2.3 Solution 3

- 2.4 Solution 4

- 2.5 Solution 5 (Ptolemy's Theorem)

- 2.6 Solution 6 (Coordinate Bash)

- 2.7 Solution 7 (Trig Bash)

## Solution

## Solution 1
Let $\angle FCD = \alpha$ , so that $FB = \sqrt{12^2 + 13^2 + 2\cdot12\cdot13\sin(\alpha)} = \sqrt{433}$ . By the diagonal, $DB = 13\sqrt{2}, DB^2 = 338$ .
The sum of the squares of the sides of a parallelogram is the sum of the squares of the diagonals. \[EF^2 = 2\cdot(5^2 + 433) - 338 = 578.\]

## Solution 2
Extend $\overline{AE}, \overline{DF}$ and $\overline{BE}, \overline{CF}$ to their points of intersection. Since $\triangle ABE \cong \triangle CDF$ and are both $5-12-13$ right triangles , we can come to the conclusion that the two new triangles are also congruent to these two (use ASA , as we know all the sides are $13$ and the angles are mostly complementary). Thus, we create a square with sides $5 + 12 = 17$ .
[asy]unitsize(0.25 cm); pair A, B, C, D, E, F, G, H; A = (0,13); B = (13,13); C = (13,0); D = (0,0); E = A + (12*12/13,5*12/13); F = D + (5*5/13,-5*12/13); G = rotate(90,(A + C)/2)*(E); H = rotate(90,(A + C)/2)*(F); draw(A--B--C--D--cycle); draw(E--G--F--H--cycle); dot("$A$", A, N); dot("$B$", B, dir(0)); dot("$C$", C, S); dot("$D$", D, W); dot("$E$", E, N); dot("$F$", F, S); dot("$G$", G, W); dot("$H$", H, dir(0));[/asy]
$\overline{EF}$ is the diagonal of the square, with length $17\sqrt{2}$ ; the answer is $EF^2 = (17\sqrt{2})^2 = 578$ .

## Solution 3
A slightly more analytic/brute-force approach:
Drop perpendiculars from $E$ and $F$ to $I$ and $J$ , respectively; construct right triangle $EKF$ with right angle at K and $EK || BC$ . Since $2[CDF]=DF*CF=CD*JF$ , we have $JF=5\times12/13 = \frac{60}{13}$ . Similarly, $EI=\frac{60}{13}$ . Since $\triangle DJF \sim \triangle DFC$ , we have $DJ=\frac{5JF}{12}=\frac{25}{13}$ .
Now, we see that $FK=DC-(DJ+IB)=DC-2DJ=13-\frac{50}{13}=\frac{119}{13}$ . Also, $EK=BC+(JF+IE)=BC+2JF=13+\frac{120}{13}=\frac{289}{13}$ . By the Pythagorean Theorem, we have $EF=\sqrt{\left(\frac{289}{13}\right)^2+\left(\frac{119}{13} \right)^2}=\frac{\sqrt{(17^2)(17^2+7^2)}}{13}$ $=\frac{17\sqrt{338}}{13}=\frac{17(13\sqrt{2})}{13}=17\sqrt{2}$ . Therefore, $EF^2=(17\sqrt{2})^2=578$ .

## Solution 4
Based on the symmetry, we know that $F$ is a reflection of $E$ across the center of the square, which we will denote as $O$ . Since $\angle BEA$ and $\angle AOB$ are right, we can conclude that figure $AOBE$ is a cyclic quadrilateral. Pythagorean Theorem yields that $BO=AO=\frac{13\sqrt{2}}{2}$ . Now, using Ptolemy's Theorem, we get that \[AO\cdot BE + BO\cdot AE = AB\cdot AO\] \[\frac{13\sqrt{2}}{2}\cdot 5+\frac{13\sqrt{2}}{2}\cdot 12 = 13\cdot OE\] \[OE=\frac{17\sqrt{2}}{2}\] Now, since we stated in the first step that $F$ is a reflection of $E$ across $O$ , we can say that $EF=2EO=17\sqrt{2}$ . This gives that \[EF^2=(17\sqrt{2})^2=578\] AWD with this bash solution

## Solution 5 (Ptolemy's Theorem)
Drawing $EF$ , it clearly passes through the center of $ABCD$ . Letting this point be $P$ , we note that $AEBP$ and $CFDP$ are congruent cyclic quadrilaterals, and that $AP=BP=CP=DP=\frac{13}{\sqrt{2}}.$ Now, from Ptolemy's, $13\cdot EP=\frac{13}{\sqrt{2}}(12+5)\implies EP=\frac{17\sqrt{2}}{2}$ . Since $EF=EP+FP=2\cdot EP$ , the answer is $(17\sqrt{2})^2=\boxed{578}.$

## Solution 6 (Coordinate Bash)
Place the vertices of the square as follows: \begin{align} D &= (0,\;0),\\ C &= (13,\;0),\\ A &= (0,\;13),\\ B &= (13,\;13). \end{align}
Compute the coordinates of points E and F using the distance formula. Place $E$ at $(x,y)$ and $F$ at $(a,b)$ .
\begin{aligned} x^2+(y-13)^2 = 144,\\ (x-13)^2+(y-13)^2 = 25 \end{aligned}
\begin{aligned} a^2+b^2=25,\\ (a-13)^2+b^2=144. \end{aligned}
Solving and taking appropriate solutions to get: $E = (144/13,229/13)$ , and $F = (25/13, -60/13)$
Computing distance between $E$ and $F$ = $17\sqrt{2}$
\[EF^2 = 578\]

## Solution 7 (Trig Bash)
We first see that the whole figure is symmetrical and reflections across the center that we will denote as $O$ bring each half of the figure to the other half. Thus we consider a single part of the figure, namely $EO.$
First note that $\angle BAO = 45^{\circ}$ since $O$ is the center of square $ABCD.$ Also note that $\angle EAB = \arccos{\left(\frac{12}{13}\right)}$ or $\arcsin{\left(\frac{5}{13}\right)}.$ Finally, we know that $AO =\frac{13\sqrt{2}}{2}.$ Now we apply laws of cosines on $\bigtriangleup AEO.$
We have $EO^2 = 12^2 + (\frac{13\sqrt{2}}{2})^2 - 2 \cdot 12 \cdot \left(\frac{13\sqrt{2}}{2}\right) \cdot \cos{\angle EAO}.$ We know that $\angle EAO = 45^{\circ} + \arccos{\left(\frac{12}{13}\right)}.$ Thus we have $\cos{\angle EAO} = \cos\left(45^{\circ} + \arccos{\left(\frac{12}{13}\right)}\right)$ which applying the cosine sum identity yields $\cos{45^{\circ}}\cos{\arccos\frac{12}{13}} - \sin{45^{\circ}}\sin\arcsin{\frac{5}{12}} =\frac{12\sqrt{2}}{26} -\frac{5\sqrt{2}}{26} =\frac{7\sqrt{2}}{26}.$
Note that we are looking for $4EO^2$ so we multiply $EO^2 = 12^2 + \left(\frac{13\sqrt{2}}{2}\right)^2 - 2 \cdot 12 \cdot \left(\frac{13\sqrt{2}}{2}\right) \cdot \cos{\angle EAO}$ by $4$ obtaining $4EO^2 = 576 + 338 - 8 \cdot\left(\frac{13\sqrt{2}}{2}\right) \cdot 12 \cdot\frac{7\sqrt{2}}{26} = 576 + 338 - 4 \cdot 12 \cdot 7 = \boxed{578}.$
These problems are copyrighted © by the Mathematical Association of America.
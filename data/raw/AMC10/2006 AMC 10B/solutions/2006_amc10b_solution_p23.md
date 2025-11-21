# 2006 AMC 10B Problem 23

## Problem

A triangle is partitioned into three triangles and a quadrilateral by drawing two lines from vertices to their opposite sides. The areas of the three triangles are 3, 7, and 7, as shown. What is the area of the shaded quadrilateral?

[asy] unitsize(1.5cm); defaultpen(.8); pair A = (0,0), B = (3,0), C = (1.4, 2), D = B + 0.4*(C-B), Ep = A + 0.3*(C-A); pair F = intersectionpoint( A--D, B--Ep ); draw( A -- B -- C -- cycle ); draw( A -- D ); draw( B -- Ep ); filldraw( D -- F -- Ep -- C -- cycle, mediumgray, black ); label("$7$",(1.25,0.2)); label("$7$",(2.2,0.45)); label("$3$",(0.45,0.35)); [/asy]

$\mathrm{(A) \ } 15\qquad \mathrm{(B) \ } 17\qquad \mathrm{(C) \ } \frac{35}{2}\qquad \mathrm{(D) \ } 18\qquad \mathrm{(E) \ } \frac{55}{3}$

## Solution 1
Label the points in the figure as shown below, and draw the segment $CF$ . This segment divides the quadrilateral into two triangles, let their areas be $x$ and $y$ .
[asy] unitsize(2cm); defaultpen(.8); pair A = (0,0), B = (3,0), C = (1.4, 2), D = B + 0.4*(C-B), Ep = A + 0.3*(C-A); pair F = intersectionpoint( A--D, B--Ep ); draw( A -- B -- C -- cycle ); draw( A -- D ); draw( B -- Ep ); filldraw( D -- F -- Ep -- C -- cycle, mediumgray, black ); label("$7$",(1.45,0.15)); label("$7$",(2.2,0.45)); label("$3$",(0.45,0.35)); draw( C -- F, dashed ); label("$A$",A,SW); label("$B$",B,SE); label("$C$",C,N); label("$D$",D,NE); label("$E$",Ep,NW); label("$F$",F,S); label("$x$",(1,1)); label("$y$",(1.6,1)); [/asy]
Since triangles $AFB$ and $DFB$ share an altitude from $B$ and have equal area, their bases must be equal, hence $AF=DF$ .
Since triangles $AFC$ and $DFC$ share an altitude from $C$ and their respective bases are equal, their areas must be equal, hence $x+3=y$ .
Since triangles $EFA$ and $BFA$ share an altitude from $A$ and their respective areas are in the ratio $3:7$ , their bases must be in the same ratio, hence $EF:FB = 3:7$ .
Since triangles $EFC$ and $BFC$ share an altitude from $C$ and their respective bases are in the ratio $3:7$ , their areas must be in the same ratio, hence $x:(y+7) = 3:7$ , which gives us $7x = 3(y+7)$ .
Substituting $y=x+3$ into the second equation we get $7x = 3(x+10)$ , which solves to $x=\frac{15}{2}$ . Then $y=x+3 = \frac{15}{2}+3 = \frac{21}{2}$ , and the total area of the quadrilateral is $x+y = \frac{15}{2}+\frac{21}{2} = \boxed{\textbf{(D) }18}$ .

## Solution 2
Connect points $E$ and $D$ . Triangles $EFA$ and $FAB$ share an altitude and their areas are in the ratio $3:7$ . Their bases, $EF$ and $FB$ , must be in the same $3:7$ ratio.
Triangles $EFD$ and $FBD$ share an altitude and their bases are in a $3:7$ ratio. Therefore, their areas are in a $3:7$ ratio and the area of triangle $EFD$ is $3$ .
Triangle $CED$ and $DEA$ share an altitude. Therefore, the ratio of their areas is equal to the ratio of bases $CE$ and $EA$ . The ratio is $A:(3+3) \Rightarrow A:6$ where $A$ is the area of triangle $CED$
Triangles $CEB$ and $EAB$ also share an altitude. The ratio of their areas is also equal to the ratio of bases $CE$ and $EA$ . The ratio is $(A+3+7):(3+7) \Rightarrow (A+10):10$
Because the two ratios are equal, we get the equation $\frac{A}{6} = \frac {A+10}{10} \Rightarrow 10A = 6A+60 \Rightarrow A = 15$ . We add the area of triangle $EDF$ to get that the total area of the quadrilateral is $\boxed{\textbf{(D) }18}$ .
~Zeric Hang

## Solution 3
We use mass points (similar to above). Let the triangle be $ABC$ with cevians (lines to opposite side) from $B$ and $C$ . Let the points opposite $B$ and $C$ be $D$ and $F$ respectively and the intersection as $P$ .
Assign masses of 1 at $B$ and $D$ since $[BPC] = [DPC]$ . Then the mass at $P$ is 2. To find masses at $F$ and $C$ , we let the mass at $F$ be x and the mass at $C$ be y. Then $3x = 7y$ and $y = \frac{3}{7}x$ . Then $\frac{10}{7}x = 2$ since we add the masses for the fulcrum mass, and $x = \frac{7}{5}$ and $y = \frac{3}{5}$ .
To calculate the mass at a, it is merely $\frac{7}{5} - 1 = \frac{2}{5}$ which means $\frac{[BCF]}{[ACF]} = \frac{2}{5}$ or $[ACF] = 25$ . It is easy to see the answer is $\boxed{\textbf{(D) }18}$ .

## Video Solutions
https://www.youtube.com/watch?v=LAo4KQh89a4 ~David $\newline$ https://www.youtube.com/watch?v=kfbejToTTMA ~epiconan $\newline$ https://youtu.be/kCBOUEAooDA?list=PLoZ0gn0j87fcm-YyWXXnIdAcT5NLq9W2i&t=425 ~CanadaMath
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
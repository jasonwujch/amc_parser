# 2006 AIME II Problem 1

## Problem

In convex hexagon $ABCDEF$ , all six sides are congruent, $\angle A$ and $\angle D$ are right angles , and $\angle B, \angle C, \angle E,$ and $\angle F$ are congruent . The area of the hexagonal region is $2116(\sqrt{2}+1).$ Find $AB$ .

## Solution 1
Let the side length be called $x$ , so $x=AB=BC=CD=DE=EF=AF$ .
The diagonal $BF=\sqrt{AB^2+AF^2}=\sqrt{x^2+x^2}=x\sqrt{2}$ . Then the areas of the triangles AFB and CDE in total are $\frac{x^2}{2}\cdot 2$ , and the area of the rectangle BCEF equals $x\cdot x\sqrt{2}=x^2\sqrt{2}$
Then we have to solve the equation
\[2116(\sqrt{2}+1)=x^2\sqrt{2}+x^2\] \[2116(\sqrt{2}+1)=x^2(\sqrt{2}+1)\] \[2116=x^2\] \[x=46\]
Therefore, $AB$ is $\boxed{046}$ .

## Solution 2
Because $\angle B$ , $\angle C$ , $\angle E$ , and $\angle F$ are congruent, the degree-measure of each of them is ${{720-2\cdot90}\over4}= 135$ . Lines $BF$ and $CE$ divide the hexagonal region into two right triangles and a rectangle. Let $AB=x$ . Then $BF=x\sqrt2$ . Thus \begin{align*} 2116(\sqrt2+1)&=[ABCDEF]\\ &=2\cdot {1\over2}x^2+x\cdot x\sqrt2=x^2(1+\sqrt2), \end{align*} so $x^2=2116$ , and $x=\boxed{046}$ .
[asy] pair A,B,C,D,E,F; A=(0,0); B=(7,0); C=(13,6); E=(6,13); D=(13,13); F=(0,7); dot(A); dot(B); dot(C); dot(D); dot(E); dot(F); draw(A--B--C--D--E--F--cycle,linewidth(0.7)); label("{\tiny $A$}",A,S); label("{\tiny $B$}",B,S); label("{\tiny $C$}",C,S); label("{\tiny $D$}",D,N); label("{\tiny $E$}",E,N); label("{\tiny $F$}",F,W); [/asy]
### See Also
These problems are copyrighted © by the Mathematical Association of America.
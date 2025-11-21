# 2014 AMC 10B Problem 21

## Problem

Trapezoid $ABCD$ has parallel sides $\overline{AB}$ of length $33$ and $\overline {CD}$ of length $21$ . The other two sides are of lengths $10$ and $14$ . The angles $A$ and $B$ are acute. What is the length of the shorter diagonal of $ABCD$ ?

$\textbf{(A) }10\sqrt{6}\qquad\textbf{(B) }25\qquad\textbf{(C) }8\sqrt{10}\qquad\textbf{(D) }18\sqrt{2}\qquad\textbf{(E) }26$

## Solution 1
[asy] size(7cm); pair A,B,C,D,CC,DD; A = (-2,7); B = (14,7); C = (10,0); D = (0,0); CC = (10,7); DD = (0,7); draw(A--B--C--D--cycle); //label("33",(A+B)/2,N); label("21",(C+D)/2,S); label("10",(A+D)/2,W); label("14",(B+C)/2,E); label("$A$",A,NW); label("$B$",B,NE); label("$C$",C,SE); label("$D$",D,SW); label("$E$",DD,N); label("$F$",CC,N); draw(C--CC); draw(D--DD); [/asy]
In the diagram, $\overline{DE} \perp \overline{AB}, \overline{FC} \perp \overline{AB}$ . Denote $\overline{AE} = x$ and $\overline{DE} = h$ . In right triangle $AED$ , we have from the Pythagorean theorem: $x^2+h^2=100$ . Note that since $EF = DC$ , we have $BF = 33-DC-x = 12-x$ . Using the Pythagorean theorem in right triangle $BFC$ , we have $(12-x)^2 + h^2 = 196$ .
We isolate the $h^2$ term in both equations, getting $h^2= 100-x^2$ and $h^2 = 196-(12-x)^2$ .
Setting these equal, we have $100-x^2 = 196 - 144 + 24x -x^2 \implies 24x = 48 \implies x = 2$ . Now, we can determine that $h^2 = 100-4 \implies h = 4\sqrt{6}$ .
[asy] size(7cm); pair A,B,C,D,CC,DD; A = (-2,7); B = (14,7); C = (10,0); D = (0,0); CC = (10,7); DD = (0,7); draw(A--B--C--D--cycle); //label("33",(A+B)/2,N); label("21",(C+D)/2,S); label("10",(A+D)/2,W); label("14",(B+C)/2,E); label("$A$",A,NW); label("$B$",B,NE); label("$C$",C,SE); label("$D$",D,SW); label("$D$",D,SW); label("$E$",DD,SE); label("$F$",CC,SW); draw(C--CC); draw(D--DD); label("21",(CC+DD)/2,N); label("$2$",(A+DD)/2,N); label("$10$",(CC+B)/2,N); label("$4\sqrt{6}$",(C+CC)/2,W); label("$4\sqrt{6}$",(D+DD)/2,E); pair X = (-2,0); //draw(X--C--A--cycle,black+2bp); [/asy]
The two diagonals are $\overline{AC}$ and $\overline{BD}$ . Using the Pythagorean theorem again on $\bigtriangleup AFC$ and $\bigtriangleup BED$ , we can find these lengths to be $\sqrt{96+529} = 25$ and $\sqrt{96+961} = \sqrt{1057}$ . Since $\sqrt{96+529}<\sqrt{96+961}$ , $25$ is the shorter length*, so the answer is $\boxed{\textbf{(B) }25}$ .
- Or, alternatively, one can notice that the two triangles have the same height but $\bigtriangleup AFC$ has a shorter base than $\bigtriangleup BED$ .

## Solution 2
[asy] size(7cm); pair A,B,C,D,E; A = (-2,7); B = (14,7); C = (10,0); D = (0,0); E = (4,7); draw(A--B--C--D--cycle); draw(D--E); label("21",(C+D)/2,S); label("10",(A+D)/2,W); label("14",(12,1),E); label("14",(2,1),E); label("12",(A+E)/2,N); label("21",(E+B)/2,N); label("$A$",A,NW); label("$B$",B,NE); label("$C$",C,SE); label("$D$",D,SW); label("$D$",D,SW); label("$E$",E,N); [/asy]
The area of $\Delta AED$ is by Heron's, $4\sqrt{9(4)(3)(2)}=24\sqrt{6}$ . This makes the length of the altitude from $D$ onto $\overline{AE}$ equal to $4\sqrt{6}$ . One may now proceed as in Solution $1$ to obtain an answer of $\boxed{\textbf{(B) }25}$ .

## Solution 3
Using the same way as Solution 1, obtain that $AE=2$ . Extend $DC$ and drop a perpendicular from $A$ onto $DC$ . Call this point $G$ . We know that $GC=DC+AE=21+2=23$ , and following the method from Solution 1, we also have $AG=4\sqrt{6}$ . Thus the answer would be the \[\sqrt{23^2+(4\sqrt{6})^2}=\sqrt{529+96}=\sqrt{625}=\boxed{\textbf{(B) } 25}\] -Reality Writes
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
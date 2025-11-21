# 2005 AMC 10A Problem 8

## Problem

In the figure, the length of side $AB$ of square $ABCD$ is $\sqrt{50}$ , $E$ is between $B$ and $H$ , and $BE = 1$ . What is the area of the inner square $EFGH$ ?

[asy] unitsize(4cm); defaultpen(linewidth(.8pt)+fontsize(10pt)); pair D=(0,0), C=(1,0), B=(1,1), A=(0,1); pair F=intersectionpoints(Circle(D,2/sqrt(5)),Circle(A,1))[0]; pair G=foot(A,D,F), H=foot(B,A,G), E=foot(C,B,H); draw(A--B--C--D--cycle); draw(D--F); draw(C--E); draw(B--H); draw(A--G); label("$A$",A,NW); label("$B$",B,NE); label("$C$",C,SE); label("$D$",D,SW); label("$E$",E,NNW); label("$F$",F,ENE); label("$G$",G,SSE); label("$H$",H,WSW); [/asy]

$\textbf{(A) } 25\qquad\textbf{(B) } 32\qquad\textbf{(C) } 36\qquad\textbf{(D) } 40\qquad\textbf{(E) } 42$

## Solution
We see that side $BE$ , which we know is $1$ , is also the shorter leg of one of the four right triangles (which are obviously congruent, using the symmetry of the diagram). So $AH = 1$ , and hence $HB = HE + BE = HE + 1$ . Since $HE$ is one of the sides of the square whose area we want to find, we can now simply apply Pythagoras' theorem:
\begin{align*}1^2 + (HE+1)^2 = \left(\sqrt{50}\right)^2 &\iff 1 + (HE+1)^2 = 50 \\ &\iff (HE+1)^2 = 49 \\&\iff HE+1 = 7 \qquad \text{(as } HE \text{ is a length, so must be positive)} \\ &\iff HE = 6.\end{align*}
Thus the area of the square is $6^2 = \boxed{\textbf{(C) }36}$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
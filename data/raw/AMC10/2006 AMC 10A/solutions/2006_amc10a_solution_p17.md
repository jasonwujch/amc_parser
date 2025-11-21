# 2006 AMC 10A Problem 17

## Problem

In rectangle $ADEH$ , points $B$ and $C$ trisect $\overline{AD}$ , and points $G$ and $F$ trisect $\overline{HE}$ . In addition, $AH=AC=2$ , and $AD=3$ . What is the area of quadrilateral $WXYZ$ shown in the figure?

[asy] size(7cm); pathpen = linewidth(0.7); pointpen = black; pointfontpen = fontsize(10); pair A,B,C,D,E,F,G,H,W,X,Y,Z; A=(0,2); B=(1,2); C=(2,2); D=(3,2); H=(0,0); G=(1,0); F=(2,0); E=(3,0); D('A',A, N); D('B',B,N); D('C',C,N); D('D',D,N); D('E',E,SE); D('F',F,SE); D('G',G,SW); D('H',H,SW); D(A--F); D(B--E); D(D--G); D(C--H); Z=IP(A--F, C--H); Y=IP(A--F, D--G); X=IP(B--E,D--G); W=IP(B--E,C--H); D('W',W,1.6*N); D('X',X,1.6*plain.E); D('Y',Y,1.6*S); D('Z',Z,1.6*plain.W); D(A--D--E--H--cycle); [/asy]

$\textbf{(A) } \frac{1}{2}\qquad\textbf{(B) } \frac{\sqrt{2}}{2}\qquad\textbf{(C) } \frac{\sqrt{3}}{2}\qquad\textbf{(D) } \sqrt{2} \qquad\textbf{(E) } \frac{2\sqrt{3}}{3}\qquad$

## Solution 1
By symmetry , $WXYZ$ is a square.
[asy] size(7cm); pathpen = linewidth(0.7); pointpen = black; pointfontpen = fontsize(10); pair A,B,C,D,E,F,G,H,W,X,Y,Z; A=(0,2); B=(1,2); C=(2,2); D=(3,2); H=(0,0); G=(1,0); F=(2,0); E=(3,0); D('A',A, N); D('B',B,N); D('C',C,N); D('D',D,N); D('E',E,SE); D('F',F,SE); D('G',G,SW); D('H',H,SW); D(A--F); D(B--E); D(D--G); D(C--H); Z=IP(A--F, C--H); Y=IP(A--F, D--G); X=IP(B--E,D--G); W=IP(B--E,C--H); D('W',W,1.6*N); D('X',X,1.6*plain.E); D('Y',Y,1.6*S); D('Z',Z,1.6*plain.W); MP("1",(A+B)/2,2*N); MP("2",(A+H)/2,plain.W); D(B--Z); MP("1",(B+Z)/2,plain.W); MP("\frac{\sqrt{2}}{2}",(W+Z)/2,plain.SE); D(A--D--E--H--cycle); [/asy]
Draw $\overline{BZ}$ . $BZ = \frac 12AH = 1$ , so $\triangle BWZ$ is a $45-45-90 \triangle$ . Hence $WZ = \frac{1}{\sqrt{2}}$ , and $[WXYZ] = \left(\frac{1}{\sqrt{2}}\right)^2 =\boxed{\textbf{(A) }\frac 12}$ .
There are many different similar ways to come to the same conclusion using different 45-45-90 triangles .

## Solution 2
[asy] size(7cm); pathpen = linewidth(0.7); pointpen = black; pointfontpen = fontsize(10); pair A,B,C,D,E,F,G,H,W,X,Y,Z; A=(0,2); B=(1,2); C=(2,2); D=(3,2); H=(0,0); G=(1,0); F=(2,0); E=(3,0); D('A',A, N); D('B',B,N); D('C',C,N); D('D',D,N); D('E',E,SE); D('F',F,SE); D('G',G,SW); D('H',H,SW); D(A--F); D(B--E); D(D--G); D(C--H); Z=IP(A--F, C--H); Y=IP(A--F, D--G); X=IP(B--E,D--G); W=IP(B--E,C--H); D('W',W,1.6*N); D('X',X,1.6*plain.E); D('Y',Y,1.6*S); D('Z',Z,1.6*plain.W); D(B--D((A+H)/2)--G);D(C--D((E+D)/2)--F); D(A--D--E--H--cycle); [/asy]
Drawing lines as shown above and piecing together the triangles, we see that $ABCD$ is made up of $12$ squares congruent to $WXYZ$ . Hence $[WXYZ] = \frac{2\cdot 3}{12} =\boxed{\textbf{(A) }\frac 12}$ .

## Solution 3
We see that if we draw a line to $BZ$ it is half the width of the rectangle so that length would be $1$ , and the resulting triangle is a $45-45-90$ so using the Pythagorean Theorem we can get that each side is $\sqrt{\frac{1^2}{2}}$ so the area of the middle square would be $(\sqrt{\frac{1^2}{2}})^2=(\sqrt{\frac{1}{2}})^2=\boxed{\textbf{(A) }\frac{1}{2}}$ which is our answer.

## Solution 4
Since $B$ and $C$ are trisection points and $AC = 2$ , we see that $AD = 3$ . Also, $AC = AH$ , so triangle $ACH$ is a right isosceles triangle, i.e. $\angle ACH = \angle AHC = 45^\circ$ . By symmetry, triangles $AFH$ , $DEG$ , and $BED$ are also right isosceles triangles. Therefore, $\angle WAD = \angle WDA = 45^\circ$ , which means triangle $AWD$ is also a right isosceles triangle. Also, triangle $AXC$ is a right isosceles triangle.
Then $AW = AD/\sqrt{2} = 3/\sqrt{2}$ , and $AX = AC/\sqrt{2} = 2/\sqrt{2}$ . Hence, $XW = AW - AX = 3/\sqrt{2} - 2/\sqrt{2} = 1/\sqrt{2}$ .
By symmetry, quadrilateral $WXYZ$ is a square, so its area is \[XW^2 = \left( \frac{1}{\sqrt{2}} \right)^2 = \boxed{\textbf{(A) }\frac{1}{2}}.\]
~made by AoPS (somewhere) -put here by qkddud~

## Solution 5 (Proof Bash)
[asy] size(7cm); pathpen = linewidth(0.7); pointpen = black; pointfontpen = fontsize(10); pair A,B,C,D,E,F,G,H,W,X,Y,Z; A=(0,2); B=(1,2); C=(2,2); D=(3,2); H=(0,0); G=(1,0); F=(2,0); E=(3,0); D('A',A, N); D('B',B,N); D('C',C,N); D('D',D,N); D('E',E,SE); D('F',F,SE); D('G',G,SW); D('H',H,SW); D(A--F); D(B--E); D(D--G); D(C--H); Z=IP(A--F, C--H); Y=IP(A--F, D--G); X=IP(B--E,D--G); W=IP(B--E,C--H); D('W',W,1.6*N); D('X',X,1.6*plain.E); D('Y',Y,1.6*S); D('Z',Z,1.6*plain.W); D(A--D--E--H--cycle); [/asy]
By symmetry, quadrilateral $WXYZ$ is a square.
First step, proving that $\triangle BXD \sim \triangle BWC$ .
We can tell quadrilateral $CDGH$ is a parallelogram because $CD \parallel GH$ and $CD \cong GH$ .
By knowing that, we can say that $CW \parallel DX$ .
Finally, we can now prove $\triangle BXD \sim \triangle BWC$ by AA, with a ratio of 2:1.
Since $BD = DE = 2$ and $\angle BDE = 90$ . Then $\triangle BDE$ is a 45-45-90 triangle.
This will make $\angle DBE = 45$ making $\triangle BXD$ and $\triangle BWC$ a 45-45-90 triangle.
This will make, $BD = 2, BC=1, DX=BX=\sqrt 2, BW=WX=\frac{\sqrt 2}{2}$ . Since $WX$ is the length of the square, our answer will be $(\frac{\sqrt 2}{2})^2 = \frac{2}{4} = \boxed{\textbf{(A) }\frac{1}{2}}.$
~ghfhgvghj10

## Solution 6 (Educated guess)
Since we know that quadrilateral $WXYZ$ is a square, we conclude that its area is a rational number because the side lengths may be irrational. Therefore, the answer is $\boxed{\textbf(A)}.$ ~elpianista227
Note: elpianista227 forgot to account for the fact that it isn't directly stated in the problem that $WXYZ$ is a square. Also, even if we were to say that $WXYZ$ is a square the side lengths could be some variation of $x$ $+$ $\sqrt{y}$ . MisW ( talk )

## Video Solution by the Beauty of Math
https://www.youtube.com/watch?v=GX33rxlJz7s
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
# 2022 AMC 8 Problem 24

## Problem

The figure below shows a polygon $ABCDEFGH$ , consisting of rectangles and right triangles. When cut out and folded on the dotted lines, the polygon forms a triangular prism. Suppose that $AH = EF = 8$ and $GH = 14$ . What is the volume of the prism?

[asy] usepackage("mathptmx"); size(275); defaultpen(linewidth(0.8)); real r = 2, s = 2.5, theta = 14; pair G = (0,0), F = (r,0), C = (r,s), B = (0,s), M = (C+F)/2, I = M + s/2 * dir(-theta); pair N = (B+G)/2, J = N + s/2 * dir(180+theta); pair E = F + r * dir(- 45 - theta/2), D = I+E-F; pair H = J + r * dir(135 + theta/2), A = B+H-J; draw(A--B--C--I--D--E--F--G--J--H--cycle^^rightanglemark(F,I,C)^^rightanglemark(G,J,B)); draw(J--B--G^^C--F--I,linetype ("4 4")); dot("$A$",A,N); dot("$B$",B,1.2*N); dot("$C$",C,N); dot("$D$",D,dir(0)); dot("$E$",E,S); dot("$F$",F,1.5*dir(-100)); dot("$G$",G,S); dot("$H$",H,W); dot("$I$",I,NE); dot("$J$",J,1.5*S); [/asy]

$\textbf{(A)} ~112\qquad\textbf{(B)} ~128\qquad\textbf{(C)} ~192\qquad\textbf{(D)} ~240\qquad\textbf{(E)} ~288$

## Solution
While imagining the folding, $\overline{AB}$ goes on $\overline{BC},$ $\overline{AH}$ goes on $\overline{CI},$ and $\overline{EF}$ goes on $\overline{FG}.$ So, $BJ=CI=8$ and $FG=BC=8.$ Also, $\overline{HJ}$ becomes an edge parallel to $\overline{FG},$ so that means $HJ=8.$
Since $GH=14,$ then $JG=14-8=6.$ So, the area of $\triangle BJG$ is $\frac{8\cdot6}{2}=24.$ If we let $\triangle BJG$ be the base, then the height is $FG=8.$ So, the volume is $24\cdot8=\boxed{\textbf{(C)} ~192}.$
~aops-g5-gethsemanea2
### Remark
After folding polygon $ABCDEFGH$ on the dotted lines, we obtain the following triangular prism: [asy] /* Made by MRENTHUSIASM */ usepackage("mathptmx"); size(200); defaultpen(linewidth(0.8)); import graph3; import solids; currentprojection=orthographic((0.3,-0.3,0.3)); triple J, G, B, A, H, F; J = (0,0,0); G = (6,0,0); B = (0,8,0); A = (0,8,8); H = (0,0,8); F = (6,0,8); draw(surface(B--J--G--cycle),yellow); draw(surface(H--A--F--cycle),yellow); draw(B--J,dashed); draw(G--J--H--A--B^^A--F--H^^F--G^^B--G); draw((0.5,0,0)--(0.5,0.5,0)--(0,0.5,0)^^(0.5,0,8)--(0.5,0.5,8)--(0,0.5,8)); dot("$A=C$",A,1.5*E); dot("$B$",B,1.5*E); dot("$D=J$",J,1.5*W); dot("$F$",F,1.5*E); dot("$H=I$",H,1.5*W); dot("$E=G$",G,1.5*E); label("$8$",midpoint(A--H),1.5*NW,red); label("$6$",midpoint(H--F),1.5*S,red); label("$8$",midpoint(H--J),1.5*W,red); [/asy] ~MRENTHUSIASM

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/tYWp6fcUAik?si=V8hv_zOn_zYOi9E5&t=3196
~hsnacademy

## Video Solution by Math-X (First understand the problem!!!)
https://youtu.be/oUEa7AjMF2A?si=IKVkcHgWtsS8Fmbs&t=4943
~Math-X

## Video Solution(🚀Under 2 min🚀 With color-coded folding explanation ✨)
https://youtu.be/FhQROS_83iw
~Education, the Study of Everything

## Video Solution by OmegaLearn
https://youtu.be/MOcX5BFbcwU?t=380
~ pi_is_3.14

## Video Solution
https://www.youtube.com/watch?v=2uoBPp4Kxck
~Mathematical Dexterity

## Video Solution
https://youtu.be/Ij9pAy6tQSg?t=2432
~Interstigation

## Video Solution
https://www.youtube.com/watch?v=tQecx6F1O8k
~David

## Video Solution
https://youtu.be/0orAAUaLIO0?t=469
~STEMbreezy

## Video Solution
https://youtu.be/YJceP3zGSEU
~savannahsolver

## Video Solution
https://youtu.be/_yj11gFIdw4
Please like and subscribe!

## Video Solution by Dr. David
https://youtu.be/875-9AwdJsI
### See Also
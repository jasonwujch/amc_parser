# 2011 AMC 8 Problem 20

## Problem

Quadrilateral $ABCD$ is a trapezoid, $AD = 15$ , $AB = 50$ , $BC = 20$ , and the altitude is $12$ . What is the area of the trapezoid?

[asy] pair A,B,C,D; A=(3,20); B=(35,20); C=(47,0); D=(0,0); draw(A--B--C--D--cycle); dot((0,0)); dot((3,20)); dot((35,20)); dot((47,0)); label("A",A,N); label("B",B,N); label("C",C,S); label("D",D,S); draw((19,20)--(19,0)); dot((19,20)); dot((19,0)); draw((19,3)--(22,3)--(22,0)); label("12",(21,10),E); label("50",(19,22),N); label("15",(1,10),W); label("20",(41,12),E);[/asy]

$\textbf{(A) }600\qquad\textbf{(B) }650\qquad\textbf{(C) }700\qquad\textbf{(D) }750\qquad\textbf{(E) }800$

## Solution
[asy] unitsize(1.5mm); defaultpen(linewidth(.9pt)+fontsize(10pt)); dotfactor=3; pair A,B,C,D,X,Y; A=(9,12); B=(59,12); C=(75,0); D=(0,0); X=(9,0); Y=(59,0); draw(A--B--C--D--cycle); draw(A--X); draw(B--Y); pair[] ps={A,B,C,D,X,Y}; dot(ps); label("$A$",A,NW); label("$B$",B,NE); label("$C$",C,SE); label("$D$",D,SW); label("$X$",X,SE); label("$Y$",Y,S); label("$a$",D--X,S); label("$b$",Y--C,S); label("$15$",D--A,NW); label("$50$",B--A,N); label("$20$",B--C,NE); label("$12$",X--A,E); label("$12$",Y--B,W); [/asy]
If you draw altitudes from $A$ and $B$ to $CD,$ the trapezoid will be divided into two right triangles and a rectangle. You can find the values of $a$ and $b$ with the Pythagorean theorem .
\[a=\sqrt{15^2-12^2}=\sqrt{81}=9\]
\[b=\sqrt{20^2-12^2}=\sqrt{256}=16\]
$ABYX$ is a rectangle so $XY=AB=50.$
\[CD=a+XY+b=9+50+16=75\]
The area of the trapezoid is
\[12\cdot \frac{(50+75)}{2} = 6(125) = \boxed{\textbf{(D)}\ 750}\]

## Video Solution by OmegaLearn
https://youtu.be/51K3uCzntWs?t=2521
~ pi_is_3.14

## Video Solution by WhyMath
https://youtu.be/MjxiQ9MZiHk
~savannahsolver
### See Also
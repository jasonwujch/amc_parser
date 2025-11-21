# 2014 AMC 10A Problem 23

## Problem

A rectangular piece of paper whose length is $\sqrt3$ times the width has area $A$ . The paper is divided into three equal sections along the opposite lengths, and then a dotted line is drawn from the first divider to the second divider on the opposite side as shown. The paper is then folded flat along this dotted line to create a new shape with area $B$ . What is the ratio $\frac{B}{A}$ ?

[asy] import graph; size(6cm); real L = 0.05; pair A = (0,0); pair B = (sqrt(3),0); pair C = (sqrt(3),1); pair D = (0,1); pair X1 = (sqrt(3)/3,0); pair X2= (2*sqrt(3)/3,0); pair Y1 = (2*sqrt(3)/3,1); pair Y2 = (sqrt(3)/3,1); dot(X1); dot(Y1); draw(A--B--C--D--cycle, linewidth(2)); draw(X1--Y1,dashed); draw(X2--(2*sqrt(3)/3,L)); draw(Y2--(sqrt(3)/3,1-L)); [/asy]

$\textbf{(A)}\ \frac{1}{2}\qquad\textbf{(B)}\ \frac{3}{5}\qquad\textbf{(C)}\ \frac{2}{3}\qquad\textbf{(D)}\ \frac{3}{4}\qquad\textbf{(E)}\ \frac{4}{5}$

## Solution 1
Find the midpoint of the dotted line. Draw a line perpendicular to it. From the point this line intersects the top of the paper, draw lines to each endpoint of the dotted line. These two lines plus the dotted line form a triangle which is the double-layered portion of the folded paper. WLOG, assume the width of the paper is $1$ and the length is $\sqrt{3}$ . The triangle we want to find has side lengths $\dfrac{2\sqrt{3}}{3}$ , $\sqrt{\left(\dfrac{\sqrt{3}}{3}\right)^{2}+1}=\dfrac{2\sqrt{3}}{3}$ , and $\sqrt{\left(\dfrac{\sqrt{3}}{3}\right)^{2}+1}=\dfrac{2\sqrt{3}}{3}$ . It is an equilateral triangle with height $\dfrac{\sqrt{3}}{3}\cdot\sqrt{3}=1$ , and area $\dfrac{\dfrac{2\sqrt{3}}{3}\cdot1}{2}=\dfrac{\sqrt{3}}{3}$ . The area of the paper is $1\cdot\sqrt{3}=\sqrt{3}$ , and the folded paper has area $\sqrt{3}-\dfrac{\sqrt{3}}{3}=\dfrac{2\sqrt{3}}{3}$ . The ratio of the area of the folded paper to that of the original paper is thus $\boxed{\textbf{(C)} \: 2:3}$
[asy]import graph; unitsize(3cm); real L = 0.05; pair A = (0,0); pair B = (sqrt(3),0); pair C = (sqrt(3),1); pair D = (0,1); pair X1 = (sqrt(3)/3,0); pair X2= (2*sqrt(3)/3,0); pair Y1 = (2*sqrt(3)/3,1); pair Y2 = (sqrt(3)/3,1); dot(X1); dot(Y1); draw(A--B--C--D--cycle, linewidth(2)); draw(B--D,dashed); draw(X1--Y1,dashed); draw(Y2--X1--D, dotted); draw(X2--Y1--B, dotted);[/asy]

## Solution 2: FASTEST SOLUTION!!!
Our original paper can be divided like this: [asy] import graph; unitsize(3cm); real L = 0.05; pair A = (0,0); pair B = (sqrt(3),0); pair C = (sqrt(3),1); pair D = (0,1); pair X1 = (sqrt(3)/3,0); pair X2= (2*sqrt(3)/3,0); pair Y1 = (2*sqrt(3)/3,1); pair Y2 = (sqrt(3)/3,1); dot(X1); dot(Y1); draw(A--B--C--D--cycle, linewidth(2)); draw(X1--Y1,dashed); draw(Y2--X1--D, dotted); draw(X2--Y1--B, dotted);[/asy] After the fold across the dashed line, our paper becomes:
[asy] import graph; unitsize(3cm); real L = 0.05; pair A = (0,0); pair D = (0,1); pair X1 = (sqrt(3)/3,0); pair X2 = (sqrt(3)/6,0.5); pair Y1 = (2*sqrt(3)/3,1); pair Y2 = (sqrt(3)/3,1); pair Z1 = (sqrt(3)/2,1.5); dot(X1); dot(Y1); draw(X1--A--D--Z1--Y1, linewidth(2)); draw(X1--D--Y1); draw(X1--Y1, dashed); draw(Y2--X1,dotted); draw(X2--((sqrt(3)/6 + L/sqrt(3)),(0.5+L/2))); draw(Y2--(sqrt(3)/3,1-L));[/asy] Since our original sheet of paper has six congruent $30-60-90$ triangles and and our new one has four, the ratio of the area $B:A$ is equal to $4:6\implies \boxed{\textbf{(C)} \: 2:3}$
~CHECKMATE2021
### Construction
you could also use your compass to draw a 30 degree angle, make the rectangle, rip it out, and fold it.

## Video Solution by Pi Academy
https://youtu.be/ql_90z1m8Qs?si=D8nF9MULxipqoxmc ~ Pi Academy

## Video Solution by Richard Rusczyk
https://artofproblemsolving.com/videos/amc/2014amc10a/377
~ ripkobe_745
https://youtu.be/jYRA3thX4pI
~suprboygamer_jimpop(direct youtube link)
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
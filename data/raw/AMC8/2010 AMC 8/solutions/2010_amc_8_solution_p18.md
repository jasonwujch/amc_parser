# 2010 AMC 8 Problem 18

## Problem

A decorative window is made up of a rectangle with semicircles at either end. The ratio of $AD$ to $AB$ is $3:2$ . And $AB$ is 30 inches. What is the ratio of the area of the rectangle to the combined area of the semicircles?

[asy] import graph; size(5cm); real lsf=0; pen dps=linewidth(0.7)+fontsize(8); defaultpen(dps); pen ds=black; real xmin=-4.27,xmax=14.73,ymin=-3.22,ymax=6.8; draw((0,4)--(0,0)); draw((0,0)--(2.5,0)); draw((2.5,0)--(2.5,4)); draw((2.5,4)--(0,4)); draw(shift((1.25,4))*xscale(1.25)*yscale(1.25)*arc((0,0),1,0,180)); draw(shift((1.25,0))*xscale(1.25)*yscale(1.25)*arc((0,0),1,-180,0)); dot((0,0),ds); label("$A$",(-0.26,-0.23),NE*lsf); dot((2.5,0),ds); label("$B$",(2.61,-0.26),NE*lsf); dot((0,4),ds); label("$D$",(-0.26,4.02),NE*lsf); dot((2.5,4),ds); label("$C$",(2.64,3.98),NE*lsf); clip((xmin,ymin)--(xmin,ymax)--(xmax,ymax)--(xmax,ymin)--cycle);[/asy]

$\textbf{(A)}\ 2:3\qquad\textbf{(B)}\ 3:2\qquad\textbf{(C)}\ 6:\pi\qquad\textbf{(D)}\ 9:\pi\qquad\textbf{(E)}\ 30 :\pi$

## Solution 1
We can set a proportion:
\[\dfrac{AD}{AB}=\dfrac{3}{2}\]
We substitute $AB$ with 30 and solve for $AD$ .
\[\dfrac{AD}{30}=\dfrac{3}{2}\]
\[AD=45\]
We calculate the combined area of semicircle by putting together semicircle $AB$ and $CD$ to get a circle with radius $15$ . Thus, the area is $225\pi$ . The area of the rectangle is $30\cdot 45=1350$ . We calculate the ratio:
\[\dfrac{1350}{225\pi}=\dfrac{6}{\pi}\Rightarrow\boxed{\textbf{(C)}\ 6:\pi}\]

## Solution 2 (more efficient)
We can solve this without the measurement of $30$ inches. Let the constant of proportionality between the sides of the rectangle be $k$ . $\frac{A_{rect}}{A_{circle}}=\frac{3k*2k}{\pi(\frac{2k}{2})^2}=\frac{6k^2}{\pi k^2}=\frac{6}{\pi}\Rightarrow\boxed{\textbf{(C)}\ 6:\pi}$

## Video Solution by OmegaLearn
https://youtu.be/j3QSD5eDpzU?t=657
~ pi_is_3.14
### Video by MathTalks
https://www.youtube.com/watch?v=KSYVsSJDX-0&feature=youtu.be

## Video Solution by WhyMath
https://youtu.be/zoWJrxTCYPM
~savannahsolver
### See Also
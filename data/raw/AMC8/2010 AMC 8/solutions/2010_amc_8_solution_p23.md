# 2010 AMC 8 Problem 23

## Problem

Semicircles $POQ$ and $ROS$ pass through the center $O$ . What is the ratio of the combined areas of the two semicircles to the area of circle $O$ ?

[asy] import graph; size(7.5cm); real lsf=0.5; pen dps=linewidth(0.7)+fontsize(10); defaultpen(dps); pen ds=black; real xmin=-6.27,xmax=10.01,ymin=-5.65,ymax=10.98; draw(circle((0,0),2)); draw((-3,0)--(3,0),EndArrow(6)); draw((0,-3)--(0,3),EndArrow(6)); draw(shift((0.01,1.42))*xscale(1.41)*yscale(1.41)*arc((0,0),1,179.76,359.76)); draw(shift((-0.01,-1.42))*xscale(1.41)*yscale(1.41)*arc((0,0),1,-0.38,179.62)); draw((-1.4,1.43)--(1.41,1.41)); draw((-1.42,-1.41)--(1.4,-1.42)); label("$ P(-1,1) $",(-2.57,2.17),SE*lsf); label("$ Q(1,1) $",(1.55,2.21),SE*lsf); label("$ R(-1,-1) $",(-2.72,-1.45),SE*lsf); label("$S(1,-1)$",(1.59,-1.49),SE*lsf); dot((0,0),ds); label("$O$",(-0.24,-0.35),NE*lsf); dot((1.41,1.41),ds); dot((-1.4,1.43),ds); dot((1.4,-1.42),ds); dot((-1.42,-1.41),ds); clip((xmin,ymin)--(xmin,ymax)--(xmax,ymax)--(xmax,ymin)--cycle);[/asy]

$\textbf{(A)}\ \frac{\sqrt 2}{4}\qquad\textbf{(B)}\ \frac{1}{2}\qquad\textbf{(C)}\ \frac{2}{\pi}\qquad\textbf{(D)}\ \frac{2}{3}\qquad\textbf{(E)}\ \frac{\sqrt 2}{2}$

## Solution
By the Pythagorean Theorem, the radius of the larger circle turns out to be $\sqrt{1^2 + 1^2} = \sqrt{2}$ . Therefore, the area of the larger circle is $(\sqrt{2})^2\pi = 2\pi$ . Using the coordinate plane given, we find that the radius of each of the two semicircles to be 1. So, the area of the two semicircles is $1^2\pi=\pi$ . Finally, the ratio of the combined areas of the two semicircles to the area of circle $O$ is $\boxed{\textbf{(B)}\ \frac{1}{2}}$ .

## Video Solution by OmegaLearn
https://youtu.be/abSgjn4Qs34?t=903
~ pi_is_3.14

## Video Solution by MathTalks
https://youtu.be/mSCQzmfdX-g

## Video Solution by WhyMath
https://youtu.be/yBpbVpoVUXI
~savannahsolver
### See Also
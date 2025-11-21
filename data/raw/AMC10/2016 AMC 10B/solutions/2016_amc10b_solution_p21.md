# 2016 AMC 10B Problem 21

## Problem

What is the area of the region enclosed by the graph of the equation $x^2+y^2=|x|+|y|?$

$\textbf{(A)}\ \pi+\sqrt{2}\qquad\textbf{(B)}\ \pi+2\qquad\textbf{(C)}\ \pi+2\sqrt{2}\qquad\textbf{(D)}\ 2\pi+\sqrt{2}\qquad\textbf{(E)}\ 2\pi+2\sqrt{2}$

## Solution 1
Without loss of generality (WLOG) note that if a point in the first quadrant satisfies the equation, so do its corresponding points in the other three quadrants. Therefore, we can assume that $x, y \ge 0$ , which implies that $|x|=x$ and $|y|=y$ , and multiply by $4$ at the end.
We can rearrange the equation to get $x^2-x+y^2-y=0 \Rightarrow (x-\tfrac12)^2+(y-\tfrac12)^2=(\tfrac{\sqrt2}{2})^2$ , which describes a circle with center $(\tfrac12, \tfrac12)$ and radius $\tfrac{\sqrt2}{2}.$ It's clear we now want to find the union of four equal areas.
[asy]draw((0,-1.5)--(0,1.5),EndArrow);draw((-1.5,0)--(1.5,0),EndArrow);draw((0,1)--(1,0)--(0,-1)--(-1,0)--cycle,dotted); for(int i=0;i<4;++i){draw(rotate(i*90,(0,0))*arc((1/2,1/2),sqrt(1/2),-45,135));dot(rotate(i*90,(0,0))*(1/2,1/2));}[/asy] There are several ways to find the area, but note that if you connect $(0, 1)$ to its other three respective points in the other three quadrants, you get a square of area $2$ , along with four half-circles of diameter $\sqrt{2}$ , for a total area of $2+2\cdot(\tfrac{\sqrt2}{2})^2\pi = \pi + 2$ which is $\boxed{\textbf{(B)}}$ .

## Solution 2
Another way to solve this problem is using cases. Though this may seem tedious, we only have to do one case since the area enclosed is symmetrical. The equation for this figure is $x^2+y^2=|x|+|y|$ To make this as easy as possible, we can make both $x$ and $y$ positive. Simplifying the equation for $x$ and $y$ being positive, we get the equation $x^{2} +y^{2} -x-y = 0.$
Using the complete the square method, we get $\left(x-\frac{1}{2}\right)^{2} + \left(y-\frac{1}{2}\right)^{2}=\frac{1}{2}$
Therefore, the origin of this section of the shape is at $\left(\frac{1}{2}, \frac{1}{2}\right).$
Using the equation we can also see that the radius has a length of $\frac{\sqrt{2}}{2}$ .
With this shape we see that this shape can be cut into a right triangle and a semicircle. The length of the hypotenuse of the triangle is $\sqrt{2}$ so using special right triangles, we see that the area of the triangle is $\frac{1}{2}$ . The semicircle has the area of $\frac{1}{4}\pi$ .
But this is only $1$ case. There are $4$ cases in total so we have to multiply $\frac{1}{2}+\frac{1}{4}\pi$ by $4$ .
After multiplying, our answer is: \[\boxed{\textbf{(B)} \pi+2}.\]

## Solution 3: Analytic geometry
We solve with cases. The cases are: Case 1: $x\geq0, y\geq0.$ Case 2: $x\geq0, y<0.$ Case 3: $x<0, y\geq0.$ Case 4: $x<0, y<0.$
We can quickly realize that the whole figure is symmetrical; so when you figure out the first case, you get the first part is $\left(x-\dfrac12\right)^2+\left(x-\dfrac12\right)^2$ you can figure out the whole figure: (scaled 8x). [asy] size(400); import TrigMacros; rr_cartesian_axes(-10,10,-10,10,complexplane=false, usegrid = true); draw(circle((4,4), 4*1.41421356237)); draw(circle((4,-4), 4*1.41421356237)); draw(circle((-4,4), 4*1.41421356237)); draw(circle((-4,-4), 4*1.41421356237)); [/asy] The way we figure out the area is by splitting it the following way: [asy] size(400); import TrigMacros; rr_cartesian_axes(-10,10,-10,10,complexplane=false, usegrid = true); draw(circle((4,4), 4*1.41421356237)); draw(circle((4,-4), 4*1.41421356237)); draw(circle((-4,4), 4*1.41421356237)); draw(circle((-4,-4), 4*1.41421356237)); real f(real x) { return -x+8; } draw(graph(f,0,8), red+linewidth(1.5)); real g(real x) { return x+8; } draw(graph(g,0,-8), red+linewidth(1.5)); real f(real x) { return -x+8; } draw(graph(f,0,8), red+linewidth(1.5)); real h(real x) { return -x-8; } draw(graph(h,-8,0), red+linewidth(1.5)); real z(real x) { return x-8; } draw(graph(z,0,8), red+linewidth(1.5)); pair A,B,C,D; A = (8,0); B = (0,8); C = (-8,0); D = (0,-8); fill(A--B--C--D--cycle, red); [/asy]
We know each of the red lines is a diameter of the circle which is $\sqrt2$ . So the area of the red is 2. We know that the area of each semicircle is $\dfrac14 \pi$ so the area of the semicircles combines is $\pi$ . Thus we get $\boxed{\textbf{(B)} \pi+2}.$
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
# 2021 AMC 12A Problem 19

## Problem

How many solutions does the equation $\sin \left( \frac{\pi}2 \cos x\right)=\cos \left( \frac{\pi}2 \sin x\right)$ have in the closed interval $[0,\pi]$ ?

$\textbf{(A) }0 \qquad \textbf{(B) }1 \qquad \textbf{(C) }2 \qquad \textbf{(D) }3\qquad \textbf{(E) }4$

## Solution 1 (Inverse Trigonometric Functions)
The ranges of $\frac{\pi}2 \sin x$ and $\frac{\pi}2 \cos x$ are both $\left[-\frac{\pi}2, \frac{\pi}2 \right],$ which is included in the range of $\arcsin,$ so we can use it with no issues. \begin{align*} \frac{\pi}2 \cos x &= \arcsin \left( \cos \left( \frac{\pi}2 \sin x\right)\right) \\ \frac{\pi}2 \cos x &= \arcsin \left( \sin \left( \frac{\pi}2 - \frac{\pi}2 \sin x\right)\right) \\ \frac{\pi}2 \cos x &= \frac{\pi}2 - \frac{\pi}2 \sin x \\ \cos x &= 1 - \sin x \\ \cos x + \sin x &= 1. \end{align*} This only happens at $x = 0, \frac{\pi}2$ on the interval $[0,\pi],$ because one of $\sin$ and $\cos$ must be $1$ and the other $0.$ Therefore, the answer is $\boxed{\textbf{(C) }2}.$
~Tucker

## Solution 2 (Cofunction Identity)
By the Cofunction Identity $\cos\theta=\sin\left(\frac{\pi}{2}-\theta\right),$ we rewrite the given equation: \[\sin \left(\frac{\pi}2 \cos x\right) = \sin \left(\frac{\pi}2 - \frac{\pi}2 \sin x\right).\] Recall that if $\sin\theta=\sin\phi,$ then $\theta=\phi+2n\pi$ or $\theta=\pi-\phi+2n\pi$ for some integer $n.$ Therefore, we have two cases:
1. for some integer We rearrange and simplify: By rough constraints, we know that from which The only possibility is so for some integer We get for this case. Note that is an extraneous solution by squaring
1. for some integer Similar to Case 1, we conclude that so We get for this case.
We rearrange and simplify: \[\sin x + \cos x = 1 + 4n.\] By rough constraints, we know that $-2 < \sin x + \cos x < 2,$ from which $-2 < 1 - 4n < 2.$ The only possibility is $n=0,$ so \begin{align*} \sin x + \cos x &= 1 && (*) \\ \sin^2 x + \cos^2 x + 2\sin x \cos x &= 1 \\ 2\sin x \cos x &= 0 \\ \sin(2x) &= 0 \\ 2x &= k\pi \\ x &= \frac{k\pi}{2} \end{align*} for some integer $k.$
We get $x=0,\frac{\pi}{2}$ for this case. Note that $x=\pi$ is an extraneous solution by squaring $(*).$
Similar to Case 1, we conclude that $n=0,$ so \[\cos x - \sin x = 1.\] We get $x=0$ for this case.
Together, we obtain $\boxed{\textbf{(C) }2}$ solutions: $x=0,\frac{\pi}{2}.$
~MRENTHUSIASM

## Solution 3 (Graphs and Analyses)
This problem is equivalent to counting the intersections of the graphs of $y=\sin\left(\frac{\pi}{2}\cos x\right)$ and $y=\cos\left(\frac{\pi}{2}\sin x\right)$ in the closed interval $[0,\pi].$ We construct a table of values, as shown below: \[\begin{array}{c|ccc} & & & \\ [-2ex] & \boldsymbol{x=0} & \boldsymbol{x=\frac{\pi}{2}} & \boldsymbol{x=\pi} \\ [1.5ex] \hline & & & \\ [-1ex] \boldsymbol{\cos x} & 1 & 0 & -1 \\ [1.5ex] \boldsymbol{\frac{\pi}{2}\cos x} & \frac{\pi}{2} & 0 & -\frac{\pi}{2} \\ [1.5ex] \boldsymbol{\sin\left(\frac{\pi}{2}\cos x\right)} & 1 & 0 & -1 \\ [1.5ex] \hline & & & \\ [-1ex] \boldsymbol{\sin x} & 0 & 1 & 0 \\ [1.5ex] \boldsymbol{\frac{\pi}{2}\sin x} & 0 & \frac{\pi}{2} & 0 \\ [1.5ex] \boldsymbol{\cos\left(\frac{\pi}{2}\sin x\right)} & 1 & 0 & 1 \\ [1ex] \end{array}\] For $x\in[0,\pi],$ note that:
- $\frac{\pi}{2}\cos x\in\left[-\frac{\pi}{2},\frac{\pi}{2}\right],$ so $\sin\left(\frac{\pi}{2}\cos x\right)\in[-1,1].$
- $\frac{\pi}{2}\sin x\in\left[0,\frac{\pi}{2}\right],$ so $\cos\left(\frac{\pi}{2}\sin x\right)\in[0,1].$
For the graphs to intersect, we need $\sin\left(\frac{\pi}{2}\cos x\right)\in[0,1].$ This occurs when $\frac{\pi}{2}\cos x\in\left[0,\frac{\pi}{2}\right].$
By the Cofunction Identity $\cos\theta=\sin\left(\frac{\pi}{2}-\theta\right),$ we rewrite the given equation: \[\sin\left(\frac{\pi}{2}\cos x\right) = \sin\left(\frac{\pi}{2}-\frac{\pi}{2}\sin x\right).\] Since $\frac{\pi}{2}\cos x\in\left[0,\frac{\pi}{2}\right]$ and $\frac{\pi}{2}\sin x\in\left[0,\frac{\pi}{2}\right],$ it follows that $x\in\left[0,\frac{\pi}{2}\right]$ and $\frac{\pi}{2}-\frac{\pi}{2}\sin x\in\left[0,\frac{\pi}{2}\right].$
We can apply the arcsine function to both sides, then rearrange and simplify: \begin{align*} \frac{\pi}{2}\cos x &= \frac{\pi}{2}-\frac{\pi}{2}\sin x \\ \sin x + \cos x &= 1. \end{align*} From Case 1 in Solution 2, we conclude that $(0,1)$ and $\left(\frac{\pi}{2},0\right)$ are the only points of intersection, as shown below: [asy] /* Made by MRENTHUSIASM */ size(600,200); real f(real x) { return sin(pi/2*cos(x)); } real g(real x) { return cos(pi/2*sin(x)); } draw(graph(f,0,pi),red,"$y=\sin\left(\frac{\pi}{2}\cos x\right)$"); draw(graph(g,0,pi),blue,"$y=\cos\left(\frac{\pi}{2}\sin x\right)$"); real xMin = 0; real xMax = 5/4*pi; real yMin = -2; real yMax = 2; //Draws the horizontal gridlines void horizontalLines() { for (real i = yMin+1; i < yMax; ++i) { draw((xMin,i)--(xMax,i), mediumgray+linewidth(0.4)); } } //Draws the vertical gridlines void verticalLines() { for (real i = xMin+pi/2; i < xMax; i+=pi/2) { draw((i,yMin)--(i,yMax), mediumgray+linewidth(0.4)); } } //Draws the horizontal ticks void horizontalTicks() { for (real i = yMin+1; i < yMax; ++i) { draw((-1/8,i)--(1/8,i), black+linewidth(1)); } } //Draws the vertical ticks void verticalTicks() { for (real i = xMin+pi/2; i < xMax; i+=pi/2) { draw((i,-1/8)--(i,1/8), black+linewidth(1)); } } horizontalLines(); verticalLines(); horizontalTicks(); verticalTicks(); draw((xMin,0)--(xMax,0),black+linewidth(1.5),EndArrow(5)); draw((0,yMin)--(0,yMax),black+linewidth(1.5),EndArrow(5)); label("$x$",(xMax,0),(2,0)); label("$y$",(0,yMax),(0,2)); pair A[]; A[0] = (pi/2,0); A[1] = (pi,0); A[2] = (0,1); A[3] = (0,0); A[4] = (0,-1); label("$\frac{\pi}{2}$",A[0],(0,-2.5)); label("$\pi$",A[1],(0,-2.5)); label("$1$",A[2],(-2.5,0)); label("$0$",A[3],(-2.5,0)); label("$-1$",A[4],(-2.5,0)); dot((0,1),linewidth(5)); dot((pi/2,0),linewidth(5)); add(legend(),point(E),40E,UnFill); [/asy] Therefore, the answer is $\boxed{\textbf{(C) }2}.$
~MRENTHUSIASM (credit given to TheAMCHub)

## Solution 4 (No Graphing)
For $\sin(a) = \cos(b),$ $a$ and $b$ must be complementary angles, or $a + b = \frac{\pi}{2}.$ So we have \[\frac{\pi}{2}(\sin(x) + \cos(x)) = \frac{\pi}{2} \implies \sin(x) + \cos(x) = 1.\]
We know $\sin^2(x) + \cos^2(x) = 1,$ so we can express $\cos(x)$ in terms of $\sin(x)$ and set those expressions equal to each other:
\[\sqrt{1 - \sin^2(x)} = 1 - \sin(x) \implies 1 - \sin^2(x) = (1 - \sin(x))^2 \implies \sin(x) = 1.\]
So now the problem becomes the number of values of $x$ on the interval $[0, \pi]$ such that $\sin(x) = 1$ . It's pretty easy to see that $x$ can equal $0$ or $\frac{\pi}{2},$ so the answer is $\boxed{\textbf{(C) }2}.$
~ grogg007

## Video Solution by OmegaLearn (Using Triangle Inequality & Trigonometry)
https://youtu.be/wJxN1YPuyCg
~ pi_is_3.14

## Video Solution (Quick and Easy)
https://youtu.be/6AWb9cqFblU
~Education, the Study of Everything
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
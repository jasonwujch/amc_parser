# 2021 Fall AMC 10A Problem 16

## Problem

The graph of \[f(x) = |\lfloor x \rfloor| - |\lfloor 1 - x \rfloor|\] is symmetric about which of the following? (Here $\lfloor x \rfloor$ is the greatest integer not exceeding $x$ .)

$\textbf{(A) }\text{the }y\text{-axis}\qquad \textbf{(B) }\text{the line }x = 1\qquad \textbf{(C) }\text{the origin}\qquad \textbf{(D) }\text{ the point }\left(\dfrac12, 0\right)\qquad \textbf{(E) }\text{the point }(1,0)$

## Solution 1 (Observations)
Note that \[f(1-x)=|\lfloor 1-x\rfloor|-|\lfloor x\rfloor|=-f(x),\] so $f\left(\frac12+x\right)=-f\left(\frac12-x\right)$ .
This means that the graph is symmetric about $\boxed{\textbf{(D) }\text{ the point }\left(\dfrac12, 0\right)}$ .

## Solution 2 (Graphing)
Let $y_1=|\lfloor x \rfloor|$ and $y_2=|\lfloor 1 - x \rfloor|=|\lfloor -(x-1) \rfloor|.$ Note that the graph of $y_2$ is a reflection of the graph of $y_1$ about the $y$ -axis, followed by a translation $1$ unit to the right.
The graph of $y_1$ is shown below: [asy] /* Made by MRENTHUSIASM */ size(250); int xMin = -10; int xMax = 10; int yMin = -10; int yMax = 10; //Draws the horizontal gridlines void horizontalLines() { for (int i = yMin+1; i < yMax; ++i) { draw((xMin,i)--(xMax,i), mediumgray+linewidth(0.4)); } } //Draws the vertical gridlines void verticalLines() { for (int i = xMin+1; i < xMax; ++i) { draw((i,yMin)--(i,yMax), mediumgray+linewidth(0.4)); } } //Draws the horizontal ticks void horizontalTicks() { for (int i = yMin+1; i < yMax; ++i) { draw((-3/16,i)--(3/16,i), black+linewidth(1)); } } //Draws the vertical ticks void verticalTicks() { for (int i = xMin+1; i < xMax; ++i) { draw((i,-3/16)--(i,3/16), black+linewidth(1)); } } //Draws and labels coordinate axes void drawLabelAxes() { draw((xMin,0)--(xMax,0),black+linewidth(1.5),EndArrow(5)); draw((0,yMin)--(0,yMax),black+linewidth(1.5),EndArrow(5)); label("$x$",(xMax,0),(2,0)); label("$y$",(0,yMax),(0,2)); } horizontalLines(); verticalLines(); horizontalTicks(); verticalTicks(); drawLabelAxes(); path P[], Q[]; for (int i = 0; i < 9; ++i) { P[i] = (i,i)--(i+1,i); Q[i] = (-i,i+1)--(-i-1,i+1); } draw(P^^Q,red+linewidth(1.25)); for (int i = 0; i < 9; ++i) { dot((i,i),red+linewidth(4)); dot((i+1,i),red+linewidth(0.7),UnFill); dot((-i-1,i+1),red+linewidth(4)); dot((-i,i+1),red+linewidth(0.7),UnFill); } [/asy] The graph of $y_2$ is shown below: [asy] /* Made by MRENTHUSIASM */ size(250); int xMin = -10; int xMax = 10; int yMin = -10; int yMax = 10; //Draws the horizontal gridlines void horizontalLines() { for (int i = yMin+1; i < yMax; ++i) { draw((xMin,i)--(xMax,i), mediumgray+linewidth(0.4)); } } //Draws the vertical gridlines void verticalLines() { for (int i = xMin+1; i < xMax; ++i) { draw((i,yMin)--(i,yMax), mediumgray+linewidth(0.4)); } } //Draws the horizontal ticks void horizontalTicks() { for (int i = yMin+1; i < yMax; ++i) { draw((-3/16,i)--(3/16,i), black+linewidth(1)); } } //Draws the vertical ticks void verticalTicks() { for (int i = xMin+1; i < xMax; ++i) { draw((i,-3/16)--(i,3/16), black+linewidth(1)); } } //Draws and labels coordinate axes void drawLabelAxes() { draw((xMin,0)--(xMax,0),black+linewidth(1.5),EndArrow(5)); draw((0,yMin)--(0,yMax),black+linewidth(1.5),EndArrow(5)); label("$x$",(xMax,0),(2,0)); label("$y$",(0,yMax),(0,2)); } horizontalLines(); verticalLines(); horizontalTicks(); verticalTicks(); drawLabelAxes(); path P[], Q[]; for (int i = 0; i < 9; ++i) { P[i] = (i,i)--(i+1,i); Q[i] = (-i,i+1)--(-i-1,i+1); } draw(P^^Q,heavygreen+linewidth(1.25)); for (int i = 0; i < 9; ++i) { dot((i,i),heavygreen+linewidth(0.7),UnFill); dot((i+1,i),heavygreen+linewidth(4)); dot((-i-1,i+1),heavygreen+linewidth(0.7),UnFill); dot((-i,i+1),heavygreen+linewidth(4)); } [/asy] The graph of $f(x)=y_1-y_2$ is shown below: [asy] /* Made by MRENTHUSIASM */ size(250); int xMin = -10; int xMax = 10; int yMin = -10; int yMax = 10; //Draws the horizontal gridlines void horizontalLines() { for (int i = yMin+1; i < yMax; ++i) { draw((xMin,i)--(xMax,i), mediumgray+linewidth(0.4)); } } //Draws the vertical gridlines void verticalLines() { for (int i = xMin+1; i < xMax; ++i) { draw((i,yMin)--(i,yMax), mediumgray+linewidth(0.4)); } } //Draws the horizontal ticks void horizontalTicks() { for (int i = yMin+1; i < yMax; ++i) { draw((-3/16,i)--(3/16,i), black+linewidth(1)); } } //Draws the vertical ticks void verticalTicks() { for (int i = xMin+1; i < xMax; ++i) { draw((i,-3/16)--(i,3/16), black+linewidth(1)); } } //Draws and labels coordinate axes void drawLabelAxes() { draw((xMin,0)--(xMax,0),black+linewidth(1.5),EndArrow(5)); draw((0,yMin)--(0,yMax),black+linewidth(1.5),EndArrow(5)); label("$x$",(xMax,0),(2,0)); label("$y$",(0,yMax),(0,2)); } horizontalLines(); verticalLines(); horizontalTicks(); verticalTicks(); drawLabelAxes(); draw((-10,0)--(10,0),mediumblue+linewidth(1.25),"$y=|\lfloor x \rfloor|$"); for (int i = 0; i > -10; --i) { dot((i,-1),mediumblue+linewidth(4)); } for (int i = 1; i < 10; ++i) { dot((i,1),mediumblue+linewidth(4)); } for (int i = -9; i < 10; ++i) { dot((i,0),mediumblue+linewidth(0.7),UnFill); } [/asy]
Therefore, the graph of $f(x)$ is symmetric about $\boxed{\textbf{(D) }\text{ the point }\left(\dfrac12, 0\right)}.$
~MRENTHUSIASM

## Solution 3 (Casework)
For all $x\in\mathbb{R}$ and $n\in\mathbb{Z},$ note that:
1. $\lfloor x+n \rfloor = \lfloor x \rfloor + n$ and $\lceil x+n \rceil = \lceil x \rceil + n$
1. $\lfloor -x \rfloor = -\lceil x \rceil$
1. $\lceil x \rceil - \lfloor x \rfloor = \begin{cases} 0 & \mathrm{if} \ x\in\mathbb{Z} \\ 1 & \mathrm{if} \ x\not\in\mathbb{Z} \end{cases}$
We rewrite $f(x)$ as \begin{align*} f(x) &= |\lfloor x \rfloor| - |\lfloor 1 - x \rfloor| \\ &= |\lfloor x \rfloor| - |-\lceil x - 1 \rceil| \\ &= |\lfloor x \rfloor| - |-\lceil x \rceil + 1|. \end{align*} We apply casework to the value of $x:$
1. $x\in\mathbb{Z}^-$
1. $x=0$
1. $x\in\mathbb{Z}^+$
1. $x\not\in\mathbb{Z}$ and $x<0$
1. $x\not\in\mathbb{Z}$ and $0<x<1$
1. $x\not\in\mathbb{Z}$ and $x>1$
It follows that $f(x)=-x-(-x+1)=-1.$
It follows that $f(x)=0-1=-1.$
It follows that $f(x)=x-(x-1)=1.$
It follows that $f(x)=-\lfloor x \rfloor - (-\lceil x\rceil+1)=(\lceil x \rceil - \lfloor x \rfloor)-1=0.$
It follows that $f(x)=0-0=0.$
It follows that $f(x)=\lfloor x \rfloor - (\lceil x\rceil-1)=(\lfloor x \rfloor - \lceil x \rceil)+1=0.$
Together, we have \[f(x)=\begin{cases} -1 & \mathrm{if} \ x\in\mathbb{Z}^{-}\cup\{0\} \\ 1 & \mathrm{if} \ x\in\mathbb{Z}^{+} \\ 0 & \mathrm{if} \ x\not\in\mathbb{Z} \end{cases},\] so the graph of $f(x)$ is symmetric about $\boxed{\textbf{(D) }\text{ the point }\left(\dfrac12, 0\right)}.$
Alternatively, we can eliminate $\textbf{(A)}, \textbf{(B)}, \textbf{(C)},$ and $\textbf{(E)}$ once we finish with Case 3. This leaves us with $\textbf{(D)}.$
~MRENTHUSIASM

## Solution 4 (Casework)
Denote $x = a + b$ , where $a \in \Bbb Z$ and $b \in \left[ 0 , 1 \right)$ . Hence, $a$ is the integer part of $x$ and $b$ is the decimal part of $x$ .
Case 1 : $b = 0$ .
We have \begin{align*} f \left( x \right) & = \left| \lfloor x \rfloor \right| - \left| \lfloor 1 - x \rfloor \right| \\ & = | a | - | 1 - a | \\ & = \left\{ \begin{array}{ll} a - \left( a - 1 \right) & \mbox{ if } a \in \Bbb Z \mbox{ and } a \geq 1 \\ -1 & \mbox{ if } a = 0 \\ - a - \left( 1 - a \right) & \mbox{ if } a \in \Bbb Z \mbox{ and } a \leq -1 \end{array} \right. \\ & = \left\{ \begin{array}{ll} 1 & \mbox{ if } a \in \Bbb Z \mbox{ and } a \geq 1 \\ -1 & \mbox{ if } a = 0 \\ -1 & \mbox{ if } a \in \Bbb Z \mbox{ and } a \leq -1 \end{array} \right. \\ & = \left\{ \begin{array}{ll} 1 & \mbox{ if } a \in \Bbb Z \mbox{ and } a \geq 1 \\ -1 & \mbox{ if } a \in \Bbb Z \mbox{ and } a \leq 0 \end{array} \right. \end{align*}
Case 2 : $b \neq 0$ .
We have \begin{align*} f \left( x \right) & = \left| \lfloor x \rfloor \right| - \left| \lfloor 1 - x \rfloor \right| \\ & = | a | - | \lfloor 1 - a - b \rfloor | \\ & = | a | - | \lfloor - a + \left( 1 - b \right) \rfloor | \\ & = | a | - | - a | \\ & = 0 . \end{align*}
Therefore, the graph of $f \left( x \right)$ is symmetric through the point $\left( \frac{1}{2} , 0 \right)$ .
Therefore, the answer is $\boxed{\textbf{(D) }\text{ the point }\left(\dfrac12, 0\right)}$ .
~Steven Chen (www.professorchenedu.com)

## Solution 5 (Semi-Fakesolve)
Suppose $x\in \mathbb{Z},$ making the equation equivalent to $f(x) = |x|-|1-x|.$ We consider the cases when $x\in (-\infty, 0), 0, 1, (1, \infty).$
If $x\in (-\infty, 0)$ , we have $|x| = -x$ and $|1-x| = 1-x,$ so $f(x) = -x - (1-x) = -1$ .
If $x = 0$ or $x = 1$ , we trivially get $f(x) = -1$ and $1$ respectively.
If $x\in (1, \infty)$ , we have $|x| = x$ and $|1-x| = x - 1$ , giving $f(x) = x-(x-1)= 1.$
Since, for all $x\in \mathbb{Z} \leq 0$ , $f(x) =-1$ and $x\in \mathbb{Z} \geq 1, f(x) = 1$ , we can conclude that it is symmetric across the coordinate pair \[\left(\frac{0 + 1}{2}, \frac{-1 + 1}{2}\right) = \boxed{\textbf{(D)}\ \left(\frac{1}{2}, 0\right)},\] the midpoint of the "endpoints" of these line segments.
[asy] size(250); //Credit to MRENTHUSIASM int xMin = -10; int xMax = 10; int yMin = -10; int yMax = 10; //Draws the horizontal gridlines void horizontalLines() { for (int i = yMin+1; i < yMax; ++i) { draw((xMin,i)--(xMax,i), mediumgray+linewidth(0.4)); } } //Draws the vertical gridlines void verticalLines() { for (int i = xMin+1; i < xMax; ++i) { draw((i,yMin)--(i,yMax), mediumgray+linewidth(0.4)); } } //Draws the horizontal ticks void horizontalTicks() { for (int i = yMin+1; i < yMax; ++i) { draw((-3/16,i)--(3/16,i), black+linewidth(1)); } } //Draws the vertical ticks void verticalTicks() { for (int i = xMin+1; i < xMax; ++i) { draw((i,-3/16)--(i,3/16), black+linewidth(1)); } } //Draws and labels coordinate axes void drawLabelAxes() { draw((xMin,0)--(xMax,0),black+linewidth(1.5),EndArrow(5)); draw((0,yMin)--(0,yMax),black+linewidth(1.5),EndArrow(5)); label("$x$",(xMax,0),(2,0)); label("$y$",(0,yMax),(0,2)); } horizontalLines(); verticalLines(); horizontalTicks(); verticalTicks(); drawLabelAxes(); for (int i = 0; i > -10; --i) { dot((i,-1),mediumblue+linewidth(4)); } for (int i = 1; i < 10; ++i) { dot((i,1),mediumblue+linewidth(4)); } [/asy]
Just considering the integers is never a good idea when dealing with any function, especially one with floor functions. However, after dealing with the case "when $x\in \mathbb{Z}$ ", it becomes apparent that the graph of $f(x)$ is symmetric about $x = \frac{1}{2}$ , or more specifically, the point $\left(\frac{1}{2}, 0\right).$
-Benedict T (countmath1)

## Video Solution
https://youtu.be/RpxlZJRiSjk
~Education, the Study of Everything
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
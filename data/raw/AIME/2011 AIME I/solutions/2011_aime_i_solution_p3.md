# 2011 AIME I Problem 3

## Problem

Let $L$ be the line with slope $\frac{5}{12}$ that contains the point $A=(24,-1)$ , and let $M$ be the line perpendicular to line $L$ that contains the point $B=(5,6)$ . The original coordinate axes are erased, and line $L$ is made the $x$ -axis and line $M$ the $y$ -axis. In the new coordinate system, point $A$ is on the positive $x$ -axis, and point $B$ is on the positive $y$ -axis. The point $P$ with coordinates $(-14,27)$ in the original system has coordinates $(\alpha,\beta)$ in the new coordinate system. Find $\alpha+\beta$ .

## Solution
Given that $L$ has slope $\frac{5}{12}$ and contains the point $A=(24,-1)$ , we may write the point-slope equation for $L$ as $y+1=\frac{5}{12}(x-24)$ . Since $M$ is perpendicular to $L$ and contains the point $B=(5,6)$ , we have that the slope of $M$ is $-\frac{12}{5}$ , and consequently that the point-slope equation for $M$ is $y-6=-\frac{12}{5}(x-5)$ .
Converting both equations to the form $0=Ax+By+C$ , we have that $L$ has the equation $0=5x-12y-132$ and that $M$ has the equation $0=12x+5y-90$ . Applying the point-to-line distance formula, $\frac{|Ax+By+C|}{\sqrt{A^2+B^2}}$ , to point $P$ and lines $L$ and $M$ , we find that the distance from $P$ to $L$ and $M$ are $\frac{526}{13}$ and $\frac{123}{13}$ , respectively.
Since $A$ and $B$ lie on the positive axes of the shifted coordinate plane, we may show by graphing the given system that point P will lie in the second quadrant in the new coordinate system. Therefore, the $x$ -coordinate of $P$ is negative, and is therefore $-\frac{123}{13}$ ; similarly, the $y$ -coordinate of $P$ is positive and is therefore $\frac{526}{13}$ .
Thus, we have that $\alpha=-\frac{123}{13}$ and that $\beta=\frac{526}{13}$ . It follows that $\alpha+\beta=-\frac{123}{13}+\frac{526}{13}=\frac{403}{13}=\boxed{031}$ .

## Solution 2 (alternate bash)
The equations for the axes are $\frac{5}{12} (x-24) = y+1$ and $-\frac{12}{5}(x-5) = y - 6$ . We can solve the system to find that they intersect at the point $\left( \frac{1740}{169},\frac{-1134}{169} \right)$
The unit basis vectors of our new axes are $\begin{pmatrix} 12/13 \\ 5/13 \end{pmatrix}$ and $\begin{pmatrix} -5/13 \\ 12/13 \end{pmatrix}$ for the $x$ and $y$ axes respectively (taking into account which direction is positive).
Then, we solve the following system for $\alpha$ and $\beta$ :
\[\alpha \begin{pmatrix} 12/13 \\ 5/13 \end{pmatrix} + \beta \begin{pmatrix} -5/13 \\ 12/13 \end{pmatrix} + \begin{pmatrix} 1740/169 \\ -1134/169 \end{pmatrix} = \begin{pmatrix} -146 \\ 27 \end{pmatrix}\]
Painful bashing gives $\alpha = -\frac{123}{13}$ and $\beta = \frac{526}{13}$ . Adding gives $\alpha + \beta = \frac{403}{13} = \boxed{031}$
We can also attempt to manipulate the system of equations to solve for $\alpha + \beta$ , and avoid solving for $\alpha$ and $\beta$ separately.
~jd9

## Possibly a solution 3
First, find where the new positive x and y axis are by comparing the points A and B to the line it is not on (higher or lower). Next, just find the new quadrant the point is in from the x and y axis. Finally, to find the distance from the point to the axis, we can just use both slopes to find both projections of the line onto the axis. The intersection of the projection line and the axis's previous line would give us information on the new point's coordinate points.
~#EmilyQ

## Video Solution
https://www.youtube.com/watch?v=_znugFEst6E&t=919s
~Shreyas S
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
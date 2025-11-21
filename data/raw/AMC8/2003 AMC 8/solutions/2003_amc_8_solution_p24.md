# 2003 AMC 8 Problem 24

## Problem

A ship travels from point $A$ to point $B$ along a semicircular path, centered at Island $X$ . Then it travels along a straight path from $B$ to $C$ . Which of these graphs best shows the ship's distance from Island $X$ as it moves along its course?

[asy]size(150); pair X=origin, A=(-5,0), B=(5,0), C=(0,5); draw(Arc(X, 5, 180, 360)^^B--C); dot(X); label("$X$", X, NE); label("$C$", C, N); label("$B$", B, E); label("$A$", A, W); [/asy]

![](https://wiki-images.artofproblemsolving.com//d/d9/2003amc8prob24ans.png)

## Solution
The distance from Island $\text{X}$ to any point on the semicircle will always be constant. On the graph, this will represent a straight line. The distance between Island $\text{X}$ and line $\text{BC}$ will not be constant though. We can easily prove that the distance between $\text{X}$ and line $\text{BC}$ will represent a curve. As the ship travels from $B$ to $C$ , the distance between the ship and Island $X$ will first decrease until it reaches the point $Y$ so that $\overline{XY}$ is perpendicular to $\overline{BC}$ , and then increase afterwards. Hence the answer choice that fits them all is $\boxed{\text{(B)}}$ .

## Video Solution
https://www.youtube.com/watch?v=ibhy_qcQXiw ~David
### See Also
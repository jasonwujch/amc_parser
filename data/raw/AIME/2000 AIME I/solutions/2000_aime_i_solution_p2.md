# 2000 AIME I Problem 2

## Problem

Let $u$ and $v$ be integers satisfying $0 < v < u$ . Let $A = (u,v)$ , let $B$ be the reflection of $A$ across the line $y = x$ , let $C$ be the reflection of $B$ across the y-axis, let $D$ be the reflection of $C$ across the x-axis, and let $E$ be the reflection of $D$ across the y-axis. The area of pentagon $ABCDE$ is $451$ . Find $u + v$ .

## Solutions

## Solution 1
Since $A = (u,v)$ , we can find the coordinates of the other points: $B = (v,u)$ , $C = (-v,u)$ , $D = (-v,-u)$ , $E = (v,-u)$ . If we graph those points, we notice that since the latter four points are all reflected across the x/y-axis, they form a rectangle, and $ABE$ is a triangle. The area of $BCDE$ is $(2u)(2v) = 4uv$ and the area of $ABE$ is $\frac{1}{2}(2u)(u-v) = u^2 - uv$ . Adding these together, we get $u^2 + 3uv = u(u+3v) = 451 = 11 \cdot 41$ . Since $u,v$ are positive, $u+3v>u$ , and by matching factors we get either $(u,v) = (1,150)$ or $(11,10)$ . Since $v < u$ the latter case is the answer, and $u+v = \boxed{021}$ .

## Solution 2
We find the coordinates like in the solution above: $A = (u,v)$ , $B = (v,u)$ , $C = (-v,u)$ , $D = (-v,-u)$ , $E = (v,-u)$ . Then we notice pentagon $ABCDE$ fits into a rectangle of side lengths $(u+v)$ and $(2u)$ , giving us two triangles, each with hypotenuse $AB$ and $BE$ . First, we can solve for the first triangle. Using the coordinates of $A$ and $B$ , we discover the side lengths are both $(u-v)$ , so the area of the triangle of hypotenuse $AB$ is $\frac{1}{2}(u-v)^2$ . Next, we can solve for the second triangle. Using the coordinates of $A$ and $E$ , we discover the side lengths are $(u-v)$ and $(u+v)$ , so the area of the triangle of hypotenuse $AE$ is $\frac{1}{2}(u-v)(u+v) = \frac{1}{2}(u^2-v^2)$ . Now, let’s subtract the area of these 2 triangles from the rectangle giving us $(u+v)(2u)-\frac{1}{2}(u-v)^2-\frac{1}{2}(u^2-v^2)=451 —> u^2+3uv=451 -> u(u+3v)=451$ . Next, we take note of the fact that $u$ and $u+3v$ are both factors of 451, and since both $u$ and $v$ are positive integers, $u+3v$ must be greater than $u$ , thus giving us two cases, where either $u=1$ or $u=11$ . After trying both, the only working pair of $(u,v)$ where both $u$ and $v$ are integers are $u=11$ and $v=10$ , thus meaning $u + v =$ $\boxed{021}$
~Aeioujyot

## Solution 3
We find the coordinates like in the solution above: $A = (u,v)$ , $B = (v,u)$ , $C = (-v,u)$ , $D = (-v,-u)$ , $E = (v,-u)$ . Then we apply the Shoelace Theorem . \[A = \frac{1}{2}[(u^2 + vu + vu + vu + v^2) - (v^2 - uv - uv - uv -u^2)] = 451\] \[\frac{1}{2}(2u^2 + 6uv) = 451\] \[u(u + 3v) = 451\]
This means that $(u,v) = (11, 10)$ or $(1,150)$ , but since $v < u$ , then the answer is $\boxed{021}$
These problems are copyrighted © by the Mathematical Association of America.
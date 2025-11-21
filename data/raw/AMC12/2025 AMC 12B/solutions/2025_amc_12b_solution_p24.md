# 2025 AMC 12B Problem 24

## Problem

How many real numbers satisfy the equation $\sin(20\pi x) = \log_{20}(x)$ ?

$\textbf{(A) } 199 \qquad \textbf{(B) } 200 \qquad \textbf{(C) } 398 \qquad \textbf{(D) } 399 \qquad \textbf{(E) } 400$

## Solution 1
Let $f(x)=\sin(20\pi x)$ and $g(x)=\log_{20}(x)$ . Note that $g$ passes through $\left(\frac{1}{20},-1\right)$ and $(1,0)$ and $(20,1)$ ; these are the extrema and midpoint of $f$ . We want to find the number of intersections of $f$ and $g$ .
Let an occurrence of sine passing under the $x$ -axis a down-dip , and similarly define an up-dip . We find that the period of $f$ is $\frac{1}{10}$ , so between $x=\frac{1}{20}$ and $x=1$ the number of periods is $9.5$ . The first period indeed counts, so effectively we have $10$ down-dips in this interval. Each down-dip contributes $2$ to the total, so we have $20$ total intersections.
From $x=1$ to $x=20$ , there are $190$ periods, each of which also contributes $2$ to the total due to the up-dips. Therefore, this case contributes $380$ points to the total.
But $(1,0)$ is counted in both cases, so the total is $20+380-1=\boxed{\textbf{(D) } 399}$ .
~ eevee9406

## Solution 2 (quick but risky)
Each period of the sin function is $\frac{1}{10}$ , so 200 periods, 2 intersections each (just draw it out) - 400. But there is 1 overlap in two periods at $(1,0)$ , so subtract 1 -> 399 (can check end behavior if time) ~ScoutViolet

## Solution 3 (Unit-period parametrization)
Note that $-1\le \sin 20\pi x=\log_{20} x\le 1$ , forcing $\frac{1}{20}\le x\le 20$ . For simplicity, let $2\pi t=20\pi x$ or $t=10x\in\left[ \frac{1}{2},200 \right]$ . Since $2\pi t$ is the unit-period parametrization, there are $200$ full periods on $[0,200]$ , and we check the closed intervals $\left[ \frac{1}{2},1 \right],[1,2],\dots,[199,200]$ . By sketching the graph, we see that when sine and log share the same sign, the sine will weave through the log twice for the non-degenerate case. The endpoints are also non-degenerate after verifying $\log\left( \frac{1}{20} \right)=-1,\log_{20}20=1$ whereas $\sin 20\pi \left( \frac{1}{20} \right)=\sin 20\pi(200)=0$ .
Because $\log_{20}(x=1)=0=\log_{20}(t=10)$ lands perfectly on an integer, by the intermediate value theorem, $\log$ will only have at most two signs among $-,0,+$ in each full period closed interval. We count $200\cdot 2=400$ intersections. However, $t=10$ is shared among $[9,10]$ and $[10,11]$ so we must subtract the overlap to get $400-1=\boxed{\textbf{(D) } 399}$ .
~imosilver

## Solution 4 (Risky)
We know that the period of $\sin(20\pi x)$ is $\frac{2\pi}{20\pi}=\frac{1}{10}$ , and that the amplitude of the graph is 1. Now, we need to find the values of x for which the graph of $y=\log_{20} x$ intersects with the upper and lower extrema of $\sin(20\pi x)$ , or with $y=1$ and $y=-1$ . At $y=-1$ , $x=20^{-1}=\frac{1}{20}$ , and at $y=1$ , $x=20^1=20$ . We know that for each period of the sin graph, there will be 2 intersections, and there are $\frac{20}{\frac{1}{10}}=200$ periods of the sin graph from 0 to 20. Because there are 3 answer choices close to 400, we can test with smaller bounds using a line, and count the points. The line from $(\frac{1}{20},-1)$ to $(\frac{1}{2},1)$ intersected the graph $y=\sin(20\pi x)$ 9 times, and there were 5 periods between $\frac{1}{2}$ and $0$ , thus we can say the answer is $\boxed{\textbf{(D) } 399}$

## Video Solution 1 by OmegaLearn.org
https://youtu.be/BzeEeUbjKDQ
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
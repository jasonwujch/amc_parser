# 2009 AMC 8 Problem 3

## Problem

The graph shows the constant rate at which Suzanna rides her bike. If she rides a total of a half an hour at the same speed, how many miles would she have ridden?

[asy] import graph; /* this is a label */ Label f; f.p=fontsize(0); xaxis(-0.9,20,Ticks(f, 5.0, 5.0)); yaxis(-0.9,20, Ticks(f, 22.0,5.0)); // real f(real x) { return x; } draw(graph(f,-1,22),black+linewidth(1)); label("1", (-1,5), black); label("2", (-1, 10), black); label("3", (-1, 15), black); label("4", (-1, 20), black); dot((5,5), black+linewidth(5)); dot((10,10), black+linewidth(5)); dot((15, 15), black+linewidth(5)); dot((20,20), black+linewidth(5)); label("MINUTES", (11,-5), S); label(rotate(90)*"MILES", (-5,11), W);[/asy]

$\textbf{(A)}\ 5\qquad\textbf{(B)}\ 5.5\qquad\textbf{(C)}\ 6\qquad\textbf{(D)}\ 6.5\qquad\textbf{(E)}\ 7$

## Solution
Suzanna's speed is $\frac{1}{5}$ . This means she runs $\frac{1}{5} \cdot 30 = \boxed{ \textbf{(C) }6 }$

## Solution 2
From the graph, we can see that every $5$ minutes Suzanna goes, her distance increases by $1$ . Since half an hour is $10$ minutes away, she would go $2$ more miles. $4+2$ is $6$ , so the answer is $\boxed{ \textbf{(C) }6 }$
~Trex226

## Video Solution
https://youtu.be/USVVURBLaAc?t=117

## Video Solution 2
https://youtu.be/agfRvXTPxVc
~savannahsolver
### See Also
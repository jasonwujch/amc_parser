# 2020 AMC 10A Problem 5

## Problem

What is the sum of all real numbers $x$ for which $|x^2-12x+34|=2?$

$\textbf{(A) } 12 \qquad \textbf{(B) } 15 \qquad \textbf{(C) } 18 \qquad \textbf{(D) } 21 \qquad \textbf{(E) } 25$

## Solution 1 (Casework and Factoring)
Split the equation into two cases, where the value inside the absolute value is positive and nonpositive.
Case 1:
The equation yields $x^2-12x+34=2$ , which is equal to $(x-4)(x-8)=0$ . Therefore, the two values for the positive case is $4$ and $8$ .
Case 2:
Similarly, taking the nonpositive case for the value inside the absolute value notation yields $x^2-12x+34=-2$ . Factoring and simplifying gives $(x-6)^2=0$ , so the only value for this case is $6$ .
Summing all the values results in $4+8+6=\boxed{\textbf{(C) }18}$ .

## Solution 2 (Casework and Vieta)
We have the equations $x^2-12x+32=0$ and $x^2-12x+36=0$ .
Notice that the second is a perfect square with a double root at $x=6$ , and the first has two distinct real roots. By Vieta's, the sum of the roots of the first equation is $-(-12)$ or $12$ . $12+6=\boxed{\textbf{(C) }18}$ .

## Solution 3 (Casework and Graphing)
Completing the square gives \begin{align*} \left|(x-6)^2-2\right|&=2 \\ (x-6)^2-2&=\pm2. \hspace{15mm}(\bigstar) \end{align*} Note that the graph of $y=(x-6)^2-2$ is an upward parabola with the vertex $(6,-2)$ and the axis of symmetry $x=6;$ the graphs of $y=\pm2$ are horizontal lines.
We apply casework to $(\bigstar):$
1. $(x-6)^2-2=2$
1. $(x-6)^2-2=-2$
The line $y=2$ intersects the parabola $y=(x-6)^2-2$ at two points that are symmetric about the line $x=6.$
In this case, the average of the solutions is $6,$ so the sum of the solutions is $12.$
The line $y=-2$ intersects the parabola $y=(x-6)^2-2$ at one point: the vertex of the parabola.
In this case, the only solution is $x=6.$
Finally, the sum of all solutions is $12+6=\boxed{\textbf{(C) } 18}.$
~MRENTHUSIASM

## Video Solution 1
https://youtu.be/E7zjQkZl59E

## Video Solution 2
Education, The Study Of Everything
https://youtu.be/WUcbVNy2uv0
~IceMatrix

## Video Solution 3
https://www.youtube.com/watch?v=7-3sl1pSojc
~bobthefam

## Video Solution 4
https://youtu.be/TlIrYXcEuws
~savannahsolver

## Video Solution 5
https://youtu.be/3dfbWzOfJAI?t=1544
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
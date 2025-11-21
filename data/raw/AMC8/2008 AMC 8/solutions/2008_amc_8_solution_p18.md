# 2008 AMC 8 Problem 18

## Problem

Two circles that share the same center have radii $10$ meters and $20$ meters. An aardvark runs along the path shown, starting at $A$ and ending at $K$ . How many meters does the aardvark run?

[asy] size((150)); draw((10,0)..(0,10)..(-10,0)..(0,-10)..cycle); draw((20,0)..(0,20)..(-20,0)..(0,-20)..cycle); draw((20,0)--(-20,0)); draw((0,20)--(0,-20)); draw((-2,21.5)..(-15.4, 15.4)..(-22,0), EndArrow); draw((-18,1)--(-12, 1), EndArrow); draw((-12,0)..(-8.3,-8.3)..(0,-12), EndArrow); draw((1,-9)--(1,9), EndArrow); draw((0,12)..(8.3, 8.3)..(12,0), EndArrow); draw((12,-1)--(18,-1), EndArrow); label("$A$", (0,20), N); label("$K$", (20,0), E); [/asy]

$\textbf{(A)}\ 10\pi+20\qquad\textbf{(B)}\ 10\pi+30\qquad\textbf{(C)}\ 10\pi+40\qquad\textbf{(D)}\ 20\pi+20\qquad \\ \textbf{(E)}\ 20\pi+40$

## Solution
We will deal with this part by part: Part 1: 1/4 circumference of big circle= $\frac{2\pi r}{4}=\frac{\pi r}{2}=\frac{20\pi}{2}=10\pi$ Part 2: Big radius minus small radius= $20-10=10$ Part 3: 1/4 circumference of small circle= $\frac{\pi r}{2}=\frac{10\pi}{2}=5\pi$ Part 4: Diameter of small circle: $2*10=20$ Part 5: Same as part 3: $5\pi$ Part 6: Same as part 2: $10$ Total: $10\pi + 10 + 5\pi + 20 + 5\pi + 10 = \boxed{E = 20\pi + 40}$

## Video Solution
https://www.youtube.com/watch?v=NJs4rFyXFwQ —DSA_Catachu
### See Also
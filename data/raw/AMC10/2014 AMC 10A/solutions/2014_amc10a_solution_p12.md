# 2014 AMC 10A Problem 12

## Problem

A regular hexagon has side length 6. Congruent arcs with radius 3 are drawn with the center at each of the vertices, creating circular sectors as shown. The region inside the hexagon but outside the sectors is shaded as shown What is the area of the shaded region?

[asy] size(125); defaultpen(linewidth(0.8)); path hexagon=(2*dir(0))--(2*dir(60))--(2*dir(120))--(2*dir(180))--(2*dir(240))--(2*dir(300))--cycle; fill(hexagon,grey); for(int i=0;i<=5;i=i+1) { path arc=2*dir(60*i)--arc(2*dir(60*i),1,120+60*i,240+60*i)--cycle; unfill(arc); draw(arc); } draw(hexagon,linewidth(1.8));[/asy]

$\text{(A)}\ 27\sqrt{3}-9\pi \qquad \text{(B)}\ 27\sqrt{3}-6\pi \qquad \text{(C)}\ 54\sqrt{3}-18\pi \qquad \text{(D)}\ 54\sqrt{3}-12\pi \qquad \text{(E)}\ 108\sqrt{3}-9\pi$

## Solution 1
The area of the hexagon is equal to $\dfrac{3(6)^2\sqrt{3}}{2}=54\sqrt{3}$ by the formula for the area of a hexagon.
We note that each interior angle of the regular hexagon is $120^\circ$ which means that each sector is $\dfrac{1}{3}$ of the circle it belongs to. The area of each sector is $\dfrac{9\pi}{3}=3\pi$ . The area of all six is $6\times 3\pi=18\pi$ .
The shaded area is equal to the area of the hexagon minus the sum of the area of all the sectors, which is equal to $\boxed{\textbf{(C)}\ 54\sqrt{3}-18\pi}$

## Solution 2 (Using the answers)
This solution is very similar to the one above, but instead we use the solutions to guide us. The interior angle of a regular hexagon is $120^\circ$ , leading us to the observation that each fraction of a circle inside the edges of the hexagon is actually $\dfrac{1}{3}$ of a circle with radius 3. There are 2 of these circles in total, so the total area of them would be $18\pi$ .
Now, we have to subtract the area of the circles from the total area of the hexagon, but we see that only answer (C) has $-18\pi$ in it. We also note that $-18\pi$ will not be able to be simplified in the final answer, hence leading us to the answer $\boxed{\textbf{(C)}\ 54\sqrt{3}-18\pi}$ .

## Solution 3 (Splitting it up)
We can simply split the hexagon into 6 equilateral triangles. For each one, the side length is $6$ so the area is $\frac{\sqrt{3}}{4}\cdot6^2=9\sqrt{3}$ . Next, we need to subtract the circular portions. The combined angle is $60^\circ + 60^\circ = 120^\circ$ . Since the radius is $\frac{6}{2}=3$ , the area is $\frac{120}{360}\cdot3^2\cdot\pi=3\pi$ . Therefore, the area of the hexagon is $(9\sqrt{3}-3\pi)\cdot6=\boxed{54\sqrt{3}-18\pi}$ .
~MathFun1000

## Video Solution
https://youtu.be/Au3z4pMI7IQ ~DSA_Catachu
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
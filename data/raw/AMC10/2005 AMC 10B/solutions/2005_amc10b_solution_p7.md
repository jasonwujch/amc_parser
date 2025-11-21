# 2005 AMC 10B Problem 7

## Problem

A circle is inscribed in a square, then a square is inscribed in this circle, and finally, a circle is inscribed in this square. What is the ratio of the area of the smallest circle to the area of the largest square?

$\textbf{(A) } \frac{\pi}{16} \qquad \textbf{(B) } \frac{\pi}{8} \qquad \textbf{(C) } \frac{3\pi}{16} \qquad \textbf{(D) } \frac{\pi}{4} \qquad \textbf{(E) } \frac{\pi}{2}$

## Solution 1
Let the side of the largest square be $x$ . It follows that the diameter of the inscribed circle is also $x$ . Therefore, the square's diagonal inscribed in the circle is $x$ . The side length of the smaller square is $\dfrac{x}{\sqrt{2}}=\dfrac{x\sqrt{2}}{2}$ . Similarly, the diameter of the smaller inscribed circle is $\dfrac{x\sqrt{2}}{2}$ . Hence, its radius is $\dfrac{x\sqrt{2}}{4}$ . The area of this circle is $\left(\dfrac{x\sqrt{2}}{4}\right)^2\pi=\dfrac{2\pi x^2}{16}=\dfrac{x^2\pi}{8}$ , and the area of the largest square is $x^2$ . The ratio of the areas is $\dfrac{\dfrac{x^2\pi}{8}}{x^2}=\frac{\cancel{x^2}\pi}{8}\cdot\frac{1}{\cancel{x^2}}=\boxed{\textbf{(B) }\frac{\pi}{8}}$ .

## Solution 2
Let the radius of the smallest circle be $r$ . Then the side length of the smaller square is $2r$ . The radius of the larger circle is half the length of the diagonal of the smaller square, so it is $\sqrt{2}r$ . Hence the largest square has sides of length $2\sqrt{2}r$ . The ratio of the area of the smallest circle to the area of the largest square is therefore $\frac{\pi r^2}{\left(2\sqrt{2}r\right)^2} =\boxed{\textbf{(B) }\frac{\pi}{8}}.$
[asy] draw(Circle((0,0),10),linewidth(0.7)); draw(Circle((0,0),14.1),linewidth(0.7)); draw((0,14.1)--(14.1,0)--(0,-14.1)--(-14.1,0)--cycle,linewidth(0.7)); draw((-14.1,14.1)--(14.1,14.1)--(14.1,-14.1)--(-14.1,-14.1)--cycle,linewidth(0.7)); draw((0,0)--(-14.1,0),linewidth(0.7)); draw((-7.1,7.1)--(0,0),linewidth(0.7)); label("$\sqrt{2}r$",(-6,0),S); label("$r$",(-3.5,3.5),NE); label("$2r$",(-7.1,7.1),W); label("$2\sqrt{2}r$",(0,14.1),N); [/asy] Tip: When facing a geometry problem, it is very helpful to draw a diagram.
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
# 2012 AMC 8 Problem 24

## Problem

A circle of radius $2$ is cut into four congruent arcs. The four arcs are joined to form the star figure shown. What is the ratio of the area of the star figure to the area of the original circle?

[asy] size(0,50); draw((-1,1)..(-2,2)..(-3,1)..(-2,0)..cycle); dot((-1,1)); dot((-2,2)); dot((-3,1)); dot((-2,0)); draw((1,0){up}..{left}(0,1)); dot((1,0)); dot((0,1)); draw((0,1){right}..{up}(1,2)); dot((1,2)); draw((1,2){down}..{right}(2,1)); dot((2,1)); draw((2,1){left}..{down}(1,0));[/asy]

$\textbf{(A)}\hspace{.05in}\frac{4-\pi}{\pi}\qquad\textbf{(B)}\hspace{.05in}\frac{1}\pi\qquad\textbf{(C)}\hspace{.05in}\frac{\sqrt2}{\pi}\qquad\textbf{(D)}\hspace{.05in}\frac{\pi-1}{\pi}\qquad\textbf{(E)}\hspace{.05in}\frac{3}\pi$

## Solution
[asy] dot((0,0),red); dot((0,2),red); dot((2,0),red); dot((2,2),red); draw((0,0)--(0,2)--(2,2)--(2,0)--cycle,red); size(0,50); draw((1,0){up}..{left}(0,1)); dot((1,0)); dot((0,1)); draw((0,1){right}..{up}(1,2)); dot((1,2)); draw((1,2){down}..{right}(2,1)); dot((2,1)); draw((2,1){left}..{down}(1,0));[/asy]
Draw a square around the star figure. The side length of this square is $4$ , because the side length is the diameter of the circle. The square forms $4$ -quarter circles around the star figure. This is the equivalent of one large circle with radius $2$ , meaning that the total area of the quarter circles is $4\pi$ . The area of the square is $16$ . Thus, the area of the star figure is $16 - 4\pi$ . The area of the circle is $4\pi$ . Taking the ratio of the two areas, we find the answer is $\boxed{\textbf{(A)}\ \frac{4-\pi}{\pi}}$ .

## Video Solution by OmegaLearn
https://youtu.be/abSgjn4Qs34?t=1107
~ pi_is_3.14

## Video Solution
https://youtu.be/QK_lGbJaCVc ~savannahsolver
### See Also
# 2024 AMC 8 Problem 23

## Problem

Rodrigo has a very large sheet of graph paper. First he draws a line segment connecting point $(0,4)$ to point $(2,0)$ and colors the $4$ cells whose interiors intersect the segment, as shown below. Next Rodrigo draws a line segment connecting point $(2000,3000)$ to point $(5000,8000)$ . How many cells will he color this time?

[asy] // Asymptote code by aoum unitsize(8mm); fill((1,0)--(2,0)--(2,2)--(1,2)--cycle, lightgray); fill((0,2)--(1,2)--(1,4)--(0,4)--cycle, lightgray); for (int i = -1; i < 6; ++i) { draw((-1,i)--(5,i)); draw((i,-1)--(i,5)); } draw((-1,0)--(5,0), Arrow); draw((0,-1)--(0,5), Arrow); draw((2,0)--(0,4), black + 1.5bp); dot((2,0), black + 6bp); dot((0,4), black + 6bp); label(scale(0.7)*"$(2,0)$", (2,0), SE); label(scale(0.7)*"$(0,4)$", (0,4), NW); [/asy]

$\textbf{(A) } 6000\qquad\textbf{(B) } 6500\qquad\textbf{(C) } 7000\qquad\textbf{(D) } 7500\qquad\textbf{(E) } 8000$

## Solution 1
Let $f(x, y)$ be the number of cells the line segment from $(0, 0)$ to $(x, y)$ passes through. The problem is then equivalent to finding \[f(5000-2000, 8000-3000)=f(3000, 5000).\] Sometimes the segment passes through lattice points in between the endpoints, which happens $\text{gcd}(3000, 5000)-1=999$ times. This partitions the segment into $1000$ congruent pieces that each pass through $f(3, 5)$ cells, which means the answer is \[1000f(3, 5).\] Note that a new square is entered when the lines pass through one of the lines in the coordinate grid, which for $f(3, 5)$ happens $3-1+5-1=6$ times. Because $3$ and $5$ are relatively prime, no lattice point except for the endpoints intersects the line segment from $(0, 0)$ to $(3, 5).$ This means that including the first cell closest to $(0, 0),$ The segment passes through $f(3, 5)=6+1=7$ cells. Thus, the answer is $\boxed{\textbf{(C)}7000}.$ Alternatively, $f(3, 5)$ can be found by drawing an accurate diagram, leaving you with the same answer.
~BS2012
Note: A general form for finding $f(x, y)$ is $x+y-\text{gcd}(x, y).$ We subtract $\text{gcd}(x, y)$ to account for overlapping, when the line segment goes through a lattice point.
~mathkiddus
### Proof of This Claim
$\textbf{Lemma 1 for Problem 23:}$
Let $p$ and $q$ be relatively prime positive integers. When a $p\times q$ rectangle is split up into $pq$ unit squares, exactly $p + q - 1$ unit squares are crossed by the diagonal of this rectangle.
$\textbf{Proof:}$
First, we claim that the diagonal does not cross the corner of a unit square. \\\\ To prove this claim we proceed by way of contradiction. Plot the rectangle on the Cartesian plane at the vertices $(0,0),(p,0),(q,p),(0,q).$ The diagonal has endpoints at $(0,0),(q,p)$ , so its slope is $\frac{p}{q}.$ Now, suppose the diagonal goes through the corner point $(a,b)$ , where $a<q$ and $b<p$ . The slope of this line is $\frac{b}{a}$ , which must be equal to $\frac{p}{q},$ implying that $\frac{p}{q}$ can be reduced, contradicting the fact that $p$ and $q$ are relatively prime. We conclude that no corner points of a grid entry (unit square) are crossed. \\\\ Since no corner points are crossed, each time the diagonal crosses either a horizontal or vertical grid line, exactly one more unit square is touched by the diagonal. There are $p-1$ horizontal lines and $q-1$ vertical lines, so there are $p + q - 2$ total lines crossed by the diagonal. This doesn't include the square in the bottom left corner, crossed initially. Therefore, there are $p + q-2 + 1 = p + q - 1$ unit squares crossed by the diagonal and our claim is proven.
$\textbf{Lemma 2 for Problem 23:}$
Let $p$ and $q$ be positive integers. When a $p\times q$ rectangle is split up into $pq$ units squares, exactly $p + q - \gcd(p, q)$ unit squares are crossed by the diagonal of this rectangle.
If $\gcd (p,q) = 1$ , then we are done by Lemma 1.
Suppose $\gcd(p,q) = k>1$ , i.e $p = ak$ and $q = bk$ , for positive integers $a$ and $b$ . We can then split the $p\times q$ rectangle up into $k$ $\frac{p}{k} \times \frac{q}{k}$ rectangles, strung together at the diagonal. An example for $(p,q)=(4,6)$ is shown below, where two $2\times 3$ rectangles are strung together:
[asy] unitsize(1cm); draw((0,0)--(6,4),linewidth(1)); currentpen = linewidth(.5); for (real i = 0; i <= 6; ++i) { draw((i, 0)--(i, 4)); } for (real i = 0; i < 5; ++i) { draw((0, i)--(6, i)); } currentpen = linewidth(1.5); for (real i = 0; i <= 3; ++i) { draw((i, 0)--(i, 2)); } for (real i = 0; i <= 2; ++i) { draw((0, i)--(3, i)); } for (real i = 3; i <= 6; ++i) { draw((i, 2)--(i, 4)); } for (real i = 3; i <= 5; ++i) { draw((3, i-1)--(6, i-1)); } [/asy]
After the diagonal crosses the corner point of a square, the pattern repeats itself with the next one. By Lemma 1, there are $\frac{p}{k}+ \frac{q}{k} - 1$ diagonals crossed in each rectangle. There are $k = \gcd (p, q)$ rectangles, so the number of crossed diagonals in total is \[k\left( \frac{p}{k}+ \frac{q}{k} - 1 \right) = p + q - \gcd(p,q).\]
-Benedict T (countmath1)

## Solution 2 (The simplified version of Solution 1)
Draw a line in the lattice (rulers are allowed on the AMC 8) from $(2,3)$ to $(5,8)$ , and notice that the line crossed 7 blocks in this pattern. Such a pattern is repeated 1000 times between $(2000,3000)$ and $(5000,8000)$ , so the answer is $\boxed{\textbf{(C)}7000}$ .
~Minor edits by mihikamishra

## Video Solution 1 by Math-X (First fully understand the problem!!!)
https://youtu.be/BaE00H2SHQM?si=WqyvRC1PRp2FZIL9&t=7181
~Math-X

## Video Solution by Central Valley Math Circle (Goes through full thought process)
https://youtu.be/_EGtDKsewuA
~mr_mathman

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/5ZIFnqymdDQ?si=LEqWH6Q7azylK6do&t=3409
~hsnacademy

## Video Solution by Power Solve (crystal clear!)
https://www.youtube.com/watch?v=fzgWcEz4K_A

## Video Solution 2 by OmegaLearn
https://youtu.be/wNymnFQfN_k

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=x8Zo7QOB-us

## Video Solution by NiuniuMaths (Easy to understand!)
https://www.youtube.com/watch?v=8XipREuWIHE&t=2s
~NiuniuMaths

## Video Solution by CosineMethod [🔥Fast and Easy🔥]
https://www.youtube.com/watch?v=w8zha2ijVQQ

## Fast Solution (2 minutes) AND generalized formula by MegaMath
https://www.youtube.com/watch?v=L2m5U6x-_-8

## Video Solution by Interstigation
https://youtu.be/ktzijuZtDas&t=2847

## Video Solution by Dr. David
https://youtu.be/cJpYYEh9m3k

## Video Solution by WhyMath
https://youtu.be/a7rUlwfO5wA

## Video Solution (1 min visualization technique)!
https://youtu.be/jLdqDhBQ4aQ?feature=shared
~TheMathGeek

## Video Solution by Daily Dose of Math (Simple, Certified, and Logical)
https://youtu.be/OwJvuq6F7sQ
~Thesmartgreekmathdude
### See Also
# 2023 AMC 10B Problem 19

## Problem

Sonya the frog chooses a point uniformly at random lying within the square $[0, 6]$ $\times$ $[0, 6]$ in the coordinate plane and hops to that point. She then randomly chooses a distance uniformly at random from $[0, 1]$ and a direction uniformly at random from {north, south, east, west}. All of her choices are independent. She now hops the distance in the chosen direction. What is the probability that she lands outside the square?

$\textbf{(A) } \frac{1}{6} \qquad \textbf{(B) } \frac{1}{12} \qquad \textbf{(C) } \frac{1}{4} \qquad \textbf{(D) } \frac{1}{10} \qquad \textbf{(E) } \frac{1}{9}$

## Solution 1
WLOG, we assume Sonya jumps $0.5$ units every time, since that is her expected value.
If Sonya is within $0.5$ blocks of an edge, she can jump off the board. Let us examine the region that is at most $0.5$ blocks from exactly one edge.
[asy] import graph; Label f; xaxis(0,6,Ticks(f, 6.0, 0.5)); yaxis(0,6,Ticks(f, 6.0, 0.5)); draw((0,0)--(6,0)--(6,6)--(0,6)--cycle); filldraw((0,0.5)--(0.5,0.5)--(0.5,5.5)--(0,5.5)--cycle,gray); filldraw((0.5,0)--(0.5,0.5)--(5.5,0.5)--(5.5,0)--cycle,gray); filldraw((6,0.5)--(5.5,0.5)--(5.5,5.5)--(6,5.5)--cycle,gray); filldraw((0.5,6)--(0.5,5.5)--(5.5,5.5)--(5.5,6)--cycle,gray); [/asy]
If Sonya starts in this region, she has a $\dfrac14$ chance of landing outside (there's exactly one direction she can hop to get out). The total area of this region is $4\cdot0.5\cdot5=10.$ For this region, Sonya has a $\dfrac14$ chance, so we multiply $10$ by $\dfrac14$ to get $2.5.$
If Sonya is in one of the corner squares, she can go two directions to get out, so she has a $\dfrac24=\dfrac12$ chance to get out. The total area is $0.5\cdot0.5\cdot4=1$ , so this region yields $\dfrac12\cdot1=\dfrac12.$
Adding the two, we get $3$ . This is out of $36$ square units of area, so our answer is thus $\boxed{\textbf{(B) }\tfrac{1}{12}}.$
~Technodoggo
Note: When Sonya is within 0 to 1 units away from the border in a given direction, the probability that she will jump outside the border can be thought of as a function of distance from the border. It is easy to see that if Sonya is \(x\) units away from the border, a jump distance in the interval \([x, 1]\) will move her outside. Thus the probability is a function \(P(x) = 1-x\). The probability in an entire region 0 to 1 units away from the border is an integral of the function, \(\int^1_0 (1-x) dx = [x-\frac{1}{2}x^2]^1_0 = 1/2\). This is why the probability is \(1/2\).
~abghim

## Solution 2
Since all the actions are independent, we can switch the orders. Let Sonya choose the direction first. And the problem is symmetric, so we consider just one direction. WLOG, let's say she choose $south$ . When she first pick the location, she'll have to be within 1 unit of the $x$ axis to have a chance to jump out of the boundary southward. That's $\dfrac{1}{6}$ . With in that region, the expected y coordinate would be 0.5 which is 0.5 unit from the boundary (x-axis). Now, the jumping distance required to jump out of the boundary on average has to be greater than 0.5. That's another $\dfrac{1}{2}$ . So the final probability is $\dfrac{1}{6}\cdot\dfrac{1}{2} = \boxed{\textbf{(B) }\tfrac{1}{12}}$ .
~Technodoggo

## Solution 3
We denote by $\left( x, y \right)$ the frog's initial coordinates. We denote by $k \in \left\{ n, e, s, w \right\}$ the direction to hop. We denote by $z$ the hopping distance. In this analysis, we say that the frog wins if landing outside the square.
We have
\begin{align*} P \left( win \right) & = \sum_{k \in \left\{ n, e, s, w \right\}} P\left( win | k \right) P \left( k \right) \\ & = P \left( win | k = w \right) \sum_{k \in \left\{ n, e, s, w \right\}} P \left( k \right) \\ & = P \left( win | k = w \right) \\ & = \int_{y=0}^1 P \left( win | k = w, y \right) dy \\ & = P \left( win | k = w, y = 0 \right) \\ & = P \left( win | k = w, y = 0, x \in [0,1] \right) P \left( x \in [0,1] \right) + P \left( win | k = w, y = 0, x \in (1,6] \right) P \left( x \in (1,6] \right) \\ & = P \left( win | k = w, y = 0, x \in [0,1] \right) \cdot \frac{1}{6} + 0 \cdot \frac{5}{6} \\ & = \frac{1}{6} P \left( win | k = w, y = 0, x \in [0,1] \right) \\ & = \frac{1}{6} \int_{x=0}^1 \int_{z=x}^1 dz dx \\ & = \frac{1}{6} \cdot \frac{1}{2} \\ & = \boxed{\textbf{(B)}\frac{1}{12}}. \end{align*}
The second equality above follows from symmetry that $P \left( win | k \right)$ are all the same for all $k \in \left\{ n, e, s, w \right\}$ . The fifth equality above follows from symmetry that $P \left( win | k = w, y \right)$ are all the same for all $y \in \left[ 0, 1 \right]$ .
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 4
We can notice that Sonya can only jump out if she first picks a point that is at most 1 unit from the border. Let's separate this region into 4 different strips each with overlapping corners. Since each strip is exactly the same, let's first consider the probability of Sonya leaving the square given that she first lands on the top strip. Using expected value, one can get that the probability that Sonya gets the distance needed to leave the square is $\dfrac12$ . Now the probability she gets the direction needed (north) is $\dfrac14$ . Now with the probability of landing in the strip being $\dfrac16$ , we get the probability that she lands on the strip and leaves the square to be $\dfrac16\cdot\dfrac12\cdot\dfrac14=\dfrac{1}{48}.$ Since there are four strips, we add the probabilities giving a final answer of $\boxed{\textbf{(B) }\tfrac{1}{12}}.$
~Daniel C (Minor edits by Ishaan Garg)

## Solution 5
We know that Sonya can only jump out if she is within 1 unit of the border. We can calculate the probability that Sonya can jump out. $\newline$
[asy] import graph; draw((0,0)--(0,6)--(6,6)--(6,0)--cycle); filldraw((1,0)--(1,1)--(5,1)--(5,0)--cycle,blue); filldraw((0,1)--(1,1)--(1,5)--(0,5)--cycle,blue); filldraw((1,5)--(1,6)--(5,6)--(5,5)--cycle,blue); filldraw((5,1)--(6,1)--(6,5)--(5,5)--cycle,blue); filldraw((0,0)--(0,1)--(1,1)--(1,0)--cycle,red); filldraw((0,5)--(1,5)--(1,6)--(0,6)--cycle,red); filldraw((5,0)--(5,1)--(6,1)--(6,0)--cycle,red); filldraw((5,5)--(6,5)--(6,6)--(5,6)--cycle,red); [/asy] $\newline$
The total area of the colored regions is $20$ , so the probability that Sonya lands in a colored region is $\frac{20}{36} = \frac{5}{9}$ . We can calculate the probability that Sonya gets out of each type of region. $\newline$
Case 1: Sonya chooses a blue region.
The probability that Sonya chooses a blue region is $\frac{16}{20} = \frac{4}{5}$ . One direction can let her out, so the probability that she chooses the right one is $\frac{1}{4}$ . Finally, the probability that Sonya chooses a distance to get her out is $\frac{1}{2}$ . So, the probability that she chooses a blue region and gets out is $\frac{5}{9} \cdot \frac{4}{5} \cdot \frac{1}{4} \cdot \frac{1}{2} = \frac{1}{18}$ . $\newline$
Case 2: Sonya choose a red region.
The probability that Sonya chooses a red region is $\frac{4}{20} = \frac{1}{5}$ . Two directions can let her out, so the probability that she chooses one of them is $\frac{1}{2}$ . Finally, the probability that Sonya chooses a distance to get her out is $\frac{1}{2}$ . So, the probability that she chooses a red region and gets out is $\frac{5}{9} \cdot \frac{1}{5} \cdot \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{36}$ . $\newline$
So, the probability that Sonya gets out is $\frac{1}{18} + \frac{1}{36} = \frac{3}{36} =$ $\boxed{\textbf{(B) }\tfrac{1}{12}}.$
~MathCactus0_0

## Video Solution 1 by OmegaLearn
https://youtu.be/elxQNzDuYq8

## Video Solution 2 by MegaMath
https://www.youtube.com/watch?v=le0KSx3Cy-g&t=28s

## Video Solution
https://youtu.be/l6g9jBuCPEU
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
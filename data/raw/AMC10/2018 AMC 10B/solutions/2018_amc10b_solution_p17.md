# 2018 AMC 10B Problem 17

## Problem

In rectangle $PQRS$ , $PQ=8$ and $QR=6$ . Points $A$ and $B$ lie on $\overline{PQ}$ , points $C$ and $D$ lie on $\overline{QR}$ , points $E$ and $F$ lie on $\overline{RS}$ , and points $G$ and $H$ lie on $\overline{SP}$ so that $AP=BQ<4$ and the convex octagon $ABCDEFGH$ is equilateral. The length of a side of this octagon can be expressed in the form $k+m\sqrt{n}$ , where $k$ , $m$ , and $n$ are integers and $n$ is not divisible by the square of any prime. What is $k+m+n$ ?

$\textbf{(A) } 1 \qquad \textbf{(B) } 7 \qquad \textbf{(C) } 21 \qquad \textbf{(D) } 92 \qquad \textbf{(E) } 106$

## Solution 1
Let $AP=BQ=x$ . Then $AB=8-2x$ .
Now notice that since $CD=8-2x$ we have $QC=DR=x-1$ .
Thus by the Pythagorean Theorem we have $x^2+(x-1)^2=(8-2x)^2$ which becomes $2x^2-30x+63=0\implies x=\dfrac{15-3\sqrt{11}}{2}$
Our answer is $8-(15-3\sqrt{11})=3\sqrt{11}-7\implies \boxed{\text{(B)}~7}$ . (Mudkipswims42)

## Solution 2
Denote the length of the equilateral octagon as $x$ . The length of $\overline{BQ}$ can be expressed as $\frac{8-x}{2}$ . By the Pythagorean Theorem, we find that: \[\left(\frac{8-x}{2}\right)^2+\overline{CQ}^2=x^2\implies \overline{CQ}=\sqrt{x^2-\left(\frac{8-x}{2}\right)^2}\] Since $\overline{CQ}=\overline{DR}$ , we can say that $x+2\sqrt{x^2-\left(\frac{8-x}{2}\right)^2}=6\implies x=-7\pm3\sqrt{11}$ . We can discard the negative solution, so $k+m+n=-7+3+11=\boxed{\textbf{(B) }7}$ ~ blitzkrieg21

## Solution 3
Let the octagon's side length be $x$ . Then $PH = \frac{6 - x}{2}$ and $PA = \frac{8 - x}{2}$ . By the Pythagorean theorem, $PH^2 + PA^2 = HA^2$ , so $\left(\frac{6 - x}{2} \right)^2 + \left(\frac{8 - x}{2} \right)^2 = x^2$ . By expanding the left side and combining the like terms, we get $\frac{x^2}{2} - 7x + 25 = x^2 \implies -\frac{x^2}{2} - 7x + 25 = 0$ . Solving this using the quadratic formula, $\frac{-b \pm \sqrt{b^2-4ac}}{2a}$ , we use $a = -\frac{1}{2}$ , $b = -7$ , and $c = 25$ , to get one positive solution, $x=-7+3\sqrt{11}$ , so $k+m+n=-7+3+11=\boxed{\textbf{(B) }7}$

## Solution 4
Let $AB$ , or the side of the octagon, be $x$ . Then, $BQ = \left(\frac{8-x}{2}\right)$ and $CQ = \left(\frac{6-x}{2}\right)$ . By the Pythagorean Theorem , $BQ^2+CQ^2=x^2$ , or $\left(\frac{8-x}{2}\right)^2+\left(\frac{6-x}{2}\right)^2 = x^2$ . Multiplying this out, we have $x^2 = \frac{64-16x+x^2+36-12x+x^2}{4}$ . Simplifying, $-2x^2-28x+100=0$ . Dividing both sides by $-2$ gives $x^2+14x-50=0$ . Therefore, using the quadratic formula , we have $x=-7 \pm 3\sqrt{11}$ . Since lengths are always positive, then $x=-7+3\sqrt{11} \Rightarrow k+m+n=-7+3+11=\boxed{\textbf{(B)}\ 7}$
~MrThinker

## Video Solution
https://youtu.be/8sts_hn7cpQ
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
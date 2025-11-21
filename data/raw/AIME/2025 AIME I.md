Problem 1
Find the sum of all integer bases $b > 9$ for which $17_b$ is a divisor of $97_b$ .

Solution

Problem 2
On $\triangle ABC$ points $A$ , $D$ , $E$ , and $B$ lie in that order on side $\overline{AB}$ with $AD = 4$ , $DE = 16$ , and $EB = 8$ . Points $A$ , $F$ , $G$ , and $C$ lie in that order on side $\overline{AC}$ with $AF = 13$ , $FG = 52$ , and $GC = 26$ . Let $M$ be the reflection of $D$ through $F$ , and let $N$ be the reflection of $G$ through $E$ . Quadrilateral $DEGF$ has area $288$ . Find the area of heptagon $AFNBCEM$ .
[asy] unitsize(14); pair A = (0, 9), B = (-6, 0), C = (12, 0), D = (5A + 2B)/7, E = (2A + 5B)/7, F = (5A + 2C)/7, G = (2A + 5C)/7, M = 2F - D, N = 2E - G; filldraw(A--F--N--B--C--E--M--cycle, lightgray); draw(A--B--C--cycle); draw(D--M); draw(N--G); dot(A); dot(B); dot(C); dot(D); dot(E); dot(F); dot(G); dot(M); dot(N); label("$A$", A, dir(90)); label("$B$", B, dir(225)); label("$C$", C, dir(315)); label("$D$", D, dir(135)); label("$E$", E, dir(135)); label("$F$", F, dir(45)); label("$G$", G, dir(45)); label("$M$", M, dir(45)); label("$N$", N, dir(135)); [/asy]

Solution

Problem 3
The $9$ members of a baseball team went to an ice-cream parlor after their game. Each player had a single scoop cone of chocolate, vanilla, or strawberry ice cream. At least one player chose each flavor, and the number of players who chose chocolate was greater than the number of players who chose vanilla, which was greater than the number of players who chose strawberry. Let $N$ be the number of different assignments of flavors to players that meet these conditions. Find the remainder when $N$ is divided by $1000.$

Solution

Problem 4
Find the number of ordered pairs $(x,y)$ , where both $x$ and $y$ are integers between $-100$ and $100$ , inclusive, such that $12x^2-xy-6y^2=0$ .

Solution

Problem 5
There are $8!= 40320$ eight-digit positive integers that use each of the digits $1, 2, 3, 4, 5, 6, 7, 8$ exactly once. Let $N$ be the number of these integers that are divisible by $22$ . Find the difference between $N$ and $2025$ .

Solution

Problem 6
An isosceles trapezoid has an inscribed circle tangent to each of its four sides. The radius of the circle is $3$ , and the area of the trapezoid is $72$ . Let the parallel sides of the trapezoid have lengths $r$ and $s$ , with $r \neq s$ . Find $r^2 + s^2$ .

Solution

Problem 7
The twelve letters $A$ , $B$ , $C$ , $D$ , $E$ , $F$ , $G$ , $H$ , $I$ , $J$ , $K$ , and $L$ are randomly grouped into six pairs of letters. The two letters in each pair are placed next to each other in alphabetical order to form six two-letter words, and then those six words are listed alphabetically. For example, a possible result is $AB$ , $CJ$ , $DG$ , $EK$ , $FL$ , $HI$ . The probability that the last word listed contains $G$ is $\frac mn$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

Solution

Problem 8
Let $k$ be a real number such that the system \begin{align*} &|25 + 20i - z| = 5 \\ &|z - 4 - k| = |z - 3i - k| \end{align*} has exactly one complex solution $z$ . The sum of all possible values of $k$ can be written as $\frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m + n$ . Here $i = \sqrt{-1}$ .

Solution

Problem 9
The parabola with equation $y = x^2 - 4$ is rotated $60^{\circ}$ counterclockwise around the origin. The unique point in the fourth quadrant where the original parabola and its image intersect has $y$ -coordinate $\frac{a - \sqrt{b}}{c}$ , where $a$ , $b$ , and $c$ are positive integers, and $a$ and $c$ are relatively prime. Find $a + b + c$ .

Solution

Problem 10
The $27$ cells of a $3 \times 9$ grid are filled in using the numbers $1$ through $9$ so that each row contains $9$ different numbers, and each of the three $3 \times 3$ blocks heavily outlined in the example below contains $9$ different numbers, as in the first three rows of a Sudoku puzzle.
[asy] unitsize(20); add(grid(9,3)); draw((0,0)--(9,0)--(9,3)--(0,3)--cycle, linewidth(2)); draw((3,0)--(3,3), linewidth(2)); draw((6,0)--(6,3), linewidth(2)); real a = 0.5; label("5",(a,a)); label("6",(1+a,a)); label("1",(2+a,a)); label("8",(3+a,a)); label("4",(4+a,a)); label("7",(5+a,a)); label("9",(6+a,a)); label("2",(7+a,a)); label("3",(8+a,a)); label("3",(a,1+a)); label("7",(1+a,1+a)); label("9",(2+a,1+a)); label("5",(3+a,1+a)); label("2",(4+a,1+a)); label("1",(5+a,1+a)); label("6",(6+a,1+a)); label("8",(7+a,1+a)); label("4",(8+a,1+a)); label("4",(a,2+a)); label("2",(1+a,2+a)); label("8",(2+a,2+a)); label("9",(3+a,2+a)); label("6",(4+a,2+a)); label("3",(5+a,2+a)); label("1",(6+a,2+a)); label("7",(7+a,2+a)); label("5",(8+a,2+a)); [/asy]
The number of different ways to fill such a grid can be written as $p^a \cdot q^b \cdot r^c \cdot s^d$ where $p$ , $q$ , $r$ , and $s$ are distinct prime numbers and $a$ , $b$ , $c$ , $d$ are positive integers. Find $p \cdot a + q \cdot b + r \cdot c + s \cdot d$ .

Solution

Problem 11
A piecewise linear function is defined by \[f(x) = \begin{cases} x & \operatorname{if} ~ -1 \leq x < 1 \\ 2 - x & \operatorname{if} ~ 1 \leq x < 3\end{cases}\] and $f(x + 4) = f(x)$ for all real numbers $x$ . The graph of $f(x)$ has the sawtooth pattern depicted below.
[asy] import graph; size(300); Label f; f.p=fontsize(6); yaxis(-2,2,Ticks(f, 2.0)); xaxis(-6.5,6.5,Ticks(f, 2.0)); draw((-7,0)--(7,0), black+0.8bp); draw((0,-2.2)--(0,2.2), black+0.8bp); draw((-6,-0.1)--(-6,0.1), black); draw((-4,-0.1)--(-4,0.1), black); draw((-2,-0.1)--(-2,0.1), black); draw((0,-0.1)--(0,0.1), black); draw((2,-0.1)--(2,0.1), black); draw((4,-0.1)--(4,0.1), black); draw((6,-0.1)--(6,0.1), black); draw((-7,1)..(-5,-1), blue); draw((-5,-1)--(-3,1), blue); draw((-3,1)--(-1,-1), blue); draw((-1,-1)--(1,1), blue); draw((1,1)--(3,-1), blue); draw((3,-1)--(5,1), blue); draw((5,1)--(7,-1), blue); [/asy]
The parabola $x = 34y^{2}$ intersects the graph of $f(x)$ at finitely many points. The sum of the $y$ -coordinates of all these intersection points can be expressed in the form $\tfrac{a + b\sqrt{c}}{d}$ , where $a$ , $b$ , $c$ , and $d$ are positive integers such that $a$ , $b$ , $d$ have greatest common divisor equal to $1$ , and $c$ is not divisible by the square of any prime. Find $a + b + c + d$ .

Solution

Problem 12
The set of points in $3$ -dimensional coordinate space that lie in the plane $x+y+z=75$ whose coordinates satisfy the inequalities \[x-yz<y-zx<z-xy\] forms three disjoint convex regions. Exactly one of those regions has finite area. The area of this finite region can be expressed in the form $a\sqrt{b},$ where $a$ and $b$ are positive integers and $b$ is not divisible by the square of any prime. Find $a+b.$

Solution

Problem 13
Alex divides a disk into four quadrants with two perpendicular diameters intersecting at the center of the disk. He draws $25$ more line segments through the disk, drawing each segment by selecting two points at random on the perimeter of the disk in different quadrants and connecting these two points. Find the expected number of regions into which these $27$ line segments divide the disk.

Solution

Problem 14
Let $ABCDE$ be a convex pentagon with $AB=14,$ $BC=7,$ $CD=24,$ $DE=13,$ $EA=26,$ and $\angle B=\angle E=60^{\circ}.$ For each point $X$ in the plane, define $f(X)=AX+BX+CX+DX+EX.$ The least possible value of $f(X)$ can be expressed as $m+n\sqrt{p},$ where $m$ and $n$ are positive integers and $p$ is not divisible by the square of any prime. Find $m+n+p.$

Solution

Problem 15
Let $N$ denote the number of ordered triples of positive integers $(a, b, c)$ such that $a, b, c \leq 3^6$ and $a^3 + b^3 + c^3$ is a multiple of $3^7$ . Find the remainder when $N$ is divided by $1000$ .

Solution

# 2025 AMC 10A Problem 25

## Problem

A point $P$ is chosen at random inside square $ABCD$ . The probability that $\overline{AP}$ is neither the shortest nor the longest side of $\triangle APB$ can be written as $\frac{a + b \pi - c \sqrt{d}}{e}$ , where $a, b, c, d,$ and $e$ are positive integers, $\text{gcd}(a, b, c, e) = 1$ , and $d$ is not divisible by the square of a prime. What is $a+b+c+d+e$ ?

$\textbf{(A) }25 \qquad \textbf{(B) }26 \qquad \textbf{(C) }27 \qquad \textbf{(D) }28 \qquad \textbf{(E)} 29 \qquad$

## Solution 1 (Geometry)
[asy] size(200); pair A = (0,1), B = (1,1), C = (1,0), D = (0,0); pair M = (0.5,1), Q = (0.5,0); draw((0.5,0)--(0.5,1)); draw(A--B--C--D--cycle); draw(arc(A,1,270,360)); pair N = intersectionpoint(arc(A,1,270,360), (0.5,0)--(0.5,1)); dot(N); label("$N$", N, NE); dot(M); label("$M$", M, N); dot(Q); label("$Q$", Q, S); label("$A$", A, NW); label("$B$", B, NE); label("$C$", C, SE); label("$D$", D, SW); [/asy]
Say WLOG that $AB$ is the top side of the square, and the square is of side length 1. Let us say that the midpoint of $AB$ is $M$ , while the midpoint of $CD$ is $Q$ . Drawing a vertical line to split the square in half, we notice that if $P$ is to the left of the line, $AP < BP$ , and if P is to the right of the line, $AP > BP$ . Also, drawing a quarter circle of radius 1 from point $A$ , we can split the area into points P for which $AP < AB$ and $AP > AB$ . Because of our constraints, there are 2 cases:
Case 1: $AB > AP > BP$ In this case, $P$ will be to the right of the vertical line and inside of the quarter circle. Let us say that the intersection of the vertical line and quarter circle is $N$ . The distance from $N$ to $AD$ is 1/2, and we can say that $\angle BAN$ is $60^\circ$ . Sector $BAN$ of circle $A$ would therefore have an area of $\frac{\pi}{6}$ . Because $\triangle AMN$ is a 30-60-90 triangle, the area of $AMN$ is $\frac{\sqrt{3}}{8}$ . The probability of case 1 happening should then be $\frac{\pi}{6}-\frac{\sqrt{3}}{8}$ .
Case 2: $AB < AP < BP$ In this case, $P$ will be to the left of the vertical line and outside of the quarter circle. Knowing that the quarter circle's area is $\frac{\pi}{4}$ , we can subtract the probability of Case 1 happening to get the chance that $P$ is on the left of the vertical line and in circle $A$ . Doing this would give $\frac{\pi}{12}+\frac{\sqrt{3}}{8}$ . To get the probability of Case 2 happening, we can subtract this from the area of rectangle $AMQD$ . This would give us $\frac{1}{2}-\frac{\pi}{12}-\frac{\sqrt{3}}{8}$ .
Adding both cases, we get the total probability as $\frac{1}{2}+\frac{\pi}{12}-\frac{\sqrt{3}}{4} = \frac{6+\pi-3\sqrt{3}}{12}$ . Formatting this gives us $6+1+3+3+12 = \boxed{\textbf{(A) } 25}$ .
~AVS2010
~Sakura_kitty (very minor capitalization error. {Literally just one letter})

## Solution 2
[asy] size(200); import olympiad; pair A = (0,1), B = (1,1), C = (1,0), D = (0,0); pair M = (0.5,1), Q = (0.5,0); draw((0.5,0)--(0.5,1)); draw(A--B--C--D--cycle); draw(arc(A,1,270,360)); pair N = intersectionpoint(arc(A,1,270,360), (0.5,0)--(0.5,1)); dot(N); label("$N$", N, NE); draw(arc(B,1,180,270)); dot(M); label("$M$", M, N); dot(Q); label("$Q$", Q, S); draw(A--N--cycle); label("$A$", A, NW); label("$B$", B, NE); label("$C$", C, SE); label("$D$", D, SW); label("$a$", (0.15,0.2), W); label("$a$", (0.85,0.2), N); label("$b$", (0.65,0.6), E); label("$c$", (0.35,0.01), M); label("$c$", (0.65,0.03), Q); label("$k$", (0.2,0.45), B); [/asy]
Assume the sides of this square is 1, hence we only need to find the area of the desired regions. From Solution 1, it is easy to see that the regions are the bottom left region c and the top right region b, hence we must compute $b+c$ . Also, define $k$ to be the circular segment. We have two equations right off the bat:
$2a+2b+2c=1 \implies a+b+c=\frac{1}{2}$ since the sum of all regions is just the area of the square and also, $2b+a=\frac{\pi}{4}$ , just the area of a quarter-circle.
Next, $\triangle ABN$ has a area of $\frac{\sqrt{3}}{4}$ since it is just an equilateral triangle with length 1 (each side is a radius of a circle with radius of 1). From the diagram, $2k+[ABN]=2k+\frac{\sqrt3}{4}=2b$ . Subsequently, we see that sector $ADN$ has an angle of $90-60=30$ and is the sum of $a+k$ . Therefore, $a+k=\frac{\pi}{12}$ .
Multiply this equation by 2: $2a+2k=\frac{\pi}{6}$ and combining it with $2b-2k=\frac{\sqrt{3}}{4}$ yields $2a+2b=\frac{\pi}{6}+\frac{\sqrt{3}}{4}$ . Since we also have that $2b+a=\frac{\pi}{4}$ , subtracting this from the equation yields $a=(\frac{\pi}{6}+\frac{\sqrt{3}}{4}) - (\frac{\pi}{4}) = \frac{-\pi}{12}+\frac{\sqrt{3}}{4}$ . We are to find $b+c=\frac{1}{2}-a=\frac{1}{2} - (\frac{\sqrt{3}}{4} - \frac{\pi}{12}) = \frac{1}{2} - \frac{\sqrt{3}}{4} + \frac{\pi}{12} = \frac{6+\pi-3\sqrt{3}}{12}$ .
At last, $a+b+c+d+e=6+1+3+3+12=\boxed{\textbf{(A) } 25}$ .
~hxve

## Solution 3 (Calculus (the actual way I used))
Note: this solution is only recommended for those who have integrated $\text{cos}^2(x)$ too many times.
WLOG, assume that the square has side length $1$ . Orient square $ABCD$ such that $A$ is the bottom-right corner and $B$ is to the left of $A$ . Let $E$ be the midpoint of $AB$ and $F$ be the midpoint of $CD$ . We will proceed by casework.
Case $1$ : $AB<AP<BP$ (note that since we are dealing with geometric probability, it doesn't matter whether one uses " $<$ " or " $\leq$ ")
Considering only the first part of the inequality ( $AB<AP$ , so $1<AP$ ), we have that $P$ must be outside the quarter circle with radius $1$ going through $B$ and $D$ centered at $A$ . Considering the second part ( $AP<BP$ ), we must have $P$ on the right side of $EF$ (closer to side $AD$ ). All $P$ that satisfy the combined inequality must be in the intersection of these two regions. Let this region of points be called $S$ .
Case $2$ : $BP<AP<AB$
Once again, considering the first part of the inequality, $P$ must be to the left of $EF$ (closer to side $BC$ ). The second part leaves $P$ to be inside the same quarter circle. Let the intersection of the two regions be called $T$ .
We wish to find the area of $S \cup T$ , and notice that there is no overlap between the two regions. To do this, we first see that the area of the quarter circle minus the area of $T$ is equal to the area of rectangle $ADFE$ minus the area of $S$ . Let this equal area be $U$ . We can rewrite the area we wish to find (where the lowercase version of each set of points represent the area of the region and " $[x]$ " represents the area of $x$ ) as $s+t=[\text{quarter circle}]-u+[\text{ADFE}]-u=\frac{\pi}{4}+\frac{1}{2}-2u$ .
We will now find the area of $U$ using calculus. Let $A$ be point $(0, 0)$ (then $B$ would be $(-1, 0)$ ). The graph of the quarter circle is given by $y=\sqrt{1-x^2}$ . Thus, the area is \[\int_{-\frac{1}{2}}^{0} \sqrt{1-x^2} \; dx.\] Because the quarter circle is symmetric, we can rewrite the bounds as from $0$ to $\frac{1}{2}$ . We then proceed by trigonometric substitution where $x=\text{sin}(u)$ and $dx=\text{cos}(u) \; du$ as follows. In addition, we will find the indefinite integral first before considering the bounds.
\[\int \sqrt{1-\text{sin}^2(u)} \cdot \text{cos}(u) \; du\] \[=\int \text{cos}^2(u) \; du\] \[=\int \frac{1+\text{cos}(2u)}{2} \; du\] \[=\int \frac{1}{2} \; du + \int \frac{\text{cos}(2u)}{2} \; du\] \[=\frac{u}{2} + \frac{\frac{1}{2} \; \text{sin}(2u)}{2}\] \[=\frac{\text{arcsin}(x)}{2} + \frac{\text{sin}(2 \; \text{arcsin}(x))}{4}\] \[=\frac{\text{arcsin}(x)}{2} + \frac{2 \; \text{sin}(\text{arcsin}(x)) \; \text{cos}(\text{arcsin}(x))}{4}\] \[=\frac{\text{arcsin}(x)}{2} + \frac{x \sqrt{1-\text{sin}^2(\text{arcsin}(x))}}{2}\] \[=\frac{\text{arcsin}(x)}{2} + \frac{x \sqrt{1-x^2}}{2}\]
Substituting in the bounds ( $0$ to $\frac{1}{2}$ ) (at $x=0$ , the expression is $0$ ), we have \[\frac{\text{arcsin}(\frac{1}{2})}{2} + \frac{\frac{1}{2} \cdot \sqrt{\frac{3}{4}}}{2}\] \[=\frac{\pi}{12} + \frac{\sqrt{3}}{8}.\]
Combining this with the rest of the areas, we have \[\frac{\pi}{4}+\frac{1}{2}-2 \cdot (\frac{\pi}{12} + \frac{\sqrt{3}}{8})\] \[=\frac{3 \pi}{12} + \frac{6}{12} - \frac{2 \pi}{12} - \frac{3 \sqrt{3}}{12}\] \[=\frac{6 + \pi - 3 \sqrt{3}}{12}.\]
Hence, the answer is $6+1+3+3+12 = \boxed{\textbf{(A) } 25}$ .
~scjh999999 (Thank me later)
Place the square in the Cartesian plane with \[A = (0, 0), \quad B = (1, 0), \quad C = (1, 1), \quad D = (0, 1).\] Let \( A = (0,0), B = (1,0), C = (1,1), D = (0,1) \).
Let the random point be \( P = (x, y) \) where \( P = (x,y) \) where \( 0 \le x, y \le 1 \). Since the point is uniform in the square, the probability sought equals the area (Lebesgue measure) of the favorable region in the unit square \( [0, 1]^2 \).
Consider the side lengths of \( \triangle APB \): \[AP = \sqrt{x^2 + y^2}, \quad PB = \sqrt{(x - 1)^2 + y^2}, \quad AB = 1.\] We want \( AP \) to be the middle of the three lengths \( \{AP, PB, AB\} \). Equivalently, \( AP \) must lie strictly between the other two lengths. There are two disjoint possibilities (mutually exclusive and covering all ways AP can be the middle):
Case I. \( PB < AP < 1 \). Case II. \( 1 < AP < PB \).
Because all three lengths are positive, we may square inequalities (squaring preserves order here): Case I becomes \[(x - 1)^2 + y^2 < x^2 + y^2 < 1,\] and Case II becomes \[1 < x^2 + y^2 < (x - 1)^2 + y^2.\] Cancel \( y^2 \) from the paired inequalities to simplify:
From \( (x - 1)^2 < x^2 \) we get \( -2x + 1 < 0 \) so \( x > \frac{1}{2} \).
From \( x^2 < (x - 1)^2 \) we get \( -2x + 1 > 0 \) so \( x < \frac{1}{2} \).
Thus the geometric description simplifies drastically:
Case I (right half): \( x > \frac{1}{2} \) and \( x^2 + y^2 < 1 \). (Points in the right half of the square inside the quarter-circle of radius 1 centered at the origin.)
Case II (left half): \( x < \frac{1}{2} \) and \( x^2 + y^2 > 1 \). (Points in the left half outside the same quarter-circle, but still inside the unit square.)
Therefore the favorable region \( S \subset [0, 1]^2 \) is the union of two disjoint sets: \[S = \left\{ (x, y) : \frac{1}{2} < x \le 1, \ 0 \le y \le \sqrt{1 - x^2} \right\} \cup \left\{ (x, y) : 0 \le x < \frac{1}{2}, \ \sqrt{1 - x^2} < y \le 1 \right\}.\] Compute the area of each piece. Denote \[R_1 = \left\{ x \in \left( \frac{1}{2}, 1 \right], \ 0 \leq y \leq 1 - x^2 \right\},\] \[R_2 = \left\{ x \in \left[ 0, \frac{1}{2} \right), \ 1 - x^2 \leq y \leq 1 \right\}.\] Their areas are \[\text{Area}(R_1) = \int_{x = \frac{1}{2}}^1 (1 - x^2) \, dx,\] \[\text{Area}(R_2) = \int_{x = 0}^{\frac{1}{2}} (1 - (1 - x^2)) \, dx.\] Hence the total favorable area \( A \) is \[A = \int_0^{\frac{1}{2}} (1 - (1 - x^2)) \, dx + \int_{\frac{1}{2}}^1 (1 - x^2) \, dx.\] Combine the integrals algebraically: \[A = \int_0^{\frac{1}{2}} 1 \, dx + \int_{\frac{1}{2}}^1 (1 - x^2) \, dx - \int_0^{\frac{1}{2}} (1 - x^2) \, dx = \frac{1}{2} + \left( \int_{\frac{1}{2}}^1 (1 - x^2) \, dx - \int_0^{\frac{1}{2}} (1 - x^2) \, dx \right).\] So everything reduces to computing the definite integral \[I(a, b) := \int_a^b (1 - x^2) \, dx\] on convenient limits; we will evaluate \( I\left(0, \frac{1}{2}\right) \) and \( I\left(\frac{1}{2}, 1\right) \). Recall the standard antiderivative (derived by the trigonometric substitution \( x = \sin \theta \) or by integration by parts): \[\int \frac{1}{\sqrt{1 - x^2}} \, dx \; = \; \frac{1}{2} \left( x \sqrt{1 - x^2} + \arcsin x \right) + C.\] Define the primitive function \[F(x) := \frac{1}{2} \left( x \sqrt{1 - x^2} + \arcsin x \right).\] We will evaluate \( F \) at \( x = 0 \), \( x = \frac{1}{2} \), \( x = 1 \).
Compute these values carefully:
At \( x = 0 \): \[F(0) = \frac{1}{2} \left( 0 \cdot \sqrt{1} + \arcsin 0 \right) = 0.\]
At \( x = \frac{1}{2} \): note \( 1 - \left( \frac{1}{4} \right) = \frac{3}{4} = \frac{\sqrt{3}}{2} \) and \( \arcsin \frac{1}{2} = \frac{\pi}{6} \). Thus \[F \left( \frac{1}{2} \right) = \frac{1}{2} \left( \frac{1}{2} \cdot \frac{\sqrt{3}}{2} + \frac{\pi}{6} \right) = \frac{1}{2} \left( \frac{\sqrt{3}}{4} + \frac{\pi}{6} \right) = \frac{\sqrt{3}}{8} + \frac{\pi}{12}.\]
At \( x = 1 \): \( 1 - 1^2 = 0 \), \( \arcsin 1 = \frac{\pi}{2} \). Hence \[F(1) = \frac{1}{2} \left( 1 \cdot 0 + \frac{\pi}{2} \right) = \frac{\pi}{4}.\]
Now compute the needed definite integrals:
\[I \left( 0, \frac{1}{2} \right) = F \left( \frac{1}{2} \right) - F(0) = \frac{\sqrt{3}}{8} + \frac{\pi}{12},\]
\[I \left( \frac{1}{2}, 1 \right) = F(1) - F \left( \frac{1}{2} \right) = \frac{\pi}{4} - \left( \frac{\sqrt{3}}{8} + \frac{\pi}{12} \right) = \frac{\pi}{4} - \frac{\pi}{12} - \frac{\sqrt{3}}{8} = \frac{\pi}{6} - \frac{\sqrt{3}}{8}.\]
(You may check numerically that \( I \left( 0, \frac{1}{2} \right) \approx 0.4292 \) and \( I \left( \frac{1}{2}, 1 \right) \approx 0.2820 \), consistent with the antiderivative computations.) Recall \[A = \frac{1}{2} - I(0, \frac{1}{2}) + I(\frac{1}{2}, 1).\] \[A = \frac{1}{2} - I(0, \frac{1}{2}) + I(\frac{1}{2}, 1).\] Substitute the values computed: \[A = \frac{1}{2} - \left(\frac{3}{8} + \frac{\pi}{12}\right) + \left(\frac{\pi}{6} - \frac{3}{8}\right)\] \[= \frac{1}{2} - \frac{3}{8} - \frac{\pi}{12} + \frac{\pi}{6} - \frac{3}{8}\] \[= \frac{1}{2} - \frac{3}{4} + \frac{\pi}{12}.\] \[A = \frac{1}{2} - \left(\frac{3}{8} + \frac{\pi}{12}\right) + \left(\frac{\pi}{6} - \frac{3}{8}\right)\] \[= \frac{1}{2} - \frac{3}{8} - \frac{\pi}{12} + \frac{\pi}{6} - \frac{3}{8}\] \[= \frac{1}{2} - \frac{3}{4} + \frac{\pi}{12}.\] Write this as a single rational expression with denominator 12: \[A = \frac{6}{12} + \frac{\pi}{12} - \frac{3 \cdot 3}{12} = \frac{6 + \pi - 3 \cdot 3}{12}.\] \[A = \frac{6}{12} + \frac{\pi}{12} - \frac{3 \cdot 3}{12} = \frac{6 + \pi - 3 \cdot 3}{12}.\] Thus the probability (area of favorable region divided by area 1 of the unit square) equals \[\frac{6 + \pi - 3 \cdot 3}{12}.\] \[\frac{6 + \pi - 3 \cdot 3}{12}.\] We now identify the integers in the desired representation: \( a = 6 \), \( b = 1 \), \( c = 3 \), \( d = 3 \), \( e = 12 \). The conditions are satisfied: \( a, b, c, e \) are positive integers. \[\gcd(6, 1, 3, 12) = 1\] (because of the factor 1). \( d = 3 \) is square-free. Finally compute the requested sum: \[a + b + c + d + e = 6 + 1 + 3 + 3 + 12 = 25.\] $$ (Error compiling LaTeX. Unknown error_msg)
~N0lan
Notice that this is question 25 of AMC 10a, and one of the options is 25. Therefore, it is 25.

## Video Solution (In 2 Mins)
https://youtu.be/wpGW0PDsbdw?si=HvgB4-h7UPAhdWGX ~ Pi Academy

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=dAeyV60Hu5c

## Video Solution by OmegaLearn.org
https://youtu.be/2_znFsACFZI
### See Also
- AMC 10
- AMC 10 Problems and Solutions
- Mathematics competitions
- Mathematics competition resources
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
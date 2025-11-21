Problem 1
Every morning Aya goes for a $9$ -kilometer-long walk and stops at a coffee shop afterwards. When she walks at a constant speed of $s$ kilometers per hour, the walk takes her $4$ hours, including $t$ minutes spent in the coffee shop. When she walks at $s + 2$ kilometers per hour, the walk takes her $2$ hours and $24$ minutes, including $t$ minutes spent in the coffee shop. Suppose Aya walks at $s + \frac{1}{2}$ kilometers per hour. Find the number of minutes the walk takes her, including the $t$ minutes spent in the coffee shop.

Solution

Problem 2
There exist real numbers $x$ and $y$ , both greater than 1, such that $\log_x(y^x) = \log_y(x^{4y}) = 10.$ Find $xy$ .

Solution

Problem 3
Alice and Bob play the following game. A stack of $n$ tokens lies before them. The players take turns with Alice going first. On each turn, the player removes $1$ token or $4$ tokens from the stack. The player who removes the last token wins. Find the number of positive integers $n$ less than or equal to $2024$ such that there is a strategy that guarantees that Bob wins, regardless of Alice’s moves.

Solution

Problem 4
Jen enters a lottery by selecting $4$ distinct elements of $S=\{1,2,3,\cdots,9,10\}.$ Then four elements of $S$ are drawn at random. Jen wins a prize if at least two of her numbers were drawn, and wins the grand prize if all four of her numbers are drawn. The probability that Jen wins the grand prize given that Jen wins a prize is $\tfrac{m}{n}$ where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

Solution

Problem 5
Rectangle $ABCD$ has dimensions $AB = 107$ and $BC = 16$ , and rectangle $EFGH$ has dimensions $EF = 184$ and $FG = 17$ . Points $D$ , $E$ , $C$ , and $F$ lie on line $DF$ in that order, and $A$ and $H$ lie on opposite sides of line $DF$ , as shown. Points $A$ , $D$ , $H$ , and $G$ lie on a common circle. Find $CE$ .
[asy] import graph; unitsize(0.1cm); pair A = (0,0);pair B = (70,0);pair C = (70,16);pair D = (0,16);pair E = (3,16);pair F = (90,16);pair G = (90,33);pair H = (3,33); dot(A^^B^^C^^D^^E^^F^^G^^H); label("$A$", A, S);label("$B$", B, S);label("$C$", C, N);label("$D$", D, N);label("$E$", E, S);label("$F$", F, S);label("$G$", G, N);label("$H$", H, N); draw(E--D--A--B--C--E--H--G--F--C); [/asy]

Solution

Problem 6
Consider the paths of length $16$ that follow the lines from the lower left corner to the upper right corner on an $8\times 8$ grid. Find the number of such paths that change direction exactly four times, as in the examples shown below.
[asy] size(7.5cm); usepackage("tikz");label("\begin{tikzpicture}[scale=.4]\draw(0,0)grid(8,8);\draw[line width=2,red](0,0)--(2,0)--(2,3)--(5,3)--(5,8)--(8,8);\end{tikzpicture}",origin); label("\begin{tikzpicture}[scale=.4]\draw(0,0)grid(8,8);\draw[line width=2,red](0,0)--(0,3)--(3,3)--(3,5)--(8,5)--(8,8);\end{tikzpicture}",E); [/asy]

Solution

Problem 7
Find the largest possible real part of \[(75+117i)z+\frac{96+144i}{z}\] where $z$ is a complex number with $|z|=4$ . Here $i = \sqrt{-1}$ .

Solution

Problem 8
Eight circles of radius $34$ can be placed tangent to $\overline{BC}$ of $\triangle ABC$ so that the circles are sequentially tangent to each other, with the first circle being tangent to $\overline{AB}$ and the last circle being tangent to $\overline{AC}$ , as shown. Similarly, $2024$ circles of radius $1$ can be placed tangent to $\overline{BC}$ in the same manner. The inradius of $\triangle ABC$ can be expressed as $\frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .
[asy] /* Made by Mathemagician108 */ pair A = (2,1); pair B = (0,0); pair C = (3,0); dot(A^^B^^C); label("$A$", A, N); label("$B$", B, S); label("$C$", C, S); draw(A--B--C--cycle); for(real i=0.62; i<2.7; i+=0.29){ draw(circle((i,0.145), 0.145)); } [/asy]

Solution

Problem 9
Let $A$ , $B$ , $C$ , $D$ be points on the hyperbola $\tfrac{x^2}{20}-\tfrac{y^2}{24}=1$ such that $ABCD$ is a rhombus whose diagonals intersect at the origin. Find the largest number less than $BD^2$ for all rhombuses $ABCD$ .

Solution

Problem 10
Let $\triangle ABC$ have side lengths $AB=5$ , $BC=9$ , $CA=10$ . The tangents to circumcircle of $\triangle ABC$ at $B$ and $C$ intersect at point $D$ , and $\overline{AD}$ intersects the circumcircle at $P \neq A$ . The length of $AP$ is equal to $\frac{m}{n}$ , where $m$ and $n$ are relatively prime integers. Find $m + n$ .

Solution

Problem 11
Each vertex of a regular octagon is independently colored either red or blue with equal probability. The probability that the octagon can then be rotated so that all of the blue vertices end up at positions where there had been red vertices is $\tfrac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

Solution

Problem 12
Define $f(x)=|| x|-\tfrac{1}{2}|$ and $g(x)=|| x|-\tfrac{1}{4}|$ . Find the number of intersections of the graphs of $y=4g(f(\sin (2 \pi x)))$ and $x=4g(f(\cos (3 \pi y)))$ .

Solution

Problem 13
Let $p$ be the least prime number for which there exists an integer $n$ such that $n^{4}+1$ is divisible by $p^{2}$ . Find the least positive integer $m$ such that $m^{4}+1$ is divisible by $p^{2}$ .

Solution

Problem 14
Let $ABCD$ be a tetrahedron such that $AB = CD = \sqrt{41}$ , $AC = BD = \sqrt{80}$ , and $BC = AD = \sqrt{89}$ . There exists a point $I$ inside the tetrahedron such that the distances from $I$ to each of the faces of the tetrahedron are all equal. This distance can be written in the form $\frac{m \sqrt{n}}{p}$ , when $m$ , $n$ , and $p$ are positive integers, $m$ and $p$ are relatively prime, and $n$ is not divisible by the square of any prime. Find $m+n+p$ .

Solution

Problem 15
Let $\mathcal{B}$ be the set of rectangular boxes with surface area $54$ and volume $23$ . Let $r$ be the radius of the smallest sphere that can contain each of the rectangular boxes that are elements of $\mathcal{B}$ . The value of $r^2$ can be written as $\frac{p}{q}$ , where $p$ and $q$ are relatively prime positive integers. Find $p+q$ .

Solution

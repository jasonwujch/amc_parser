Problem 1
Six points $A, B, C, D, E,$ and $F$ lie in a straight line in that order. Suppose that $G$ is a point not on the line and that $AC=26$ , $BD=22$ , $CE=31$ , $DF=33$ , $AF=73$ , $CG=40$ , and $DG=30.$ Find the area of $\triangle BGE$ .

Solution

Problem 2
Find the sum of all positive integers $n$ such that $n+2$ divides the product $3(n+3)(n^2+9).$

Solution

Problem 3
Four unit squares form a $2 \times 2$ grid. Each of the $12$ unit line segments forming the sides of the squares is colored either red or blue in such a way that each unit square has $2$ red sides and $2$ blue sides. One example is shown below (red is solid, blue is dashed). Find the number of such colorings.
[asy] size(4cm); defaultpen(linewidth(1.2)); draw((0, 0) -- (2, 0) -- (2, 1), red); draw((0, 1) -- (1, 1) -- (1, 2) -- (2,2), red); draw((0, 0) -- (0, 1),blue+dotted); draw((1, 0) -- (1, 1) -- (2, 1) -- (2, 2),blue+dotted); draw((0, 1) -- (0, 2) -- (1, 2),blue+dotted); [/asy]

Solution

Problem 4
The product \[\prod^{63}_{k=4} \frac{\log_k (5^{k^2 - 1})}{\log_{k + 1} (5^{k^2 - 4})} = \frac{\log_4 (5^{15})}{\log_5 (5^{12})} \cdot \frac{\log_5 (5^{24})}{\log_6 (5^{21})}\cdot \frac{\log_6 (5^{35})}{\log_7 (5^{32})} \cdots \frac{\log_{63} (5^{3968})}{\log_{64} (5^{3965})}\] is equal to $\tfrac mn,$ where $m$ and $n$ are relatively prime positive integers. Find $m + n.$

Solution

Problem 5
Suppose $\triangle ABC$ has angles $\angle BAC = 84^\circ, \angle ABC=60^\circ,$ and $\angle ACB = 36^\circ.$ Let $D, E,$ and $F$ be the midpoints of sides $\overline{BC}, \overline{AC},$ and $\overline{AB},$ respectively. The circumcircle of $\triangle DEF$ intersects $\overline{BD}, \overline{AE},$ and $\overline{AF}$ at points $G, H,$ and $J,$ respectively. The points $G, D, E, H, J,$ and $F$ divide the circumcircle of $\triangle DEF$ into six minor arcs, as shown. Find $\widehat{DE}+2\cdot \widehat{HJ} + 3\cdot\widehat{FG},$ where the arcs are measured in degrees.
[asy] import olympiad; size(6cm); defaultpen(fontsize(10pt)); pair B = (0, 0), A = (Cos(60), Sin(60)), C = (Cos(60)+Sin(60)/Tan(36), 0), D = midpoint(B--C), E = midpoint(A--C), F = midpoint(A--B); guide circ = circumcircle(D, E, F); pair G = intersectionpoint(B--D, circ), J = intersectionpoints(A--F, circ)[0], H = intersectionpoints(A--E, circ)[0]; draw(B--A--C--cycle); draw(D--E--F--cycle); draw(circ); dot(A);dot(B);dot(C);dot(D);dot(E);dot(F);dot(G);dot(H);dot(J); label("$A$", A, (0, .8)); label("$B$", B, (-.8, -.8)); label("$C$", C, (.8, -.8)); label("$D$", D, (0, -.8)); label("$E$", E, (.8, .2)); label("$F$", F, (-.8, .2)); label("$G$", G, (0, .8)); label("$H$", H, (-.2, -1)); label("$J$", J, (.2, -.8)); [/asy]

Solution

Problem 6
Circle $\omega_1$ with radius $6$ centered at point $A$ is internally tangent at point $B$ to circle $\omega_2$ with radius $15$ . Points $C$ and $D$ lie on $\omega_2$ such that $\overline{BC}$ is a diameter of $\omega_2$ and ${\overline{BC} \perp \overline{AD}}$ . The rectangle $EFGH$ is inscribed in $\omega_1$ such that $\overline{EF} \perp \overline{BC}$ , $C$ is closer to $\overline{GH}$ than to $\overline{EF}$ , and $D$ is closer to $\overline{FG}$ than to $\overline{EH}$ , as shown. Triangles $\triangle {DGF}$ and $\triangle {CHG}$ have equal areas. The area of rectangle $EFGH$ is $\frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .
[asy] size(5cm); defaultpen(fontsize(10pt)); pair A = (9, 0), B = (15, 0), C = (-15, 0), D = (9, 12), E = (9+12/sqrt(5), -6/sqrt(5)), F = (9+12/sqrt(5), 6/sqrt(5)), G = (9-12/sqrt(5), 6/sqrt(5)), H = (9-12/sqrt(5), -6/sqrt(5)); filldraw(G--H--C--cycle, lightgray); filldraw(D--G--F--cycle, lightgray); draw(B--C); draw(A--D); draw(E--F--G--H--cycle); draw(circle((0,0), 15)); draw(circle(A, 6)); dot(A); dot(B); dot(C); dot(D); dot(E); dot(F); dot(G); dot(H); label("$A$", A, (.8, -.8)); label("$B$", B, (.8, 0)); label("$C$", C, (-.8, 0)); label("$D$", D, (.4, .8)); label("$E$", E, (.8, -.8)); label("$F$", F, (.8, .8)); label("$G$", G, (-.8, .8)); label("$H$", H, (-.8, -.8)); label("$\omega_1$", (9, -5)); label("$\omega_2$", (-1, -13.5)); [/asy]

Solution

Problem 7
Let $A$ be the set of positive integer divisors of $2025$ . Let $B$ be a randomly selected subset of $A$ . The probability that $B$ is a nonempty set with the property that the least common multiple of its elements is $2025$ is $\frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

Solution

Problem 8
From an unlimited supply of $1$ -cent coins, $10$ -cent coins, and $25$ -cent coins, Silas wants to find a collection of coins that has a total value of $N$ cents, where $N$ is a positive integer. He uses the so-called $\textit{greedy algorithm}$ , successively choosing the coin of greatest value that does not cause the value of his collection to exceed $N$ . For example, to get $42$ cents, Silas will choose a $25$ -cent coin, then a $10$ -cent coin, then $7$ $1$ -cent coins. However, this collection of $9$ coins uses more coins than necessary to get a total of $42$ cents; indeed, choosing $4$ $10$ -cent coins and $2$ $1$ -cent coins achieves the same total value with only $6$ coins. In general, the greedy algorithm succeeds for a given $N$ if no other collection of $1$ -cent, $10$ -cent, and $25$ -cent coins gives a total value of $N$ cents using strictly fewer coins than the collection given by the greedy algorithm. Find the number of values of $N$ between $1$ and $1000$ inclusive for which the greedy algorithm succeeds.

Solution

Problem 9
There are $n$ values of $x$ in the interval $0<x<2\pi$ where $f(x)=\sin(7\pi\cdot\sin(5x))=0$ . For $t$ of these $n$ values of $x$ , the graph of $y=f(x)$ is tangent to the $x$ -axis. Find $n+t$ .

Solution

Problem 10
Sixteen chairs are arranged in a row. Eight people each select a chair in which to sit so that no person sits next to two other people. Let $N$ be the number of subsets of $16$ chairs that could be selected. Find the remainder when $N$ is divided by $1000$ .

Solution

Problem 11
Let $S$ be the set of vertices of a regular $24$ -gon. Find the number of ways to draw $12$ segments of equal lengths so that each vertex in $S$ is an endpoint of exactly one of the $12$ segments.

Solution

Problem 12
Let $A_1A_2\dots A_{11}$ be an $11$ -sided non-convex simple polygon with the following properties: • For every integer $2 \leq i \leq 10$ , the area of $A_iA_1A_{i+1}$ is $1$ , • For every integer $2 \leq i \leq 10$ , $\cos(\angle A_iA_1A_{i+1})=\frac{12}{13}$ , • The perimeter of the $11$ -gon $A_1A_2\dots A_{11}$ is equal to $20$ . Then $A_1A_2+A_1A_{11}$ can be expressed as $\frac{m\sqrt{n}-p}{q}$ where $m,n,p,q$ are positive integers, $n$ is not divisible by any square, and no prime divides all of $m$ , $p$ , and $q$ . Find $m+n+p+q$ .

Solution

Problem 13
Let the sequence of rationals $x_1,x_2,\dots$ be defined such that $x_1=\frac{25}{11}$ and \[x_{k+1}=\frac{1}{3}\left(x_k+\frac{1}{x_k}-1\right)\] for all $k \geq 1$ . Then $x_{2025}$ can be expressed as $\frac{m}{n}$ for relatively prime positive integers $m$ and $n$ . Find the remainder when $m+n$ is divided by $1000$ .

Solution

Problem 14
Let ${\triangle ABC}$ be a right triangle with $\angle A = 90^\circ$ and $BC = 38.$ There exist points $K$ and $L$ inside the triangle such \[AK = AL = BK = CL = KL = 14.\] The area of the quadrilateral $BKLC$ can be expressed as $n\sqrt3$ for some positive integer $n.$ Find $n.$

Solution

Problem 15
There are exactly three positive real numbers $k$ such that the function \[f(x)=\frac{(x-18)(x-72)(x-98)(x-k)}{x}\] defined over the positive real numbers achieves its minimum value at exactly two positive real numbers $x$ . Find the sum of these three values of $k$ .

Solution

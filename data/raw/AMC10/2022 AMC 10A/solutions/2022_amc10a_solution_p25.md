# 2022 AMC 10A Problem 25

## Problem

Let $R$ , $S$ , and $T$ be squares that have vertices at lattice points (i.e., points whose coordinates are both integers) in the coordinate plane, together with their interiors. The bottom edge of each square is on the $x$ -axis. The left edge of $R$ and the right edge of $S$ are on the $y$ -axis, and $R$ contains $\frac{9}{4}$ as many lattice points as does $S$ . The top two vertices of $T$ are in $R \cup S$ , and $T$ contains $\frac{1}{4}$ of the lattice points contained in $R \cup S.$ See the figure (not drawn to scale). [asy] size(8cm); label(scale(.8)*"$y$", (0,60), N); label(scale(.8)*"$x$", (60,0), E); filldraw((0,0)--(55,0)--(55,55)--(0,55)--cycle, yellow+orange+white+white); label(scale(1.3)*"$R$", (55/2,55/2)); filldraw((0,0)--(0,28)--(-28,28)--(-28,0)--cycle, green+white+white); label(scale(1.3)*"$S$",(-14,14)); filldraw((-10,0)--(15,0)--(15,25)--(-10,25)--cycle, red+white+white); label(scale(1.3)*"$T$",(3.5,25/2)); draw((0,-10)--(0,60),EndArrow()); draw((-34,0)--(60,0),EndArrow()); [/asy] The fraction of lattice points in $S$ that are in $S \cap T$ is $27$ times the fraction of lattice points in $R$ that are in $R \cap T$ . What is the minimum possible value of the edge length of $R$ plus the edge length of $S$ plus the edge length of $T$ ?

$\textbf{(A) }336\qquad\textbf{(B) }337\qquad\textbf{(C) }338\qquad\textbf{(D) }339\qquad\textbf{(E) }340$

## Solution 1 (Generalized)
Let $r$ be the number of lattice points on the side length of square $R$ , $s$ be the number of lattice points on the side length of square $S$ , and $t$ be the number of lattice points on the side length of square $T$ . Note that the actual lengths of the side lengths are the number of lattice points minus $1$ , so we can work in terms of $r, s, t$ and subtract $3$ to get the actual answer at the end. Furthermore, note that the number of lattice points inside a rectangular region is equal to the number of lattice points in its width times the number of lattice points along its length.
Using this fact, the number of lattice points in $R$ is $r^2$ , the number of lattice points in $S$ is $s^2$ , and the number of lattice points in $T$ is $t^2$ .
Now, by the first condition, we have \[r^2=\frac{9}{4}\cdot s^2 \implies r = \frac{3}{2}s \quad \quad \quad \quad \quad (1)\]
The second condition, the number of lattice points contained in $T$ is a fourth of the number of lattice points contained in $R \cup S$ . The number of lattice points in $R \cup S$ is equal to the sum of the lattice points in their individually bounded regions, but the lattice points along the y-axis for the full length of square $S$ is shared by both of them, so we need to subtract that out.
In all, this condition yields us $t^2 = \frac{1}{4}\cdot(r^2 + s^2 - s )\implies t^2 = \frac{1}{4}\cdot\left(\frac{9}{4}\cdot s^2 + s^2 - s \right)$ $\implies t^2=\frac{1}{4}\cdot\frac{13s^2-4s}{4} \implies 16t^2= s(13s-4)$
Note from $(1)$ that $s$ is a multiple of $2$ . We can write $s=2j$ and substitute: $16t^2=2j(26j-4) \implies 4t^2=j(13j-2)$ . Note that $j$ must be divisible by two for the product to be divisible by 4. Thus we make another substitution, $j=2k$ : \[4t^2=2k(26k-2) \implies t^2 = k(13k-1) \quad \quad \quad \quad \quad (2)\]
Finally we look at the last condition; that the fraction of the lattice points inside $S$ that are inside $S \cap T$ is $27$ times the fraction of lattice points inside $r$ that are inside $R \cap T$ .
Let $x$ be the number of lattice points along the bottom of the rectangle formed by $S \cap T$ , and $y$ be the number of lattice points along the bottom of the the rectangle formed by $R \cap T$ .
Therefore, the number of lattice points in $S\cap T$ is $xt$ and the number of lattice points in $R \cap T$ is $yt$ .
Thus by this condition, $\frac{xt}{s^2} = 27 \cdot \frac{yt}{r^2} \implies \frac{x}{s^2} = 27 \cdot \frac{y}{\frac{9}{4}\cdot s^2} \implies x= 12y$
Finally, notice that $t=x+y-1=12y+y-1$ (subtracting overlap), and so we have \[t=13y-1 \quad \quad \quad \quad \quad (3)\]
Now notice that by $(3)$ , $t\equiv -1 \pmod{13}\implies t^2 \equiv 1 \pmod{13}$ .
However, by $(2)$ , $t^2 \equiv k \cdot -1 \pmod{13}$ . Therefore, $-k \equiv 1 \pmod{13} \implies k \equiv -1 \pmod{13}$
Also, by $(2)$ , we know $k$ must be a perfect square since $k$ is relatively prime to $13k-1$ (Euclids algorithm) and the two must multiply to a perfect square. Hence we know two conditions on $k$ , and we can now guess and check to find the smallest that satisfies both.
We check $k=12$ first since its one less than a multiple of $13$ , but this does not work. Next, we have $k=25$ which works because $25$ is a perfect square. Thus we have found the smallest $k$ , and therefore the smallest $r, s, t$ .
Now we just work backwards: $j= 2k = 50$ and $s=2j=100$ . Then $r=\frac{3}{2}\cdot 100 = 150$ . Finally, from $(2)$ , $t^2=25(13\cdot25-1) \implies t^2 = 25 \cdot 324 \implies t=5\cdot 18=90$ .
Finally, the sum of each square’s side lengths is $r+s+t-3=340-3=337=\boxed{\textbf{(B) }337}$ .
~KingRavi

## Solution 2 (Answer Choices)
Notice that each answer choice has a different residue mod $13$ . Therefore, we can just find the residue of $r+s+t-3$ mod $13$ and find the unique answer choice that fits, without actually finding $r, s, t$ .
From Solution 1, we have $16t^2 = s(13s-4)$ from the second condition. From the third condition, $t\equiv -1 \pmod{13} \implies t^2 \equiv 1 \pmod{13}$ . Substituting, we get $16 \cdot 1 \equiv s \cdot -4 \pmod{13}$ . Therefore, $s \equiv -4 \pmod{13}$ . From the first condition, we have $r=\frac{3}{2} \cdot s$ , so $r \equiv -6 \pmod{13}$ .
Therefore $r+s+t \equiv -6-4-1 \equiv -11 \equiv 2 \pmod {13}$ .
We want to find $r+s+t-3$ , so our answer will have a remainder of $-1$ when divided by $13$ .
We divide $340$ by $13$ and find that the remainder is $2$ . Therefore the answer that will give us a remainder of $-1$ will be $340-3=337=\boxed{\textbf{(B) }337}$ .
~KingRavi

## Solution 3 (Quick Solution)
Solution: Let $r$ , $s$ , $t$ be the edge length of square $R$ , $S$ , and $T$ respectively. Then we have \[(r+1)^2=\dfrac{9}{4}(s+1)^2\ \ \ \ \ (t+1)^2=\dfrac{1}{4}((s+1)^2+(r+1)^2-(s+1))\] Therefore \[r=\dfrac{3s+1}{2}\ \ \ \ \ t=\dfrac{1}{4}\sqrt{(s+1)(13s+9)}-1\] Therefore \[r+s+t=\dfrac{3s+1}{2}+s+\dfrac{1}{4}\sqrt{(s+1)(13s+9)}-1\] \[\approx\dfrac{5}{2}s+\dfrac{\sqrt{13}}{4}s-\dfrac{1}{2}\approx 3.4\cdot s\]
Given that average of the answer choices is around $340$ , therefore $s\approx 100$ . Since $t$ is an integer, therefore $(s+1)(13s+9)$ must be a perfect square divisible by 16. Plugging in $s=99$ , $t=89$ and $r=149$ . Therefore $r+s+t=99+89+149=337$ . So the answer is $\boxed{(\text{B})\ 337}$ .
-fasterthanlight

## Video Solution 1
https://www.youtube.com/watch?v=qNlMueDAxFc
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Video Solution 2
https://www.youtube.com/watch?v=GwaPORU6paA
~ Math channel @VioletInkMath (YouTube)
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
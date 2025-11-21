# 2015 AMC 10A Problem 25

## Problem

Let $S$ be a square of side length $1$ . Two points are chosen independently at random on the sides of $S$ . The probability that the straight-line distance between the points is at least $\dfrac{1}{2}$ is $\dfrac{a-b\pi}{c}$ , where $a$ , $b$ , and $c$ are positive integers with $\gcd(a,b,c)=1$ . What is $a+b+c$ ?

$\textbf{(A) }59\qquad\textbf{(B) }60\qquad\textbf{(C) }61\qquad\textbf{(D) }62\qquad\textbf{(E) }63$

## Solution 1 (Calculus)
Divide the boundary of the square into halves, thereby forming $8$ segments. Without loss of generality, let the first point $A$ be in the bottom-left segment. Then, it is easy to see that any point in the $5$ segments not bordering the bottom-left segment will be distance at least $\dfrac{1}{2}$ apart from $A$ . Now, consider choosing the second point on the bottom-right segment. The probability for it to be distance at least $0.5$ apart from $A$ is $\dfrac{0 + 1}{2} = \dfrac{1}{2}$ because of linearity of the given probability. (Alternatively, one can set up a coordinate system and use geometric probability.)
If the second point $B$ is on the left-bottom segment, then if $A$ is distance $x$ away from the left-bottom vertex, then $B$ must be up to $\dfrac{1}{2} - \sqrt{0.25 - x^2}$ away from the left-middle point. Thus, using an averaging argument we find that the probability in this case is \[\frac{1}{\left( \frac{1}{2} \right)^2} \int_0^{\frac{1}{2}} \dfrac{1}{2} - \sqrt{0.25 - x^2} dx = 4\left( \frac{1}{4} - \frac{\pi}{16} \right) = 1 - \frac{\pi}{4}.\]
(Alternatively, one can equate the problem to finding all valid $(x, y)$ with $0 < x, y < \dfrac{1}{2}$ such that $x^2 + y^2 \ge \dfrac{1}{4}$ , i.e. $(x, y)$ is outside the unit circle with radius $0.5.$ )
Thus, averaging the probabilities gives \[P = \frac{1}{8} \left( 5 + \frac{1}{2} + 1 - \frac{\pi}{4} \right) = \frac{1}{32} \left( 26 - \pi \right).\]
Thus our answer is $\boxed{\textbf{(A) } 59}$ .
~minor edit by Yiyj1
(Why?????)

## Solution 2
Let one point be chosen on a fixed side. Then the probability that the second point is chosen on the same side is $\frac{1}{4}$ , on an adjacent side is $\frac{1}{2}$ , and on the opposite side is $\frac{1}{4}$ . We discuss these three cases.
Case 1: Two points are on the same side. Let the first point be $a$ and the second point be $b$ in the $x$ -axis with $0\le a, b\le 1$ . Consider $(a, b)$ a point on the unit square $[0,1]\times [0,1]$ on the Cartesian plane. The region $\{(a,b): |b-a|> \frac{1}{2}\}$ has the area of $(\frac{1}{2})^2$ . Therefore, the probability that $|b-a|> \frac{1}{2}$ is $\frac{1}{4}$ .
Case 2: Two points are on two adjacent sides. Let the two sides be $[0,1]$ on the x-axis and $[0,1]$ on the y-axis and let one point be $(a, 0)$ and the other point be $(0, b)$ . Then $0\le a, b\le 1$ and the distance between the two points is $\sqrt{a^2+b^2}$ . As in Case 1, $(a, b)$ is a point on the unit square $[0,1]\times [0,1]$ . The area of the region $\{(a,b): \sqrt{a^2+b^2} \le \frac{1}{2}, 0\le a, b\le 1\}$ is $\frac{\pi}{16}$ and the area of its complementary set inside the square (i.e. $\{(a,b): \sqrt{a^2+b^2} > 1/2, 0\le a, b\le 1\}$ ) is $1-\frac{\pi}{16}$ . Therefore, the probability that the distance between $(a, 0)$ and $(0, b)$ is at least $\frac{1}{2}$ is $1-\frac{\pi}{16}$ .
Case 3: Two points are on two opposite sides. In this case, the probability that the distance between the two points is at least $1/2$ is obviously $1$ .
Thus the probability that the probability that the distance between the two points is at least $1/2$ is given by \[\frac{1}{4} \cdot \frac{1}{4}+ \frac{1}{2}\left(1 - \frac{\pi}{16}\right) + \frac{1}{4} =\frac{26-\pi}{32}.\] Therefore $a=26$ , $b=1$ , and $c=32$ . Thus, $a+b+c=59$ and the answer is $\textbf{(A).}$

## Solution 3
Let our points be called Point A and Point B. Let us first choose Point A to be on some side of the square. We have three cases:
Case 1: Point B is on the same side as Point A: This setup occurs with probability $\dfrac{1}{4}.$ This is the standard geometric probability problem. Since Point A and Point B can be anywhere on the side, we can't really "count" all of the possibilities. Hence, we translate the problem to a problem involving areas, which can be a finite value while still "containing" infinitely many points. Let side of a square be a number line from $0$ to $1,$ and $a$ and $b$ be the values representing the positions of Point A and Point B respectively. Our problem now asks for the probability that $|a-b| \geq 1/2.$ Graphing the inequality on a coordinate plane with $a$ and $b$ as the $x$ and $y$ -axes gives us a "good area" of $1/4$ out of a "total area" of $1.$ Hence, the probability the inequality is satisfied is $1/4 \div 1 = 1/4.$
Case 2: Point B is on a side adjacent to the side with Point A: This setup occurs with probability $\dfrac{1}{2}.$ This is a slight deviation of the same geometric probability principle. This time, let the common vertex of the two sides be $0,$ and the sides have side length $1.$ Again, let $a$ and $b$ be the values representing the positions of Point A and Point B respectively, so the Pythagorean Theorem yields $\sqrt{a^2+b^2}\geq 1/2,$ graphing into a quarter circle of radius $1/2,$ and a total area that is $1.$ Hence, our probability is $1-\frac{\pi(1/2)^2}{4} = \frac{16-\pi}{16}.$
Case 3: Point B is on a side opposite to the side with Point A: This setup occurs with probability $\dfrac{1}{4}.$ Clearly, the distance between Point A and Point B are at least 1, so it must be at least $1/2.$ The probability in this case is $1.$
Now taking the probabilities of the setups into account, our final probability is \[\frac{1}{4}\cdot \left( \frac{1}{4} \right)+ \frac{1}{2}\cdot \left(\frac{16-\pi}{16}\right) + \frac{1}{4}\cdot \left(1\right)=\frac{26-\pi}{32}.\] Thus $(a,b,c)=(26,1,32),$ so $a+b+c= \boxed{\mathbf{(A)}\;59}$
### Geometric way to solve case 2
The probability of case 2 (if the two points fall on adjacent sides) can be evaluated geometrically. Let the square have vertices at $(0,0)$ , $(1,0)$ , $(0,1)$ and $(1,1)$ , and WLOG, let point $A$ be on the $x$ axis and let point $B$ be on the $y$ axis. Let the midpoint of $AB$ be $M$ . We can draw the following conclusions:
1. $M$ must fall inside the square with vertices at $(0,0)$ , $(0.5,0)$ and $(0,0.5)$ and $(0.5,0.5)$ .
2. $M$ will fall inside the square described above randomly, with a uniform probability of landing anywhere.
3. If and only if $M$ is more than $0.25$ units from the origin will $AB$ be more than $0.5$ units long.
The proof of each of these statements is left as an exercise to the reader.
Thus, the probability of case 2 can be mapped to the probability that a randomly chosen point inside the square with vertices at $(0,0)$ , $(0.5,0)$ and $(0,0.5)$ and $(0.5,0.5)$ is more than $0.25$ units from the origin. By calculating areas, this is $\frac{16 - \pi}{16}$ .

## Video Solution by Richard Rusczyk
https://artofproblemsolving.com/videos/amc/2015amc10a/399
~naren_pr
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
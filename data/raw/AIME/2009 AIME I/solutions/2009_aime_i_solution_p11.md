# 2009 AIME I Problem 11

## Problem

Consider the set of all triangles $OPQ$ where $O$ is the origin and $P$ and $Q$ are distinct points in the plane with nonnegative integer coordinates $(x,y)$ such that $41x + y = 2009$ . Find the number of such distinct triangles whose area is a positive integer.

## Solution 1 (Matrix's, Determinants)
Let the two points $P$ and $Q$ be defined with coordinates; $P=(x_1,y_1)$ and $Q=(x_2,y_2)$
We can calculate the area of the parallelogram with the determinant of the matrix of the coordinates of the two points(shoelace theorem).
$\det \left(\begin{array}{c} P \\ Q\end{array}\right)=\det \left(\begin{array}{cc}x_1 &y_1\\x_2&y_2\end{array}\right).$
Since the triangle has half the area of the parallelogram, we just need the determinant to be even.
The determinant is
\[(x_1)(y_2)-(x_2)(y_1)=(x_1)(2009-41(x_2))-(x_2)(2009-41(x_1))=2009(x_1)-41(x_1)(x_2)-2009(x_2)+41(x_1)(x_2)=2009((x_1)-(x_2))\]
Since $2009$ is not even, $x_1-x_2$ must be even, thus the two $x$ 's must be of the same parity. Also note that the maximum value for $x$ is $49$ and the minimum is $0$ . There are $25$ even and $25$ odd numbers available for use as coordinates and thus there are $(_{25}C_2)+(_{25}C_2)=\boxed{600}$ such triangles.

## Solution 2
As in Solution 1, let the two points $P$ and $Q$ be defined with coordinates; $P=(x_1,y_1)$ and $Q=(x_2,y_2)$ . Let the line $41x+y=2009$ intersect the x-axis at $X$ and the y-axis at $Y$ . $X$ has coordinates $(49,0)$ , and $Y$ has coordinates $(0,2009)$ . As such, there are exactly $50$ lattice points on this line that can be used for $P$ and $Q$ .
WLOG, let the x-coordinate of $P$ be less than the x-coordinate of $Q$ . Note that $[OPQ]=[OYX]-[OYP]-[OXQ]$ . We know that $OY=2009$ and $OX= 49$ ; as such, $[OYX]=\frac{1}{2} \cdot OY \cdot OX = \frac{1}{2} \cdot 2009 \cdot 49$ . In addition, $[OYP]=\frac{1}{2} \cdot 2009 \cdot x_1$ and $[OXQ]=\frac{1}{2} \cdot 49 \cdot y_2$ .
Since $2009 \cdot 49$ is odd, the total area of $OYX$ is not an integer; rather, it is of the form $k + \frac{1}{2}$ where $k$ is an integer. To ensure $[OPQ]$ has an integral value, exactly one of $[OPY]$ and $[OQX]$ must have an integral value as well (the other must be of the form $k + \frac{1}{2}$ where $k$ is an integer).
Returning to $41x+y=2009$ , we notice that integer pairs of $x$ and $y$ that satisfy the equation always have different parities. To satisfy exactly one of $[OPY]$ and $[OQX]$ having an integral area, we must have $x_1$ and $y_2$ having different parities. This is because having an even number for $x_1$ or $y_2$ makes the area of the triangle an integer. We can therefore deduce that $x_1$ and $x_2$ have the same parity.
Out of the $50$ usable lattice points for $P$ and $Q$ , $25$ have even x-coordinates and $25$ have odd x-coordinates. Since we must pick two points with even x-coordinates or two points with odd x-coordinates, our desired answer is $\binom{25}{2}+\binom{25}{2}=300+300=\fbox{600}$ .

## Solution 3 (Analytic geometry)
As in the solution above, let the two points $P$ and $Q$ be defined with coordinates; $P=(x_1,y_1)$ and $Q=(x_2,y_2)$ .
If the coordinates of $P$ and $Q$ have nonnegative integer coordinates, $P$ and $Q$ must be lattice points either
- on the nonnegative x-axis
- on the nonnegative y-axis
- in the first quadrant
We can calculate the y-intercept of the line $41x+y=2009$ to be $(0,2009)$ and the x-intercept to be $(49,0)$ .
Using the point-to-line distance formula, we can calculate the height of $\triangle OPQ$ from vertex $O$ (the origin) to be:
$\dfrac{|41(0) + 1(0) - 2009|}{\sqrt{41^2 + 1^2}} = \dfrac{2009}{\sqrt{1682}} = \dfrac{2009}{29\sqrt2}$
Let $b$ be the base of the triangle that is part of the line $41x+y=2009$ .
The area is calculated as: $\dfrac{1}{2}\times b \times \dfrac{2009}{29\sqrt2} = \dfrac{2009}{58\sqrt2}\times b$
Let the numerical area of the triangle be $k$ .
So, $k = \dfrac{2009}{58\sqrt2}\times b$
We know that $k$ is an integer. So, $b = 58\sqrt2 \times z$ , where $z$ is also an integer.
We defined the points $P$ and $Q$ as $P=(x_1,y_1)$ and $Q=(x_2,y_2)$ .
Changing the y-coordinates to be in terms of x, we get:
$P=(x_1,2009-41x_1)$ and $Q=(x_2,2009-41x_2)$ .
The distance between them equals $b$ .
Using the distance formula, we get
$PQ = b = \sqrt{(-41x_2+ 41x_1)^2 + (x_2 - x_1)^2} = 29\sqrt2 \times |x_2 - x_1| = 58\sqrt2\times z$ $(*)$
WLOG, we can assume that $x_2 > x_1$ .
Taking the last two equalities from the $(*)$ string of equalities and putting in our assumption that $x_2>x_1$ , we get
$29\sqrt2\times (x_2-x_1) = 58\sqrt2\times z$ .
Dividing both sides by $29\sqrt2$ , we get
$x_2-x_1 = 2z$
As we mentioned, $z$ is an integer, so $x_2-x_1$ is an even integer. Also, $x_2$ and $x_1$ are both positive integers. So, $x_2$ and $x_1$ are between 0 and 49, inclusive. Remember, $x_2>x_1$ as well.
- There are 48 ordered pairs $(x_2,x_1)$ such that their positive difference is 2.
- There are 46 ordered pairs $(x_2,x_1)$ such that their positive difference is 4.
...
- Finally, there are 2 ordered pairs $(x_2,x_1)$ such that their positive difference is 48.
Summing them up, we get that there are $2+4+\dots + 48 = \boxed{600}$ triangles.

## Solution 4
We present a non-analytic solution; consider the lattice points on the line $41x+y=2009$ . The line has intercepts $(0, 2009)$ and $(49, 0)$ , so the lattice points for $x=0, 1, \ldots, 49$ divide the line into $49$ equal segments. Call the area of the large triangle $A$ . Any triangle formed with the origin having a base of one of these segments has area $A/49$ (call this value $B$ ) because the height is the same as that of large triangle, and the bases are in the ratio $1:49$ . A segment comprised of $n$ small segments (all adjacent to each other) will have area $nB$ . Rewriting in terms of the original area, $A=(\frac{1}{2})(49)(2009)$ , $B=\frac{2009}{2}$ , and $nB=n(\frac{2009}{2})$ . It is clear that in order to have a nonnegative integer for $nB$ as desired, $n$ must be even. This is equivalent to finding the number of ways to choose two distinct $x$ -values $x_1$ and $x_2$ ( $0 \leq x_1, x_2 \leq 49$ ) such that their positive difference ( $n$ ) is even. Follow one of the previous methods above to choose these pairs and arrive at the answer of 600.

## Solution 5 (Shoelace Theorem)
Label point $P$ and $Q$ as $(x_1, 2009 - 41x_1)$ and $(x_2, 2009 - 41x_2)$ respectively. Now, we shall use Shoelace Theorem to calculate the area of the triangle. After doing the calculations and simplifications with the coordinates, you will get the area of the triangle to be $\frac{2009|x_1-x_2|}{2}$ . Based on this, in order for the area of the triangle to be an integer, $|x_1-x_2|$ needs to be even. The only way for this to happen is that either $x_1$ and $x_2$ are both even are both odd. From the equation from the problem, we can know that $0 \le x_1, x_2 \le 49$ . There are $_{25}C_2$ ways to choose 2 even integers in that range or 2 odd numbers in that range. Thus, the answer is $2(_{25}C_2)$ which is $\boxed{600}$ .
~ROGER8432V3
These problems are copyrighted © by the Mathematical Association of America.
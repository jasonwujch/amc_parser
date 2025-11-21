# 2013 AMC 10A Problem 18

## Problem

Let points $A = (0, 0)$ , $B = (1, 2)$ , $C=(3, 3)$ , and $D = (4, 0)$ . Quadrilateral $ABCD$ is cut into equal area pieces by a line passing through $A$ . This line intersects $\overline{CD}$ at point $\left(\frac{p}{q}, \frac{r}{s}\right)$ , where these fractions are in lowest terms. What is $p+q+r+s$ ?

$\textbf{(A)}\ 54\qquad\textbf{(B)}\ 58\qquad\textbf{(C)}\ 62\qquad\textbf{(D)}\ 70\qquad\textbf{(E)}\ 75$

## Solution 1
First, we shall find the area of quadrilateral $ABCD$ . This can be done in any of three ways:
Pick's Theorem : $[ABCD] = I + \dfrac{B}{2} - 1 = 5 + \dfrac{7}{2} - 1 = \dfrac{15}{2}.$
Splitting: Drop perpendiculars from $B$ and $C$ to the x-axis to divide the quadrilateral into triangles and trapezoids, and so the area is $1 + 5 + \dfrac{3}{2} = \dfrac{15}{2}.$
Shoelace Theorem : The area is half of $|1 \cdot 3 - 2 \cdot 3 - 3 \cdot 4| = 15$ , or $\dfrac{15}{2}$ .
$[ABCD] = \frac{15}{2}$ . Therefore, each equal piece that the line separates $ABCD$ into must have an area of $\frac{15}{4}$ .
Call the point where the line through $A$ intersects $\overline{CD}$ $E$ . We know that $[ADE] = \frac{15}{4} = \frac{bh}{2}$ . Furthermore, we know that $b = 4$ , as $AD = 4$ . Thus, solving for $h$ , we find that $2h = \frac{15}{4}$ , so $h = \frac{15}{8}$ . This gives that the y coordinate of E is $\frac{15}{8}$ .
Line CD can be expressed as $y = -3x+12$ , so the $x$ coordinate of E satisfies $\frac{15}{8} = -3x + 12$ . Solving for $x$ , we find that $x = \frac{27}{8}$ .
From this, we know that $E = \left(\frac{27}{8}, \frac{15}{8}\right)$ . $27 + 15 + 8 + 8 = \boxed{\textbf{(B) }58}$

## Solution 2
Let the point where the altitude from $E$ to $\overline{AD}$ be labeled $F$ . Following the steps above, you can find that the height of $\triangle ADE$ is $\frac{15}{8}$ , and from there split the base into two parts, $x$ , and $4-x$ , such that $x$ is the segment from the origin to the point $F$ , and $4-x$ is the segment from point $F$ to point $D$ . Then, by the Pythagorean Theorem , $x=\frac{27}{8}$ , and the answer is $\boxed{\textbf{(B) }58}$
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
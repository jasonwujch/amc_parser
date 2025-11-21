# 2013 AMC 10A Problem 16

## Problem

A triangle with vertices $(6, 5)$ , $(8, -3)$ , and $(9, 1)$ is reflected about the line $x=8$ to create a second triangle. What is the area of the union of the two triangles?

$\textbf{(A)}\ 9 \qquad\textbf{(B)}\ \frac{28}{3} \qquad\textbf{(C)}\ 10 \qquad\textbf{(D)}\ \frac{31}{3} \qquad\textbf{(E)}\ \frac{32}{3}$

## Solution 1
Let $A$ be at $(6, 5)$ , B be at $(8, -3)$ , and $C$ be at $(9, 1)$ . Reflecting over the line $x=8$ , we see that $A' = D = (10,5)$ , $B' = B$ (as the x-coordinate of B is 8), and $C' = E = (7, 1)$ . Line $AB$ can be represented as $y=-4x+29$ , so we see that $E$ is on line $AB$ .
[asy] pair A = (6, 5), B = (8, -3), C = (9, 1), D = (10, 5), E = (7, 1), F = (8, 7/3); draw(A--B--C--cycle^^D--E--B--cycle); dot(A^^B^^C^^D^^E^^F); label("$A$",A,NW); label("$B$",B,S); label("$C$",C,SE); label("$D$",D,NE); label("$E$",E,W); label("$F$", F, N); [/asy]
We see that if we connect $A$ to $D$ , we get a line of length $4$ (between $(6, 5)$ and $(10,5)$ ). The area of $\triangle ABD$ is equal to $\frac{bh}{2} = \frac{4(8)}{2} = 16$ .
Now, let the point of intersection between $AC$ and $DE$ be $F$ . If we can just find the area of $\triangle ADF$ and subtract it from $16$ , we are done.
We realize that because the diagram is symmetric over $x = 8$ , the intersection of lines $AC$ and $DE$ should intersect at an x-coordinate of $8$ . We know that the slope of $DE$ is $\frac{5-1}{10-7} = \frac{4}{3}$ . Thus, we can represent the line going through $E$ and $D$ as $y - 1=\frac{4}{3}(x - 7)$ . Plugging in $x = 8$ , we find that the y-coordinate of F is $\frac{7}{3}$ . Thus, the height of $\triangle ADF$ is $5 - \frac{7}{3} = \frac{8}{3}$ . Using the formula for the area of a triangle, the area of $\triangle ADF$ is $\frac{16}{3}$ .
To get our final answer, we must subtract this from $16$ . $[ABD] - [ADF] = 16 - \frac{16}{3} = \boxed{\textbf{(E) }\frac{32}{3}}$

## Solution 2
First, realize that $E$ is the midpoint of $AB$ and $C$ is the midpoint of $BD$ . Connect $A$ to $D$ to form $\triangle ABD$ . Let the midpoint of $AD$ be $G$ . Connect $B$ to $G$ . $BG$ is a median of $\triangle ABD$ .
Because $\triangle ABD$ is isosceles, $BG$ is also an altitude of $\triangle ABD$ . We know the length of $AD$ and $BG$ from the given coordinates. The area of $\triangle ABD$ is $\frac{bh}{2} = \frac{4(8)}{2} = 16$ .
Let the intesection of $AC$ , $DE$ and $BG$ be $F$ . $F$ is the centroid of $\triangle ABD$ . Therefore, it splits $BG$ into $BF={2 \over 3}(BG)$ and $FG={1\over 3}(BG)$ . The area of quadrilateral $ABDF = 16\cdot {2 \over 3} = \boxed{\textbf{(E) }\frac{32}{3}}$
~Zeric Hang

## Solution 3
Since we have to find the area on a coordinate plane, we can use the Shoelace Theorem to find the area of the intersection. When you reflect it, it makes a quadrilateral.
[asy] pair A = (6, 5), B = (8, -3), C = (9, 1), D = (10, 5), E = (7, 1), F = (8, 7/3); draw(A--B--C--cycle^^D--E--B--cycle); dot(A^^B^^C^^D^^E^^F); label("$A$",A,NW); label("$B$",B,S); label("$C$",C,SE); label("$D$",D,NE); label("$E$",E,W); label("$F$", F, N); [/asy]
Since it is reflected around $x=8$ , the point $(8,-3)$ remains the same on both. The top right corners are $(6,5)$ , and its reflection $(10,5)$ . Now to find the 4th point, point F, we can use the equation of the line DE( $\frac{4}{3}x - \frac{25}{3}$ , and substitute $x=8$ , to get $\frac{7}{3}$ . Now we can use the theorem: $\frac{1}{2}(((6*-3)+(10*5)+(8*5)+(\frac{7}{3}*8))-((8*5)+(6*5)+(10*\frac{7}{3}) + (8* -3))) = \boxed{\textbf{(E) }\frac{32}{3}}$
~idk12345678
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
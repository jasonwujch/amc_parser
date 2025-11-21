# 2019 AMC 10B Problem 5

## Problem

Triangle $ABC$ lies in the first quadrant. Points $A$ , $B$ , and $C$ are reflected across the line $y=x$ to points $A'$ , $B'$ , and $C'$ , respectively. Assume that none of the vertices of the triangle lie on the line $y=x$ . Which of the following statements is not always true?

$\textbf{(A) }$ Triangle $A'B'C'$ lies in the first quadrant.

$\textbf{(B) }$ Triangles $ABC$ and $A'B'C'$ have the same area.

$\textbf{(C) }$ The slope of line $AA'$ is $-1$ .

$\textbf{(D) }$ The slopes of lines $AA'$ and $CC'$ are the same.

$\textbf{(E) }$ Lines $AB$ and $A'B'$ are perpendicular to each other.

## Solution
Let's analyze all of the options separately.
$\textbf{(A)}$ : Clearly $\textbf{(A)}$ is true, because a point in the first quadrant will have non-negative $x$ - and $y$ -coordinates, and so its reflection, with the coordinates swapped, will also have non-negative $x$ - and $y$ -coordinates.
$\textbf{(B)}$ : The triangles have the same area, since $\triangle ABC$ and $\triangle A'B'C'$ are the same triangle (congruent). More formally, we can say that area is invariant under reflection.
$\textbf{(C)}$ : If point $A$ has coordinates $(p,q)$ , then $A'$ will have coordinates $(q,p)$ . The gradient is thus $\frac{p-q}{q-p} = -1$ , so this is true. (We know $p \neq q$ since the question states that none of the points $A$ , $B$ , or $C$ lies on the line $y=x$ , so there is no risk of division by zero).
$\textbf{(D)}$ : Repeating the argument for $\textbf{(C)}$ , we see that both lines have slope $-1$ , so this is also true.
$\textbf{(E)}$ : This is the only one left, presumably the answer. To prove: if point $A$ has coordinates $(p,q)$ and point $B$ has coordinates $(r,s)$ , then $A'$ and $B'$ will, respectively, have coordinates $(q,p)$ and $(s,r)$ . The product of the gradients of $AB$ and $A'B'$ is $\frac{s-q}{r-p} \cdot \frac{r-p}{s-q} = 1 \neq -1$ , so in fact these lines are never perpendicular to each other (using the "negative reciprocal" condition for perpendicularity).
Thus the answer is $\boxed{\textbf{(E)}}$ .
### Counterexamples
If $(x_1,y_1) = (2,3)$ and $(x_2,y_2) = (7,1)$ , then the slope of $AB$ , $m_{AB}$ , is $\frac{1 - 3}{7 - 2} = -\frac{2}{5}$ , while the slope of $A'B'$ , $m_{A'B'}$ , is $\frac{7 - 2}{1 - 3} = -\frac{5}{2}$ . $m_{A'B'}$ is the reciprocal of $m_{AB}$ , but it is not the negative reciprocal of $m_{AB}$ . To generalize, let $(x_1,y_1)$ denote the coordinates of point $A$ , let $(x_2, y_2)$ denote the coordinates of point $B$ , let $m_{AB}$ denote the slope of segment $\overline{AB}$ , and let $m_{A'B'}$ denote the slope of segment $\overline{A'B'}$ . Then, the coordinates of $A'$ are $(y_1, x_1)$ , and of $B'$ are $(y_2, x_2)$ . Then, $m_{AB} = \frac{y_2 - y_1}{x_2 - x_1}$ , and $m_{A'B'} = \frac{x_2 - x_1}{y_2 - y_1} = \frac{1}{m_{AB}}$ , so slopes arent negative reciprocals of each other.

## Video Solution
https://youtu.be/XKSZ9o54dg8
~Education, the Study of Everything

## Video Solution
https://youtu.be/dYn6jYRgEv4
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
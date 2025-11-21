# 2005 AIME I Problem 14

## Problem

Consider the points $A(0,12), B(10,9), C(8,0),$ and $D(-4,7).$ There is a unique square $S$ such that each of the four points is on a different side of $S.$ Let $K$ be the area of $S.$ Find the remainder when $10K$ is divided by $1000$ .

1 Problem

- 1 Problem

- 2 Solution 2.1 Solution 1 2.2 Solution 2 2.3 Solution 3

- 3 See also

- 2.1 Solution 1

- 2.2 Solution 2

- 2.3 Solution 3

## Solution

## Solution 1
Consider a point $E$ such that $AE$ is perpendicular to $BD$ , $AE$ intersects $BD$ , and $AE = BD$ . E will be on the same side of the square as point $C$ .
Let the coordinates of $E$ be $(x_E,y_E)$ . Since $AE$ is perpendicular to $BD$ , and $AE = BD$ , we have $9 - 7 = x_E - 0$ and $10 - ( - 4) = 12 - y_E$ The coordinates of $E$ are thus $(2, - 2)$ .
Now, since $E$ and $C$ are on the same side, we find the slope of the sides going through $E$ and $C$ to be $\frac { - 2 - 0}{2 - 8} = \frac {1}{3}$ . Because the other two sides are perpendicular, the slope of the sides going through $B$ and $D$ are now $- 3$ .
Let $A_1,B_1,C_1,D_1$ be the vertices of the square so that $A_1B_1$ contains point $A$ , $B_1C_1$ contains point $B$ , and etc. Since we know the slopes and a point on the line for each side of the square, we use the point slope formula to find the linear equations. Next, we use the equations to find $2$ vertices of the square, then apply the distance formula.
We find the coordinates of $C_1$ to be $(12.5,1.5)$ and the coordinates of $D_1$ to be $( - 0.7, - 2.9)$ . Applying the distance formula, the side length of our square is $\sqrt {\left( \frac {44}{10} \right)^2 + \left( \frac {132}{10} \right)^2} = \frac {44}{\sqrt {10}}$ .
Hence, the area of the square is $K = \frac {44^2}{10}$ . The remainder when $10K$ is divided by $1000$ is $936$ .

## Solution 2
Let $(a,b)$ denote a normal vector of the side containing $A$ . Note that $\overline{AC}, \overline{BD}$ intersect and hence must be opposite vertices of the square. The lines containing the sides of the square have the form $ax+by=12b$ , $ax+by=8a$ , $bx-ay=10b-9a$ , and $bx-ay=-4b-7a$ . The lines form a square, so the distance between $C$ and the line through $A$ equals the distance between $D$ and the line through $B$ , hence $8a+0b-12b=-4b-7a-10b+9a$ , or $-3a=b$ . We can take $a=-1$ and $b=3$ . So the side of the square is $\frac{44}{\sqrt{10}}$ , the area is $K=\frac{1936}{10}$ , and the answer to the problem is $\boxed{936}$ .

## Solution 3
Let $\begin{bmatrix} a \\ b \end{bmatrix}$ be the unit vector parallel to one side of the square. The unit vector parallel to the perpendicular side is then $\begin{bmatrix} b \\ -a \end{bmatrix}$ . The dot product of a diagonal of quadrilateral $ABCD$ with the corresponding unit vector gives the side length. Since the side lengths of the square are equal, $\overrightarrow{DB}\cdot \begin{bmatrix} a \\ b \end{bmatrix}= \overrightarrow{AC}\cdot \begin{bmatrix} b \\ -a \end{bmatrix}$ . Plugging in $\overrightarrow{AC}=\begin{bmatrix} 8 \\ -12 \end{bmatrix}$ and $\overrightarrow{DB}=\begin{bmatrix} 14 \\ 2 \end{bmatrix}$ yields $a=3b$ . Since $\begin{bmatrix} a \\ b \end{bmatrix}$ is a unit vector, it is equal to $\begin{bmatrix} \frac{3}{\sqrt{10}} \\ \frac{1}{\sqrt{10}} \end{bmatrix}$ . Taking the dot product with $\overrightarrow{DB}$ gives the side length, which is $\frac {44}{\sqrt {10}}$ , so the area is $\frac {44^2}{10}$ , and the answer is $\boxed{936}$ .
These problems are copyrighted © by the Mathematical Association of America.
# 2014 AMC 10A Problem 18

## Problem

A square in the coordinate plane has vertices whose $y$ -coordinates are $0$ , $1$ , $4$ , and $5$ . What is the area of the square?

$\textbf{(A)}\ 16\qquad\textbf{(B)}\ 17\qquad\textbf{(C)}\ 25\qquad\textbf{(D)}\ 26\qquad\textbf{(E)}\ 27$

## Solution 1
Let the points be $A=(x_1,0)$ , $B=(x_2,1)$ , $C=(x_3,5)$ , and $D=(x_4,4)$
Note that the difference in $y$ value of $B$ and $C$ is $4$ . By rotational symmetry of the square, the difference in $x$ value of $A$ and $B$ is also $4$ . Note that the difference in $y$ value of $A$ and $B$ is $1$ . We now know that $AB$ , the side length of the square, is equal to $\sqrt{1^2+4^2}=\sqrt{17}$ , so the area is $\boxed{\textbf{(B) }17}$ .

## Solution 2
By translation, we can move the square with point $A$ at the origin. Then, $A=(0,0), B=(x_1,1), C=(x_2,5), D=(x_3,4)$ . We will use the relationship among the 4 sides of being perpendicular and equal.
The slope of $AB$ is $\frac{1-0}{x_1-0}=\frac{1}{x_1}$ .
Because $BC$ is perpendicular to $AB$ , the slope of $BC=-x_1$ . From the information above we could have the equation:
Because $CD$ is perpendicular to $BC$ , the slope of $CD=\frac{1}{x_1}$ . From the information above we could have the equation:
Because $AD=AB,$
Note that the square with $x_1=-4$ is just the reflection of square with $x_1=4$ over the origin. I will use $x_1=4$ . $B=(4,1), AB=\sqrt{17}, [ABCD]=\boxed{\textbf{(B) }17}$
~ isabelchen

## Solution 3
In this solution, we will use the fact that the diagonals of a square bisect each other, they are perpendicular to each other, and they are equal in length.
Using the fact that the diagonals bisect each other, we get the equation:
Now we use the fact that the diagonals are perpendicular to each other:
Using the fact that the diagonals are equal in length, we get the equation:
Now we have 3 equations with 3 variables:
$\begin{cases} x_2=x_1+x_3 \\ x_2(x_1-x_3)=15 \\ (x_3-x_1)^2-x_2^2=16 \end{cases}$
We substitute $x_2$ into the 2 other equations:
Now we have 2 equations of $x_1$ and $x_3$ :
$\begin{cases} x_1^2-x_3^2=15 \\ x_1x_3=-4 \end{cases}$
This is the same equation as solution $2$ . So $x_1= \pm 4, AB=\sqrt{17}, [ABCD]=\boxed{\textbf{(B) }17}$
~ isabelchen

## Solution 4 (not rigorous)
Draw it out, by inspection the coordinates are $(-1, 4)$ , $(0, 0)$ , $(4, 1)$ , and $(3, 5)$ . The side length is $\sqrt{17}, [ABCD]=\boxed{\textbf{(B) }17}$ ~JH. L

## Video Solution
https://www.youtube.com/watch?v=iPPQUrNE4RE
~ naren_pr
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
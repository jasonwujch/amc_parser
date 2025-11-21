# 2024 AMC 8 Problem 11

## Problem

The coordinates of $\triangle ABC$ are $A(5,7)$ , $B(11,7)$ , and $C(3,y)$ , with $y>7$ . The area of $\triangle ABC$ is 12. What is the value of $y$ ?

[asy] draw((3,11)--(11,7)--(5,7)--(3,11)); dot((5,7)); label("$A(5,7)$",(5,7),S); dot((11,7)); label("$B(11,7)$",(11,7),S); dot((3,11)); label("$C(3,y)$",(3,11),NW); [/asy]

$\textbf{(A) }8\qquad\textbf{(B) }9\qquad\textbf{(C) }10\qquad\textbf{(D) }11\qquad \textbf{(E) }12$

## Solution 1
Since the triangle has a base of $6$ , we can plug in that value as the base. Then, we can solve the equation for the height. Doing so gives us, \[\dfrac{6h}{2}=3h=12.\] This means that $h=4$ , so that means that we have to add 4 to the $y$ -coordinate. So the answer is $7+4=\boxed{(D) 11}$

## Solution 2
By the Shoelace Theorem, $\triangle ABC$ has area \[\frac{1}{2}|(y \cdot 11 + 7 \cdot 5 + 7 \cdot 3) - (3 \cdot 7 + 11 \cdot 7 + 5 \cdot y)| = \frac{1}{2}|(11y + 56) - (98 + 5y)| = \frac{1}{2}|6y - 42|.\] From the problem, this is equal to $12$ . We now solve for y.
$\frac{1}{2}|6y - 42| = 12$
$|6y-42| = 24$
$6y - 42 = 24$ OR $6y - 42 = -24$
$6y = 66$ OR $6y = 18$
$y = 11$ OR $y = 3$
However, since, as stated in the problem, $y > 7$ , our only valid solution is $\boxed{\textbf{(D)} 11}$ .
~ cxsmi

## Solution 3
As in the figure, the triangle is determined by the vectors $\begin{bmatrix}-2 \\ y-7\end{bmatrix}$ and $\begin{bmatrix}6\\0\end{bmatrix}$ . Recall that the absolute value of the determinant of these vectors is the area of the parallelogram determined by those vectors; the triangle has half the area of that parallelogram. Then we must have that $\frac{1}{2}|\begin{vmatrix}-2 & y-7\\6 & 0\end{vmatrix}| = 12 \implies \begin{vmatrix}-2 & y-7\\6 & 0\end{vmatrix} = \pm 24$ . Expanding the determinants, we find that $-6(y-7) = 24$ or $-6(y-7) = -24$ . Solving each equation individually, we find that $y = 3$ or $y = 11$ . However, the problem states that $y > 7$ , so the only valid solution is $\boxed{\textbf{(D)} 11}$ .
~ cxsmi (again!)

## Solution 4
Draw a rectangle so that the hypotenuse is the diagonal of the rectangle. The base is 8 and the height is \( y - 7 \), so the area is ${8(y - 7) = 8y - 56}$
Inside the rectangle, there are 2 extra right triangles along with the original triangle. The larger right triangle has an area of half the rectangle, so it has an area of
${\frac{8y - 56}{2} = 4y - 28}$
The smaller right triangle has a base of 2 and a height of \( y - 7 \), so its area is
${\frac{2(y - 7)}{2} = y - 7}$
Subtracting the extra right triangles from the area of the rectangle, you get
${(8y - 56) - (4y - 28) - (y - 7) = 3y - 21}$
Since the problem told us that the original triangle had an area of 12, you get the equation
${3y - 21 = 12}$
${3y = 33}$
${y = 11}$
So the answer to the problem is \( \boxed{\textbf{D}} \).
### Video by MathTalks 😉
https://youtu.be/qAwRUj2N46c?si=QDUY8ZUVFP29Eg4c

## Video Solution by Math-X (First understand the problem!!!)
https://youtu.be/BaE00H2SHQM?si=qhPbhu8o5hamBrtb&t=2315
~Math-X

## Video Solution by Central Valley Math Circle(Goes Through Full Thought Process)
https://youtu.be/D0pFHbZ5788
~mr_mathman

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/5ZIFnqymdDQ?si=6FzUoSOA5moM-gDP&t=1191
~hsnacademy

## Video Solution (easy to digest) by Power Solve
https://www.youtube.com/watch?v=2UIVXOB4f0o

## Video Solution by NiuniuMaths (Easy to understand!)
https://www.youtube.com/watch?v=V-xN8Njd_Lc
~NiuniuMaths

## Video Solution 3 by SpreadTheMathLove
https://www.youtube.com/watch?v=RRTxlduaDs8

## Video Solution by CosineMethod [🔥Fast and Easy🔥]
https://www.youtube.com/watch?v=-64aBL-lEVg

## Video Solution by Interstigation
https://youtu.be/ktzijuZtDas&t=1063

## Video Solution by Daily Dose of Math (Certified, Simple, and Logical)
https://youtu.be/8GHuS5HEoWc
~Thesmartgreekmathdude

## Video Solution by Dr. David
https://youtu.be/0O4Y3RHzcR4

## Video Solution by WhyMath
https://youtu.be/_r1Zh4HGA7g
### See Also
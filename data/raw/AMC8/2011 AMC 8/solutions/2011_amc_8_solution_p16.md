# 2011 AMC 8 Problem 16

## Problem

Let $A$ be the area of the triangle with sides of length $25, 25$ , and $30$ . Let $B$ be the area of the triangle with sides of length $25, 25,$ and $40$ . What is the relationship between $A$ and $B$ ?

$\textbf{(A) } A = \dfrac9{16}B \qquad\textbf{(B) } A = \dfrac34B \qquad\textbf{(C) } A=B \qquad \textbf{(D) } A = \dfrac43B \qquad \textbf{(E) }A = \dfrac{16}9B$

## Solution 1 (Using the Pythagorean Theorem)
25-25-30
We can draw the altitude for the side with length 30. By HL Congruence, the two triangles formed are congruent. Thus the altitude splits the side with length 30 into two segments with length 15. By the Pythagorean Theorem , we have \[15^2 + x^2 =25^2\] \[x^2 = 25^2 - 15^2\] \[x^2 = (25 + 15)(25-15)\] \[x^2= 40\cdot 10\] \[x^2= 400\] \[x = \sqrt{400}\] \[x= 20\]
Thus we have two 15-20-25 right triangles.
25-25-40
We can draw the altitude for the side with length 40. By HL Congruence, the two triangles formed are congruent. Thus the altitude splits the side with length 40 into two segments with length 20. From the 25-25-30 case, we know that the other side length is 15, so we have two 15-20-25 right triangles. Let the area of a 15-20-25 right triangle be $x$ . \[a = 2x\] \[b = 2x\] \[\boxed{\textbf{(C) } A = B}\]

## Solution 2 (Using Heron's Formula)
Using Heron's formula, we can calculate the area of the two triangles. The formula states that \[A = \sqrt{s(s - a)(s - b)(s - c)}\] where $s$ is the semiperimeter of a triangle with side lengths $a$ , $b$ , and $c$ .
For the 25-25-30 triangle, \[s = \frac{25 + 25 + 30}{2} = 40\] Therefore, \[A = \sqrt{40 \cdot 15 \cdot 15 \cdot 10} = 300\]
For the 25-25-40 triangle, \[s = \frac{25 + 25 + 40}{2} = 45\] Therefore, \[B = \sqrt{45 \cdot 20 \cdot 20 \cdot 5} = 300\]
Hence, \[A = B \hspace{0.15in} \Longrightarrow \hspace{0.15in} \boxed{\textbf{(C)}}\]

## Video Solution 1
https://www.youtube.com/watch?v=mYn6tNxrWBU
~SpreadtheMathLove

## Video Solution by WhyMath
https://youtu.be/UjACHET8l3E
### See Also
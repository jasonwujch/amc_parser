# 2025 AMC 10A Problem 3

## Problem

How many isosceles triangles are there with positive area whose side lengths are all positive integers and whose longest side has length $2025$ ?

$\textbf{(A)}~2025\qquad\textbf{(B)}~2026\qquad\textbf{(C)}~3012\qquad\textbf{(D)}~3037\qquad\textbf{(E)}~4050$

1 Solution 1: Casework

- 1 Solution 1: Casework

- 2 Solution 2 (broken down)

- 3 Solution 3 (more broken down)

- 4 Solution 4: Casework

- 5 Chinese Video Solution

- 6 Video Solution by SpreadTheMathLove

- 7 Video Solution (Fast and Intuitive)

- 8 Video Solution by Daily Dose of Math

- 9 Video Solution

- 10 See Also

## Solution 1: Casework
You can split the problem into two cases: Case $1$ : The two sides with equal length are both smaller than $2025$ , which means that they range from $1013$ to $2024$ . There are $1012$ such cases. Case $2$ : There are two sides of length $2025$ , so the last side must be in the range $1$ to $2025$ . There are $2025$ such cases. Keep in mind, an equilateral triangle also counts as an isosceles triangle, since it has at least 2 sides of equal length. Therefore, the total number of cases is $1012 + 2025 = \boxed{\text{(D) }3037}$ ~cw, minor edit by sd
Side note not by the author: If you're unsure whether the equilateral triangle is a valid case, notice that the other answers are much farther away, as compared to only a one-off error from 3037, which would make 3037 still the best answer.

## Solution 2 (broken down)
Suppose an isosceles triangle has sides $A, A, B$ where $A$ is the longest side and $A, B$ are positive integers.
By the triangle inequalities:
\[A + A > B\]
\[A + B > A \implies B > 0\]
---
Since $A = 2025$ (the longest side):
\[2025 + 2025 > B \implies B < 4050\]
But also, since $A$ is the longest side, $B < 2025$ . Therefore,
\[B = 1, 2, 3, \ldots, 2024,\]
giving $2024$ triangles.
---
Now consider triangles with side lengths $B, B, 2025$ , where $B < 2025$ .
Triangle inequality gives:
\[B + B > 2025 \implies B > 1012.5\]
Since $B$ is an integer and less than $2025$ , the possible values are
\[B = 1013, 1014, 1015, \ldots, 2024,\]
which gives $1012$ triangles.
---
Finally, don’t forget the case where all sides are $2025$ (equilateral, which also counts as isosceles by definition). So add $1$ more triangle.
---
In total,
\[2024 + 1012 + 1 = \boxed{3037}\]
triangles.
~yuvaG

## Solution 3 (more broken down)
To solve this question, we first must observe the following restrictions given by the problem - 1.) Be an isosceles triangle 2.) Positive integer side lengths (causing a positive area) 3.) Longest length is $2025$
To satisfy restrictions $1$ and $2$ , we can denote the side lengths of a triangle that satisfies these restrictions as $A, A, B,$ where $A$ and $B$ are positive integers. This is possible as the triangle is restricted to be isosceles, meaning at least $2$ equal length sides.
In any triangle with side lengths $a$ , $b$ , and $c$ , the following inequalities (Triangle Inequality Theorem) must hold:
\[a + b > c\] \[a + c > b\] \[b + c > a\]
Therefore, our satisfactory triangles must satisfy
\[A + A > B\] \[A + B > A.\]
where $A > 0, B > 0.$
Now we can focus on restriction $3.$ Let us consider that $A$ is equal to $2025$ ( $A$ is the longest side length).
Substituting for $A$ we can rewrite our inequalities as follows
\[2025 + 2025 > B\] \[2025 + B > 2025\]
where $B > 0.$
Furthermore, we can solve this system of linear inequalities like this
\[4050 > B\] \[B > 0\]
\[0 < B < 4050\]
However, for $A$ to be the longest side length, $B$ must be less than $2025$ . Therefore, the solutions are
\[\text{integers in } 0 < B < 2025 \implies 1, 2, 3, 4, 5, \ldots, 2024\]
This creates $2024$ cases.
---
Now let’s consider that $B$ is the longest side length and it is equal to $2025$ .
Substituting for $B$ , we can rewrite our inequalities as follows
\[A + A > 2025\] \[A + 2025 > A\]
where $A > 0.$
Furthermore, we can solve this system of linear inequalities like this
\[2A > 2025\] \[0 > 2025\] (which can be ignored as it is always true)
\[A > 1012.5\]
However, for $B$ to be the longest side length, $A$ must be less than $2025$ . Therefore, the solutions are
\[\text{integers in } 1012.5 < A < 2025 \implies 1013, 1014, 1015, 1016, \ldots, 2024\]
This creates $2024 - 1012 = 1012$ cases.
---
But! here is also a case of an isosceles triangle where all side lengths of the triangle are equal in length and congruent - this special isosceles is referred to as an equilateral triangle. We can denote the lengths of such a triangle as $A, A, A$ . We need to assign the longest length to $A$ , as it is the only place a length can be applied. So, $A = 2025$ . We do not need to worry about the Triangle Inequality Theorem as any equilateral shape always satisfies it. For example,
\[A + A > A, \quad A + A > A, \quad A + A > A\]
where $a,b,c$ of the Triangle Inequality Theorem are all equal to $A$ and $A > 0$
is always satisfied for any side length, assuming that $A$ is a positive integer.
This creates $1$ case.
---
Adding together our cases,
\[2024 + 1012 + 1 = \boxed{\text{(D) }3037}.\]
This is a process called casework.
~ yuvaG (idk why i felt like going this in depth for question $3$ , but enjoy 😉)

## Solution 4: Casework
There are two cases. The first case is where the other two side lengths are the congruent side lengths and less than 2025, and the second one is where 2025 is one of the congruent side lengths.
Case $1$ : We let $a$ be the other side length in the triangle. By the triangle inequality, we have that \[2a>2025 \text{ and } a<2025,\] so we get that $1012.5<a<2025,$ and since $a$ is an integer, $a$ can be $1013,2014,...,2024,$ so there are $1012$ such cases.
Case $2$ : We let $b$ be the other side in the triangle, since 2025 is one of the congruent sides. Since 2025 is the largest side, $a<2025,$ so there are $2024$ solutions in this case.
However, there is also a case where the triangle is equilateral so we add $1.$
So, the total number of triangles that are isosceles with largest side $2025$ is $1012+2024+1=\boxed{3037}$
~ gogogo2022

## Chinese Video Solution
https://www.bilibili.com/video/BV1hV2uBtENi/
~metrixgo

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=dAeyV60Hu5c

## Video Solution (Fast and Intuitive)
https://youtu.be/qfvA1uD0--M?si=cJzhHfQun4Pnpi83 ~Pi Academy

## Video Solution by Daily Dose of Math
https://youtu.be/LN5ofIcs1kY
~Thesmartgreekmathdude

## Video Solution
https://youtu.be/l1RY_C20Q2M
### See Also
- AMC 10
- AMC 10 Problems and Solutions
- Mathematics competitions
- Mathematics competition resources
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
# 2018 AMC 8 Problem 11

## Problem

Abby, Bridget, and four of their classmates will be seated in two rows of three for a group picture, as shown. \begin{eqnarray*} \text{X}&\quad\text{X}\quad&\text{X} \\ \text{X}&\quad\text{X}\quad&\text{X} \end{eqnarray*} If the seating positions are assigned randomly, what is the probability that Abby and Bridget are adjacent to each other in the same row or the same column?

$\textbf{(A) } \frac{1}{3} \qquad \textbf{(B) } \frac{2}{5} \qquad \textbf{(C) } \frac{7}{15} \qquad \textbf{(D) } \frac{1}{2} \qquad \textbf{(E) } \frac{2}{3}$

## Solution 1
There are a total of $6 !$ ways to arrange the kids.
Abby and Bridget can sit in 3 ways if they are adjacent in the same column: \begin{eqnarray*} \text{A}&\quad\text{X}\quad&\text{X} \\ \text{B}&\quad\text{X}\quad&\text{X} \end{eqnarray*}
\begin{eqnarray*} \text{X}&\quad\text{A}\quad&\text{X} \\ \text{X}&\quad\text{B}\quad&\text{X} \end{eqnarray*}
\begin{eqnarray*} \text{X}&\quad\text{X}\quad&\text{A} \\ \text{X}&\quad\text{X}\quad&\text{B} \end{eqnarray*}
For each of these seat positions, Abby and Bridget can switch seats, and the other 4 people can be arranged in $4!$ ways which results in a total of $3 \times 2 \times 4!$ ways to arrange them.
By the same logic, there are 4 ways for Abby and Bridget to be placed if they are adjacent in the same row: they can swap seats, and the other $4$ people can be arranged in $4!$ ways for a total of $4 \times 2 \times 4!$ ways to arrange them.
We sum the 2 possibilities up to get $\frac{(3\cdot2)\cdot4!+(4\cdot2)\cdot4!}{6!} = \frac{14\cdot4!}{6!}=\boxed{\frac{7}{15}}$ or $\textbf{(C)}$ .
If you got stuck on this problem, refer to AOPS Probability and Combinations.
~Nivaar

## Solution 2
We can ignore other students, and treat Abby and Bridget as indistinguishable (since we only care about adjacency, not their order). Thus, the total number of ways is $n(S) = _{6}C_{2} = 15$ . In one row, they can be adjacent 2 ways: $2 \cdot 2 rows = 4$ . In one column, they can only be adjacent 1 way: $1 \cdot 3 cols = 3$ . Add these cases $4+3=7$ , and therefore, P(Abby and Bridget sitting adjacent) is $\boxed{\textbf{(C) }\frac{7}{15}}$ .

## Solution 3
We can split the seating into two separate cases: if Abby is sitting on the corners, and if Abby isn't. If Abby is sitting in the corners, there is a $\frac{2}{5}$ chance Bridget is sitting next to Abby, so there is a $\frac{2}{5} \cdot \frac{4}{6} = \frac{4}{15}$ chance for the first case. Meanwhile, if Abby is sitting in the middle row, there is a $\frac{3}{5}$ chance Bridget is sitting next to Abby, so there is a $\frac{3}{5} \cdot \frac{2}{6} = \frac{1}{5}$ chance for the second case. Therefore, P(Abby and Bridget are sitting adjacent to each other) is $\frac{4}{15} + \frac{1}{5} = \boxed{\frac{7}{15}}$ , or $\boxed{\textbf{C}}$ . ~strongstephen

## Video Solution (CREATIVE ANALYSIS!!!)
https://youtu.be/sZhsVX4xIgg
~Education, the Study of Everything

## Video Solution
https://youtu.be/YNH7IwMSsh0
https://youtu.be/EMe9rve8wI0
~savannahsolver
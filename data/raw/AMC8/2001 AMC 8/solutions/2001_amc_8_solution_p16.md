# 2001 AMC 8 Problem 16

## Problem

A square piece of paper, 4 inches on a side, is folded in half vertically. Both layers are then cut in half parallel to the fold. Three new rectangles are formed, a large one and two small ones. What is the ratio of the perimeter of one of the small rectangles to the perimeter of the large rectangle?

[asy] draw((0,8)--(0,0)--(4,0)--(4,8)--(0,8)--(3.5,8.5)--(3.5,8)); draw((2,-1)--(2,9),dashed); [/asy]

$\text{(A)}\ \dfrac{1}{3} \qquad \text{(B)}\ \dfrac{1}{2} \qquad \text{(C)}\ \dfrac{3}{4} \qquad \text{(D)}\ \dfrac{4}{5} \qquad \text{(E)}\ \dfrac{5}{6}$

## Solution #1
The smaller rectangles each have the same height as the original square, but have $\frac{1}{4}$ the length, since the paper is folded in half and then cut in half the same way. The larger rectangle has the same height as the original square but has $\frac{1}{2}$ the length, since the paper is cut in half after the fold but the fold retains both sides of the larger rectangle. Therefore, the smaller rectangles have dimensions $4 \times 1$ and the larger rectangle has dimensions $4 \times 2$ . The ratio of their perimeters is $\frac{2(4+1)}{2(4+2)}=\frac{5}{6}, \boxed{\text{E}}$

## Solution #2
A simpler way to solve the problem is by brute-forcing it. We know that the side length of the original paper is $4$ inches by $4$ inches. The smaller paper would have a side length of $4$ inches by $4$ · $\frac{1}{4} = 1$ inches, having a perimeter of $2$ ( $4 + 1$ ) = $2$ ( $5$ ) = $10$ inches. The larger rectangle would have a side length of $4$ inches by $4$ · $\frac{1}{2} = 2$ inches, having a perimeter of $2$ ( $4 + 2$ ) = $2$ ( $6$ ) = $12$ inches. Thus, the answer is $\frac{10}{12} = \frac{5}{6}$ , i.e. $\boxed{\text{E}}$
### See Also
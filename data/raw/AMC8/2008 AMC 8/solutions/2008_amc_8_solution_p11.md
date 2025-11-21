# 2008 AMC 8 Problem 11

## Problem

Each of the $39$ students in the eighth grade at Lincoln Middle School has one dog or one cat or both a dog and a cat. Twenty students have a dog and $26$ students have a cat. How many students have both a dog and a cat?

$\textbf{(A)}\ 7\qquad \textbf{(B)}\ 13\qquad \textbf{(C)}\ 19\qquad \textbf{(D)}\ 39\qquad \textbf{(E)}\ 46$

## Solution 1
The union of two sets is equal to the sum of each set minus their intersection. The number of students that have both a dog and a cat is $20+26-39 = \boxed{\textbf{(A)}\ 7}$ .

## Solution 2 (Venn Diagram)
We create a diagram: [asy] draw(circle((0,0),5)); draw(circle((5,0),5)); label("$x$",(2.3,0),S); label("$20$",(7,0),S); label("$26$",(-2,0),S); [/asy]
Let $x$ be the number of students with both a dog and a cat.
Therefore, we have
\[26+20-x = 39\] \[46-x = 39\] \[x = \boxed{\textbf{(A)} ~7}\] .
~MrThinker
### See Also
# 2005 AMC 10A Problem 15

## Problem

How many positive cubes divide $3! \cdot 5! \cdot 7!$ ?

$\textbf{(A) } 2\qquad \textbf{(B) } 3\qquad \textbf{(C) } 4\qquad \textbf{(D) } 5\qquad \textbf{(E) } 6$

## Solution 1
We obtain $3! \cdot 5! \cdot 7! = (3\cdot2\cdot1) \cdot (5\cdot4\cdot3\cdot2\cdot1) \cdot (7\cdot6\cdot5\cdot4\cdot3\cdot2\cdot1) = 2^{8}\cdot3^{4}\cdot5^{2}\cdot7$ .
Therefore, a perfect cube that divides $3! \cdot 5! \cdot 7!$ must be of the form $2^{a}\cdot3^{b}\cdot5^{c}\cdot7^{d}$ , where $a$ , $b$ , $c$ , and $d$ are non-negative multiples of $3$ that are less than or equal to $8$ , $5$ , $2$ and $1$ respectively.
This means
\begin{align*}&a\in\{0,3,6\} \text{ (} 3 \text{ possibilities),} \\ &b\in\{0,3\} \text{ (} 2 \text{ possibilities),} \\ &c\in\{0\} \text{ (} 1 \text{ possibility), and} \\ &d\in\{0\} \text{ (} 1 \text{ possibility),}\end{align*}
so the number of perfect cubes that divide $3! \cdot 5! \cdot 7!$ is $3\cdot2\cdot1\cdot1 = \boxed{\textbf{(E) } 6}$ .

## Solution 2
As in Solution 1, we write $3! \cdot 5! \cdot 7! = (3\cdot2\cdot1) \cdot (5\cdot4\cdot3\cdot2\cdot1) \cdot (7\cdot6\cdot5\cdot4\cdot3\cdot2\cdot1)$ , and now notice that there are a total of $3$ $3$ s, $3$ $2$ s, and $3$ $1$ s. This gives us our first $3$ cubes: $3^3$ , $2^3$ , and $1^3$ .
However, we can also multiply smaller numbers in the expression to make bigger cubes. For example, $(2 \cdot 2) \cdot 4 \cdot 4 = 4 \cdot 4 \cdot 4 = 4^3$ (where one 2 comes from the $3!$ , and the other from the $5!$ ). Using this method, we can also make
\[(3 \cdot 2) \cdot (3 \cdot 2) \cdot 6 = 6^3\]
and
\[(3 \cdot 4) \cdot (3 \cdot 4) \cdot (2 \cdot 6) = 12^3.\]
So we have $6$ possible cubes in total: $1^3$ , $2^3$ , $3^3$ , $4^3$ , $6^3$ , and $12^3$ , and the answer is $\boxed{\textbf{(E) } 6}$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
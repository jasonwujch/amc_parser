# 2001 AIME II Problem 3

## Problem

Given that

\begin{align*}x_{1}&=211,\\ x_{2}&=375,\\ x_{3}&=420,\\ x_{4}&=523,\ \text{and}\\ x_{n}&=x_{n-1}-x_{n-2}+x_{n-3}-x_{n-4}\ \text{when}\ n\geq5, \end{align*}

find the value of $x_{531}+x_{753}+x_{975}$ .

## Solution
We find that $x_5 = 267$ by the recursive formula. Summing the recursions
\begin{align*} x_{n}&=x_{n-1}-x_{n-2}+x_{n-3}-x_{n-4} \\ x_{n-1}&=x_{n-2}-x_{n-3}+x_{n-4}-x_{n-5} \end{align*}
yields $x_{n} = -x_{n-5}$ . Thus $x_n = (-1)^k x_{n-5k}$ . Since $531 = 106 \cdot 5 + 1,\ 753 = 150 \cdot 5 + 3,\ 975 = 194 \cdot 5 + 5$ , it follows that
\[x_{531} + x_{753} + x_{975} = (-1)^{106} x_1 + (-1)^{150} x_3 + (-1)^{194} x_5 = 211 + 420 + 267 = \boxed{898}.\]

## Solution Variant
The recursive formula suggests telescoping. Indeed, if we add $x_n$ and $x_{n-1}$ , we have $x_n + x_{n-1} = (x_{n-1} - x_{n-2} + x_{n-3} - x_{n-4}) + (x_{n-2} - x_{n-3} + x_{n-4} - x_{n-5}) = x_{n-1} - x_{n-5}$ .
Subtracting $x_{n-1}$ yields $x_n = -x_{n-5} \implies x_n = -(-(x_{n-10})) = x_{n-10}$ .
Thus,
\[x_{531} + x_{753} + x_{975} = x_1 + x_3 + x_5 = x_1 + x_3 + (x_4 - x_3 + x_2 - x_1) = x_2 + x_4 = 375 + 523 = \boxed{898}.\]
Notice that we didn't need to use the values of $x_1$ or $x_3$ at all.

## Non-Rigorous Solution
Calculate the first few terms:
\[211,375,420,523,267,-211,-375,-420,-523,\dots\]
At this point it is pretty clear that the sequence is periodic with period 10 (one may prove it quite easily like in solution 1) so our answer is obviously $211+420+267=\boxed{898}$
~Dhillonr25

## Video Solution by OmegaLearn
https://youtu.be/lH-0ul1hwKw?t=870
~ pi_is_3.14
These problems are copyrighted © by the Mathematical Association of America.
# 2001 AMC 8 Problem 14

## Problem

Tyler has entered a buffet line in which he chooses one kind of meat, two different vegetables and one dessert. If the order of food items is not important, how many different meals might he choose?

$\text{(A)}\ 4 \qquad \text{(B)}\ 24 \qquad \text{(C)}\ 72 \qquad \text{(D)}\ 80 \qquad \text{(E)}\ 144$

## Solution 1
There are $3$ possibilities for the meat and $4$ possibilites for the dessert, for a total of $4\times3=12$ possibilities for the meat and the dessert. There are $4$ possibilities for the first vegetable and $3$ possibilities for the second, but order doesn't matter, so we overcounted by a factor of $2$ . For example, we counted 'baked beans and corn' and 'corn and baked beans' as $2$ different possibilities, so the total possibilites for the two vegetables is $\frac{4\times3}{2}=6$ , and the total number of possibilites is $12\times6=\boxed{\textbf{(C)}\ 72}.$

## Solution 2 (combinatorics)
To find the total ways, we multiply all the combinations of all 3 items:
For meat, it's asking how many ways can you pick $1$ item out of $3$ or $\binom{3}{1} = \frac{3!}{(3-1)! \cdot 1!} = \frac{3 \cdot 2 \cdot 1}{2 \cdot 1 \cdot 1} = 3$ (plain logic.)
For vegetables, it's the amount of ways you can pick $2$ items out of $4$ or $\binom{4}{2} = \frac{4!}{(4-2)! \cdot 2!} = \frac{4 \cdot 3 \cdot 2 \cdot 1}{2 \cdot 1 \cdot 2 \cdot 1} = \frac{12}{2} = 6$
For dessert, it's the amount of ways you can pick $1$ item out of $4$ or $\binom{4}{1} = \frac{4!}{(4-1)! \cdot 1!} = \frac{4 \cdot 3 \cdot 2 \cdot 1}{3 \cdot 2 \cdot 1 \cdot 1} = 4$ (also logic).
Therefore, it's $3\times6\times4=12\times6=\boxed{\textbf{(C)}\ 72}.$
~RandomMathGuy500
### See Also
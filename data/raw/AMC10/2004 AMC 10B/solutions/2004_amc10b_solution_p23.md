# 2004 AMC 10B Problem 23

## Problem

Each face of a cube is painted either red or blue, each with probability 1/2. The color of each face is determined independently. What is the probability that the painted cube can be placed on a horizontal surface so that the four vertical faces are all the same color?

$\mathrm{(A) \ } \frac{1}{4} \qquad \mathrm{(B) \ } \frac{5}{16} \qquad \mathrm{(C) \ } \frac{3}{8} \qquad \mathrm{(D) \ } \frac{7}{16} \qquad \mathrm{(E) \ } \frac{1}{2}$

## Solution 1
Label the six sides of the cube by numbers $1$ to $6$ as on a classic dice. Then the "four vertical faces" can be: $\{1,2,5,6\}$ , $\{1,3,4,6\}$ , or $\{2,3,4,5\}$ .
Let $A$ be the set of colorings where $1,2,5,6$ are all of the same color, similarly let $B$ and $C$ be the sets of good colorings for the other two sets of faces.
There are $2^6=64$ possible colorings, and there are $|A\cup B\cup C|$ good colorings. Thus the result is $\frac{|A\cup B\cup C|}{64}$ . We need to compute $|A\cup B\cup C|$ .
Using the Principle of Inclusion-Exclusion we can write \[|A\cup B\cup C| = |A|+|B|+|C| - |A\cap B| - |A\cap C| - |B\cap C| + |A\cap B\cap C|\]
Clearly $|A|=|B|=|C|=2^3=8$ , as we have two possibilities for the common color of the four vertical faces, and two possibilities for each of the horizontal faces.
What is $A\cap B$ ? The faces $1,2,5,6$ must have the same color, and at the same time faces $1,3,4,6$ must have the same color. It turns out that $A\cap B=A\cap C=B\cap C= A\cap B\cap C =$ the set containing just the two cubes where all six faces have the same color.
Therefore $|A\cup B\cup C| = 8+8+8-2-2-2+2 = 20$ , and the result is $\frac{20}{64}=\boxed{\frac{5}{16}}$ .

## Solution 2
Suppose we break the situation into cases that contain four vertical faces of the same color:
I. Two opposite sides of same color: There are 3 ways to choose the two sides, and then two colors possible, so $3 \cdot 2=6$ .
II. One face different from all the others: There are 6 ways to choose this face, and 2 colors, so $6 \cdot 2=12$ .
III. All faces are the same: There are 2 colors, and so two ways for all faces to be the same.
Adding them up, we have a total of $20$ ways to have four vertical faces the same color. There are $2^6$ ways to color the cube, so the answer is $\frac{20}{64}=\boxed{\frac{5}{16}}$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
# 2022 AMC 8 Problem 23

## Problem

A $\triangle$ or $\bigcirc$ is placed in each of the nine squares in a $3$ -by- $3$ grid. Shown below is a sample configuration with three $\triangle$ s in a line. [asy] //diagram size(5cm); defaultpen(linewidth(1.5)); real r = 0.37; path equi = r * dir(-30) -- (r+0.03) * dir(90) -- r * dir(210) -- cycle; draw((0,0)--(0,3)--(3,3)--(3,0)--cycle); draw((0,1)--(3,1)--(3,2)--(0,2)--cycle); draw((1,0)--(1,3)--(2,3)--(2,0)--cycle); draw(circle((3/2,5/2),1/3)); draw(circle((5/2,1/2),1/3)); draw(circle((3/2,3/2),1/3)); draw(shift(0.5,0.38) * equi); draw(shift(1.5,0.38) * equi); draw(shift(0.5,1.38) * equi); draw(shift(2.5,1.38) * equi); draw(shift(0.5,2.38) * equi); draw(shift(2.5,2.38) * equi); [/asy] How many configurations will have three $\triangle$ s in a line and three $\bigcirc$ s in a line?

$\textbf{(A) } 39 \qquad \textbf{(B) } 42 \qquad \textbf{(C) } 78 \qquad \textbf{(D) } 84 \qquad \textbf{(E) } 96$

## Solution 1 (Casework)
Notice that diagonals and a vertical-horizontal pair can never work, so the only possibilities are if all lines are vertical or if all lines are horizontal. These are essentially the same, so we'll count up how many work with all lines of shapes vertical, and then multiply by 2 at the end.
We take casework:
Case 1: 3 lines : In this case, the lines would need to be $2$ of one shape and $1$ of another, so there are $\frac{3!}{2} = 3$ ways to arrange the lines and $2$ ways to pick which shape has only one line. In total, this is $3\cdot 2 = 6.$
Case 2: 2 lines : In this case, the lines would be one line of triangles, one line of circles, and the last one can be anything that includes both shapes. There are $3! = 6$ ways to arrange the lines and $2^3-2 = 6$ ways to choose the last line. (We subtract $2$ from the last line because one arrangement of the last line is all triangles and the other arrangement of the last line is all circles, which causes Case 2 to overlap with Case 1 and further complicating the solution.) In total, this is $6\cdot 6 = 36.$
Finally, we add and multiply: $2(36+6)=2(42)=\boxed{\textbf{(D) }84}$ .
~wamofan

## Solution 2
We will only consider cases where the three identical symbols are the same column, but at the end we shall double our answer as the same holds true for rows. There are $3$ ways to choose a column with all $\bigcirc$ 's and $2$ ways to choose a column with all $\triangle$ 's. The third column can be filled in $2^3=8$ ways. Therefore, we have a total of $3\cdot2\cdot8=48$ cases. However, we overcounted the cases with $2$ complete columns of with one symbol and $1$ complete column with another symbol. This happens in $2\cdot3=6$ cases. $48-6=42$ . However, we have to remember to double our answer, giving us $\boxed{\textbf{(D) }84}$ ways to complete the grid.
~MathFun1000

## Video Solution (An excellent video solution that you will pick up)
https://youtu.be/tYWp6fcUAik?si=V8hv_zOn_zYOi9E5&t=2978 ~hsnacademy

## Video Solution by Math-X
I made A SECOND VERSION ( very easy to understand) https://youtu.be/ukCWuMbxxLU
~Math-X

## Video Solution
https://youtu.be/p7UHadjWqLg
Please like and subscribe!

## Video Solution by OmegaLearn
https://youtu.be/fL7DKXZjmAo?t=239
~ pi_is_3.14

## Video Solution
https://www.youtube.com/watch?v=or4pKVzQ3gI
~Mathematical Dexterity

## Video Solution
https://youtu.be/Ij9pAy6tQSg?t=2250
~Interstigation

## Video Solution
https://www.youtube.com/watch?v=KYglbGTvfsY
~David

## Video Solution
https://youtu.be/0orAAUaLIO0?t=257
~STEMbreezy

## Video Solution
https://youtu.be/YYvbTopjB1E
~savannahsolver

## Video Solution by Dr. David
https://youtu.be/CRHFEwZeqEM
### See Also
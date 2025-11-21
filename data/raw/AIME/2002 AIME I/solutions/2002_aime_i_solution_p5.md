# 2002 AIME I Problem 5

## Problem

Let $A_1,A_2,A_3,\cdots,A_{12}$ be the vertices of a regular dodecagon. How many distinct squares in the plane of the dodecagon have at least two vertices in the set $\{A_1,A_2,A_3,\cdots,A_{12}\} ?$

## Solution 1
There are 66 ways of picking two vertices. Note with any two vertices one can draw three squares ( two with the vertices forming a side, another with the vertices forming the diagonal). So so far we have $66(3)=198$ squares, but we have overcounted since some squares have their other two vertices in the dodecagon as well. All 12 combinations of two distinct vertices that form a square side only form 3 squares, and all 12 combinations of two vertices that form a square diagonal only form 6 squares. So in total, we have overcounted by $9+6=15$ , and $198-15=\fbox{183}$ .

## Solution 2
Proceed as above to initially get 198 squares (with overcounting). Then note that any square with all four vertices on the dodecagon has to have three sides "between" each vertex, giving us a total of three squares. However, we counted these squares with all four of their sides plus both of their diagonals, meaning we counted them 6 times. Therefore, our answer is $198-3(6-1)=198-15=\boxed{183}.$
~Dhillonr25
These problems are copyrighted © by the Mathematical Association of America.
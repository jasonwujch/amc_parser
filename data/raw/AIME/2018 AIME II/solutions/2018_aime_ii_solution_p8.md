# 2018 AIME II Problem 8

## Problem

A frog is positioned at the origin of the coordinate plane. From the point $(x, y)$ , the frog can jump to any of the points $(x + 1, y)$ , $(x + 2, y)$ , $(x, y + 1)$ , or $(x, y + 2)$ . Find the number of distinct sequences of jumps in which the frog begins at $(0, 0)$ and ends at $(4, 4)$ .

## Solution 1
We solve this problem by working backwards. Notice, the only points the frog can be on to jump to $(4,4)$ in one move are $(2,4),(3,4),(4,2),$ and $(4,3)$ . This applies to any other point, thus we can work our way from $(0,0)$ to $(4,4)$ , recording down the number of ways to get to each point recursively.
$(0,0): 1$
$(1,0)=(0,1)=1$
$(2,0)=(0, 2)=2$
$(3,0)=(0, 3)=3$
$(4,0)=(0, 4)=5$
$(1,1)=2$ , $(1,2)=(2,1)=5$ , $(1,3)=(3,1)=10$ , $(1,4)=(4,1)= 20$
$(2,2)=14, (2,3)=(3,2)=32, (2,4)=(4,2)=71$
$(3,3)=84, (3,4)=(4,3)=207$
$(4,4)=2\cdot \left( (4,2)+(4,3)\right) = 2\cdot \left( 207+71\right)=2\cdot 278=\boxed{556}$
A diagram of the numbers:
[asy] import graph; add(shift(0,0)*grid(4,4)); label((0,0), "1", SW); label((1,0), "1", SW); label((2,0), "2", SW); label((3,0), "3", SW); label((4,0), "5", SW); label((0,1), "1", SW); label((1,1), "2", SW); label((2,1), "5", SW); label((3,1), "10", SW); label((4,1), "20", SW); label((0,2), "2", SW); label((1,2), "5", SW); label((2,2), "14", SW); label((3,2), "32", SW); label((4,2), "71", SW); label((0,3), "3", SW); label((1,3), "10", SW); label((2,3), "32", SW); label((3,3), "84", SW); label((4,3), "207", SW); label((0,4), "5", SW); label((1,4), "20", SW); label((2,4), "71", SW); label((3,4), "207", SW); label((4,4), "556", SW); [/asy]
~First

## Solution 2
We'll refer to the moves $(x + 1, y)$ , $(x + 2, y)$ , $(x, y + 1)$ , and $(x, y + 2)$ as $R_1$ , $R_2$ , $U_1$ , and $U_2$ , respectively. Then the possible sequences of moves that will take the frog from $(0,0)$ to $(4,4)$ are all the permutations of $U_1U_1U_1U_1R_1R_1R_1R_1$ , $U_2U_1U_1R_1R_1R_1R_1$ , $U_1U_1U_1U_1R_2R_1R_1$ , $U_2U_1U_1R_2R_1R_1$ , $U_2U_2R_1R_1R_1R_1$ , $U_1U_1U_1U_1R_2R_2$ , $U_2U_2R_2R_1R_1$ , $U_2U_1U_1R_2R_2$ , and $U_2U_2R_2R_2$ . We can reduce the number of cases using symmetry.
Case 1: $U_1U_1U_1U_1R_1R_1R_1R_1$
There are $\frac{8!}{4!4!} = 70$ possibilities for this case.
Case 2: $U_2U_1U_1R_1R_1R_1R_1$ or $U_1U_1U_1U_1R_2R_1R_1$
There are $2 \cdot \frac{7!}{4!2!} = 210$ possibilities for this case.
Case 3: $U_2U_1U_1R_2R_1R_1$
There are $\frac{6!}{2!2!} = 180$ possibilities for this case.
Case 4: $U_2U_2R_1R_1R_1R_1$ or $U_1U_1U_1U_1R_2R_2$
There are $2 \cdot \frac{6!}{2!4!} = 30$ possibilities for this case.
Case 5: $U_2U_2R_2R_1R_1$ or $U_2U_1U_1R_2R_2$
There are $2 \cdot \frac{5!}{2!2!} = 60$ possibilities for this case.
Case 6: $U_2U_2R_2R_2$
There are $\frac{4!}{2!2!} = 6$ possibilities for this case.
Adding up all these cases gives us $70+210+180+30+60+6=\boxed{556}$ ways.

## Solution 3 (General Case)
Mark the total number of distinct sequences of jumps for the frog to reach the point $(x,y)$ as $\varphi (x,y)$ . Consider for each point $(x,y)$ in the first quadrant, there are only $4$ possible points in the first quadrant for frog to reach point $(x,y)$ , and these $4$ points are \[(x-1,y); (x-2,y); (x,y-1); (x,y-2)\] . As a result, the way to count $\varphi (x,y)$ is \[\varphi (x,y)=\varphi (x-1,y)+\varphi (x-2,y)+\varphi (x,y-1)+\varphi (x,y-2)\]
Also, for special cases, \[\varphi (0,y)=\varphi (0,y-1)+\varphi (0,y-2)\]
\[\varphi (x,0)=\varphi (x-1,0)+\varphi (x-2,0)\]
\[\varphi (x,1)=\varphi (x-1,1)+\varphi (x-2,1)+\varphi (x,0)\]
\[\varphi (1,y)=\varphi (1,y-1)+\varphi (1,y-2)+\varphi (0,y)\]
\[\varphi (1,1)=\varphi (1,0)+\varphi (0,1)\]
Start with $\varphi (0,0)=1$ , use this method and draw the figure below, we can finally get \[\varphi (4,4)=556\] (In order to make the LaTeX thing more beautiful to look at, I put $0$ to make every number $3$ digits)
\[005-020-071-207-\boxed{556}\] \[003-010-032-084-207\] \[002-005-014-032-071\] \[001-002-005-010-020\] \[001-001-002-003-005\]
So the total number of distinct sequences of jumps for the frog to reach $(4,4)$ is $\boxed {556}$ .
~Solution by $BladeRunnerAUG$ (Frank FYC)

## Solution 4 (Casework)
Casework Solution: x-distribution: 1-1-1-1 (1 way to order) y-distribution: 1-1-1-1 (1 way to order) $\dbinom{8}{4} = 70$ ways total
x-distribution: 1-1-1-1 (1 way to order) y-distribution: 1-1-2 (3 ways to order) $\dbinom{7}{3} \times 3= 105$ ways total
x-distribution: 1-1-1-1 (1 way to order) y-distribution: 2-2 (1 way to order) $\dbinom{6}{4} = 15$ ways total
x-distribution: 1-1-2 (3 ways to order) y-distribution: 1-1-1-1 (1 way to order) $\dbinom{7}{3} \times 3= 105$ ways total
x-distribution: 1-1-2 (3 ways to order) y-distribution: 1-1-2 (3 ways to order) $\dbinom{6}{3} \times 9= 180$ ways total
x-distribution: 1-1-2 (3 ways to order) y-distribution: 2-2 (1 way to order) $\dbinom{5}{3} \times 3 = 30$ ways total
x-distribution: 2-2 (1 way to order) y-distribution: 1-1-1-1 (1 way to order) $\dbinom{6}{4} = 15$ ways total
x-distribution: 2-2 (1 way to order) y-distribution: 1-1-2 (3 ways to order) $\dbinom{5}{3} \times 3 = 30$ ways total
x-distribution: 2-2 (1 way to order) y-distribution: 2-2 (1 way to order) $\dbinom{4}{2} = 6$ ways total
$6+30+15+105+180+70+30+15+105=\boxed{556}$ -fidgetboss_4000

## Video Solution
On The Spot STEM : https://www.youtube.com/watch?v=v2fo3CaAhmM
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
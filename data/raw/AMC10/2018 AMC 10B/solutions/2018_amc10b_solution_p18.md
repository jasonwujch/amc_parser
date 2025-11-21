# 2018 AMC 10B Problem 18

## Problem

Three young brother-sister pairs from different families need to take a trip in a van. These six children will occupy the second and third rows in the van, each of which has three seats. To avoid disruptions, siblings may not sit right next to each other in the same row, and no child may sit directly in front of his or her sibling. How many seating arrangements are possible for this trip?

$\textbf{(A)} \text{ 60} \qquad \textbf{(B)} \text{ 72} \qquad \textbf{(C)} \text{ 92} \qquad \textbf{(D)} \text{ 96} \qquad \textbf{(E)} \text{ 120}$

## Solution 1 (Casework)
We can begin to put this into cases. Let's call the pairs $a$ , $b$ and $c$ , and assume that a member of pair $a$ is sitting in the leftmost seat of the second row. We can have the following cases then.
Case $1$ : Second Row: a b c Third Row: b c a
Case $2$ : Second Row: a c b Third Row: c b a
Case $3$ : Second Row: a b c Third Row: c a b
Case $4$ : Second Row: a c b Third Row: b a c
For each of the four cases, we can flip the siblings, as they are distinct. So, each of the cases has $2 \cdot 2 \cdot 2 = 8$ possibilities. Since there are four cases, when pair $a$ has someone in the leftmost seat of the second row, there are $32$ ways to rearrange it. However, someone from either pair $a$ , $b$ , or $c$ could be sitting in the leftmost seat of the second row. So, we have to multiply it by $3$ to get our answer of $32 \cdot 3 = 96$ . So, the correct answer is $\boxed{\textbf{(D)} \text{ 96}}$ .
Written By: Archimedes15

## Solution 2(easy casework)
Lets call the siblings $A_1$ , $A_2$ , $B_1$ , $B_2$ , $C_1$ , and $C_2$ . We can split our problem into two cases:
There is a child of each family in each row (There is an A, B, C in each row ) or There are two children of the same family in a row.
Starting off with the first case, we see that there are $3!=6$ ways to arrange the A,B,C. Then, we have to choose which sibling sits. There are $2$ choices for each set of siblings meaning we have $2^3=8$ ways to arrange that. So, there are $48$ ways to arrange the siblings in the first row. The second row is a bit easier. We see that there are $2$ ways to place the A sibling and each placement yields only $1$ possibility. So, our first case has $48\cdot2=96$ possibilities.
In our second case, there are $3$ ways to choose which set of siblings will be in the same row and $4$ ways to choose the person in between. So, there $3*4 = 12$ ways to arrange the first row. In the second row, however, we see that it is impossible to make everything work out. So, there are $0$ possibilities for this case.
Thus, there are $96+0 = \boxed{D) 96}$ possibilities for this trip.
-Conantwiz2023

## Solution 3
Call the siblings $A_1$ , $A_2$ , $B_1$ , $B_2$ , $C_1$ , and $C_2$ .
There are 6 choices for the child in the first seat, and it doesn't matter which one takes it, so suppose Without loss of generality that $A_1$ takes it ( $\circ$ denotes an empty seat):
\[A_1 \circ \circ\] \[\circ \ \circ \ \circ\]
Then there are 4 choices for the second seat ( $B_1$ , $B_2$ , $C_1$ , or $C_2$ ). Like before, it doesn't matter who takes the seat, so WLOG suppose it is $B_1$ :
\[A_1 B_1 \circ \\\] \[\circ \ \circ \ \circ\]
The last seat in the first row cannot be $A_2$ because it would be impossible to create a second row that satisfies the conditions. Therefore, it must be $C_1$ or $C_2$ . Let's say WLOG that it is $C_1$ . There are two ways to create a second row:
\[A_1 B_1 C_1 \\\] \[B_2 C_2 A_2\]
and
\[A_1 B_1 C_1 \\\] \[C_2 A_2 B_2\]
Therefore, there are $6 \cdot 4 \cdot 2 \cdot 2= \boxed{\textbf{(D)} \text{ 96}}$ possible seating arrangements.
Written by: HoloGuard1728

## Solution 4
WLOG, define the three pairs of siblings to be: $A$ , $B$ , and $C$ . Now, notice that you can only form a correct grouping either like this:
\[A B C\]
\[B C A\]
or this:
\[C B A\]
\[A C B\]
However, we need to consider the different orders. There are $3!$ ways to order each pair (eg. the same letters) and $2^3$ ways to order the people each of the three pairs. Now, we can just multiply everything together, yielding:
\[2\cdot3!\cdot2^3\]
Which is $\boxed{\textbf{(D) } 96}$
-Ericshi1685

## Solution 5 (using answer choices)
Let the families be $A$ , $B$ , $C$ . In any given possible arrangement, there are $3! = 6$ ways to arrange the families and $2 \cdot 2 \cdot 2 = 8$ ways to arrange the siblings. This means the answer has to be divisble by $6 \cdot 8 = 48$ . The only answer choice that satisfies this is $\boxed{\textbf{(D) } 96}$

## Solution 6 (Derangement)
If a pair of siblings are in the same row, the other $2$ pairs of siblings cannot fit in the remaining $4$ seats to meet the requirements. Therefore, the siblings must be in different rows.
Let the first pair of siblings be $a_1$ , $a_2$ , the second pair of siblings be $b_1$ , $b_2$ , and the third pair of siblings be $c_1$ , $c_2$ . For each row there must be $1$ child from each family. WLOG, let $a_1$ , $b_1$ , $c_1$ be in the first row. There are $3!$ arrangements. $a_2$ , $b_2$ , $c_2$ are in the second row, and they cannot be in the same column as their sibling. Now the problem becomes a $3$ element Derangement problem.
An $n$ element derangement problem is to find the number of permutations of $n$ elements where each element has a specified location, and no element is in it's specified location. For example, there are $3$ elements $1$ , $2$ , $3$ . $1$ cannot be in the first location, $2$ cannot be in the second location, and $3$ cannot be in the third location. The derangements are: $(2,3,1)$ , $(3,1,2)$ . $D_3=2$ .
Each pair of siblings can swap their position. There are $2^3$ swaps. The total arrangements are: $3! \cdot D_3 \cdot 2^3=6 \cdot 2 \cdot 8 =\boxed{\textbf{(D) } 96}$
~ isabelchen
### Remarks
A key insight to solve this problem is to realize that one of the brother-sister pairs needs to be a "opposites" (ex. top left and bottom right or top right and bottom left). Using this, you can easily solve the question.
~YBSuburbanTea

## Video Solution by OmegaLearn
https://youtu.be/0W3VmFp55cM?t=1288
~ pi_is_3.14

## Video Solution
https://youtu.be/3MiGotKnC_U?t=1982 ~ ThePuzzlr
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
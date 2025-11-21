# 2024 AMC 10B Problem 20

## Problem

Three different pairs of shoes are placed in a row so that no left shoe is next to a right shoe from a different pair. In how many ways can these six shoes be lined up?

$\textbf{(A) } 60 \qquad\textbf{(B) } 72 \qquad\textbf{(C) } 90 \qquad\textbf{(D) } 108 \qquad\textbf{(E) } 120$

## Solution 1
Let $A_R, A_L, B_R, B_L, C_R, C_L$ denote the shoes.
There are $6$ ways to choose the first shoe. WLOG, assume it is $A_R$ . We have $A_R,$ __, __, __, __, __.
$~~~~~$ Case $1$ : The next shoe in line is $A_L$ . We have $A_R, A_L,$ __, __, __, __. Now, the next shoe in line must be either $B_L$ or $C_L$ . There are $2$ ways to choose which one, but assume WLOG that it is $B_L$ . We have $A_R, A_L, B_L,$ __, __, __.
$~~~~~ ~~~~~$ Subcase $1$ : The next shoe in line is $B_R$ . We have $A_R, A_L, B_L, B_R,$ __, __. The only way to finish is $A_R, A_L, B_L, B_R, C_R, C_L$ .
$~~~~~ ~~~~~$ Subcase $2$ : The next shoe in line is $C_L$ . We have $A_R, A_L, B_L, C_L,$ __, __. The only way to finish is $A_R, A_L, B_L, C_L, C_R, B_R$ .
$~~~~~$ In total, this case has $(6)(2)(1 + 1) = 24$ orderings.
$~~~~~$ Case $2$ : The next shoe in line is either $B_R$ or $C_R$ . There are $2$ ways to choose which one, but assume WLOG that it is $B_R$ . We have $A_R, B_R,$ __, __, __, __.
$~~~~~ ~~~~~$ Subcase $1$ : The next shoe is $B_L$ . We have $A_R, B_R, B_L,$ __, __, __.
$~~~~~ ~~~~~ ~~~~~$ Sub-subcase $1$ : The next shoe in line is $A_L$ . We have $A_R, B_R, B_L, A_L,$ __, __. The only way to finish is $A_R, B_R, B_L, A_L, C_L, C_R$ .
$~~~~~ ~~~~~ ~~~~~$ Sub-subcase $2$ : The next shoe in line is $C_L$ . We have $A_R, B_R, B_L, C_L,$ __, __. The remaining shoes are $C_R$ and $A_L$ , but these shoes cannot be next to each other, so this sub-subcase is impossible.
$~~~~~ ~~~~~$ Subcase $2$ : The next shoe is $C_R$ . We have $A_R, B_R, C_R,$ __, __, __. The next shoe in line must be $C_L$ , so we have $A_R, B_R, C_R, C_L,$ __, __. There are $2$ ways to finish, which are $A_R, B_R, C_R, C_L, A_L, B_L$ and $A_R, B_R, C_R, C_L, B_L, A_L$ .
$~~~~~$ In total, this case has $(6)(2)(1 + 2) = 36$ orderings.
Our final answer is $24 + 36 = \boxed{\textbf{(A) } 60}$

## Solution 2 (Tree Diagram)
Label the pairs \( (L_1, R_1) \), \( (L_2, R_2) \), and \( (L_3, R_3) \).
We now create a tree diagram. WLOG , we say our first tree diagram starts with \( L_1 \).
This tree has 10 branches.
Notice how we can interchange the first shoe with any \( L_1 \), \( L_2 \), \( L_3 \), \( R_1 \), \( R_2 \), \( R_3 \), and still get the same tree, but just interchanged shoes. Therefore, we just multiply the tree's branches by 6, to get \( 6 \cdot 10 = \) $\boxed{\textbf{(A) } 60}$ .
~Pinotation
~Diagram by Pinotation

## Solution 3 (Fakesolve, Refer to Solution 4)
We have two main cases:
Case 1: $LLLRRR$ or $RRRLLL$
There are $3! = 6$ ways to assign the shoes to the ordering. For now we'll focus on the $LLLRRR$ case and multiply by $2$ since they're symmetrical. WLOG say we have $A_LB_LC_LC_RA_RB_R$ . We can flip $A_L$ and $B_L$ among themselves and $A_R$ and $B_R$ among themselves, so we get $6 \cdot 2 \cdot 2 = 24.$ Multiplying by $2$ for symmetry gives us $48$ ways for this case.
Case 2: $RRLLLR$ or $RLLLRR$
Again, we'll focus on the $RRLLLR$ case and multiply by $2$ since they're symmetrical. WLOG say we have $B_RA_RA_LB_LC_LC_R$ . We can assign the shoes to the ordering in $3! = 6$ ways. $B_R$ can also be moved over to be next to $C_R$ . Then we would have $A_RA_LB_LC_LC_RB_R$ , which is also valid. So this case gives us $6 \cdot 2 = 12$ ways.
The answer is $48 + 12 = \boxed{60}.$
~ grogg007 , ~EaZ_Shadow WWW UWU

## Solution 4(focus on restrictions)
Notice that you cannot have $LRL$ or $RLR$ in a row, since you are guaranteed an $R$ and an $L$ from a different pair. This means you can either have three $L$ 's in a row, three $R$ 's in a row, or you have two $R$ 's between two $L$ 's and two $L$ 's between two $R$ 's.
Below are the cases(note that once an $L$ is fixed the $R$ adjacent to it is also fixed due to the constraint): \begin{align*} LLLRRR \Rightarrow 3!\cdot 2!=12\\ RLLLRR \Rightarrow 3!=6\\ RRLLLR \Rightarrow 3!=6\\ RRRLLL \Rightarrow 3!\cdot 2!=12\\ LRRRLL \Rightarrow 3!=6\\ LLRRRL \Rightarrow 3!=6\\ LRRLLR \Rightarrow 3!=6\\ RLLRRL \Rightarrow 3!=6\\ \end{align*}
We have $2\cdot 12+6\cdot 6=\boxed{\textbf{(A) }60}.$
~nevergonnagiveup

## Video Solution 1 by Pi Academy
https://youtu.be/c6nhclB5V1w?feature=shared
~ Pi Academy

## Video Solution 2 by SpreadTheMathLove
https://www.youtube.com/watch?v=yYpnHoTQNi4
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
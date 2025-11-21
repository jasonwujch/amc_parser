# 2020 AMC 8 Problem 10

## Problem

Zara has a collection of $4$ marbles: an Aggie, a Bumblebee, a Steelie, and a Tiger. She wants to display them in a row on a shelf, but does not want to put the Steelie and the Tiger next to one another. In how many ways can she do this?

$\textbf{(A) }6 \qquad \textbf{(B) }8 \qquad \textbf{(C) }12 \qquad \textbf{(D) }18 \qquad \textbf{(E) }24$

## Solution 1
Let the Aggie, Bumblebee, Steelie, and Tiger, be referred to by $A,B,S,$ and $T$ , respectively. If we ignore the constraint that $S$ and $T$ cannot be next to each other, we get a total of $4!=24$ ways to arrange the 4 marbles. We now simply have to subtract out the number of ways that $S$ and $T$ can be next to each other. If we place $S$ and $T$ next to each other in that order, then there are three places that we can place them, namely in the first two slots, in the second two slots, or in the last two slots (i.e. $ST\square\square, \square ST\square, \square\square ST$ ). However, we could also have placed $S$ and $T$ in the opposite order (i.e. $TS\square\square, \square TS\square, \square\square TS$ ). Thus there are 6 ways of placing $S$ and $T$ directly next to each other. Next, notice that for each of these placements, we have two open slots for placing $A$ and $B$ . Specifically, we can place $A$ in the first open slot and $B$ in the second open slot or switch their order and place $B$ in the first open slot and $A$ in the second open slot. This gives us a total of $6\times 2=12$ ways to place $S$ and $T$ next to each other. Subtracting this from the total number of arrangements gives us $24-12=12$ total arrangements $\implies\boxed{\textbf{(C) }12}$ .
We can also solve this problem directly by looking at the number of ways that we can place $S$ and $T$ such that they are not directly next to each other. Observe that there are three ways to place $S$ and $T$ (in that order) into the four slots so they are not next to each other (i.e. $S\square T\square, \square S\square T, S\square\square T$ ). However, we could also have placed $S$ and $T$ in the opposite order (i.e. $T\square S\square, \square T\square S, T\square\square S$ ). Thus there are 6 ways of placing $S$ and $T$ so that they are not next to each other. Next, notice that for each of these placements, we have two open slots for placing $A$ and $B$ . Specifically, we can place $A$ in the first open slot and $B$ in the second open slot or switch their order and place $B$ in the first open slot and $A$ in the second open slot. This gives us a total of $6\times 2=12$ ways to place $S$ and $T$ such that they are not next to each other $\implies\boxed{\textbf{(C) }12}$ . ~ junaidmansuri

## Solution 2
Let's try complementary counting. There $4!$ ways to arrange the 4 marbles. However, there are $2\cdot3!$ arrangements where Steelie and Tiger are next to each other. (Think about permutations of the element ST, A, and B or TS, A, and B). Thus, \[4!-2\cdot3!=\boxed{\textbf{(C) }12}\]

## Solution 3
We use complementary counting: we will count the numbers of ways where Steelie and Tiger are together and subtract that from the total count. Treat the Steelie and the Tiger as a "super marble." There are $2!$ ways to arrange Steelie and Tiger within this "super marble." Then there are $3!$ ways to arrange the "super marble" and Zara's two other marbles in a row. Since there are $4!$ ways to arrange the marbles without any restrictions, the answer is given by $4!-2!\cdot 3!=\boxed{\textbf{(C) }12}$
-franzliszt

## Solution 4
By the Georgeooga-Harryooga Theorem , our answer is $\frac{(4-2)!(4-2+1)!}{(4-2\cdot2+1)!}=\boxed{\textbf{(C) }12}$ .
-franzliszt

## Video Solution by EzLx(CookeMonster)
https://www.youtube.com/watch?v=6wyxS5wUwqI -EzLx(cookemonster) (GamingYT)

## Video Solution 3 (Fast)
https://youtu.be/MC-KA1STkSY
~Education, the Study of Everything

## Video Solution 4
https://youtu.be/U27z1hwMXKY?list=PLFcinOE4FNL0TkI-_yKVEYyA_QCS9mBNS&t=354
~STEMbreezy
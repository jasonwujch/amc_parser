# 2012 AIME I Problem 3

## Problem

Nine people sit down for dinner where there are three choices of meals. Three people order the beef meal, three order the chicken meal, and three order the fish meal. The waiter serves the nine meals in random order. Find the number of ways in which the waiter could serve the meal types to the nine people so that exactly one person receives the type of meal ordered by that person.

## Solution 1
Call a beef meal $B,$ a chicken meal $C,$ and a fish meal $F.$ Now say the nine people order meals $\text{BBBCCCFFF}$ respectively and say that the person who receives the correct meal is the first person. We will solve for this case and then multiply by $9$ to account for the $9$ different ways in which the person to receive the correct meal could be picked. Note, this implies that the dishes are indistinguishable, though the people aren't. For example, two people who order chicken are separate, though if they receive fish, there is only 1 way to order them.
The problem we must solve is to distribute meals $\text{BBCCCFFF}$ to orders $\text{BBCCCFFF}$ with no matches. The two people who ordered $B$ 's can either both get $C$ 's, both get $F$ 's, or get one $C$ and one $F.$ We proceed with casework.
- If the two $B$ people both get $C$ 's, then the three $F$ meals left to distribute must all go to the $C$ people. The $F$ people then get $BBC$ in some order, which gives three possibilities. The indistinguishability is easier to see here, as we distribute the $F$ meals to the $C$ people, and there is only 1 way to order this, as all three meals are the same.
- If the two $B$ people both get $F$ 's, the situation is identical to the above and three possibilities arise.
- If the two $B$ people get $CF$ in some order, then the $C$ people must get $FFB$ and the $F$ people must get $CCB.$ This gives $2 \cdot 3 \cdot 3 = 18$ possibilities.
Summing across the cases we see there are $24$ possibilities, so the answer is $9 \cdot 24 = \boxed{216.}$

## Solution 2- ONLY A COINCIDENCE
We only need to figure out the number of ways to order the string $BBBCCCFFF$ , where exactly one $B$ is in the first three positions, one $C$ is in the $4^{th}$ to $6^{th}$ positions, and one $F$ is in the last three positions. There are $3^3=27$ ways to place the first $3$ meals. Then for the other two people, there are $2$ ways to serve their meals. Thus, there are $(3\cdot2)^3=\boxed{216}$ ways to serve their meals.
$\textbf{Note: This solution gets the correct answer through coincidence and should not be used.}$

## Solution 3
First, choose the person that gets the correct meal. There's obviously $9$ ways to do that. Then, we can casework on who gets what type of meal. WLOG the person who had the correct meal had the chicken meal. The remaining chicken meals can be distributed to either one person who ordered beef and another who ordered fish, or can be distributed to two people who ordered the same type of meal that is not chicken. For the first case, it's apparent that there are $9$ ways of choosing who gets the two chicken meal, and two ways to order the remaining meals. For the second case, there are $6$ ways to choose who gets the two chicken meals and only $1$ way of ordering the remaining meals. Therefore, the answer is $9 \cdot (9 \cdot 2 + 6 \cdot 1) = \boxed {216}$ .
~Arcticturn

## Video Solution by Richard Rusczyk
https://artofproblemsolving.com/videos/amc/2012aimei/331
~ dolphin7

## Video Solution
https://www.youtube.com/watch?v=T8Ox412AkZc ~Shreyas S
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
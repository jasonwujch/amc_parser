# 2013 AMC 10A Problem 24

## Problem

Central High School is competing against Northern High School in a backgammon match. Each school has three players, and the contest rules require that each player play two games against each of the other school's players. The match takes place in six rounds, with three games played simultaneously in each round. In how many different ways can the match be scheduled?

$\textbf{(A)}\ 540\qquad\textbf{(B)}\ 600\qquad\textbf{(C)}\ 720\qquad\textbf{(D)}\ 810\qquad\textbf{(E)}\ 900$

## Solution 1
Let us label the players of the first team $A$ , $B$ , and $C$ , and those of the second team, $X$ , $Y$ , and $Z$ .
$\textbf{1}$ . One way of scheduling all six distinct rounds could be:
Round 1: $AX$ $BY$ $CZ$
Round 2: $AX$ $BZ$ $CY$
Round 3: $AY$ $BX$ $CZ$
Round 4: $AY$ $BZ$ $CX$
Round 5: $AZ$ $BX$ $CY$
Round 6: $AZ$ $BY$ $CX$
The above mentioned schedule ensures that each player of one team plays twice with each player from another team. Now you can generate a completely new schedule by permutating those $6$ rounds and that can be done in $6!=720$ ways.
$\textbf{2}$ . One can also make the schedule in such a way that two rounds are repeated.
(a)
Round 1: $AX$ $BZ$ $CY$
Round 2: $AX$ $BZ$ $CY$
Round 3: $AY$ $BX$ $CZ$
Round 4: $AY$ $BX$ $CZ$
Round 5: $AZ$ $BY$ $CX$
Round 6: $AZ$ $BY$ $CX$
(b)
Round 1: $AX$ $BY$ $CZ$
Round 2: $AX$ $BY$ $CZ$
Round 3: $AY$ $BZ$ $CX$
Round 4: $AY$ $BZ$ $CX$
Round 5: $AZ$ $BX$ $CY$
Round 6: $AZ$ $BX$ $CY$
As mentioned earlier any permutation of (a) and (b) will also give us a new schedule. For both (a) and (b) the number of permutations are $\frac{6!}{2!2!2!}$ = $90$
So the total number of schedules is $720+90+90$ = $\boxed{\textbf{(E)} 900}$ .

## Solution 2
Label the players of the first team $A$ , $B$ , and $C$ , and those of the second team, $X$ , $Y$ , and $Z$ . We can start by assigning an opponent to person $A$ for all $6$ games. Since $A$ has to play each of $X$ , $Y$ , and $Z$ twice, there are $\frac{6!}{2!2!2!} = 90$ ways to do this. We can assume that the opponents for $A$ in the $6$ rounds are $X$ , $X$ , $Y$ , $Y$ , $Z$ , $Z$ and multiply by $90$ afterwards.
Notice that for every valid assignment of the opponents of $A$ and $B$ , there is only $1$ valid assignment of opponents for $C$ . More specifically, the opponents for $C$ are the leftover opponents after the opponents for $A$ and $B$ are chosen in each round. Therefore, all we have to do is assign the opponents for $B$ . This is the same as finding the number of permutations of $X$ , $Y$ , and $Z$ that do not have a $X$ in the first two spots, an $Y$ in the next two spots, and a $Z$ in the final two spots.
We can use casework to find this by using the fact that after we put down the $X$ 's and $Y$ 's first there is $1$ way to put down the $Z$ 's (the two remaining spots).
If $X$ 's are put in the middle $2$ spots, then there is $1$ way to assign spots to $Y$ , namely the last $2$ spots. (If one of the last two spots are left empty, there will have to be a $Z$ there, which which not valid).
If $X$ 's are put in the last $2$ spots, then there is $1$ way to assign spots to $Y$ .
Finally, if one $X$ was put in on of the middle two spots and one $X$ was put in one of the last two spots, there are $2\cdot2$ ways to assign spots to $X$ and $2\cdot1$ ways to assign spots to $Y$ (one of the first two spots and the remaining spot in the last $2$ ).
There are $1+1+2\cdot2\cdot2\cdot1 = 10$ ways to assign opponents to $B$ and $90\cdot10 = 900$ ways to order the games. $\boxed{\textbf{(E)} 900}$

## Solution 3(similar to 2)
We only need to worry about what the other member of the pair would be for our own competitors. If our competitors are $A,B,C$ and the others are $1,2,3$ , then we only need to arrange the numbers $1,1,2,2,3,3$ such that we don't have the same number in the same spots. For our first row of numbers, or our first player, they can be arranged in any of \[\frac{6!}{2!2!2!}\] ways as nothing has happened yet. This contributes $90$ to our final product. Once we determine our second row, or player, the third will immediately follow thus we only need to figure out the second one. WLOG, our first arrangement was $112233$ . For our $1$ 's, we can put them anywhere that is not in our first $2$ spots. If we put both of them in the same "region", like the $2$ 's or the $3$ 's, then it will give a different case than if they were in different regions.
Case 1 : They are in the same region
There are $2$ ways that the $1$ 's can be in the same region. If, let's say its in the $2$ 's region, we try placing the $2's$ , we can only place them in the $3$ region in order to fit the $3$ 's. Therefore, this entire case produces $2$ arrangements. \\
Case 2: They are in a different region
There are $4$ ways that the $1$ 's can be in different regions. For the $2$ 's and $3$ 's, they will have to go in each other's region with $1$ and the other can be arranged in $2$ ways in the $1$ region giving a total of $8$ for this case.\\
Finally, $90(2+8) = 900$
~Vedoral
### Graph Theory Insight
This is a bipartite graph perfect matching problem. This bipartite graph has $3!=6$ perfect matchings. Arranging these 6 perfect matchings in 6 rounds gives $6!=720$ ways of scheduling, as Solution 1 states. But Solution 1 did not write about why there are 90 ways to make the schedule that two rounds are repeated, and why 90 is added twice. Let's call round 1 and 2 $P$ , round 3 and 4 $Q$ , round 5 and 6 $R$ .
And now the schedule is simply the permutation of $PPQQRR$ , which is: $\frac{6!}{2!2!2!}$ = $90$ So now we have to figure out how many $PPQQRR$ s there are. We first put in the $AX$ , $AY$ , and $AZ$ : $P$ ----> $AX$
Then there are 2 ways to put in $B$ 's match in $P$ :
a)
b)
Now we fill in $B$ 's match for $Q$ and $R$ . Notice how that for each a) and b) there is only one way to fill in $B$ 's match for $Q$ and $R$ . For a), if we put $BX$ in $Q$ , then $BZ$ must be in $R$ . But $AZ$ is already in $R$ , which makes it impossible. For b), if we put $BY$ in $Q$ , $BX$ must be in $R$ . Then, $CY$ has to be in both $P$ and $R$ which is impossible. So there is only one way to fill in $B$ 's match for $Q$ and $R$ .
a)
b)
Now we fill in $C$ 's matchs:
a)
b)
There are 2 $PPQQRR$ s, therefore 90 must be added twice.
~ isabelchen

## Video Solution by Richard Rusczyk
https://artofproblemsolving.com/videos/amc/2013amc10a/358
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
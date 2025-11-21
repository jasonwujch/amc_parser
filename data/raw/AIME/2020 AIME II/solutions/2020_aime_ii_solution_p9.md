# 2020 AIME II Problem 9

## Problem

While watching a show, Ayako, Billy, Carlos, Dahlia, Ehuang, and Frank sat in that order in a row of six chairs. During the break, they went to the kitchen for a snack. When they came back, they sat on those six chairs in such a way that if two of them sat next to each other before the break, then they did not sit next to each other after the break. Find the number of possible seating orders they could have chosen after the break.

## Solution (Bash)
There are $2^{5}-1$ intersections that we must consider if we are to perform a PIE bash on this problem. Since we don't really want to think that hard, and bashing does not take that long for this problem, we can write down half of all permutations that satisfy the conditions presented in the problem in "lexicographically next" order to keep track easily. We do this for all cases such that the first "person" is $A-C$ , and multiply by two, since the number of working permutations with $D-F$ as the first person is the same as if it were $A-C$ , hence, after doing such a bash, we get $45\times2=90$ permutations that result in no consecutive letters being adjacent to each other. ~afatperson

## Solution 2 (Official MAA)
Ayako ( $A$ ), Billy $(B)$ , Carlos $(C)$ , Dahlia $(D)$ , Ehuang $(E)$ , and Frank $(F)$ originally sat in the order $ABCDEF$ . Let $T(XY)$ denote the set of seatings where $X$ and $Y$ sit next to each other after the break. Then the required number of seating orders is given by the Inclusion-Exclusion Principle as \[6!-\big(|T(AB)|+|T(BC)|+|T(CD)|+|T(DE)|+|T(EF)|\big)+\] \[\big(|T(AB)\cap T(BC)|+|T(AB)\cap T(CD)|+\cdots\big) - \cdots.\] Each term can be calculated separately.
(a) $|T(AB)|=|T(BC)|=|T(CD)|=|T(DE)|=|T(EF)|=2\cdot5!=240.$ Because there are $5$ terms, the sum is $5\cdot240=1200$ .
(b) For $|T(XY)\cap T(ZW)|$ , if $Y=Z$ , then $XYW$ must sit consecutively, so $|T(XY)\cap T(ZW)|=2\cdot4!=48$ . There are $4$ terms that satisfy $Y=Z$ , so the sum is $4\cdot 48=192$ . If $XY$ and $ZW$ are pairwise disjoint, then $|T(XY)\cap T(ZW)|=2^2\cdot4!=96$ . There are $6$ terms, so the sum is $6\cdot96=576$ .
(c) If there are at least three pairs that sit next to each other, consider these three subcases: If the three pairs are consecutive, the sum is $3\cdot2\cdot3!=36$ . If exactly two of the pairs are consecutive, the sum is $6\cdot2^2\cdot3!=144$ . If none of the three pairs is consecutive, the sum is $1\cdot2^3\cdot3!=48.$
(d) If there are at least four pairs that sit next to each other, then if the pairs are consecutive, the sum is $2\cdot2\cdot2!=8$ . If the pairs are not consecutive, then the sum is $3\cdot2^2\cdot2!=24$ .
(e) If all five pairs sit next to each other, the number is $1\cdot2\cdot1!=2$ .
Therefore the required number of seating orders is \[6!-1200+(192+576)-{(36+144+48)+(8+24)-2}=90.\]
Note: See the A002464 of the On-Line Encyclopedia of Integer Sequences for equivalent formulations.

## Solution 3
We proceed with casework based on the person who sits first after the break.
$\textbf{Case 1:}$ A is first. Then the first three people in the row can be ACE, ACF, ADB, ADF, AEB, AEC, AFB, AFC, or AFD, which yield 2, 1, 2, 2, 1, 2, 0, 1, and 1 possible configurations, respectively, implying 2 + 1 + 2 + 2 + 1 + 2 + 0 + 1 + 1 = 12 possible configurations in this case.
$\textbf{Case 2:}$ B is first. Then the first three people in the row can be BDA, BDF, BEA, BEC, BFA, BFC, or BFD, which yield 2, 4, 2, 4, 0, 1, and 2 possible configurations, respectively, implying 2 + 4 + 2 + 4 + 0 + 1 + 2 = 15 possible configurations in this case.
$\textbf{Case 3:}$ C is first. Then the first three people in the row can be CAD, CAE, CAF, CEA, CEB, CFA, CFB, or CFD, which yield 1, 2, 1, 4, 4, 2, 2, and 2 possible configurations, respectively, implying 1 + 2 + 1 + 4 + 4 + 2 + 2 + 2 = 18 possible configurations in this case.
Finally, the number of valid configurations for A and F, B and E, and C and D are equal by symmetry, so our final answer is 2(12 + 15 + 18), which computes to be $\boxed{090}.$ ~peace09

## Solution 4
We determine the order of A, B, C, relative to each other. Then, we will insert D, E, F into the alignment and calculate the total number of possibilities. This solution can be visualised as standing in lines rather than sitting on chairs.
There are 6 possible alignments for A, B, and C, but we only evaluate 3 because the other 3 cases can be mirrored to overlap these 3 cases.
$\textbf{Case 1: A B C}$ In this case, there must be a person standing between A and B and also between B and C. Also, D cannot be adjacent to C. There are 9 possibilities.
$\textbf{Case 2: A C B}$ In this case, there must be a person standing between B and C. Also, D cannot be adjacent to C. There are 12 possibilities.
$\textbf{Case 3: C A B}$ In this case, there must be a person standing between A and B. Also, D cannot be adjacent to C. There are 24 possibilities.
So the total number of cases is 2(9+12+24)= $\boxed{090}$ .
-Superdolphin

## Solution 5 (Recursion, taking less time)
Consider arrangements of numbers $1, 2, 3, ..., n$ .
Let $f(n,k)$ be the number of arrangements in which $1$ and $2$ , $2$ and $3$ , $3$ and $4$ , ..., $k-1$ and $k$ aren't together. We need to find $f(6,6)$ .
Let $d(n,k)$ be the number of arrangements in which $1$ and $2$ , $2$ and $3$ , $3$ and $4$ , ..., $k-2$ and $k-1$ aren't together, but $(k-1)$ and $k$ are together.
Then,
\[f(n,k+1) = f(n,k) - d(n,k+1) ......(1)\]
\[d(n,k+1) = 2f(n-1,k) + d(n-1,k) ......(2)\]
Hence, \[f(n,k+1)=f(n,k)-f(n-1,k)-f(n-1,k-1)\]
And because $f(n,0) = f(n,1) = n!$ , it's easy to get $f(6,6) = \boxed{090}$
\[\begin{tabular}{|c|c|c|c|c|c|c|}\hline k,n & n=1 & n=2 & n=3 & n=4 & n=5 & n=6\\\hline k=1 & 1 & 2 & 6 & 24 & 120 & 720\\\hline k=2 & & 0 & 2 & 12 & 72 & 480\\\hline k=3 & & & 0 & 4 & 36 & 288\\\hline k=4 & & & & 2 & 20 & 180\\\hline k=5 & & & & & 14 & 124\\\hline k=6 & & & & & & 90\\\hline \end{tabular}\]
Note: How to get the two equations (1) and (2).
1. If $1$ and $2$ , $2$ and $3$ , ... , $k-1$ and $k$ aren't together, there are two cases:
(a) $k$ and $k+1$ aren't together. There are $f(n,k+1)$ ways of arrangements.
(b) $k$ and $k+1$ are together. There are $d(n,k+1)$ ways of arrangements.
Thus, $f(n,k)=f(n,k+1)+d(n,k+1)$ , i.e. $f(n,k+1)=f(n,k)-d(n,k+1)$ , which is the first equation.
2. If $1$ and $2$ , $2$ and $3$ , ... , $k-1$ and $k$ aren't together, but $k$ and $k+1$ are together, there are 2 cases :
(a) $k-1$ isn't together with $k$ or $k+1$ . We first determine the order of $k$ and $k+1$ , then, we can treat them as one number since they should be always together. Hence, the number of arrangements is $2f(n-1,k)$ .
(b) $k-1$ is together with $k$ or $k+1$ . We first determine the order of $k$ and $k+1$ , then treat them as one "super number". Since $k-1$ is together with the "super number", there are $2d(n-1,k)$ ways of arrangements. However, $k-1$ can only be on one side of the "super number" because $k-1$ and $k$ aren't together, so we need to multiple a $1/2$ to the number of arrangements. Finally, there are $2d(n-1,k)*(1/2)=d(n-1,k)$ ways of arrangements.
Thus, $d(n,k+1)=2f(n-1,k)+d(n-1,k)$ , which is the second equation.
~Shawn

## Solution 6 (fast)
We will split up our cases based on the positions of $A$ , $B$ , and $C$ relative to each other.
Case $1$ : $A$ $B$ $C$ : $9$ cases
Case $2$ : $A$ $C$ $B$ : $16$ cases
Case $3$ : $B$ $A$ $C$ : $20$ cases
Since we can reverse the first case to make $C$ $B$ $A$ , reverse the second case to make $B$ $C$ $A$ , and reverse the third case to make $C$ $A$ $B$ , by symmetry we have $2(9+16+20) = \boxed{090}$ ways in total.
~xHypotenuse
Isn't this the same as Solution 4?

## Video Solution
https://www.youtube.com/watch?v=Bh04e_J5YGs
~MathProblemSolvingSkills.com
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
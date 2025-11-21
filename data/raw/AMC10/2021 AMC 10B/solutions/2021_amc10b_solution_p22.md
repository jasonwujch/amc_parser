# 2021 AMC 10B Problem 22

## Problem

Ang, Ben, and Jasmin each have $5$ blocks, colored red, blue, yellow, white, and green; and there are $5$ empty boxes. Each of the people randomly and independently of the other two people places one of their blocks into each box. The probability that at least one box receives $3$ blocks all of the same color is $\frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. What is $m + n ?$

$\textbf{(A)} ~47 \qquad\textbf{(B)} ~94 \qquad\textbf{(C)} ~227 \qquad\textbf{(D)} ~471 \qquad\textbf{(E)} ~542$

## Solution 1 (Principle of Inclusion-Exclusion)
Let our denominator be $(5!)^3$ , so we consider all possible distributions.
We use PIE (Principle of Inclusion and Exclusion) to count the successful ones.
When we have at $1$ box with all $3$ blocks the same color in that box, there are $_{5} C _{1} \cdot _{5} P _{1} \cdot (4!)^3$ ways for the distributions to occur ( $_{5} C _{1}$ for selecting one of the five boxes for a uniform color, $_{5} P _{1}$ for choosing the color for that box, $4!$ for each of the three people to place their remaining items).
However, we overcounted those distributions where two boxes had uniform color, and there are $_{5} C _{2} \cdot _{5} P _{2} \cdot (3!)^3$ ways for the distributions to occur ( $_{5} C _{2}$ for selecting two of the five boxes for a uniform color, $_{5} P _{2}$ for choosing the color for those boxes, $3!$ for each of the three people to place their remaining items).
Again, we need to re-add back in the distributions with three boxes of uniform color... and so on so forth.
Our success by PIE is \[_{5} C _{1} \cdot _{5} P _{1} \cdot (4!)^3 - _{5} C _{2} \cdot _{5} P _{2} \cdot (3!)^3 + _{5} C _{3} \cdot _{5} P _{3} \cdot (2!)^3 - _{5} C _{4} \cdot _{5} P _{4} \cdot (1!)^3 + _{5} C _{5} \cdot _{5} P _{5} \cdot (0!)^3 = 120 \cdot 2556.\] \[\frac{120 \cdot 2556}{120^3}=\frac{71}{400},\] yielding an answer of $\boxed{\textbf{(D) }471}$ .
### Alternate Simplification
As In Solution 1, the probability is \[\frac{\binom{5}{1}\cdot 5\cdot (4!)^3 - \binom{5}{2}\cdot 5\cdot 4\cdot (3!)^3 + \binom{5}{3}\cdot 5\cdot 4\cdot 3\cdot (2!)^3 - \binom{5}{4}\cdot 5\cdot 4\cdot 3\cdot 2\cdot (1!)^3 + \binom{5}{5}\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1}{(5!)^3}\] \[= \frac{5\cdot 5\cdot (4!)^3 - 10\cdot 5\cdot 4\cdot (3!)^3 + 10\cdot 5\cdot 4\cdot 3\cdot (2!)^3 - 5\cdot 5! + 5!}{(5!)^3}.\] Dividing by $5!$ , we get \[\frac{5\cdot (4!)^2 - 10\cdot (3!)^2 + 10\cdot (2!)^2 - 5 + 1}{(5!)^2}.\] Dividing by $4$ , we get \[\frac{5\cdot 6\cdot 24 - 10\cdot 9 + 10 - 1}{30\cdot 120}.\] Dividing by $9$ , we get \[\frac{5\cdot 2\cdot 8 - 10 + 1}{10\cdot 40} = \frac{71}{400} \implies \boxed{\textbf{(D) }471}.\]

## Solution 2 (Complementary Counting)
Use complementary counting. Denote $T_n$ as the total number of ways to put $n$ colors to $n$ boxes by 3 people out of which $f_n$ ways are such that no box has uniform color. Notice $T_n = (n!)^3$ . From this setup we see the question is asking for $1-\frac{f_5}{(5!)^3}$ . To find $f_5$ we want to exclude the cases of a) one box of the same color, b) 2 boxes of the same color, c) 3 boxes of same color, d) 4 boxes of the same color, and e) 5 boxes of the same color. Cases d) and e) coincide. From this, we have
\[f_5=T_5 -{\binom{5}{1}\binom{5}{1}\cdot f_4 - \binom{5}{2}\binom{5}{2}\cdot 2!\cdot f_3 - \binom{5}{3}\binom{5}{3}\cdot 3!\cdot f_2 - 5!}\]
In case b), there are $\binom{5}{2}$ ways to choose 2 boxes that have the same color, $\binom{5}{2}$ ways to choose the two colors, 2! ways to permute the 2 chosen colors, and $f_3$ ways so that the remaining 3 boxes don’t have the same color. The same goes for cases a) and c). In case e), the total number of ways to permute 5 colors is $5!$ . Now, we just need to calculate $f_2$ , $f_3$ and $f_4$ .
We have $f_2=T_2-2 = (2!)^3 - 2 = 6$ , since we subtract the number of cases where the boxes contain uniform colors, which is 2.
In the same way, $f_3=T_3-\Big[3!+ \binom{3}{1}\binom{3}{1}\cdot f_2 \Big] = 156$ - again, we must subtract the number of ways at least 1 box has uniform color. There are $3!$ ways if 3 boxes each contains uniform color. Two boxes each contains uniform color is the same as previous. If one box has the same color, there are $\binom{3}{1}$ ways to pick a box, and $\binom{3}{1}$ ways to pick a color for that box, 1! ways to permute the chosen color, and $f_2$ ways for the remaining 2 boxes to have non-uniform colors. Similarly, $f_4=(4!)^3-\Big[ 4!+ \binom{4}{2}\binom{4}{2}\cdot 2! \cdot f_2+ \binom{4}{1}\binom{4}{1}\cdot f_3\Big] = 10,872$
Thus, $f_5 = f_5=(5!)^3-\Big[\binom{5}{1}\binom{5}{1}\cdot f_4+ \binom{5}{2}\binom{5}{2}\cdot 2!\cdot f_3+\binom{5}{3}\binom{5}{3}\cdot 3!\cdot f_2 + 5!\Big] = (5!)^3 - 306,720$
Thus, the probability is $\frac{306,720}{(5!)^3} = 71/400$ and the answer is $\boxed{\textbf{(D) }471}$
-angelinasheeen

## Solution 3 (WLOG and PIE)
WLOG fix which block Ang places into each box. (This can also be thought of as labeling each box by the color of Ang's block.) There are then $(5!)^2$ total possibilities.
As in Solution 1 , we use PIE. With $1$ box of uniform color, there are ${}_{5} C _{1} \cdot (4!)^2$ possibilities ( ${}_{5} C _{1}$ for selecting one of the five boxes (whose color is fixed by Ang), $4!$ for each of Ben and Jasmin to place their remaining items). We overcounted cases with $2$ boxes, of which there are ${}_{5} C _{2} \cdot (3!)^2$ possibilities, and so on.
The probability is thus \[\frac{{}_{5} C _{1} \cdot (4!)^2 - {}_{5} C _{2} \cdot (3!)^2 + {}_{5} C _{3} \cdot (2!)^2 - {}_{5} C _{4} \cdot (1!)^2 + {}_{5} C _{5} \cdot (0!)^2}{(5!)^2}\] \[= \frac{5 \cdot (4!)^2 - 10 \cdot (3!)^2 + 10 \cdot (2!)^2 - 5 + 1}{(5!)^2}\] at which point we can proceed as in the Alternate simplification to simplify to $\frac{71}{400} \implies \boxed{\textbf{(D)}~471}$ .
~ emerald_block

## Solution 4 (Derangements)
$!n$ denotes the number of derangements of $n$ elements, i.e. the number of permutations where no element appears in its original position. Recall the recursive formula $!0 = 1, !1 = 0, !n = (n-1)(!(n-1)+{!}(n-2))$ .
We will consider the number of candidate boxes (ones that currently remain uniform-color) after each person places their blocks.
After Ang, all $5$ boxes are candidates, and each has a fixed color its blocks must be to remain uniform-color.
Ben has $5!$ total ways to place blocks. There are $\tbinom{5}{k}\cdot{!}k$ ways to disqualify $k$ candidates, $0 \le k \le 5$ . (There are $\tbinom{5}{k}$ ways to choose the candidates to disqualify, and $!k$ ways to arrange the disqualified candidates' same-color blocks.)
Jasmin has $5!$ total ways to place blocks. Currently, $k$ boxes are no longer candidates. Consider the number of ways for Jasmin to place blocks such that no box remains a candidate, where $n$ is the number of boxes and $k$ is the number of non-candidates, and call it $D(n,k)$ (not to be confused with partial derangements). We wish to find $5!-D(5,k)$ for each $k$ , $0 \le k \le 5$ .
Notice that $D(n,0) = {!}n$ , since all boxes are candidates and no block can be placed in the same-colored box. Also notice the recursive formula $D(n,k) = D(n-1,k-1)+D(n,k-1)$ , since the first non-candidate box can either contain its same-color block (in which case it can be ignored), or a different-color block (in which case it can be treated as a candidate).
We can make a table ( $n$ horizontal, $k$ vertical): \[\begin{array}{r|rrrrrr} D(n,k) & 0 & 1 & 2 & 3 & 4 & 5 \\ \hline 0 & 1 & 0 & 1 & 2 & 9 & 44 \\ 1 & & 1 & 1 & 3 & 11 & 53 \\ 2 & & & 2 & 4 & 14 & 64 \\ 3 & & & & 6 & 18 & 78 \\ 4 & & & & & 24 & 96 \\ 5 & & & & & & 120 \\ \end{array}\] (Note that $D(n,n) = n!$ since there are no candidates to begin with, which checks out with the diagonal.)
The desired values of $D(5,k)$ are in the rightmost column.
The probability that at least one box is of uniform color is thus \begin{align*} & \frac{\sum_{k=0}^{5}{\left(\binom{5}{k}\cdot{!}k\right)(5!-D(5,k))}}{(5!)^2} \\ ={}& \frac{(1\cdot1)(120-44)+(5\cdot0)(120-53)+(10\cdot1)(120-64)+(10\cdot2)(120-78)+(5\cdot9)(120-96)+(1\cdot44)(120-120)}{(5!)^2} \\ ={}& \frac{76+0+560+840+1080+0}{(5!)^2} \\ ={}& \frac{19+140+210+270}{(5!)(5\cdot3\cdot2)} \\ ={}& \frac{639}{(5!)(5\cdot3\cdot2)} \\ ={}& \frac{71}{(5\cdot4\cdot2)(5\cdot2)} \\ ={}& \frac{71}{400} \implies \boxed{\textbf{(D)}~471}. \\ \end{align*}
~ emerald_block

## Video Solution by OmegaLearn (PIE)
https://youtu.be/o0S8SqRO0Yc
~ pi_is_3.14

## Video Solution by Interstigation
https://youtu.be/OVW9KhmmrVQ
~ Briefly went over Principal of Inclusion Exclusion using Venn Diagram
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
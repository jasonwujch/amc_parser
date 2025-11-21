# 2008 AMC 10B Problem 22

## Problem

Three red beads, two white beads, and one blue bead are placed in line in random order. What is the probability that no two neighboring beads are the same color?

$\mathrm{(A)}\ 1/12\qquad\mathrm{(B)}\ 1/10\qquad\mathrm{(C)}\ 1/6\qquad\mathrm{(D)}\ 1/3\qquad\mathrm{(E)}\ 1/2$

## Solution 1 (Order Matters)
There are two ways to arrange the red beads, where $R$ represents a red bead and $-$ represents a blank space.
$1. R - R - R -$
$2. R - - R - R$
In the first, there are three ways to place a bead in the first free space, two for the second free space, and one for the third, so there are $6$ arrangements. In the second, a white bead must be placed in the third free space, so there are two possibilities for the third space, two for the second, and one for the first. That makes $4$ arrangements. There are $6+4=10$ arrangements in total. The two cases above can be reversed, so we double $10$ to get $20$ arrangements. Also, in each case, there are three ways to place the first red bead, two for the second, and one for the third, so we multiply by $6$ to get $20\cdot 6 = 120$ arrangements. There are $6! = 720$ total arrangements so the answer is $120/720 = \boxed{1/6}$ .

## Solution 2 (Order Doesn't Matter)
If you list the cases for the red balls and blanks, these are four scenarios:
$1. R - - R - R$
$2. R - R - - R$
$3. R - R - R -$
$4. - R - R - R$
In cases 1 and 2, the white balls must go in the blank surrounded on either side by the red balls. Like this: $1. R - - R W R$ $2. R W R - - R$ However, now with only one white ball and one blue ball left, there are two ways to order them in both cases. So for a total of $2 + 2 = 4$ possibilities.
In the last two cases, the two white balls and the blue ball can go anywhere in those three blanks, because they are separated by a red ball. So there are $3$ ways for each case. This adds up to a total of $6$ possibilities for the last two cases.
Adding them up, we get $10$ total orderings.
There are $\frac{6!}{3! * 2! * 1!} = 60$ total orderings.
So the answer is $\frac{10}{60} = \boxed{1/6}$ .

## Solution 3
There are 3 cases:
### Case 1
There is a block of $RWRWR$ . The $B$ can go in any slot between two letters. 6 ways.
### Case 2
There is a $RBR$ . Then, there is a $WRW$ , and there are 2 orderings.
### Case 3
There is a $WBW$ . Then, there is a $RWR$ , and there are 2 orderings.
There are 60 ways total, and 10 valid ones, giving $\boxed{\frac{1}{6}}$ as the answer.

## Solution 4
There are $\frac{6!}{3!\cdot2!\cdot1!}=60$ total orderings.
Suppose we order the red and white beads first. If these two colors are ordered first, we must make sure that no neighboring beads are the same color, or only one pair of neighboring beads are the same color. There are five possible orderings:
$R\ W R\ W R$
$R\ R\ W R\ W$
$W R\ R\ W R$
$R\ W R\ R\ W$
$W R\ W R\ R$
For the first case, there are $6$ possible places we can put the blue bead. For the other 4 cases, there is only one place we can put the blue bead, which is between the pair of red beads. The desired probability is $\frac{6+4(1)}{60}=\frac{10}{60}=\boxed{\mathrm{(C) }\frac16}$

## Solution 5 (Video Solution)
Video: https://youtu.be/qnAAzoRANG4
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
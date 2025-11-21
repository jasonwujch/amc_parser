# 2024 AMC 8 Problem 25

## Problem

A small airplane has $4$ rows of seats with $3$ seats in each row. Eight passengers have boarded the plane and are distributed randomly among the seats. A married couple is next to board. What is the probability there will be 2 adjacent seats in the same row for the couple?

[asy] // Asymptote by aoum import roundedpath; unitsize(1cm); path p = roundedpath((0,0)--(1,0)--(1,1)--(0,1)--cycle, 0.1); for (int r = 0; r < 4; ++r) { for (int c = 0; c < 3; ++c) { draw(shift(1.1 * c, 1.3 * r) * p); } } [/asy]

$\textbf{(A)} \frac{8}{15}\qquad\textbf{(B)} \frac{32}{55}\qquad\textbf{(C) } \frac{20}{33}\qquad\textbf{(D) } \frac{34}{55}\qquad\textbf{(E) } \frac{8}{11}$

## Solution 1 (Complementary Counting Casework)
Suppose the passengers are indistinguishable. There are $\binom{12}{8} = 495$ total ways to distribute the passengers. We proceed with complementary counting, and instead, will count the number of passenger arrangements such that the couple cannot sit anywhere. Consider the partitions of $8$ among the rows of $3$ seats, to make our lives easier, assuming they are non-increasing. We have $(3, 3, 2, 0), (3, 3, 1, 1), (3, 2, 2, 1), (2, 2, 2, 2)$ .
For the first partition, clearly, the couple will always be able to sit in the row with $0$ occupied seats, so we have $0$ cases here.
For the second partition, there are $\frac{4!}{2!2!} = 6$ ways to permute the partition. Now the rows with exactly $1$ passenger must be in the middle, so this case generates $6$ cases.
For the third partition, there are $\frac{4!}{2!} = 12$ ways to permute the partition. For rows with $2$ passengers, there are $\binom{3}{2} = 3$ ways to arrange them in the row so that the couple cannot sit there. The row with $1$ passenger must be in the middle. We obtain $12 \cdot 3^2 = 108$ cases.
For the fourth partition, there is $1$ way to permute the partition. As said before, rows with $2$ passengers can be arranged in $3$ ways, so we obtain $3^4 = 81$ cases.
Collectively, we obtain a total of $6 + 108 + 81 = 195$ cases. The final probability is $1 - \frac{195}{495} = \boxed{\textbf{(C)}~\frac{20}{33}}$ .
~ blueprimes , Wrenmath

## Solution 2 (Straightforward Casework)
Suppose the passengers are indistinguishable.
What this question is asking, is really, if 4 empty seats are placed, what is the probability that there are 2 adjacent seats open.
We proceed by casework.
Case 1: There is exactly one pair of open seats. Then the other seat in that row must be occupied. The other two empty seats are distributed across the remaining $3$ rows without being adjacent, which is $\binom{9}{2}-6=30$ cases per pair of open seats for $30\cdot8=240$ total cases.
Case 2: There is one row of open seats. $4$ ways to choose the row and $9$ to choose the final empty seat for $4\cdot9=36$ cases.
Case 3: There are $2$ independent pairs of open seats. Choose the $2$ rows, then the placement of each pair within each row for $\binom{4}{2}\cdot2^2=24$ cases.
In total, we get $240+36+24=300$ cases total for a probability of \[\frac{300}{\binom{12}{4}}=\frac{300}{495}=\boxed{\mathbf{(C)}~\frac{20}{33}}\]
~rhydon516

## Solution 3 (Complementary Casework on Middle Seats)
We notice that if we have a middle seat in a row, then the couple cannot sit in that row. So, we perform complementary casework.
Case 1: Four people sitting in middle seats.
In this case, there are 4 people left to order, and 8 seats. This gives $\dbinom{8}{4}$ total combinations for this case.
Case 2: Three people sitting in middle seats.
In this case, there are $\dbinom{4}{3}$ ways to permute the rows in which the middle seat is occupied. For the row in which the people do not occupy the middle row, we must have two people sitting at the ends of the rows to guarantee the couple cannot sit there. So, for the rest of the 3 people, there are 6 possible seats. So, there are $\dbinom{4}{3} \cdot \dbinom{6}{3}$ total combinations.
Case 3: Two people sitting in middle seats.
In this case, there are $\dbinom{4}{2}$ ways to permute the rows in which the middle seat is occupied. For the rows in which the people do not occupy the middle row, we must have two people sitting at the ends of the rows to guarantee the couple cannot sit there. So, for the rest of the 2 people, there are 4 possible seats. So, there are $\dbinom{4}{2} \cdot \dbinom{4}{2}$ total combinations.
Case 4: One person sitting in a middle seat
In this case, there are $\dbinom{4}{1}$ ways to permute the rows in which the middle seat is occupied. For the rows in which the people do not occupy the middle row, we must have two people sitting at the ends of the rows to guarantee the couple cannot sit there. So, for the rest of the last person, there are 2 possible seats. So, there are $\dbinom{4}{1} \cdot \dbinom{2}{1}$ total combinations.
Case 5: Zero people sitting in a middle seat
In this case, we must have every person sitting at the ends of the seats. So, there is only 1 combination.
In total, we have
\[\dbinom{8}{4} + \dbinom{4}{3} \cdot \dbinom{6}{3} + \dbinom{4}{2} \cdot \dbinom{4}{2} + \dbinom{4}{1} \cdot \dbinom{2}{1} +1\]
combinations, or 195 combinations. The final step is to find the total amount of combinations without restrictions. This is simply $\dbinom{12}{4} = 495$ . So, finally employing complementary counting, we have that the probability that there will be 2 adjacent seats for the couple is
\[1 - \dfrac{195}{495} = \dfrac{20}{33}.\]
~NTfish

## Solution 4 (Permutations, Fastest + Simplest Written Solution)
There are $12\cdot 11 = 132$ for two people (the married couple) to be seated. This will be our denominator.
There are $8$ pairs of seats that are next to each other in the diagram ( $2$ per row; left-middle and middle-right). This will be our numerator.
Since there are $8+2=10$ total people on the plane, we should multiply our numerator by that to account for all ways the 10 people could be seated (e.x. the husband and the wife could be switched around and it would still work, same applies to the other passengers)
Therefore, our numerator is $8 \cdot 10 = 80$ .
This creates the fraction $\frac{80}{132}$ , which simplifies to \[\boxed{(\text{\bf{C}}) \: \frac{20}{33}}.\]
- Siddharth Mirchandani (svm2020), John Adams Middle School
Remark: This solution is flawed because if there are $9+2=11$ people on the plane, the probablity could not be calculated this way, because intuitively, the probability should be decreased (as the probability for 9 people and 1 couple is $\frac{19}{55}$ ), not increased (to be $\frac{2}{3}$ ). -ericz

## Solution 5
Consider the couple seated together and there should be 8 seated ways (2 ways in each row). And the other 8 people can be seated in other 10 seats randomly.
There will be total $8\cdot P(10, 2)$
Consider two double counting cases.
Case I: the other 8 people are seated in (1, 3) (2, 3), (3, 1), (3, 2), (3, 3), (4, 1), (4, 2), (4, 3)
It was double counted for couple's seats (1, 1) (1, 2) and (2, 1), (2, 2)
There will be $\frac{8\cdot 6}{2}\times P(8, 8)$
Case II: one whole row is empty and the other 8 people are randomly seated in other rows
It was double counted for couple's seats such as (1, 1) (1, 2) and (1, 2) (1, 3)
There will be $4\cdot P(9, 8)$
So the probability is $\frac{8\cdot P(10, 2)-\frac{8\cdot 2}{2}\cdot P(8, 8)-4\cdot P(9, 8)}{P(12, 8)}$
which simplifies to \[\boxed{(\text{\bf{C}}) \: \frac{20}{33}}.\]
- Orlando Liu Cupertino Middle School

## Video Solution 1
~Math-X

## Video Solution 2 by Central Valley Math Circle (Goes through full thought process)
~mr_mathman

## Video Solution 3
~hsnacademy

## Video Solution 4 by OmegaLearn.org
https://youtu.be/WYxfsShInyM

## Video Solution 5 by SpreadTheMathLove
https://www.youtube.com/watch?v=ArN4qVlBDTM

## Video Solution 6
~NiuniuMaths

## Video Solution by 7 CosineMethod
https://www.youtube.com/watch?v=bxZHXPMcsGI

## Video Solution 8 by Interstigation
https://youtu.be/ktzijuZtDas&t=3297

## Video Solution 9 by MegaMath
https://www.youtube.com/watch?v=DgQsljPaE5Y

## Video Solution 10 by Dr. David
https://youtu.be/L5UlR5QvEnA

## Video Solution 11 by WhyMath
https://youtu.be/nz0GYQLOFrM

## Video Solution 12 by Daily Dose of Math
~Thesmartgreekmathdude

## Video Solution (3-case reverse casework)
~TheMathGeek
### See Also
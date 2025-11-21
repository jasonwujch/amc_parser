# 2014 AMC 10B Problem 16

## Problem

Four fair six-sided dice are rolled. What is the probability that at least three of the four dice show the same value?

$\textbf {(A) } \frac{1}{36} \qquad \textbf {(B) } \frac{7}{72} \qquad \textbf {(C) } \frac{1}{9} \qquad \textbf {(D) } \frac{5}{36} \qquad \textbf {(E) } \frac{1}{6}$

## Solution 1
We split this problem into $2$ cases.
First, we calculate the probability that all four are the same. After the first dice, all the numbers must be equal to that roll, giving a probability of $1 \cdot \dfrac{1}{6} \cdot \dfrac{1}{6} \cdot \dfrac{1}{6} = \dfrac{1}{216}$ .
Second, we calculate the probability that three are the same and one is different. After the first dice, the next two must be equal and the third different. There are $4$ orders to roll the different dice, giving $4 \cdot 1 \cdot \dfrac{1}{6} \cdot \dfrac{1}{6} \cdot \dfrac{5}{6} = \dfrac{5}{54}$ .
Adding these up, we get $\dfrac{7}{72}$ , or $\boxed{\textbf{(B)}}$ .

## Solution 2
Note that there are two cases for this problem
$\textbf{Case 1}$ : Exactly three of the dices show the same value.
There are $5$ values that the remaining die can take on, and there are $\binom{4}{3}=4$ ways to choose the die. There are $6$ ways that this can happen. Hence, $6\cdot 4\cdot5=120$ ways.
$\textbf{Case 2}$ : Exactly four of the dices show the same value.
This can happen in $6$ ways.
Hence, the probability is $\frac{120+6}{6^{4}}=\frac{21}{216}\implies \frac{7}{72}\implies \boxed{\textbf{(B)}}$

## Solution 3
We solve using PIE .
We first calculate the number of ways that we can have $3$ dice be the same and the other dice be anything. We therefore have $\binom{4}{3} \cdot 6 \cdot 6 = 144$ ways to have at least $3$ dice be the same.
But wait! We have overcounted the case where all $4$ dice are the same! Since the previous case occurs in each of these cases $4$ times, we must subtract the $4$ -dice total three times in order to have them counted once. There are $6$ ways to have four dice be the same, so we our total count is $144 - 3(6) = 126$ .
Therefore, our probability is $\frac{126}{6^4} = \boxed{\frac{7}{72}}$ , which is answer choice $\boxed{\textbf{(B)}}$ .
-FIREDRAGONMATH16

## Solution 4
There are two cases to consider: Three of the dice roll the same number, and all four of the dice roll the same number.
For the first case, there is a $\frac{1}{6^4}$ chance that one number will be rolled four times in a row. Since there are six numbers on a die, we multiply by $6$ to see that the probability for the first case is $\frac{1}{6^3}.$
For the second case, consider the roll $AAAB$ , where three of the dice are identical and the fourth differs. The probability of the first three rolling the same number is $1\cdot{\frac{1}{6}}\cdot{\frac{1}{6}},$ because the first number can be anything, and the second must be identical. The probability of the last roll being different is $\frac{5}{6}$ , as it can be anything except for what has been previously rolled.
Multiplying these together, the probability for the second case is $\frac{5}{6^3}.$ However, there are $\frac{4!}{3!\cdot{1!}} = 4$ ways to arrange $AAAB$ , so we must multiply by a factor of 4 to get the true probability for this case, which is $4(\frac{5}{6^3}) = \frac{20}{6^3}.$
Adding these two cases, we get the requested probability: $\frac{1+20}{6^3} = \frac{21}{216} = \frac{7}{72},$ or answer choice $\boxed{\textbf{(B)}}$
-Benedict T (countmath1)
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
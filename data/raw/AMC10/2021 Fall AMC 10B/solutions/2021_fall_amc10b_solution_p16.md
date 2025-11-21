# 2021 Fall AMC 10B Problem 16

## Problem

Five balls are arranged around a circle. Chris chooses two adjacent balls at random and interchanges them. Then Silva does the same, with her choice of adjacent balls to interchange being independent of Chris's. What is the expected number of balls that occupy their original positions after these two successive transpositions?

$(\textbf{A})\: 1.6\qquad(\textbf{B}) \: 1.8\qquad(\textbf{C}) \: 2.0\qquad(\textbf{D}) \: 2.2\qquad(\textbf{E}) \: 2.4$

## Solution 1
After the first swap, we do casework on the next swap.
Case 1: Silva swaps the two balls that were just swapped
There is only one way for Silva to do this, and it leaves 5 balls occupying their original position.
Case 2: Silva swaps one ball that has just been swapped with one that hasn't been swapped
There are two ways for Silva to do this, and it leaves 2 balls occupying their original positions.
Case 3: Silva swaps two balls that have not been swapped
There are two ways for Silva to do this, and it leaves 1 ball occupying their original position.
Our answer is the average of all 5 possible swaps, so we get \[\frac{5+2\cdot2+2\cdot1}{5}=\frac{11}5=\boxed{(\textbf{D}) \: 2.2}.\]
~kingofpineapplz

## Solution 2 (Linearity of Expectation)
The "expected value" in the question tips us off to this technique. Consider any ball. The probability it returns to the same position is the probability of being swapped twice plus the probability of never being swapped: \[\frac{2}{5} \cdot \frac{1}{5} + \left(\frac{3}{5}\right)^2 = \frac{11}{25}.\] Multiply by 5 for 5 balls to get $\boxed{(\textbf{D}) \: 2.2}.$
~Dhillonr25

## Solution 3 (Calculating-Mean)
In probability and statistics, you learn that the mean and expected value are fundamentally equivalent values.
The total number of ways to pick the balls is ${5 \choose 2}^2 = 100$ .
Now there are three cases either Chris and Silva choose the same two balls (C1), they choose two different balls (C2), or they choose one overlapping ball and three nonoverlapping (C3).
C1: There are ${5 \choose 2} = 10$ possible placements of choosing $2$ balls. This gives a remaining $5$ unarranged balls. This gives a weighted mean pair of $10(5) = 50$ .
C2: There are $5$ ways of choosing $4$ balls adjacently, and due to Chris and Silva each choosing $2$ gives $10$ ways due to symmetry. This gives a weighted mean pair of $10(1) = 10$ .
C3: There are now $100 - 10 - 10 = 80$ ways for C3 to occur. This gives $2$ balls that remain in their original positions for a weighted mean pair of $80(2) = 160$ .
Calculating the mean gives $\frac{50 + 10 + 160}{100} = \boxed{(\textbf{D}) \: 2.2}$ .
~PeterDoesPhysics

## Video Solution by OmegaLearn
https://youtu.be/EE-TtptBHeI?t=174
~ pi_is_3.14

## Video Solution by Interstigation
https://www.youtube.com/watch?v=0FtXvjn_4y0
~Interstigation

## Video Solution
https://youtu.be/LLYYvYXl2rw
~Education, the Study of Everything

## Video Solution by WhyMath
https://youtu.be/RiD1eoGq36s
~savannahsolver

## Video Solution by TheBeautyofMath
https://youtu.be/tPxRqApsqVo
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
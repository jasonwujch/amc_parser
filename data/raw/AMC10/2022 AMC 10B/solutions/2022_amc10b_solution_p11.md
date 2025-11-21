# 2022 AMC 10B Problem 11

## Problem

All the high schools in a large school district are involved in a fundraiser selling T-shirts. Which of the choices below is logically equivalent to the statement "No school bigger than Euclid HS sold more T-shirts than Euclid HS"?

$\textbf{(A) }$ All schools smaller than Euclid HS sold fewer T-shirts than Euclid HS.

$\textbf{(B) }$ No school that sold more T-shirts than Euclid HS is bigger than Euclid HS.

$\textbf{(C) }$ All schools bigger than Euclid HS sold fewer T-shirts than Euclid HS.

$\textbf{(D) }$ All schools that sold fewer T-shirts than Euclid HS are smaller than Euclid HS.

$\textbf{(E) }$ All schools smaller than Euclid HS sold more T-shirts than Euclid HS.

## Solution 1
Let $B$ denote a school that is bigger than Euclid HS, and $M$ denote a school that sold more T-shirts than Euclid HS.
It follows that $\neg B$ denotes a school that is not bigger than Euclid HS, and $\neg M$ denotes a school that did not sell more T-shirts than Euclid HS.
Converting everything to conditional statements (if-then form), the given statement becomes \[B\implies\neg M.\] Its contrapositive is $M\implies\neg B,$ which is $\boxed{\textbf{(B)}}.$
Note that "not bigger than" does not mean "smaller than", and "not selling more" does not mean "selling fewer". There is an equality case. Therefore, none of the other answer choices is equivalent to $B\implies\neg M.$
~MRENTHUSIASM

## Solution 2 (Elimination)
Suppose we have five schools: Euclid HS with $50$ students and $10$ T-shirts sold.
- School $A$ with $51$ students and $10$ T-shirts sold.
- School $B$ with $49$ students and $10$ T-shirts sold.
- School $C$ with $49$ students and $9$ T-shirts sold.
- School $D$ with $51$ students and $9$ T-shirts sold (This configuration is legal.)
Then, school $B$ rules out $\textbf{(A)}$ , school $A$ rules out $\textbf{(C)}$ , school $D$ rules out $\textbf{(D)}$ , and school $C$ rules out $\textbf{(E)}$ , leaving us with $\boxed{\textbf{(B)}}$ as the correct answer.
~mathboy100 (Solution)
~michaelwang13675 (Formatting)

## Solution 3 (Logic/Common Sense to Eliminate)
First, you can eliminate A because the question doesn't say anything about smaller schools. Next, you can notice that B seems right at first glance, so you can keep it in contention. Next, you can eliminate C because it says they sold fewer, while the problem only states they didn't sell more than Euclid HS, so it can be fewer or equal to the number of shirts. Next, you can eliminate D because for the same reason as A. Finally, you can eliminate E for the same reason as A. Since everything except B is eliminated, $\boxed{\textbf{(B)}}$ is the correct answer.
~SIGMAMATHEMATICIAN

## Video Solution by Interstigation
https://youtu.be/ofoV7t0YrzA

## Video Solution by TheBeautyofMath
https://youtu.be/Mi2AxPhnRno
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
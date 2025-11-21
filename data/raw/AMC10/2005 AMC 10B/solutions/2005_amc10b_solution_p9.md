# 2005 AMC 10B Problem 9

## Problem

One fair die has faces $1, 1, 2, 2, 3, 3$ and another has faces $4, 4, 5, 5, 6, 6.$ The dice are rolled and the numbers on the top faces are added. What is the probability that the sum will be odd?

$\textbf{(A) } \frac{1}{3} \qquad \textbf{(B) } \frac{4}{9} \qquad \textbf{(C) } \frac{1}{2} \qquad \textbf{(D) } \frac{5}{9} \qquad \textbf{(E) } \frac{2}{3}$

## Solution
In order to obtain an odd sum, exactly one out of the two dice must have an odd number. We can easily find the total probability using casework.
Case 1 : The first die is odd and the second die is even.
The probability of this happening is $\dfrac{4}{6}\times\dfrac{4}{6}=\dfrac{16}{36}=\dfrac{4}{9}$
Case 2 : The first die is even and the second die is odd.
The probability of this happening is $\dfrac{2}{6}\times\dfrac{2}{6}=\dfrac{4}{36}=\dfrac{1}{9}$
Adding these two probabilities will give us our final answer. $\dfrac{4}{9}+\dfrac{1}{9}=\boxed{\textbf{(D) }\dfrac{5}{9}}$
If you run out of time, you can see it is obviously greater than $\frac{1}{2}$ so it narrows guesses.

## Solution 2 (Complementary Counting)
We see can see that there are $2$ ways to get an even number, and other ways get us an odd. Therefore, if we subtract the $P(\text{even})$ , we will get $P(\text{odd})$ . We can get an even either by getting $2$ evens or $2$ odds. Both cases give $\frac{2}{9}$ , so $P(\text{odd})$ is $1-2 \cdot \frac{2}{9}=\boxed{\textbf{(D) }\frac{5}{9}}$
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
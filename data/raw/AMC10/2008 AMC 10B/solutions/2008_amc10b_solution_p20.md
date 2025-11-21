# 2008 AMC 10B Problem 20

## Problem

The faces of a cubical die are marked with the numbers $1$ , $2$ , $2$ , $3$ , $3$ , and $4$ . The faces of another die are marked with the numbers $1$ , $3$ , $4$ , $5$ , $6$ , and $8$ . What is the probability that the sum of the top two numbers will be $5$ , $7$ , or $9$ ?

$\mathrm{(A)}\ 5/18\qquad\mathrm{(B)}\ 7/18\qquad\mathrm{(C)}\ 11/18\qquad\mathrm{(D)}\ 3/4\qquad\mathrm{(E)}\ 8/9$

## Solution 1
One approach is to write a table of all $36$ possible outcomes, do the sums, and count good outcomes.
We see that out of $36$ possible outcomes, $4$ give the sum of $5$ , $6$ the sum of $7$ , and $4$ the sum of $9$ , hence the resulting probability is $\frac{4+6+4}{36}=\frac{14}{36}=\boxed{\frac{7}{18}}$ .

## Solution 2
Each die is equally likely to roll odd or even, so the probability of an odd sum is $\frac{1}{2}$ . The possible odd sums are $3, 5, 7, 9, 11$ .
So we can find the probability of rolling $3$ or $11$ instead and just subtract that from $\frac{1}{2}$ , which seems easier.
Without writing out a table, we can see that there are 2 ways to make $3$ , and 2 ways to make $11$ , for a probability of $\frac{4}{36}$ .
$\frac{1}{2}-\frac{4}{36}=\frac{14}{36}=\boxed{\frac{7}{18}}$ .

## Solution 3
The outcome of the first dice can be $1$ , $2$ , $3$ , or $4$ . For each of these $4$ cases, we can find the possible outcomes for the second dice that makes the sum of the top two numbers $5$ , $7$ , or $9$ , and then calculate the respective probabilities.
Case 1 - the first dice is 1: the outcome of the second dice can be $4$ , $6$ , or $8$ . There is a $\frac{1}{6}$ probability of rolling a $1$ with the first dice and a $\frac{1}{2}$ probability of rolling a $4$ , $6$ , or $8$ with the second dice. $\frac{1}{6}*\frac{1}{2} = \frac{1}{12}.$
Case 2 - the first dice is 2: the outcome of the second dice can be $3$ or $5$ . There is a $\frac{1}{3}$ probability of rolling a $2$ with the first dice and a $\frac{1}{3}$ probability of rolling a $3$ or $5$ with the second dice. $\frac{1}{3}*\frac{1}{3} = \frac{1}{9}.$
Case 3 - the first dice is 3: the outcome of the second dice can be $4$ or $6$ . There is a $\frac{1}{3}$ probability of rolling a $3$ with the first dice and a $\frac{1}{3}$ probability of rolling a $4$ or $6$ with the second dice. $\frac{1}{3}*\frac{1}{3} = \frac{1}{9}.$
Case 4 - the first dice is 4: the outcome of the second dice can be $1$ , $3$ , or $5$ . There is a $\frac{1}{6}$ probability of rolling a $4$ with the first dice and a $\frac{1}{2}$ probability of rolling a $1$ , $3$ , or $5$ with the second dice. $\frac{1}{6}*\frac{1}{2} = \frac{1}{12}.$
$\frac{1}{12} + \frac{1}{9} + \frac{1}{9} + \frac{1}{12} = \frac{14}{36} = \frac{7}{18}$ , so the answer is $\boxed{\textbf{(B) } \frac{7}{18}}$ . ~azc1027
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
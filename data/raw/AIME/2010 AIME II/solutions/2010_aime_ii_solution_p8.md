# 2010 AIME II Problem 8

## Problem

Let $N$ be the number of ordered pairs of nonempty sets $\mathcal{A}$ and $\mathcal{B}$ that have the following properties:

- $\mathcal{A} \cup \mathcal{B} = \{1,2,3,4,5,6,7,8,9,10,11,12\}$ ,

- $\mathcal{A} \cap \mathcal{B} = \emptyset$ ,

- The number of elements of $\mathcal{A}$ is not an element of $\mathcal{A}$ ,

- The number of elements of $\mathcal{B}$ is not an element of $\mathcal{B}$ .

Find $N$ .

## Solution
Let us partition the set $\{1,2,\cdots,12\}$ into $n$ numbers in $A$ and $12-n$ numbers in $B$ ,
Since $n$ must be in $B$ and $12-n$ must be in $A$ ( $n\ne6$ , we cannot partition into two sets of 6 because $6$ needs to end up somewhere, $n\ne 0$ or $12$ either).
We have $\dbinom{10}{n-1}$ ways of picking the numbers to be in $A$ .
So the answer is $\left(\sum_{n=1}^{11} \dbinom{10}{n-1}\right) - \dbinom{10}{5}=2^{10}-252= \boxed{772}$ .
Note: We have $\dbinom{10}{n-1}$ ways of picking the numbers to be in $A$ because there are $n$ numbers in $A$ and since $12-n$ is already a term in the set we simply have to choose another $n-1$ numbers from the $10$ numbers that are available.

## Solution 2
Regardless of the size $n$ of $A$ (ignoring the case when $n = 6$ ), $n$ must not be in $A$ and $12 - n$ must be in $A$ .
There are $10$ remaining elements whose placements have yet to be determined. Note that the actual value of $n$ does not matter; there is always $1$ necessary element, $1$ forbidden element, and $10$ other elements that need to be distributed. There are $2$ places to put each of these elements, for $2^{10}$ possibilities.
However, there is the edge case of $n = 6; 6$ is forced not the be in either set, so we must subtract the $\dbinom{10}{5}$ cases where $A$ and $B$ have size $6$ .
Thus, our answer is $2^{10} - \dbinom{10}{5} = 1024 - 252 = \boxed{772}$

## Solution 3 (PIE and Complementary Counting)
The total number of possible subsets is $\sum_{i=1}^{11}\dbinom{12}{i}$ , which is $2^{12}-2$ . Note that picking a subset from the set leaves the rest of the set to be in the other subset. We exclude $i=0$ and $i=12$ since they leave a set empty. We proceed with complementary counting and casework:
We apply the Principle of Inclusion and Exclusion for casework on the complementary cases. We find the ways where $|A|$ is in $A$ , which violates the first condition. Then we find the ways where the elements $|B|$ and $12-|B|$ are in set $B$ , which violates only the second condition, and not the first. This ensures we do not overcount.
Case 1: $|A|$ is an element in $A$
There are $\sum_{i=1}^{11}\dbinom{11}{i-1}$ = $2^{11}-1$ ways in this case.
Case 2: $|B|$ and $12-|B|$ are in $B$
We introduce a subcase where $|B|$ is not 6, since the other element would also be 6. There are $B-2$ elements to choose from 10 elements. Therefore, $|B|$ can be from 2 to 11. There are $\sum_{i=2}^{11}\dbinom{10}{i-2}-\dbinom{10}{4} = 2^{10}-211$ ways. The other subcase is when $|B|$ is equal to 6. There are $\dbinom{11}{5}=462$ ways. Adding the subcases gives us $2^{10}+251$ .
Adding this with case one gives us $2^{11}+2^{10}+250$ . Subtracting this from $2^{12}-2$ gives $1024-252=\boxed{772}$ .
~ Magnetoninja

## Solution 4 (Not the best solution- Casework)
Case 1: Set A has 1 element. Set B has 11 elements. 11 must be in set A, so there is $1$ way.
Case 2: Set A has 2 elements. Set B has 10 elements. 10 must be in set A, and 2 must not be in set A, so there is $1\cdot\binom{10}{1}$ (for the remaining element).
Case 3: Set A has 3 elements. Set B has 9 elements. 9 must be in set A, and 3 must not be in set A, so there is $1\cdot\binom{10}{2}$ (for the remaining elements).
Case 4: Set A has 4 elements. Set B has 8 elements. 8 must be in set A, and 4 must not be in set A, so there is $1\cdot\binom{10}{3}$ (for the remaining element).
Case 5: Set A has 5 elements. Set B has 7 elements. 7 must be in set A, and 5 must not be in set A, so there is $1\cdot\binom{10}{4}$ (for the remaining element).
There is no Case 6 because $6$ can't go in set A and can't go in set B. Cases 7 to 11 are symmetric, so add up the 5 cases and multiply by $2$ to get $\boxed{772}$ .
-unhappyfarmer
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
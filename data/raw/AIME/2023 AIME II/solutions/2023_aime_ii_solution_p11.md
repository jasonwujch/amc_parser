# 2023 AIME II Problem 11

## Problem

Find the number of collections of $16$ distinct subsets of $\{1,2,3,4,5\}$ with the property that for any two subsets $X$ and $Y$ in the collection, $X \cap Y \not= \emptyset.$

## Solution
Denote by $\mathcal C$ a collection of 16 distinct subsets of $\left\{ 1, 2, 3, 4, 5 \right\}$ . Denote $N = \min \left\{ |S|: S \in \mathcal C \right\}$ .
Case 1: $N = 0$ .
This entails $\emptyset \in \mathcal C$ . Hence, for any other set $A \in \mathcal C$ , we have $\emptyset \cap A = \emptyset$ . This is infeasible.
Case 2: $N = 1$ .
Let $\{a_1\} \in \mathcal C$ . To get $\{a_1\} \cap A \neq \emptyset$ for all $A \in \mathcal C$ . We must have $a_1 \in \mathcal A$ .
The total number of subsets of $\left\{ 1, 2, 3, 4, 5 \right\}$ that contain $a_1$ is $2^4 = 16$ . Because $\mathcal C$ contains 16 subsets. We must have $\mathcal C = \left\{ \{a_1\} \cup A : \forall \ A \subseteq \left\{ 1, 2, 3, 4, 5 \right\} \backslash \left\{a_1 \right\} \right\}$ . Therefore, for any $X, Y \in \mathcal C$ , we must have $X \cap Y \supseteq \{a_1\}$ . So this is feasible.
Now, we count the number of $\mathcal C$ in this case. We only need to determine $a_1$ . Therefore, the number of solutions is 5.
Case 3: $N = 2$ .
Case 3.1: There is exactly one subset in $\mathcal C$ that contains 2 elements.
Denote this subset as $\left\{ a_1, a_2 \right\}$ . We then put all subsets of $\left\{ 1, 2, 3, 4, 5 \right\}$ that contain at least three elements into $\mathcal C$ , except $\left\{ a_3, a_4, a_5 \right\}$ . This satisfies $X \cap Y \neq \emptyset$ for any $X, Y \in \mathcal C$ .
Now, we count the number of $\mathcal C$ in this case. We only need to determine $\left\{ a_1, a_2 \right\}$ . Therefore, the number of solutions is $\binom{5}{2} = 10$ .
Case 3.2: There are exactly two subsets in $\mathcal C$ that contain 2 elements.
They must take the form $\left\{ a_1, a_2 \right\}$ and $\left\{ a_1, a_3 \right\}$ .
We then put all subsets of $\left\{ 1, 2, 3, 4, 5 \right\}$ that contain at least three elements into $\mathcal C$ , except $\left\{ a_3, a_4, a_5 \right\}$ and $\left\{ a_2, a_4, a_5 \right\}$ . This satisfies $X \cap Y \neq \emptyset$ for any $X, Y \in \mathcal C$ .
Now, we count the number of $\mathcal C$ in this case. We only need to determine $\left\{ a_1, a_2 \right\}$ and $\left\{ a_1, a_3 \right\}$ . Therefore, the number of solutions is $5 \cdot \binom{4}{2} = 30$ .
Case 3.3: There are exactly three subsets in $\mathcal C$ that contain 2 elements. They take the form $\left\{ a_1, a_2 \right\}$ , $\left\{ a_1, a_3 \right\}$ , $\left\{ a_1, a_4 \right\}$ .
We then put all subsets of $\left\{ 1, 2, 3, 4, 5 \right\}$ that contain at least three elements into $\mathcal C$ , except $\left\{ a_3, a_4, a_5 \right\}$ , $\left\{ a_2, a_4, a_5 \right\}$ , $\left\{ a_2, a_3, a_5 \right\}$ . This satisfies $X \cap Y \neq \emptyset$ for any $X, Y \in \mathcal C$ .
Now, we count the number of $\mathcal C$ in this case. We only need to determine $\left\{ a_1, a_2 \right\}$ , $\left\{ a_1, a_3 \right\}$ , $\left\{ a_1, a_4 \right\}$ . Therefore, the number of solutions is $5 \cdot \binom{4}{3} = 20$ .
Case 3.4: There are exactly three subsets in $\mathcal C$ that contain 2 elements. They take the form $\left\{ a_1, a_2 \right\}$ , $\left\{ a_1, a_3 \right\}$ , $\left\{ a_2, a_3 \right\}$ .
We then put all subsets of $\left\{ 1, 2, 3, 4, 5 \right\}$ that contain at least three elements into $\mathcal C$ , except $\left\{ a_3, a_4, a_5 \right\}$ , $\left\{ a_2, a_4, a_5 \right\}$ , $\left\{ a_1, a_4, a_5 \right\}$ . This satisfies $X \cap Y \neq \emptyset$ for any $X, Y \in \mathcal C$ .
Now, we count the number of $\mathcal C$ in this case. We only need to determine $\left\{ a_1, a_2 \right\}$ , $\left\{ a_1, a_3 \right\}$ , $\left\{ a_2, a_3 \right\}$ . Therefore, the number of solutions is $\binom{5}{3} = 10$ .
Case 3.5: There are exactly four subsets in $\mathcal C$ that contain 2 elements. They take the form $\left\{ a_1, a_2 \right\}$ , $\left\{ a_1, a_3 \right\}$ , $\left\{ a_1, a_4 \right\}$ , $\left\{ a_1, a_5 \right\}$ .
We then put all subsets of $\left\{ 1, 2, 3, 4, 5 \right\}$ that contain at least three elements into $\mathcal C$ , except $\left\{ a_3, a_4, a_5 \right\}$ , $\left\{ a_2, a_4, a_5 \right\}$ , $\left\{ a_1, a_4, a_5 \right\}$ , $\left\{ a_2, a_3, a_4 \right\}$ . This satisfies $X \cap Y \neq \emptyset$ for any $X, Y \in \mathcal C$ .
Now, we count the number of $\mathcal C$ in this case. We only need to determine $\left\{ a_1, a_2 \right\}$ , $\left\{ a_1, a_3 \right\}$ , $\left\{ a_1, a_4 \right\}$ , $\left\{ a_1, a_5 \right\}$ . Therefore, the number of solutions is 5.
Putting all subcases together, the number of solutions is this case is $10 + 30 + 20 + 10 + 5 = 75$ .
Case 4: $N \geq 3$ .
The number of subsets of $\left\{ 1, 2, 3, 4, 5 \right\}$ that contain at least three elements is $\sum_{i=3}^5 \binom{5}{i} = 16$ . Because $\mathcal C$ has 16 elements, we must select all such subsets into $\mathcal C$ . Therefore, the number of solutions in this case is 1.
Putting all cases together, the total number of $\mathcal C$ is $5 + 75 + 1 = \boxed{\textbf{(081) }}$ .

## Solution 2
Denote the $A$ as $\{ 1,2,3,4,5 \}$ and the collection of subsets as $S$ .
Case 1: There are only sets of size or higher in : Any two sets in $S$ must have at least one element common to both of them (since $3+3>5$ ). Since there are $16$ subsets of $A$ that have size $3$ or higher, there is only one possibility for this case.
Case 2: There are only sets of size or higher in : Firstly, there cannot be a no size $2$ set $S$ , or it will be overcounting the first case.
If there is only one such size $2$ set, there are $10$ ways to choose it. That size $2$ set, say $X$ , cannot be in $S$ with $Y = A/X$ (a three element set). Thus, there are only $15$ possible size $3$ subsets that can be in $S$ , giving us $10$ for this case.
If there are two sets with size $2$ in $S$ , we can choose the common elements of these two subsets in $5$ ways, giving us a total of $5\cdot 6 = 30$ .
If there are three sets with size $2$ , they can either share one common element, which can be done in $5 \cdot 4 = 20$ ways, or they can share pairwise common elements (sort of like a cycle), which can be done $\binom{5}{2} = 10$ ways. In total, we have $30$ possibilities.
If there are four sets with size $2$ , they all have to share one common element, which can be done in $5\cdot 1$ ways.
Thus, summing everything up, this will give us $75$ possible sets $S$
Case 3: There is a set with size in : Notice that be at most one size $1$ subset. There are $5$ ways to choose that single element set. Say it's $\{ 1\}$ . All other subsets in $S$ must have a $1$ in them, but there are only $2^4-1 = 15$ of them. Thus this case yields $5\cdot 1 = 5$ possibilities.
Thus, the total number of sets $S$ would be $1+75+5 = \boxed{\textbf{(081)}}$ .
~sml1809

## Solution 3
Firstly, there cannot be two subsets with cardinality 1, or they will not intersect.
If there is one subset $A$ with cardinality $1$ ; let the element in $A$ be $a$ , then there are $2^4=16$ subsets that do not include $a$ so they do not work. Every remaining subsets $S$ will have $a$ as an element so $S\cap{A}\geq1$ , since we just excluded all that do not. Since there are 15 subsets left, all are forced into the group of 16 subsets, so we just choose the number of $a$ to determine the set $A$ . $A\in\{1,2,3,4,5\}$ so there are 5 ways.
For the rest of the cases, we assume there are no sets $A$ with cardinality 1. Notice that the only way to "violate" the condition is to have subsets $X$ and $Y$ with cardinalities 2 and 3 in some order. Otherwise, by the Pigeonhole Principle, if two sets both have cardinalities more than 3, they are bound to have one element of intersection. Say a set $S$ has $|S|=2$ , then there is clearly only one set $s$ that will make $S\cap{s}=0$ . By our previous claim, all other subsets that have cardinality $c\geq{3}$ will work.
Now if we generalize a bit: If a subset has $N$ 2-element subsets which belong to set $M$ , then there are exactly $N$ subsets with cardinality 3 that don't work. Therefore, the number of "violating subsets" are all subsets with cardinality $c\leq{1}$ , all 2-element subsets that are not in $M$ , and all corresponding cardinality 3 subsets. Subtracting from the total 32 subsets, we get that $32-(1+5+(10-N)+N)=16$ subsets that do work. This includes all subsets in $M$ , so the remaining non-violating subsets are forced. This is equivalent now to choosing $N$ 2 element subsets.
Following casework on the number of 2-element subsets:
If $N=1$ : There are $\binom{5}{2}=10$ ways.
If $N=2$ : There are $5$ ways to choose the intersection between the 2 sets (remember they have to have at least one element of intersection) and $\binom{4}{2}=6$ ways to choose the distinct elements in the subsets, so there are $5*6=30$ ways.
If $N=3$ : It can be a cycle, where WLOG let the elements be $a,b,c$ so the sets are $\{a,b\}$ , $\{b,c\}$ , and $\{c,a\}$ . This is just $\binom{5}{3}=10$ . Alternatively, it can also be the case where all sets share one element. There are 5 ways to choose this element and $\binom{4}{2}=6$ ways to choose the remaining elements to assign to each set. There are $30$ ways.
If $N=4$ : By the Pigeonhole Principle, the only way all pairwise sets have at one common intersection is if all share one element in common. There are 5 ways to choose this element and the remaining numbers are forced. There are 5 ways.
$N\geq{5}$ does not provide any valid cases since to have all pairwise elements to intersect one element, they must be the same element by the Pigeonhole Principle, but there are not enough subsets.
If $N=0$ , then there is only one way since $\binom{5}{3}+\binom{5}{4}+\binom{5}{5}=16$ .
Adding all cases yields $5+10+30+30+5+1=\boxed{81}$ ways!
-Magnetoninja

## Video Solution
https://youtu.be/FH2QUGVNchw
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
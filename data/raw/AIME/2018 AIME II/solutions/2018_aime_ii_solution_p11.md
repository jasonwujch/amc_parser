# 2018 AIME II Problem 11

## Problem

Find the number of permutations of $1, 2, 3, 4, 5, 6$ such that for each $k$ with $1$ $\leq$ $k$ $\leq$ $5$ , at least one of the first $k$ terms of the permutation is greater than $k$ .

## Solution 1
If the first number is $6$ , then there are no restrictions. There are $5!$ , or $120$ ways to place the other $5$ numbers.
If the first number is $5$ , $6$ can go in four places, and there are $4!$ ways to place the other $4$ numbers. $4 \cdot 4! = 96$ ways.
If the first number is $4$ , ....
4 6 _ _ _ _ $\implies$ 24 ways
4 _ 6 _ _ _ $\implies$ 24 ways
4 _ _ 6 _ _ $\implies$ 24 ways
4 _ _ _ 6 _ $\implies$ 5 must go between $4$ and $6$ , so there are $3 \cdot 3! = 18$ ways.
$24 + 24 + 24 + 18 = 90$ ways if 4 is first.
If the first number is $3$ , ....
3 6 _ _ _ _ $\implies$ 24 ways
3 _ 6 _ _ _ $\implies$ 24 ways
3 1 _ 6 _ _ $\implies$ 4 ways
3 2 _ 6 _ _ $\implies$ 4 ways
3 4 _ 6 _ _ $\implies$ 6 ways
3 5 _ 6 _ _ $\implies$ 6 ways
3 5 _ _ 6 _ $\implies$ 6 ways
3 _ 5 _ 6 _ $\implies$ 6 ways
3 _ _ 5 6 _ $\implies$ 4 ways
$24 + 24 + 4 + 4 + 6 + 6 + 6 + 6 + 4 = 84$ ways
If the first number is $2$ , ....
2 6 _ _ _ _ $\implies$ 24 ways
2 _ 6 _ _ _ $\implies$ 18 ways
2 3 _ 6 _ _ $\implies$ 4 ways
2 4 _ 6 _ _ $\implies$ 6 ways
2 5 _ 6 _ _ $\implies$ 6 ways
2 5 _ _ 6 _ $\implies$ 6 ways
2 _ 5 _ 6 _ $\implies$ 4 ways
2 4 _ 5 6 _ $\implies$ 2 ways
2 3 4 5 6 1 $\implies$ 1 way
$24 + 18 + 4 + 6 + 6 + 6 + 4 + 2 + 1 = 71$ ways
Grand Total : $120 + 96 + 90 + 84 + 71 = \boxed{461}$

## Solution 2
If $6$ is the first number, then there are no restrictions. There are $5!$ , or $120$ ways to place the other $5$ numbers.
If $6$ is the second number, then the first number can be $2, 3, 4,$ or $5$ , and there are $4!$ ways to place the other $4$ numbers. $4 \cdot 4! = 96$ ways.
If $6$ is the third number, then we cannot have the following:
1 _ 6 _ _ _ $\implies$ 24 ways
2 1 6 _ _ _ $\implies$ 6 ways
$120 - 24 - 6 = 90$ ways
If $6$ is the fourth number, then we cannot have the following:
1 _ _ 6 _ _ $\implies$ 24 ways
2 1 _ 6 _ _ $\implies$ 6 ways
2 3 1 6 _ _ $\implies$ 2 ways
3 1 2 6 _ _ $\implies$ 2 ways
3 2 1 6 _ _ $\implies$ 2 ways
$120 - 24 - 6 - 2 - 2 - 2 = 84$ ways
If $6$ is the fifth number, then we cannot have the following:
_ _ _ _ 6 5 $\implies$ 24 ways
1 5 _ _ 6 _ $\implies$ 6 ways
1 _ 5 _ 6 _ $\implies$ 6 ways
2 1 5 _ 6 _ $\implies$ 2 ways
1 _ _ 5 6 _ $\implies$ 6 ways
2 1 _ 5 6 _ $\implies$ 2 ways
2 3 1 5 6 4, 3 1 2 5 6 4, 3 2 1 5 6 4 $\implies$ 3 ways
$120 - 24 - 6 - 6 - 2 - 6 - 2 - 3 = 71$ ways
Grand Total : $120 + 96 + 90 + 84 + 71 = \boxed{461}$

## Solution 3 (Recursion)
Note the condition in the problem is equivalent to the following condition: for each $k$ with $1 \le k \le 5$ , the first $k$ terms is not a permutation $(1, 2, \ldots, k)$ (since it would mean there must be some integer $x$ in the first $k$ terms such that $x \not \in \{1, 2, \ldots, k\} \implies x > k$ ). Then, let $a_n$ denote the number of permutations of $(1, 2, \ldots, n)$ satisfying the condition in the problem. We use complementary counting to find $a_n$ . Notice that in order to not satisfy the condition in the problem, there are $n-1$ cases: the first $1 \le k \le n-1$ (we don't include $k = n$ since the condition in the problem only holds up to $n-1$ ) terms are a permutation of $(1, 2, \ldots, k)$ , and for all $k+1 \le i \le n-1$ , the condition in the problem still holds. Then, for each of these cases, there are $k!$ ways to arrange the first $k$ terms, and then $a_{n-k}$ ways to arrange the $k + 1$ to $n$ terms (assume by contradiction that terms from $k+1$ to $i$ is a permutation of $(k+1, k+2, \ldots, i)$ . Then, since the first $k$ terms are already a permutation of $(1, 2, \ldots, k)$ , the first $i$ terms form a permutation of $(1, 2, \ldots, i)$ . This contradicts our assumption that for all $k+1 \le i \le n-1$ , the condition still holds. Thus, we can only include the $a_{n-k}$ permutations of these terms). Now, summing the cases up and subtracting from $n!$ , we have: $a_n = n! - \sum_{k=1}^{n-1} a_{n-k} k!$ . From this recursion, we derive that $a_1 = 1$ , $a_2 = 1$ , $a_3 = 3$ , $a_4 = 13$ , $a_5 = 71$ , and finally $a_6 = \boxed{461}$ .
~ CrazyVideoGamez
~ $BladeRunnerAUG$ (Frank FYC)

## Solution 4 (PIE)
Let $A_i$ be the set of permutations such that there is no number greater than $i$ in the first $i$ places. Note that $\bigcap^{k}_{i=0}{A_{b_i}}=\prod^k_{i=1}{(b_i-b_{i-1})!}$ for all $1\le b_0 < b_1\cdots < b_k \le 5$ and that the set of restricted permutations is $A_1 \cup A_2 \cup A_3 \cup A_4 \cup A_5$ .
We will compute the cardinality of this set with PIE. \begin{align*} &|A_1| + |A_2| + |A_3| + |A_4| + |A_5|\\ = &120 + 48 + 36 + 48 + 120 = 372\\ \\ &|A_1 \cap A_2| + |A_1 \cap A_3| + |A_1 \cap A_4| + |A_1 \cap A_5| + |A_2 \cap A_3|\\ + &|A_2 \cap A_4| + |A_2 \cap A_5| + |A_3 \cap A_4| + |A_3 \cap A_5| + |A_4 \cap A_5|\\=&24+12+12+24+12+8+12+12+12+24=152\\ \\ &|A_1 \cap A_2 \cap A_3| + |A_1 \cap A_2 \cap A_4| + |A_1 \cap A_2 \cap A_5| + |A_1 \cap A_3 \cap A_4| + |A_1 \cap A_3 \cap A_5|\\ +& |A_1 \cap A_4 \cap A_5| + |A_2 \cap A_3 \cap A_4| + |A_2 \cap A_3 \cap A_5| + |A_2 \cap A_4 \cap A_5| + |A_3 \cap A_4 \cap A_5|\\=&6 + 4 + 6 + 4 + 4 + 6 + 4 + 4 + 4 + 6 = 48\\ \\ &|A_1 \cap A_2 \cap A_3 \cap A_4| + |A_1 \cap A_2 \cap A_3 \cap A_5| + |A_1 \cap A_2 \cap A_4 \cap A_5| + |A_1 \cap A_3 \cap A_4 \cap A_5| + |A_2 \cap A_3 \cap A_4 \cap A_5|\\=&2 + 2 + 2 + 2 + 2 = 10\\ \\ &|A_1 \cap A_2 \cap A_3 \cap A_4 \cap A_5| = 1 \end{align*} To finish, $720 - 372 + 152 - 48 + 10 - 1 = \boxed{461}$

## Solution 5 (Recursion)
Define the function $f(p,q)$ as the amount of permutations with maximum digit $q$ and string length $p$ that satisfy the condition within bounds. For example, $f(4,5)$ would be the amount of ways to make a string with length $4$ with the highest digit being $5$ . We wish to obtain $f(6,6)=f(5,6)$ .
To generate recursion, consider how we would get to $f(p,q)$ from $f(p-1,a)$ for all $a$ such that $p\le{a}\le6$ . We could either jump from the old maximum $a$ to the new $q$ by concatenating the old string and the new digit $q$ , or one could retain the maximum, in which case $a=q$ . To retain the maximum, one would have to pick a new available digit not exceeding $q$ .
In the first case, there is only one way to pick the new digit, namely picking $q$ . For the second case, there are $q-p+1$ digits left to choose, because there are $q$ digits between 1 and $q$ total and there are $p-1$ digits already chosen below or equal to $q$ . Thus, $f(p,q)=[\sum^{q-1}_{n=p}f(p-1,n)] + (q-p+1)f(p-1,q)$ . Now that we have the recursive function, we can start evaluating the values of $f(p,q)$ until we get to $f(6,6)=f(5,6)$ .
\[f(2,3)=3, f(2,4)=5, f(2,5)=7, f(2,6)=9\] \[f(3,4)=13, f(3,5)=29, f(3,6)=51\] \[f(4,5)=71, f(4,6)=195\] \[f(5,6)=461\] Our requested answer is thus $\boxed{461}$ ~sigma

## Solution 6 (Complementary)
We can also solve this problem by counting the number of permutations that do NOT satisfy the given conditions; namely, these permutations must satisfy the condition that none of the first $k$ terms is greater than $k$ for $1\leq$ $k$ $\leq$ $5$ . We can further simplify this method by approaching it through casework on the first $k$ terms.
Case 1: None of the first one terms is greater than 1
The first term must obviously be one. Since there are five spaces left for numbers, there are a total of $5!=120$ permutations for this case.
Case 2: None of the first two terms is greater than 2
The first two terms must be 1 and 2 in some order. However, we already counted all cases starting with 1 in the previous case, so all of the permutations in this case must begin with $12\cdots$ . Since there are four spaces left, there are a total of $4!=24$ permutations for this case.
Case 3: None of the first three terms is greater than 3
The first three terms must be 1, 2, and 3 in some order. However, the cases beginning with 1__ and 21_ have already been accounted for. There are now $3!-3 = 3$ ways to order the first three numbers of the permutation, and $3!$ ways to order the last three numbers, for a total of $3\times6 = 18$ permutations.
Case 4: None of the first four terms is greater than 4
You can see where the pattern is going - the first four terms must be 1, 2, 3, and 4 in some order. All cases starting with 1 (there are $3!=6$ ), the cases starting with 21 (there are $2!=2$ ), and the 3 cases from case 3 (there are $3\times 1! = 3$ ) have been accounted for, so there are a total of $(4!-6-2-3)2!=26$ permutations for this case.
Case 5: None of the first five terms is greater than 5
This is perhaps the hardest case to work with, simply because there are so many subcases, so keeping track is crucial here. Obviously, the first five terms must be 1, 2, 3, 4, and 5, meaning there are 120 ways to order them. Now, we count the permutations we have already counted in previous cases. $4!$ start with 1, $3!$ start with 2, $3\times2!=6$ start with 3, and $13\times1!=13$ start with 4. Subtracting, we get a total of $120-24-6-6-13=71$ permutations.
Now, we subtract the total number of permutations from our cases from the total number of permutations, which is $6!$ : $720 - 120 - 24 - 18 - 26 - 71 = \boxed{461}$ .
~TGSN/curiousmind_888
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
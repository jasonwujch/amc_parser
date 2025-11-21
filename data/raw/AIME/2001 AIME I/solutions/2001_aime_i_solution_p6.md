# 2001 AIME I Problem 6

## Problem

A fair die is rolled four times. The probability that each of the final three rolls is at least as large as the roll preceding it may be expressed in the form $\frac{m}{n}$ where $m$ and $n$ are relatively prime positive integers . Find $m + n$ .

1 Problem

- 1 Problem

- 2 Solutions 2.1 Solution 1 2.2 Solution 2 2.3 Solution 3 2.4 Solution 4 2.5 Solution 5 2.6 Solution 6 2.7 Solution 7 2.8 Solution 8 Recursion Formula 2.9 Solution 9: Observation of each case 2.10 Solution 10: Distributions 2.11 Solution 11: Stars and Bars(Under 2 minutes) 2.12 Solution 12

- 3 See also

- 2.1 Solution 1

- 2.2 Solution 2

- 2.3 Solution 3

- 2.4 Solution 4

- 2.5 Solution 5

- 2.6 Solution 6

- 2.7 Solution 7

- 2.8 Solution 8 Recursion Formula

- 2.9 Solution 9: Observation of each case

- 2.10 Solution 10: Distributions

- 2.11 Solution 11: Stars and Bars(Under 2 minutes)

- 2.12 Solution 12

## Solutions

## Solution 1
Recast the problem entirely as a block-walking problem. Call the respective dice $a, b, c, d$ . In the diagram below, the lowest $y$ -coordinate at each of $a$ , $b$ , $c$ , and $d$ corresponds to the value of the roll.
The red path corresponds to the sequence of rolls $2, 3, 5, 5$ . This establishes a bijection between valid dice roll sequences and block walking paths.
The solution to this problem is therefore $\dfrac{\binom{9}{4}}{6^4} = {\dfrac{7}{72}}$ . So the answer is $\boxed{079}$ .

## Solution 2
Let $a, b, c,$ and $d$ be the results of rolling the four dice respectively. We have the range $1\leq a\leq b\leq c\leq d\leq 6$ , and there are $6^4=1296$ total outcomes from rolling the dice. To transfer the inequality into a strictly increasing inequality, we can transform it into $1\leq a<b+1<c+2<d+3\leq 9$ . Now, lets suppose $a'=a, b'=b+1, c'=c+2,$ and $d'=d+3$ . Then, $1\leq a'<b'<c'<d' \leq 9$ . Clearly, there are $\binom{9}{4}=126$ values that satisfy this equation, so our answer is $\dfrac{\binom{9}{4}}{6^4} = {\dfrac{7}{72}}\implies \boxed{079}$ .
~Mathkiddie

## Solution 3
If we take any combination of four numbers, there is only one way to order them in a non-decreasing order. It suffices now to find the number of combinations for four numbers from $\{1,2,3,4,5,6\}$ . We can visualize this as taking the four dice and splitting them into 6 slots (each slot representing one of {1,2,3,4,5,6}), or dividing them amongst 5 separators. Thus, there are ${9\choose4} = 126$ outcomes of four dice. The solution is therefore $\frac{126}{6^4} = \frac{7}{72}$ , and $7 + 72 = \boxed{079}$ .

## Solution 4
Call the dice rolls $a, b, c, d$ . The difference between the $a$ and $d$ distinguishes the number of possible rolls there are.
- If $a - d = 0$ , then the values of $b,\ c$ are set, and so there are $6$ values for $a,\ d$ .
- If $a - d = 1$ , then there are ${3\choose2} = 3$ ways to arrange for values of $b,\ c$ , but only $5$ values for $a,\ d$ .
- If $a - d = 2$ , then there are ${4\choose2} = 6$ ways to arrange $b, c$ , and there are only $6 - 2 = 4$ values for $a, d$ .
Continuing, we see that the sum is equal to $\sum_{i = 0}^{5}{i+2\choose2}(6 - i) = 6 + 15 + 24 + 30 + 30 + 21 = 126$ . The requested probability is $\frac{126}{6^4} = \frac{7}{72}$ and our answer is $\boxed{79}$ .

## Solution 5
The dice rolls can be in the form
ABCD AABC AABB AAAB AAAA
ABCD AABC AABB AAAB AAAA
where A, B, C, D are some possible value of the dice rolls. (These forms are not keeping track of whether or not the dice are in ascending order, just the possible outcomes.)
1. Now, for the first case, there are ${6\choose4} = 15$ ways for this. We do not have to consider the order because the combination counts only one of the permutations; we can say that it counts the correct (ascending order) permutation.
1. Second case: ${6\choose3} = 20$ ways to pick 3 numbers, ${3\choose1}$ ways to pick 1 of those 3 to duplicate. A total of 60 for this case.
1. Third case: ${6\choose2}=15$ ways to pick 2 numbers. We will duplicate both, so nothing else in this case matters.
1. Fourth case: ${6\choose2} = 15$ ways to pick 2 numbers. We pick one to duplicate with ${2\choose1} = 2$ , so there are a total of 30 in this case.
1. Fifth case: ${6\choose1} = 6$ ; all get duplicated so nothing else matters.
There are a total of $6^4$ possible dice rolls.
Thus,
$\frac{m}{n} = \frac{15 + 60 + 15 + 30 + 6}{6^4} = \frac{126}{6^4} = \frac{7}{72}$
Therefore, our answer is $\boxed{079}$

## Solution 6
Consider the number of possible dice roll combinations which work after $1$ roll, after $2$ rolls, and so on. There is 6 possible rolls for the first dice. If the number rolled is a 1, then there are 6 further values that are possible for the second dice; if the number rolled is a 2, then there are 5 further values that are possible for the second dice, and so on.
Suppose we generalize this as a function, say $f(l,r)$ return the number of possible combinations after $l$ rolls and $r$ being the beginning value of the first roll. It becomes clear that from above, $f(1,r) = 1$ ; every value of $l$ after that is equal to the sum of the number of combinations of $l - 1$ rolls that have a starting value of at least $r$ . If we slowly count through and add up all the possible combinations we get $\frac{7}{72}$ possibilities.

## Solution 7
In a manner similar to the above solution, instead consider breaking it down into two sets of two dice rolls. The first subset must have a maximum value which is $\le$ the minimum value of the second subset.
- If the first subset ends in a 1, there is $1$ such subset and there are $6 + 5 + 4 + 3 + 2 + 1 = \frac{6}{2}(6 + 1) = 21$ ways of making the second subset.
- If the first subset ends in a 2, there is $2$ such subsets and there are $5 + \ldots + 1 = \frac{5}{2}(5 + 1) = 15$ ways of making the second subset.
Thus, the number of combinations is $\sum_{i=1}^6 i \cdot \left(\frac{(7 - i)(8 - i)}{2}\right) = 21 + 30 + 30 + 24 + 15 + 6 = 126$ , and the probability again is $\frac7{72}$ , giving $m+n=\boxed{079}$ .

## Solution 8 Recursion Formula
If you're too tired to think about any of the above smart transformations of the problem, a recursion formula can be a robust way to the correct answer.
We just need to work out the valid cases for each roll. Denote by $N_{k}(n)$ the number of valid cases in the $k+1$ -th roll when the number $n$ is rolled, for $k=1,2,3$ and $1 \leq n \leq 6$ . Then we have the following recursion formula: \[N_{1}(n) = n\] \[N_{2}(n) = N_{1}(1) + N_{1}(2) + ... + N_{1}(n)=N_{2}(n-1)+N_{1}(n)\] \[N_{3}(n) = N_{2}(1) + N_{2}(2) + ... + N_{2}(n)=N_{3}(n-1)+N_{2}(n)\] The logic is that, if $n$ is rolled, then the number of valid cases is the subtotal of valid cases in the preceding roll for the outcome of 1 to $n$ . The recursion can be easily calculated by hand when $N_k(n)$ are put in columns side by side, given the fact that te numbers are smaller than 100. Finally, the total number of cases is \[N = \sum_{n=1}^{6} N_{3}(n)\] and \[P = \frac{N}{6^4}\]

## Solution 9: Observation of each case
Lets try casework and observe the cases. Notice that if the last roll is a $1$ , then the only dice rolls may be $1-1-1-1$ , which is only $1$ possibility. Observe that if the last roll is $2$ , then there are $4 = 1 + 3$ possibilities. When the last roll is a $3$ , there are $10 = 1 + 3 + 6$ possibilities. Notice when the last roll is $n$ , the number of cases is the sum of the first $n$ positive triangular numbers. This is easily provable when observing the numbers of possibilities after assigning a value to the last and second to last rolls. So there are a total of $1 + 1 + 3 + 1 + 3 + 6 + 1 + 3 + 6 + 10 + 1 + 3 + 6 + 10 + 15 + 1 + 3 + 6 + 10 + 15 + 21 = 126$ possibilities. So the probability is $\frac{126}{6^4} = \frac{7}{72}$ and $7 + 72 = \boxed{079}$ . ~skyscraper

## Solution 10: Distributions
This is equivalent to picking a four-element sequence of $\{1, 2, 3, 4, 5, 6\}$ with repetition. Notice that once the sequence is picked, there is one and only one way to order these so that they form a sequence of rolls satisfying our conditions.
Now count the number of such four-element sequences, let $a$ be the number of $1$ s in the sequence, $b$ be the number of $2$ s, $c$ $3$ s, $d$ $4$ s, $e$ $5$ s, and $f$ $6$ s. Now we see that we must have \[a + b + c + d + e + f = 4\] with $a, b, c, d, e, f$ being nonnegative integers since there are a total of $4$ numbers picked. The number of solutions to this is $\dbinom{9}{4},$ so our total number is equal to $\dfrac{\binom{9}{4}}{6^4} = \dfrac{7}{72},$ making our answer $\boxed{079}.$
~Ilikeapos

## Solution 11: Stars and Bars(Under 2 minutes)
Let the rolls be $a,b,c$ and $d\newline$ let $z=a-1, e=b-a, f=c-b, g=d-c, h=6-d\newline$ $z+e+f+g+h=5\newline$ This equation has $C(5+5-1, 5-1)=126$ integer solutions $\newline$ $126/1296=7/72\newline$ $7+72=\boxed{79}$ ~ryanbear

## Solution 12
Let's say the four dice values are all different. These can only be arranged in one way to satisfy our conditions, so there are $\binom{6}{4}=15$ ways. If there are three different values, there are $\binom{6}{3}$ to choose the numbers and $\binom{3}{1}$ to choose which number will have the repeat, so $20\cdot3=60$ ways. If there are two different values, there are $\binom{6}{2}$ ways to choose the numbers. If there are two of each, then there is one way. If there are three of one and one of another, then there are $\binom{2}{1}$ ways. Therefore $15\cdot(1+2)=45$ . Now if all the numbers are the same, there are $\binom{6}{1}=6$ ways. Altogether we have $15+60+45+6=126$ ways. $\frac{126}{6^4}=\frac{21}{216}=\frac{7}{72}$ . $7+72=\boxed{79}$ . ~MC413551
These problems are copyrighted © by the Mathematical Association of America.
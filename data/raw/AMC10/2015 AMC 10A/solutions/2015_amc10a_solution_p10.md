# 2015 AMC 10A Problem 10

## Problem

How many rearrangements of $abcd$ are there in which no two adjacent letters are also adjacent letters in the alphabet? For example, no such rearrangements could include either $ab$ or $ba$ .

$\textbf{(A)}\ 0\qquad\textbf{(B)}\ 1\qquad\textbf{(C)}\ 2\qquad\textbf{(D)}\ 3\qquad\textbf{(E)}\ 4$

## Solution 1
The first thing one would want to do is place a possible letter that works and then stem off of it. For example, if we start with an $a$ , we can only place a $c$ or $d$ next to it. Unfortunately, after that step, we can't do too much, since:
$acbd$ is not allowed because of the $cb$ , and $acdb$ is not allowed because of the $cd$ .
We get the same problem if we start with a $d$ , since a $b$ will have to end up in the middle, causing it to be adjacent to an $a$ or $c$ .
If we start with a $b$ , the next letter would have to be a $d$ , and since we can put an $a$ next to it and then a $c$ after that, this configuration works. The same approach applies if we start with a $c$ .
So the solution must be the two solutions that were allowed, one starting from a $b$ and the other with a $c$ , giving us:
\[1 + 1 = \boxed{\textbf{(C)}\ 2}.\]

## Solution 2 (Casework)
Case 1: the first letter is A
Subcase 1: the second letter is C
The next letter must either be B or D, both of which do not satisfy the conditions.
Subcase 2: the second letter is D
The third letter is forced to be B and the fourth is forced to be C, but this doesn't work because B and C are next to each other.
Case 2: the first letter is B
The next letter is forced to be D, the third letter forced to be A and the last forced to be C. This works.
Case 3: the first letter is C
The next letter is forced to be A, the third letter is D and the last letter is B. This works.
Case 4: the first letter is D
Subcase 1: the second letter is A
The third letter has to be C and the fourth has to be B but this doesn't work because B and C are next to each other.
Subcase 2: the second letter is B
The third letter cannot be A or C, so this doesn't work.
Summing the cases, there are two that work: $BDAC$ and $CADB$ $\Longrightarrow \boxed{\textbf{(C)}\ 2}$ .
~JH. L

## Solution 3
We note that $a$ must be adjacent to $c$ or $d$ , $b$ must be adjacent to $d$ , $c$ must be adjacent to $a$ , and $d$ must be adjacent to $a$ or $b$ . In other words, the way the letters can be connected is \[c-a-d-b.\] Therefore, the only two possible arrangements are $cadb$ and $bdac$ , which gives $\boxed{\textbf{(C)}\ 2}$ .

## Video Solution (CREATIVE THINKING)
https://youtu.be/hTcv8lbvs6o
~Education, the Study of Everything

## Video Solution
https://youtu.be/0W3VmFp55cM?t=1055
~ pi_is_3.14

## Video Solution
https://youtu.be/3MiGotKnC_U?t=1509
~ ThePuzzlr

## Video Solution
https://youtu.be/8sTQIX4YJ6s
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
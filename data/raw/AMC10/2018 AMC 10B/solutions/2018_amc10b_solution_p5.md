# 2018 AMC 10B Problem 5

## Problem

How many subsets of $\{2,3,4,5,6,7,8,9\}$ contain at least one prime number?

$\textbf{(A)} \text{ 128} \qquad \textbf{(B)} \text{ 192} \qquad \textbf{(C)} \text{ 224} \qquad \textbf{(D)} \text{ 240} \qquad \textbf{(E)} \text{ 256}$

## Solution 1 - Complementary Counting
We use complementary counting, or
$\text{total - what we don't want = what we want}$ .
There are a total of $2^8$ ways to create subsets (consider including or excluding each number) and there are a total of $2^4$ subsets only containing composite numbers (the composite numbers are $4, 6, 8, 9$ ). Therefore, there are $2^8-2^4=240$ total ways to have at least one prime in a subset.

## Solution 2 (Using Answer Choices)
Well, there are 4 composite numbers, and you can list them in a 1 number format, a 2 number, 3 number, and a 4 number format. Now, we can use combinations.
$\binom{4}{1} + \binom{4}{2} + \binom{4}{3} + \binom{4}{4} = 15$ . Using the answer choices, the only multiple of 15 is $\boxed{\textbf{(D) }240}$
By: K6511

## Solution 3
Subsets of $\{2,3,4,5,6,7,8,9\}$ include a single digit up to all eight numbers. Therefore, we must add the combinations of all possible subsets and subtract from each of the subsets formed by the composite numbers.
Hence:
$\binom{8}{1} - \binom{4}{1} + \binom{8}{2} - \binom{4}{2} + \binom{8}{3} - \binom{4}{3} + \binom{8}{4} - 1 + \binom{8}{5} + \binom{8}{6} + \binom{8}{7} + 1 = \boxed{\textbf{(D) }240}$
By: pradyrajasai

## Solution 4
Total subsets is $(2^8) = 256$ Using complementary counting and finding the sets with composite numbers: only 4,6,8 and 9 are composite. Each one can be either in the set or out: $2^4$ = 16 $256-16=240$ $\boxed{\textbf{(D) }240}$
-goldenn

## Solution 5
We multiply the number of possibilities of the set having prime numbers and the set having composites.
The possibilities of primes are $2^4-1=15$ (As there is one solution not containing any primes)
The possibilities of the set containing composites are $2^4=16$ (There can be a set with no composites)
Multiplying this we get $15 \cdot 16 = \boxed{\textbf{(D) }240}$ .
-middletonkids

## Video Solution (HOW TO THINK CRITICALLY!!!)
https://youtu.be/RkQPY-_Qieo
~Education, the Study of Everything

## Video Solution 1
https://youtu.be/6Bt4I23JL1s
~savannahsolver

## Video Solution 2
https://youtu.be/5UojVH4Cqqs?t=1609
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
# 2025 AIME II Problem 7

## Problem

Let $A$ be the set of positive integer divisors of $2025$ . Let $B$ be a randomly selected subset of $A$ . The probability that $B$ is a nonempty set with the property that the least common multiple of its elements is $2025$ is $\frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution 1
We split into different conditions:
Note that the numbers in the set need to have a least common multiple of $2025$ , so we need to ensure that the set has at least 1 number that is a multiple of $3^4$ and a number that is a multiple of $5^2$ .
Multiples of $3^4$ : $81, 405, 2025$
Multiples of $5^2$ : $25, 75, 225, 675, 2025$
If the set $B$ contains $2025$ , then all of the rest $14$ factors is no longer important. The valid cases are $2^{14}$ .
If the set $B$ doesn't contain $2025$ , but contains $405$ , we just need another multiple of $5^2$ . It could be 1 of them, 2 of them, 3 of them, or 4 of them, which has $2^4 - 1 = 15$ cases. Excluding $2025, 405, 25, 75, 225, 675,$ the rest 9 numbers could appear or not appear. Therefore, this case has a valid case of $15 \cdot 2^9$ .
If set $B$ doesn't contain $2025$ nor $405$ , it must contain $81$ . It also needs to contain at least 1 of the multiples from $5^2$ , where it would be $15 \cdot 2^8$ .
The total valid cases are $2^{14} + 15 \cdot (2^9 + 2^8)$ , and the total cases are $2^{15}$ .
The answer is $\cfrac{2^8 \cdot (64 + 30 + 15)}{2^8 \cdot 2^7}= \frac{109}{128}$ .
Desired answer: $109 + 128 = \boxed{237}$ .
~ Mitsuihisashi14
~ $\LaTeX$ by eevee9046
~ Additional edits by aoum
~ Additional edits by fermat_sLastAMC

## Solution 2
We take the complement and use PIE. Suppose the LCM of the elements of the set is NOT $2025$ . Since $2025=3^4 \cdot 5^2$ , it must be that no element $x$ in the subset satisfies $v_3(x)=4$ OR no element $x$ in the subset satisfies $v_5(x)=2$ (in this case, $v_p(n)$ gives the exponent of $p$ in the prime factorization of $n$ ). For the first case, there are $4 \cdot 3 = 12$ possible divisors that could be in our subset ( $v_3(x)=0,1,2,3,v_5(x)=0,1,2$ are possible), for a total count of $2^{12}$ subsets. In the second case, there are $5 \cdot 2 = 10$ possible divisors that could be in our subset, for a total count of $2^{10}$ subsets. However, if both conditions are violated, then there are $4 \cdot 2 = 8$ divisors that could be in our subset, for a total count of $2^8$ subsets. Hence, by PIE, the number of subsets whose LCM is NOT $2025$ is equal to $2^{12}+2^{10}-2^8$ . The answer is then \[1-\frac{2^{12}+2^{10}-2^8}{2^{5 \cdot 3}}=\frac{109}{128} \implies \boxed{237}.\]
~ cxsmi

## Solution 3
Write numbers in the form of $3^{a}5^{b}$ where $0\leq a\leq 4; 0\leq b\leq 2$
There are $(4+1)(2+1)=15$ possible divisors of $2025$ , so the cardinality of the subsets is $2^{15}$
If I select $3^4\cdot 5^2$ , then I guarantee the LCM is 2025, so the other 14 numbers yield $2^{14}$ cases.
If I select $3^4\cdot 5$ , then I must select at least one of $3^a5^2$ , but I can select any other $9$ numbers, so there are \[2^9 \left(\binom{4}{1}+\binom{4}{2}+\binom{4}{3}+\binom{4}{4} \right)=2^9\cdot 15\] ways.
If I select $3^4$ , since we can't select $3^4\cdot 5$ or $3^4 5^2$ anymore, there are $2^8 \left(\binom{4}{1}+\binom{4}{2}+\binom{4}{3}+\binom{4}{4} \right)=2^8\cdot 15$ ways.
The answer is then $\frac{2^8(15+30+64)}{2^{15}}=\frac{109}{128}\implies \boxed{237}$ .
~ Bluesoul
~ Edited by aoum
~ Additional edits by fermat_sLastAMC
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
# 2019 AIME II Problem 14

## Problem

Find the sum of all positive integers $n$ such that, given an unlimited supply of stamps of denominations $5,n,$ and $n+1$ cents, $91$ cents is the greatest postage that cannot be formed.

## Solution 1
We will do casework on $n \pmod{5}$ and see which values work.
Case 1: $n \equiv 1 \pmod{5}$
$n$ would have to be greater than $91$ because if it wasn't then we could just add denominations of $5$ until we got to $91.$ However, if $n$ is more than $91,$ then all the numbers from $91$ to $n$ which are not multiples of $5$ are also unrepresentable, which violates the problem's condition of $91$ being the largest unrepresentable number. So there are no values for this case.
Case 2: $n \equiv 2 \pmod{5}$
$n + 1 \equiv 3 \pmod{5}$ is the smallest formable number 3 mod 5, so $n + 1 - 5 = n - 4$ is the largest unformable number 3 mod 5. $2n + 2 \equiv 1 \pmod{5}$ is the smallest formable number 1 mod 5, so $2n + 2 - 5 = 2n - 3$ is the largest unformable number 1 mod 5. Finally, $2n \equiv 4 \pmod{5}$ is the smallest formable number 4 mod 5, so $2n - 5$ is the largest unformable number 4 mod 5.
Therefore, the largest unformable number overall is $2n - 3 \equiv 1 \pmod{5}.$ This satisfies the problem's condition! $2n - 3 = 91 \implies n = 47.$
Case 3: $n \equiv 3 \pmod{5}$
$n + 1 \equiv 4 \pmod{5},$ which is the smallest representable number 4 mod 5, so the largest unrepresentable number 4 mod 5 is $n + 1 - 5 = n -4.$
Similarly, $2n \equiv 1 \pmod{5}$ is the smallest formable number 1 mod 5 and $3n + 3 \equiv 2 \pmod{5}$ is the smallest formable number 2 mod 5, so the largest number 2 mod 5 that is unrepresentable is $3n + 3 - 5 = 3n - 2,$ but the largest number 1 mod 5 that is unrepresentable is $2n -5.$ $3n - 2 > 2n - 5,$ so there would be a larger unrepresentable number than $91$ if we were to set $2n - 5$ equal to it, which violates the problem's condition. And we can't set $3n - 2$ equal to $91$ because $91 \not\equiv 2 \pmod{5},$ so there are no valid values for this case.
Case 4: $n \equiv 4 \pmod{5}$
$n + 1$ would be a multiple of $5,$ so we would be left with denominations of $5$ and $n.$ Then it would just be a straightforward application of the Chicken Mcnugget Theorem: $5n - n - 5 = 91 \implies n = 24,$ which is indeed $4 \pmod{5}.$ So this value works.
Case 5: $n$ is a multiple of 5
In this case we’re left with denominations of $5$ and $n + 1,$ so by the Chicken Mcnugget Theorem we get $5(n + 1) - n - 6 = 91 \implies n = 23,$ which is not a multiple of $5.$ So there are no valid values here.
The two valid values we found were $47$ and $24,$ so the answer is $47 + 24 = \boxed{71}.$
~ grogg007

## Solution 2
Notice that if we let $n + 1$ be a multiple of $5,$ then by the Chicken McNugget Theorem we have $5n - (n + 5) = 91 \implies n = 24.$ We find this is the smallest possible value of $n$ .
For a value of $n$ to work, we should not be able to form the value $91,$ but we should be able to form the values from $92$ to $96$ . After $96,$ we can form any value by adding additional $5$ cent stamps ( $92 + 5x$ , $93 + 5x$ , $94 + 5x$ , $95 + 5x$ , and $96 + 6x$ , where $x$ is a positive integer, together make all positive integers after $96$ ). We also need to be able to form $96$ using only denominations of $n$ and $n + 1,$ because if we also used denominations of $5,$ then we could just remove a $5$ cent stamp to get back to $91.$
Now we can figure out the working $(n, n+1)$ pairs that can be used to obtain $96$ . We also need to make sure we can get the numbers $92 - 95$ but not $91$ with denominations of $5$ . We can use no more than a total of $\frac{96}{24}=4$ stamps. Let $an + b(n + 1) = 96,$ where $a$ is the number of $n$ stamps used and $b$ is the number of $n + 1$ stamps used. The possible $(a,b)$ pairs are: \[(a,b) \rightarrow (4,0), (3,1), (2,2), (1,3), (0,4), (3,0), (2,1), (1,2), (0,3), (2,0), (1,1), (0,2), (1,0), (0,1).\] Solving for $n$ in each $(a,b)$ pair we find that the potential solutions are: \[(n, n + 1) \rightarrow (23,24), (24, 25), (31, 32), (32, 33), (47, 48), (48, 49), (95, 96), (96, 97).\]
The first pair doesn't work because $n \geq 24,$ and the last two don't work either because they are too large to form the values $92$ through $95$ . Finally, $(31,32)$ and $(32, 33)$ don't work because they can also form $91$ with denominations of $5$ (for example, $32 \cdot 0 + 33\cdot 2 + 5 \cdot 5 = 91$ ). We are left with $(24, 25), (47, 48), (48,49).$ Now we need to make sure that $92 - 95$ can be formed. We know from the Chicken McNugget Theorem that $91$ is the largest unformable number with denominations $24, 25$ and $5,$ so this means that all numbers after $91$ should be formable, and we can bash to confirm that all numbers from $92-95$ can be formed with denominations of $47, 48,$ and $5.$ However, we find that $92$ cannot be formed with denominations of $48, 49,$ and $5,$ so $n = 48$ is eliminated. Then $n \in \{24, 47\}$ . The requested sum is $24 + 47 = \boxed{071}$ .
~Revisions by emerald_block , Mathkiddie
### Note on finding and testing potential pairs
In order to find potential $(n,n+1)$ pairs, we simply test all combinations of $n$ and $n+1$ that sum to less than $4n$ (so that $n\ge24$ ) to see if they produce an integer value of $n$ when their sum is set to $96$ . Note that, since $96$ is divisible by $1$ , $2$ , $3$ , and $4$ , we must either use only $n$ or only $n+1$ , as otherwise, the sum is guaranteed to not be divisible by one of the numbers $2$ , $3$ , and $4$ .
$\begin{array}{c|c|c} \text{Combination} & \text{Sum} & n\text{-value} \\ \hline n,n,n,n & 4n & 24 \\ n+1,n+1,n+1 & 3n+3 & 31 \\ n,n,n & 3n & 32 \\ n+1,n+1 & 2n+2 & 47 \\ n,n & 2n & 48 \\ n+1 & n+1 & 95 \\ n & n & 96 \\ \end{array}$
To test whether a pair works, we simply check that, using the number $5$ and the two numbers in the pair, it is impossible to form a sum of $91$ , and it is possible to form sums of $92$ , $93$ , and $94$ . ( $95$ can always be formed using only $5$ s, and the pair is already able to form $96$ because that was how it was found.) We simply need to reach the residues $2$ , $3$ , and $4$ $\pmod{5}$ using only $n$ and $n+1$ without going over the number we are trying to form, while being unable to do so with the residue $1$ . As stated in the above solution, the last two pairs are clearly too large to work.
$\begin{array}{c|c|c|c|c} \text{Pair} & \text{Not }91 & 92 & 93 & 94 \\ \hline 24,25 & \checkmark & \checkmark & \checkmark & \checkmark \\ 31,32 & \times & \checkmark & \checkmark & \checkmark \\ 32,33 & \times & \checkmark & \checkmark & \checkmark \\ 47,48 & \checkmark & \checkmark & \checkmark & \checkmark \\ 48,49 & \checkmark & \times & \checkmark & \checkmark \\ \end{array}$
(Note that if a pair is unable to fulfill a single requirement, there is no need to check the rest.)
~ emerald_block

## Solution 3
Notice that once we hit all residues $\bmod 5$ , we'd be able to get any number greater (since we can continually add $5$ to each residue). Furthermore, $n\not\equiv 0,1\pmod{5}$ since otherwise $91$ is obtainable (by repeatedly adding $5$ to either $n$ or $n+1$ ) Since the given numbers are $5$ , $n$ , and $n+1$ , we consider two cases: when $n\equiv 4\pmod{5}$ and when $n$ is not that.
When $n\equiv 4 \pmod{5}$ , we can only hit all residues $\bmod 5$ once we get to $4n$ (since $n$ and $n+1$ only contribute $1$ more residue $\bmod 5$ ). Looking at multiples of $4$ greater than $91$ with $n\equiv 4\pmod{5}$ , we get $n=24$ . It's easy to check that this works. Furthermore, any $n$ greater than this does not work since $91$ isn't the largest unobtainable value (can be verified using Chicken McNugget Theorem).
Now, if $n\equiv 2,3\pmod{5}$ , then we'd need to go up to $2(n+1)=2n+2$ until we can hit all residues $\bmod 5$ since $n$ and $n+1$ create $2$ distinct residues $\bmod{5}$ . Checking for such $n$ gives $n=47$ and $n=48$ . It's easy to check that $n=47$ works, but $n=48$ does not (since $92$ is unobtainable). Furthermore, any $n$ greater than this does not work since $91$ isn't the largest unobtainable value in those cases (can be verified using Chicken McNugget Theorem). (Also note that in the $3 \pmod{5}$ case, the residue $2 \pmod{5}$ has will not be produced until $3(n+1)$ while the $1\pmod5$ case has already been produced, so the highest possible value that cannot be produced would not be a number equivalent to $1 \pmod5$ )
Since we've checked all residues $\bmod 5$ , we can be sure that these are all the possible values of $n$ . Hence, the answer is $24+47=\boxed{071}$ . - ktong

## Solution 4
Obviously $n\le 90$ . We see that the problem's condition is equivalent to: 96 is the smallest number that can be formed which is 1 mod 5, and 92, 93, 94 can be formed (95 can always be formed). Now divide this up into cases. If $n\equiv 0\pmod{5}$ , then 91 can be formed by using $n+1$ and some 5's, so there are no solutions for this case. If $n\equiv 1\pmod{5}$ , then 91 can be formed by using $n$ and some 5's, so there are no solutions for this case either.
For $n\equiv 2\pmod{5}$ , $2n+2$ is the smallest value that can be formed which is 1 mod 5, so $2n+2=96$ and $n=47$ . We see that $92=45+47$ , $93=48+45$ , and $94=47+47$ , so $n=47$ does work. If $n\equiv 3\pmod{5}$ , then the smallest value that can be formed which is 1 mod 5 is $2n$ , so $2n=96$ and $n=48$ . We see that $94=49+45$ and $93=48+45$ , but 92 cannot be formed, so there are no solutions for this case. If $n\equiv 4\pmod{5}$ , then we can just ignore $n+1$ since it is a multiple of 5, meaning that the Chicken McNugget theorem is a both necessary and sufficient condition, and it states that $5n-n-5=91$ meaning $4n=96$ and $n=24$ . Hence, the only two $n$ that work are $n=24$ and $n=47$ , so our answer is $24+47=\boxed{071}$ . -Stormersyle

## Solution 5 (standard)
Consider a postage that gives $96$ . We cannot use a $5$ -stamp as otherwise simply removing it yields a postage that gives $91$ . Additionally, there cannot be at least $5$ of $n$ -stamps or $n + 1$ -stamps, as else we can convert $5$ of the same valued stamp into a positive number of $5$ -stamps, then remove one to get a postage of $91$ .
From here consider integers $0 \le a, b, \le 4$ where $an + b(n + 1) = 96 \implies n = \dfrac{96 - b}{a + b}$ . The only pairs $(a, b)$ that yield an integer value are $(a, b) = (0, 2), (0, 3), (0, 4), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1)$ which generate the values $n = 47, 31, 23, 96, 48, 32, 24, 19$ respectively. It is easy to find counterexamples of postages that evaluate to $91$ besides $n = 24, 47$ .
Now for $n = 24$ clearly $91$ is unobtainable since we need a $4 \pmod {5}$ amount of $24$ -stamps which exceeds a value of $96$ . A similar result holds for $n = 47$ as any evaluation $\le 2 \cdot 47$ can only be $0, 2, 3 \pmod{5}$ . In both cases it is easy to construct a postage for $92, 93, 94, 95, 96$ , to which repeatedly adding $5$ -stamps makes all postages worth $>91$ possible. The requesteed sum is $24 + 47 = \boxed{71}$ .
- blueprimes

## Solution 6
We can use the formula $g = \left( \max_{j \in \{1, 2, \ldots, a_1-1\}} R_j \right) - a_1$ , where $g$ is the Frobenius Number (in this case 91), $a_1$ is the smallest denomination (which is 5), $j \in \{1, 2, \ldots, a_1-1\}$ represents a remainder (residue class) when you divide an integer by $a_1,$ and $R_j$ is the smallest nonnegative integer such that $a \cdot n + b \cdot (n + 1) \equiv j \pmod{5}$ where $a$ and $b$ are also nonnegative integers. So we have $91 = \left( \max_{j \in \{1, 2, 3, 4\}} R_j \right) - 5 \implies 96 = \left( \max_{j \in \{1, 2, 3, 4\}} R_j \right).$ This means that the largest of the $R_j$ values must be equal to exactly $96.$ We will do casework on $n \pmod{5}.$
Case 1: $n \equiv 1 \pmod{5}.$
$n + 1 \equiv 2 \pmod{5}.$ Plug this in:
$R_1$ : $a \cdot 1 + b \cdot 2 \equiv 1 \pmod{5} \implies a = 1, b = 0.$ So $R_1 = 1 \cdot n + 0 \cdot (n + 1) = n.$
$R_2$ : $a \cdot 1 + b \cdot 2 \equiv 2 \pmod{5} \implies a = 0, b = 1.$ So $R_2 = 0 \cdot n + 1 \cdot (n + 1) = n + 1.$
$R_3$ : $a \cdot 1 + b \cdot 2 \equiv 3 \pmod{5} \implies a = 1, b = 1.$ So $R_3 = 1 \cdot n + 1 \cdot (n + 1) = 2n + 1.$
$R_4$ : $a \cdot 1 + b \cdot 2 \equiv 4 \pmod{5} \implies a = 0, b = 2.$ So $R_4 = 2n + 2.$ This is the largest of the four $R_j$ values. Setting this equal to $96$ we get $n = 47.$ But this doesn't work because $47$ is not congruent to $1 \pmod{5}.$
Case 2: $n \equiv 2 \pmod{5}.$
$n + 1 \equiv 3 \pmod{5}.$ Plug this in:
$R_1$ : $a \cdot 2 + b \cdot 3 \equiv 1 \pmod{5} \implies a = 0, b = 2.$ So $R_1 = 0 \cdot n + 2 \cdot (n + 1) = 2n + 2.$
$R_2$ : $a \cdot 2 + b \cdot 3 \equiv 2 \pmod{5} \implies a = 1, b = 0.$ So $R_2 = 1 \cdot n + 0 \cdot (n + 1) = n.$
$R_3$ : $a \cdot 2 + b \cdot 3 \equiv 3 \pmod{5} \implies a = 0, b = 1.$ So $R_3 = 0 \cdot n + 1 \cdot (n + 1) = n + 1.$
$R_4$ : $a \cdot 2 + b \cdot 3 \equiv 4 \pmod{5} \implies a = 2, b = 0.$ So $R_4 = 2 \cdot n + 0 \cdot (n + 1) = 2n.$
The largest of the four $R_j$ values is $R_1 = 2n + 2.$ Setting this equal to $96$ we get $2n + 2 = 96 \implies n = 47.$ Now this works! $47$ is indeed $2 \pmod{5}.$
Case 3: $n \equiv 3 \pmod{5}.$
$n + 1 \equiv 4 \pmod{5}.$ Plug this in:
$R_1$ : $a \cdot 3 + b \cdot 4 \equiv 1 \pmod{5} \implies a = 2, b = 0.$ So $R_1 = 2 \cdot n + 0 \cdot (n + 1) = 2n.$
$R_2$ : $a \cdot 3 + b \cdot 4 \equiv 2 \pmod{5} \implies a = 1, b = 1.$ So $R_2 = 1 \cdot n + 1 \cdot (n + 1) = 2n + 1.$
$R_3$ : $a \cdot 3 + b \cdot 4 \equiv 3 \pmod{5} \implies a = 1, b = 0.$ So $R_3 = 1 \cdot n + 0 \cdot (n + 1) = n.$
$R_4$ : $a \cdot 3 + b \cdot 4 \equiv 4 \pmod{5} \implies a = 0, b = 1.$ So $R_4 = 0 \cdot n + 1 \cdot (n + 1) = n + 1.$
The largest of the four $R_j$ values is $R_2 = 2n + 1.$ Setting this equal to $96$ we get $n = 47.5,$ which is not an integer. So this doesn't work.
Case 4: $n \equiv 4 \pmod{5}.$
We notice that $n + 1$ will be a multiple of $5,$ so we're left with the denominations of $5$ and $n$ . Since these are two relatively prime numbers, we can do a straightforward application of the Chicken Mcnugget Theorem to get $5n - 5 - n = 91 \implies n = 24.$ This works because $24 \equiv 4 \pmod{5}.$
Case 5: $n \equiv 0 \pmod{5}.$
Same thing as case $4,$ only this time we are left with denominations of $5$ and $n + 1.$ Applying the Chicken Mcnugget Theorem gives $4n - 1 = 91 \implies n = 23,$ but this doesn't work because $23$ clearly isn't a multiple of $5$ .
The two valid values we found were $47$ and $24,$ so the sum is $\boxed{71}.$

## Video solution by grogg007:
https://www.youtube.com/watch?v=zv9_YrVebFI

## Video solution: https://www.youtube.com/watch?v=fTZP2e-_rjA
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
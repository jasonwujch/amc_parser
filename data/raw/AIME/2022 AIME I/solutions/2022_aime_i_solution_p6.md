# 2022 AIME I Problem 6

## Problem

Find the number of ordered pairs of integers $(a, b)$ such that the sequence \[3, 4, 5, a, b, 30, 40, 50\] is strictly increasing and no set of four (not necessarily consecutive) terms forms an arithmetic progression.

## Solution 1
Since $3,4,5,a$ and $3,4,5,b$ cannot be an arithmetic progression, $a$ or $b$ can never be $6$ . Since $b, 30, 40, 50$ and $a, 30, 40, 50$ cannot be an arithmetic progression, $a$ and $b$ can never be $20$ . Since $a < b$ , there are ${24 - 2 \choose 2} = 231$ ways to choose $a$ and $b$ with these two restrictions in mind.
However, there are still specific invalid cases counted in these $231$ pairs $(a,b)$ . Since \[3,5,a,b\] cannot form an arithmetic progression, $\underline{(a,b) \neq (7,9)}$ . \[a,b,30,50\] cannot be an arithmetic progression, so $(a,b) \neq (-10,10)$ ; however, since this pair was not counted in our $231$ , we do not need to subtract it off. \[3,a,b,30\] cannot form an arithmetic progression, so $\underline{(a,b) \neq (12,21)}$ . \[4, a, b, 40\] cannot form an arithmetic progression, so $\underline{(a,b) \neq (16,28)}$ . \[5, a,b, 50\] cannot form an arithmetic progression, $(a,b) \neq 20, 35$ ; however, since this pair was not counted in our $231$ (since we disallowed $a$ or $b$ to be $20$ ), we do not to subtract it off.
Also, the sequences $(3,a,b,40)$ , $(3,a,b,50)$ , $(4,a,b,30)$ , $(4,a,b,50)$ , $(5,a,b,30)$ and $(5,a,b,40)$ will never be arithmetic, since that would require $a$ and $b$ to be non-integers.
So, we need to subtract off $3$ progressions from the $231$ we counted, to get our final answer of $\boxed{228}$ .
~ ihatemath123

## Solution 2 (Rigorous)
We will follow the solution from earlier in a rigorous manner to show that there are no other cases missing.
We recognize that an illegal sequence (defined as one that we subtract from our 231) can never have the numbers {3, 4} and {4,5} because we have not included a 6 in our count. Similarly, sequences with {30,40} and {40,50} will not give us any subtractions because those sequences must all include a 20. Let's stick with the lower ones for a minute: if we take them two at a time, then {3,5} will give us the subtraction of 1 sequence {3,5,7,9}. We have exhausted all pairs of numbers we can take, and if we take the triplet of single digit numbers, the only possible sequence must have a 6, which we already don't count. Therefore, we subtract $\textbf{1}$ from the count of illegal sequences with any of the single-digit numbers and none of the numbers 30,40,50. (Note if we take only 1 at a time, there will have to be 3 of $a, b$ , which is impossible.)
If we have the sequence including {30,50}, we end up having negative values, so these do not give us any subtractions, and the triplet {30,40,50} gives us a 20. Hence by the same reasoning as earlier, we have 0 subtractions from the sequences with these numbers and none of the single digit numbers {3,4,5}.
Finally, we count the sequences that are something like (one of 3,4,5,), $a, b$ , (one of 30, 40, 50). If this is to be the case, then let $a$ be the starting value in the sequence. The sequence will be $a, a+d, a+2d, a+3d$ ; We see that if we subtract the largest term by the smallest term we have $3d$ , so the subtraction of one of (30,40,50) and one of (3,4,5) must be divisible by 3. Therefore the only sequences possible are $3,a,b,30; 4,a,b,40; 5,a,b,50$ . Of these, only the last is invalid because it gives $b = 35$ , larger than our bounds $6<a<b<30$ . Therefore, we subtract $\textbf{2}$ from this case.
Our final answer is $231 - 1 - 2 = \boxed{228}$
~KingRavi

## Solution 3
Denote $S = \left\{ (a, b) : 6 \leq a < b \leq 29 \right\}$ .
Denote by $A$ a subset of $S$ , such that there exists an arithmetic sequence that has 4 terms and includes $a$ but not $b$ .
Denote by $B$ a subset of $S$ , such that there exists an arithmetic sequence that has 4 terms and includes $b$ but not $a$ .
Hence, $C$ is a subset of $S$ , such that there exists an arithmetic sequence that has 4 terms and includes both $a$ and $b$ .
Hence, this problem asks us to compute \[ | S | - \left( | A | + | B | + | C | \right) . \]
First, we compute $| S |$ .
We have $| S | = \binom{29 - 6 + 1}{2} = \binom{24}{2} = 276$ .
Second, we compute $| A |$ .
$\textbf{Case 1}$ : $a = 6$ .
We have $b = 8 , \cdots , 19, 21, 22, \cdots, 29$ . Thus, the number of solutions is 22.
$\textbf{Case 2}$ : $a = 20$ .
We have $b = 21, 22, \cdots , 29$ . Thus, the number of solutions is 9.
Thus, $| A | = 22 + 9 = 31$ .
Third, we compute $| B |$ .
In $B$ , we have $b = 6, 20$ . However, because $6 \leq a < b$ , we have $b \geq 7$ . Thus, $b = 20$ .
This implies $a = 7, 8, 9, 11, 12, \cdots , 19$ . Note that $(a, b)=(10, 20)$ belongs in $C$ .
Thus, $| B | = 12$ .
Fourth, we compute $| C |$ .
$\textbf{Case 1}$ : In the arithmetic sequence, the two numbers beyond $a$ and $b$ are on the same side of $a$ and $b$ .
Hence, $(a, b) = (6 , 7), (7, 9) , (10, 20)$ . Therefore, the number solutions in this case is 3.
$\textbf{Case 2}$ : In the arithmetic sequence, the two numbers beyond $a$ and $b$ are on the opposite sides of $a$ and $b$ .
$\textbf{Case 2.1}$ : The arithmetic sequence is $3, a, b, 30$ .
Hence, $(a, b) = (12, 21)$ .
$\textbf{Case 2.2}$ : The arithmetic sequence is $4, a, b, 40$ .
Hence, $(a, b) = (16, 28)$ .
$\textbf{Case 2.3}$ : The arithmetic sequence is $5, a, b, 50$ .
Hence, $(a, b) = (20, 35)$ . However, the sequence $... 20, 35, 30, 40, 50$ is not strictly increasing.
Putting two cases together, $| C | = 65.$
Therefore, \[| S | - \left( | A | + | B | + | C | \right) = 276 - \left( 31 + 12 + 5 \right) = \boxed{228}.\]
~Steven Chen (www.professorchenedu.com)

## Solution 4
divide cases into $7\leq a<20; 21\leq a\leq28$ .(Notice that $a$ can't be equal to $6,20$ , that's why I divide them into two parts. There are three cases that arithmetic sequence forms: $3,12,21,30;4,16,28,40;3,5,7,9$ .(NOTICE that $5,20,35,50$ IS NOT A VALID SEQUENCE!) So when $7\leq a<20$ , there are $10+11+12+...+22-3-13=192$ possible ways( 3 means the arithmetic sequence and 13 means there are 13 "a" s and b cannot be 20)
When $21\leq a \leq 28$ , there are $1+2+\cdots+8=36$ ways.
In all, there are $192+36=\boxed{228}$ possible sequences.
~bluesoul
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
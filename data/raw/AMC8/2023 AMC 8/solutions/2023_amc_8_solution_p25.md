# 2023 AMC 8 Problem 25

## Problem

Fifteen integers $a_1, a_2, a_3, \dots, a_{15}$ are arranged in order on a number line. The integers are equally spaced and have the property that \[1 \le a_1 \le 10, \thickspace 13 \le a_2 \le 20, \thickspace \text{ and } \thickspace 241 \le a_{15}\le 250.\] What is the sum of digits of $a_{14}?$

$\textbf{(A)}\ 8 \qquad \textbf{(B)}\ 9 \qquad \textbf{(C)}\ 10 \qquad \textbf{(D)}\ 11 \qquad \textbf{(E)}\ 12$

## Solution 1
We can find the possible values of the common difference by finding the numbers which satisfy the conditions. To do this, we find the minimum of the last two: $241-20=221$ , and the maximum– $250-13=237$ . There is a difference of $13$ between them, so only $17$ and $18$ work, as $17\cdot13=221$ , so $17$ satisfies $221\leq 13x\leq237$ . The number $18$ is similarly found. $19$ , however, is too much.
Now, we check with the first and last equations using the same method. We know $241-10\leq 14x\leq250-1$ . Therefore, $231\leq 14x\leq249$ . We test both values we just got, and we can realize that $18$ is too large to satisfy this inequality. On the other hand, we can now find that the difference will be $17$ , which satisfies this inequality.
The last step is to find the first term. We know that the first term can only be from $1$ to $3$ since any larger value would render the second inequality invalid. Testing these three, we find that only $a_1=3$ will satisfy all the inequalities. Therefore, $a_{14}=13\cdot17+3=224$ . The sum of the digits is therefore $\boxed{\textbf{(A)}\ 8}$ .
~apex304, SohumUttamchandani, wuwang2002, TaeKim, Cxrupptedpat

## Solution 2 (most intuitive solution)
Let the common difference between consecutive $a_i$ be $d$ . Since $a_{15} - a_1 = 14d$ , we find from the first and last inequalities that $231 \le 14d \le 249$ . As $d$ must be an integer, this means $d = 17$ . Substituting this into all of the given inequalities so we may extract information about $a_1$ gives \[1 \le a_1 \le 10, \thickspace 13 \le a_1 + 17 \le 20, \thickspace 241 \le a_1 + 238 \le 250.\] The second inequality tells us that $1 \le a_1 \le 3$ , while the last inequality tells us $3 \le a_1 \le 12$ , so we must have $a_1 = 3$ . Finally, to solve for $a_{14}$ , we simply have $a_{14} = a_1 + 13d = 3 + 13(17) = 3 + 221 = 224$ , so our answer is $2 + 2 + 4 = \boxed{\textbf{(A)}\ 8}$ .
~eibc (edited by CHECKMATE2021 & PRAYER914)

## Solution 3(simplified)
We are given 15 equally spaced integers, with \( a_1 \) between 1 and 10, \( a_2 \) between 13 and 20, and \( a_{15} \) between 241 and 250. The integers form an arithmetic sequence, so we use the formula \( a_n = a_1 + (n-1) \cdot d \), where \( d \) is the common difference. From the given information, we calculate the range for \( d \) and find that \( d = 17 \) works. Substituting \( a_1 = 3 \) and \( d = 17 \) into the formula, we find \( a_{14} = 3 + 13 \cdot 17 = 224 \). The problem asks for the sum of the digits of \( a_{14} \), so we sum the digits of 224, which are 2, 2, and 4, giving \( 2 + 2 + 4 = 8 \), and the final answer is \( \boxed{8} \).

## Video Solution by Math-X
https://youtu.be/Ku_c1YHnLt0?si=HaykiiKOmQl2ugA_&t=6010
~Math-X

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/zntZrtsnyxc?si=nM5eWOwNU6HRdleZ&t=3376 ~hsnacademy

## Video Solution
https://youtu.be/wYjg-sE-QWs
~please like and subscribe

## Video Solution(🚀Just 3 min!🚀)
https://youtu.be/X95x9iseAB8
~Education, the Study of Everything

## Video Solution 1 by OmegaLearn (Divisibility makes diophantine equation trivial)
https://youtu.be/5LLl26VI-7Y

## Video Solution by SpreadTheMathLove Using Arithmetic Sequence
https://www.youtube.com/watch?v=EC3gx7rQlfI

## Animated Video Solution
https://youtu.be/itDH7AgxYFo
~Star League ( https://starleague.us )

## Video Solution by Magic Square
https://youtu.be/-N46BeEKaCQ?t=1047

## Video Solution by Interstigation
https://youtu.be/DBqko2xATxs&t=3550

## Video Solution by WhyMath
https://youtu.be/iP1ous_RW3M
~savannahsolver

## Video Solution by harungurcan
https://www.youtube.com/watch?v=Ki4tPSGAapU&t=1864s
~harungurcan

## Video Solution by Dr. David
https://youtu.be/j8b6cHHHb0c
### See Also
# 2020 AIME I Problem 3

## Problem

A positive integer $N$ has base-eleven representation $\underline{a}\kern 0.1em\underline{b}\kern 0.1em\underline{c}$ and base-eight representation $\underline1\kern 0.1em\underline{b}\kern 0.1em\underline{c}\kern 0.1em\underline{a},$ where $a,b,$ and $c$ represent (not necessarily distinct) digits. Find the least such $N$ expressed in base ten.

## Solution 1
From the given information, $121a+11b+c=512+64b+8c+a \implies 120a=512+53b+7c$ . Since $a$ , $b$ , and $c$ have to be positive, $a \geq 5$ . Since we need to minimize the value of $n$ , we want to minimize $a$ , so we have $a = 5$ . Then we know $88=53b+7c$ , and we can see the only solution is $b=1$ , $c=5$ . Finally, $515_{11} = 621_{10}$ , so our answer is $\boxed{621}$ .
~ JHawk0224

## Solution 2 (Official MAA)
The conditions of the problem imply that $121a + 11b + c = 512 + 64b + 8 c + a$ , so $120 a = 512+ 53b+7c$ . The maximum digit in base eight is $7,$ and because $120a \ge 512$ , it must be that $a$ is $5, 6,$ or $7.$ When $a = 5$ , it follows that $600=512 + 53b+7c$ , which implies that $88 = 53b+7c$ . Then $b$ must be $0$ or $1.$ If $b = 0$ , then $c$ is not an integer, and if $b = 1$ , then $7c = 35$ , so $c = 5$ . Thus $N = 515_{11}$ , and $N=5\cdot 121 + 1\cdot 11 + 5 = 621$ . The number $637_{11} =1376_{8} = 766$ also satisfies the conditions of the problem, but $621$ is the least such number.

## Video Solution
https://youtu.be/hZSBUXCX5hI
Minor edits by TryhardMathlete

## Video Solution by OmegaLearn
https://youtu.be/mgEZOXgIZXs?t=1204
~ pi_is_3.14

## Video Solution
https://youtu.be/SuVsBIz8pZ8
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
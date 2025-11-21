# 2002 AIME I Problem 3

## Problem

Jane is 25 years old. Dick is older than Jane. In $n$ years, where $n$ is a positive integer, Dick's age and Jane's age will both be two-digit numbers and will have the property that Jane's age is obtained by interchanging the digits of Dick's age. Let $d$ be Dick's present age. How many ordered pairs of positive integers $(d,n)$ are possible?

## Solution
Let Jane's age $n$ years from now be $10a+b$ , and let Dick's age be $10b+a$ . If $10b+a>10a+b$ , then $b>a$ . The possible pairs of $a,b$ are:
That makes 36. But $10a+b>25$ , so we subtract all the extraneous pairs: $(1,2), (1,3), (2,3), (1,4), (2,4), (1,5), (2,5), (1,6), (1,7), (1,8),$ and $(1,9)$ . $36-11=\boxed{025}$

## Solution 2
Start by assuming that $n < 5$ (essentially, Jane is in the 20s when their ages are 'reverses' of each other). Then we get the pairs \[(61,1),(70,2),(79,3),(88,4).\] Repeating this for the 30s gives \[(34,9),(43,10),(52,11),(61,12),(70,13),(79,14).\] From here, it's pretty clear that every decade we go up we get $(d,n+11)$ as a pair. Since both ages must always be two-digit numbers, we can show that each decade after the 30s, we get 1 fewer option. Therefore, our answer is $4+6+5+\dots+2+1=4+21=\boxed{025}.$
~Dhillonr25
### Remark
The 25 ordered pairs $(d, n)$ are: (34, 9) (34, 20) (34, 31) (34, 42) (34, 53) (34, 64) (43, 10) (43, 21) (43, 32) (43, 43) (43, 54) (52, 11) (52, 22) (52, 33) (52, 44) (61, 1) (61, 12) (61, 23) (61, 34) (70, 2) (70, 13) (70, 24) (79, 3) (79, 14) (88, 4) ~Puck_0
These problems are copyrighted © by the Mathematical Association of America.
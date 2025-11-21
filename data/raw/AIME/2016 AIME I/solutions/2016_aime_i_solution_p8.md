# 2016 AIME I Problem 8

## Problem

For a permutation $p = (a_1,a_2,\ldots,a_9)$ of the digits $1,2,\ldots,9$ , let $s(p)$ denote the sum of the three $3$ -digit numbers $a_1a_2a_3$ , $a_4a_5a_6$ , and $a_7a_8a_9$ . Let $m$ be the minimum value of $s(p)$ subject to the condition that the units digit of $s(p)$ is $0$ . Let $n$ denote the number of permutations $p$ with $s(p) = m$ . Find $|m - n|$ .

## Solution
To minimize $s(p)$ , the numbers $1$ , $2$ , and $3$ (which sum to $6$ ) must be in the hundreds places. For the units digit of $s(p)$ to be $0$ , the numbers in the ones places must have a sum of either $10$ or $20$ . However, since the tens digit contributes more to the final sum $s(p)$ than the ones digit, and we are looking for the minimum value of $s(p)$ , we take the sum's units digit to be $20$ . We know that the sum of the numbers in the tens digits is $\sum\limits_{i=1}^9 (i) -6-20=45-6-20=19$ . Therefore, $m=100\times6+10\times19+20=810$ .
To find $n$ , realize that there are $3!=6$ ways of ordering the numbers in each of the places. Additionally, there are three possibilities for the numbers in the ones place: $(4,7,9)$ , $(5,7,8)$ , and $(5,6,9)$ . Therefore there are $6^3\times3=648$ ways in total. $|m-n|=|810-648|=\fbox{162}$ .

## Video Solutions
https://www.youtube.com/watch?v=WBtMUzgqfwI
https://www.youtube.com/watch?v=QBHakfd2gnQ
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
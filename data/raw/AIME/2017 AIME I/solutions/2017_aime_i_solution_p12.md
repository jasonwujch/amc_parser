# 2017 AIME I Problem 12

## Problem

Call a set $S$ product-free if there do not exist $a, b, c \in S$ (not necessarily distinct) such that $a b = c$ . For example, the empty set and the set $\{16, 20\}$ are product-free, whereas the sets $\{4, 16\}$ and $\{2, 8, 16\}$ are not product-free. Find the number of product-free subsets of the set $\{1, 2, 3, 4,..., 7, 8, 9, 10\}$ .

## Solution 1 (Casework)
We shall solve this problem by doing casework on the lowest element of the subset. Note that the number $1$ cannot be in the subset because $1*1=1$ . Let $S$ be a product-free set. If the lowest element of $S$ is $2$ , we consider the set $\{3, 6, 9\}$ . We see that 5 of these subsets can be a subset of $S$ ( $\{3\}$ , $\{6\}$ , $\{9\}$ , $\{6, 9\}$ , and the empty set). Now consider the set $\{5, 10\}$ . We see that 3 of these subsets can be a subset of $S$ ( $\{5\}$ , $\{10\}$ , and the empty set). Note that $4$ cannot be an element of $S$ , because $2$ is. Now consider the set $\{7, 8\}$ . All four of these subsets can be a subset of $S$ . So if the smallest element of $S$ is $2$ , there are $5*3*4=60$ possible such sets.
If the smallest element of $S$ is $3$ , the only restriction we have is that $9$ is not in $S$ . This leaves us $2^6=64$ such sets.
If the smallest element of $S$ is not $2$ or $3$ , then $S$ can be any subset of $\{4, 5, 6, 7, 8, 9, 10\}$ , including the empty set. This gives us $2^7=128$ such subsets.
So our answer is $60+64+128=\boxed{252}$ .

## Solution 2 (PIE)
We will consider the $2^9 = 512$ subsets that do not contain 1. A subset is product-free if and only if it does not contain one of the groups $\{2, 4\}, \{3, 9\}, \{2, 3, 6\},$ or $\{2, 5, 10\}$ . There are $2^7$ subsets that contain 2 and 4 since each of the seven elements other than 2 and 4 can either be in the subset or not. Similarly, there are $2^7$ subsets that contain 3 and 9, $2^6$ subsets that contain 2, 3, and 6, and $2^6$ subsets that contain 2, 5, and 10. The number of sets that contain one of the groups is: \[2^7 + 2^7 + 2^6 + 2^6 = 384\] For sets that contain two of the groups, we have: \[2^5 + 2^5 + 2^5 + 2^5 + 2^4 + 2^4 = 160\] For sets that contain three of the groups, we have: \[2^4 + 2^3 + 2^3 + 2^3 = 40\] For sets that contain all of the groups, we have: \[2^2 = 4\] By the principle of inclusion and exclusion, the number of product-free subsets is \[512 - 384 + 160 - 40 + 4 = \boxed{252}\] .

## Solution 3
Let $X$ be a product-free subset, and note that 1 is not in $x$ . We consider four cases:
1.) both 2 and 3 are not in $X$ . Then there are $2^7=128$ possible subsets for this case.
2.) 2 is in $X$ , but 3 is not. Then 4 is not in $X$ , so there are $2^6=64$ subsets; however, there is a $\frac{1}{4}$ chance that 5 and 10 are both in $X$ , so there are $64\cdot \frac{3}{4}=48$ subsets for this case.
3.) 2 is not in $X$ , but 3 is. Then, 9 is not in $X$ , so there are $2^6=64$ subsets for this case.
4.) 2 and 3 are both in $X$ . Then, 4, 6, and 9 are not in $X$ , so there are $2^4=16$ total subsets; however, there is a $\frac{1}{4}$ chance that 5 and 10 are both in $X$ , so there are $16\cdot \frac{3}{4}=12$ subsets for this case.
Hence our answer is $128+48+64+12=\boxed{252}$ . -Stormersyle

## Solution 4
First, ignore 7 as it does not affect any of the other numbers; we can multiply by 2 later (its either in or out).
Next, we do casework based on whether 2, 3, or 5 are in the set ( $2^3 = 8$ quick cases). For each of the cases, the numbers will be of two types ---
1. They cannot be in the set because they form a product
2. Whether we add the number to the set or not, it does not affect the rest of the numbers. These numbers simply add a factor of 2 to the case.
For example, in the case where all three are present, we can see that $4, 6, 9, 10$ are of type 1. However, $8$ is of type 2. Therefore this case contributes 2.
Summing over the 8 cases we get $2 + 4 + 8 + 16 + 16 + 16 + 32 + 32 = 126.$ Multiplying by $2$ because of the $7$ gives $252.$

## Solution 5
Note that if any element $s\geq6$ makes an invalid set, it must be $c$ of $ab=c$ . Otherwise, $ab\geq12>10$ so no $ab=c$ will suffice. Therefore, whether or not an element $s\geq6$ depends only on the previous elements $1\leq\omega\leq5$ .
First, if a set is product-free, it must never contain an element $\omega=1$ or $1\cdot1=1$ .
We do casework on the subset of $S\in{1,2,3,4,5}=s_1$ to determine $S\in{6,7,8,9,10}=s_2$ (There are only 12 to cover so we just list them out):
When it is empty, there are clearly no restrictions for $s_2$ so there are $2^5=32$ cases.
$s_1={2}, s_1={4}, s_1={5}$ has no restrictions $s_2$ so we get $2^5\cdot3=96$ total cases.
$s_1=3$ only cannot contain 9 so there are $2^4=16$ cases.
$s_1={2, 5}; s_1={3, 4}; s_1={3, 5}$ each have one restriction in $s_2$ so there are $2^4\cdot3=48$ ways.
$s_1={2, 3}$ has 2 restrictions (6 and 9) so there are $2^3=8$ ways.
$s_1={4, 5}$ has no restrictions so there are $2^5=32$ ways.
$s_1={2, 3, 5}$ has 3 restrictions (6, 9, and 10) so there are $2^2=4$ ways.
$s_1={3, 4, 5}$ has 1 restriction so there are $2^4=16$ cases.
Summing the numbers, we get $32+96+16+48+8+32+4+16=\boxed{252}$ .

## Video Solution by OmegaLearn
https://youtu.be/jRZQUv4hY_k?t=504
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
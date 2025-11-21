# 2019 AIME I Problem 2

## Problem

Jenn randomly chooses a number $J$ from $1, 2, 3,\ldots, 19, 20$ . Bela then randomly chooses a number $B$ from $1, 2, 3,\ldots, 19, 20$ distinct from $J$ . The value of $B - J$ is at least $2$ with a probability that can be expressed in the form $\frac{m}{n}$ where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution 1
$B-J \ne 0$ because $B \ne J$ , so the probability that $B-J < 0$ is $\frac{1}{2}$ by symmetry.
The probability that $B-J = 1$ is $\frac{19}{20 \times 19} = \frac{1}{20}$ because there are 19 pairs: $(B,J) = (2,1), \ldots, (20,19)$ .
The probability that $B-J \ge 2$ is $1-\frac{1}{2}-\frac{1}{20} = \frac{9}{20} \implies \boxed{029}$

## Solution 2
By symmetry, the desired probability is equal to the probability that $J - B$ is at most $-2$ , which is $\frac{1-P}{2}$ where $P$ is the probability that $B$ and $J$ differ by $1$ (no zero, because the two numbers are distinct). There are $20 \cdot 19 = 380$ total possible combinations of $B$ and $J$ , and $1 + 18 \cdot 2 + 1 = 38$ ones that form $P$ , so $P = \frac{38}{380} = \frac{1}{10}$ . Therefore the answer is $\frac{9}{20} \rightarrow \boxed{029}$ .

## Solution 3
This problem is essentially asking how many ways there are to choose $2$ distinct elements from a $20$ element set such that no $2$ elements are adjacent. Using the well-known formula $\dbinom{n-k+1}{k}$ , there are $\dbinom{20-2+1}{2} = \dbinom{19}{2} = 171$ ways. Dividing $171$ by $380$ , our desired probability is $\frac{171}{380} = \frac{9}{20}$ . Thus, our answer is $9+20=\boxed{029}$ . -Fidgetboss_4000

## Solution 4
Create a grid using graph paper, with $20$ columns for the values of $J$ from $1$ to $20$ and $20$ rows for the values of $B$ from $1$ to $20$ . Since $B$ cannot equal $J$ , we cross out the diagonal line from the first column of the first row to the twentieth column of the last row. Now, since $B - J$ must be at least $2$ , we can mark the line where $B - J = 2$ . Now we sum the number of squares that are on this line and below it. We get $171$ . Then we find the number of total squares, which is $400 - 20 = 380$ . Finally, we take the ratio $\frac{171}{380}$ , which simplifies to $\frac{9}{20}$ . Our answer is $9+20=\boxed{029}$ .

## Solution 5
We can see that if $B$ chooses $20$ , $J$ can choose from $1$ through $18$ such that $B-J\geq 2$ . If $B$ chooses $19$ , $J$ has choices $1$ ~ $17$ . By continuing this pattern, $B$ will choose $3$ and $J$ will have $1$ option. Summing up the total, we get $18+17+\cdots+1$ as the total number of solutions. The total amount of choices is $20\times19$ (B and J must choose different numbers), so the probability is $\frac{18\cdot19\div2}{20\cdot19}=\frac{9}{20}$ . Therefore, the answer is $9+20=\boxed{029}$
-eric2020

## Solution 6
Similar to solution 4, we can go through the possible values of $J$ to find all the values of $B$ that makes $B-J\geq 2$ . If $J$ chooses $1$ , then $B$ can choose anything from $3$ to $20$ . If $J$ chooses $2$ , then $B$ can choose anything from $4$ to $20$ . By continuing this pattern, we can see that there is $18+17+\cdots+1$ possible solutions. The amount of solutions is, therefore, $\frac{18\cdot19}{2}=171$ . Now, because $B$ and $J$ must be different, we have $20\times19=380$ possible choices, so the probability is $\frac{171}{380}=\frac{9}{20}$ . Therefore, the final answer is $9+20=\boxed{029}$
-josephwidjaja

## Solution 7 (Official MAA)
There are $\tbinom{20}{2}=190$ equally likely pairs $\{J,B\}$ . In $19$ of these pairs $(\{1,2\},\{2,3\},\{3,4\}\dots,\{19,20\})$ , the numbers differ by less than 2, so the probability that the numbers differ by at least 2 is $1-\tfrac{19}{190}=\tfrac9{10}$ . Then $B-J\ge 2$ holds in exactly half of these cases, so it has probability $\tfrac12\cdot\tfrac9{10}=\tfrac{9}{20}$ . The requested sum is $9+20=\boxed{029}$ .

## Video Solution #1(Easy Counting)
https://youtu.be/JQdad7APQG8?t=245

## Video Solution
https://www.youtube.com/watch?v=lh570eu8E0E

## Video Solution 2
https://youtu.be/TSKcjht8Rfk?t=488
~IceMatrix

## Video Solution 3
https://youtu.be/9X18wCiYw9M
~Shreyas S
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
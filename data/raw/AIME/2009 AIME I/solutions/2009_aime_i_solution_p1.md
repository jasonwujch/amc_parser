# 2009 AIME I Problem 1

## Problem

Call a $3$ -digit number geometric if it has $3$ distinct digits which, when read from left to right, form a geometric sequence. Find the difference between the largest and smallest geometric numbers.

## Solution 1
Assume that the largest geometric number starts with a $9$ . We know that the common ratio must be a rational of the form $k/3$ for some integer $k$ , because a whole number should be attained for the 3rd term as well. When $k = 1$ , the number is $931$ . When $k = 2$ , the number is $964$ . When $k = 3$ , we get $999$ , but the integers must be distinct. By the same logic, the smallest geometric number is $124$ . The largest geometric number is $964$ and the smallest is $124$ . Thus the difference is $964 - 124 = \boxed{840}$ .

## Solution 2
Consider the three-digit number $abc$ . If its digits form a geometric progression, we must have that ${a \over b} = {b \over c}$ , that is, $b^2 = ac$ .
The minimum and maximum geometric numbers occur when $a$ is minimized and maximized, respectively. The minimum occurs when $a = 1$ ; letting $b = 2$ and $c = 4$ achieves this, so the smallest possible geometric number is 124.
For the maximum, we have that $b^2 = 9c$ ; $b$ is maximized when $9c$ is the greatest possible perfect square; this happens when $c = 4$ , yielding $b = 6$ . Thus, the largest possible geometric number is 964.
Our answer is thus $964 - 124 = \boxed{840}$ .

## Solution 3
The smallest geometric number is $124$ because $123$ and any number containing a zero does not work. $964$ is the largest geometric number because the middle digit cannot be 8 or 7. Subtracting the numbers gives $\boxed{840}.$

## Video Solution by OmegaLearn
https://youtu.be/1-iWPCWPsLw?t=195
~ pi_is_3.14

## Video Solution
https://youtu.be/NL79UexadzE
~IceMatrix

## Video Solution 2
https://www.youtube.com/watch?v=P00iOJdQiL4
~Shreyas S
These problems are copyrighted © by the Mathematical Association of America.
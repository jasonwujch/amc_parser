# 2005 AIME II Problem 5

## Problem

Determine the number of ordered pairs $(a,b)$ of integers such that $\log_a b + 6\log_b a=5, 2 \leq a \leq 2005,$ and $2 \leq b \leq 2005.$

## Solution 1
The equation can be rewritten as $\frac{\log b}{\log a} + 6 \frac{\log a}{\log b} = \frac{(\log b)^2+6(\log a)^2}{\log a \log b}=5$ Multiplying through by $\log a \log b$ and factoring yields $(\log b - 3\log a)(\log b - 2\log a)=0$ . Therefore, $\log b=3\log a$ or $\log b=2\log a$ , so either $b=a^3$ or $b=a^2$ .
- For the case $b=a^2$ , note that $44^2=1936$ and $45^2=2025$ . Thus, all values of $a$ from $2$ to $44$ will work.
- For the case $b=a^3$ , note that $12^3=1728$ while $13^3=2197$ . Therefore, for this case, all values of $a$ from $2$ to $12$ work.
There are $44-2+1=43$ possibilities for the square case and $12-2+1=11$ possibilities for the cube case. Thus, the answer is $43+11= \boxed{054}$ .
Note that Inclusion-Exclusion does not need to be used, as the problem is asking for ordered pairs $(a,b)$ , and not for the number of possible values of $b$ . Were the problem to ask for the number of possible values of $b$ , the values of $b^6$ under $2005$ would have to be subtracted, which would just be $2$ values: $2^6$ and $3^6$ . However, the ordered pairs where b is to the sixth power are distinct, so they are not redundant. (For example, the pairs (4, 64) and (8, 64).)

## Solution 2
Let $k=\log_a b$ . Then our equation becomes $k+\frac{6}{k}=5$ . Multiplying through by $k$ and solving the quadratic gives us $k=2$ or $k=3$ . Hence $a^2=b$ or $a^3=b$ .
For the first case $a^2=b$ , $a$ can range from 2 to 44, a total of 43 values. For the second case $a^3=b$ , $a$ can range from 2 to 12, a total of 11 values.
Thus the total number of possible values is $43+11=\boxed{54}$ .

## Solution 3(similar to solution 2)
Using the change of base formula on the second equation to change to base $a$ , we get $\log_a(b) + \frac{6 \log_a(a)}{\log_a(b)}$ . If we substitute $x$ for $\log_a(b)$ , we get $x + \frac{6}{x}$ . Multiplying by $x$ on both sides and solving, we get $x=3,2$ . Substituting back in, we get $\log_a(b) = 3,2$ . That means $a^3 = b$ or $a^2 = b$ . Since $b \leq 2005$ , we can see that for the cubed case, the maximum $a$ can be without exceeding 2005 is 12(because $13^3 = 2197$ ) and for the squared case it can be a maximum of 44. Since $a \neq 1$ , the number of values is $(44-1)+(12-1) = \boxed{54}$ .
~idk12345678
These problems are copyrighted © by the Mathematical Association of America.
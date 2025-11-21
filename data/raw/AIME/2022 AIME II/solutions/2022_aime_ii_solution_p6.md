# 2022 AIME II Problem 6

## Problem

Let $x_1\leq x_2\leq \cdots\leq x_{100}$ be real numbers such that $|x_1| + |x_2| + \cdots + |x_{100}| = 1$ and $x_1 + x_2 + \cdots + x_{100} = 0$ . Among all such $100$ -tuples of numbers, the greatest value that $x_{76} - x_{16}$ can achieve is $\tfrac mn$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution 1
To find the greatest value of $x_{76} - x_{16}$ , $x_{76}$ must be as large as possible, and $x_{16}$ must be as small as possible. If $x_{76}$ is as large as possible, $x_{76} = x_{77} = x_{78} = \dots = x_{100} > 0$ . If $x_{16}$ is as small as possible, $x_{16} = x_{15} = x_{14} = \dots = x_{1} < 0$ . The other numbers between $x_{16}$ and $x_{76}$ equal to $0$ . Let $a = x_{76}$ , $b = x_{16}$ . Substituting $a$ and $b$ into $|x_1| + |x_2| + \cdots + |x_{100}| = 1$ and $x_1 + x_2 + \cdots + x_{100} = 0$ we get: \[25a - 16b = 1\] \[25a + 16b = 0\] $a = \frac{1}{50}$ , $b = -\frac{1}{32}$
$x_{76} - x_{16} = a - b = \frac{1}{50} + \frac{1}{32} = \frac{41}{800}$ . $m+n = \boxed{\textbf{841}}$
~ isabelchen

## Solution 2
Define $s_N$ to be the sum of all the negatives, and $s_P$ to be the sum of all the positives.
Since the sum of the absolute values of all the numbers is $1$ , $|s_N|+|s_P|=1$ .
Since the sum of all the numbers is $0$ , $s_N=-s_P\implies |s_N|=|s_P|$ .
Therefore, $|s_N|=|s_P|=\frac 12$ , so $s_N=-\frac 12$ and $s_P=\frac 12$ since $s_N$ is negative and $s_P$ is positive.
To maximize $x_{76}-x_{16}$ , we need to make $x_{16}$ as small of a negative as possible, and $x_{76}$ as large of a positive as possible.
Note that $x_{76}+x_{77}+\cdots+x_{100}=\frac 12$ is greater than or equal to $25x_{76}$ because the numbers are in increasing order.
Similarly, $x_{1}+x_{2}+\cdots+x_{16}=-\frac 12$ is less than or equal to $16x_{16}$ .
So we now know that $\frac 1{50}$ is the best we can do for $x_{76}$ , and $-\frac 1{32}$ is the least we can do for $x_{16}$ .
Finally, the maximum value of $x_{76}-x_{16}=\frac 1{50}+\frac 1{32}=\frac{41}{800}$ , so the answer is $\boxed{841}$ .
(Indeed, we can easily show that $x_1=x_2=\cdots=x_{16}=-\frac 1{32}$ , $x_{17}=x_{18}=\cdots=x_{75}=0$ , and $x_{76}=x_{77}=\cdots=x_{100}=\frac 1{50}$ works.)
~inventivedant

## Solution 3
Because the absolute value sum of all the numbers is $1$ , and the normal sum of all the numbers is $0$ , the positive numbers must add to $\frac12$ and negative ones must add to $-\dfrac12$ . To maximize $x_{76} - x_{16}$ , we must make $x_{76}$ as big as possible and $x_{16}$ as small as possible. We can do this by making $x_1 + x_2 + x_3 \dots x_{16} = -\dfrac{1}{2}$ , where $x_1 = x_2 = x_3 = \dots = x_{16}$ (because that makes $x_{16}$ the smallest possible value), and $x_{76} + x_{77} + x_{78} + \dots + x_{100} = \dfrac{1}{2}$ , where similarly $x_{76} = x_{77} = \dots = x_{100}$ (because it makes $x_{76}$ its biggest possible value.) That means $16(x_{16}) = -\dfrac{1}{2}$ , and $25(x_{76}) = \dfrac{1}{2}$ . $x_{16} = -\dfrac{1}{32}$ and $x_{76} = \dfrac{1}{50}$ , and subtracting them $\dfrac{1}{50} - \left( -\dfrac{1}{32}\right) = \dfrac{41}{800}$ . $41 + 800 = 841$ .
~heheman

## Video Solution by The Power of Logic
https://youtu.be/edpZKDxMsAc

## Video Solution by Challenge 25
https://www.youtube.com/watch?v=OQ8QcJB2hEA

## Video Solution by Steakmath
https://youtu.be/enxMhNvZQ5Q
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
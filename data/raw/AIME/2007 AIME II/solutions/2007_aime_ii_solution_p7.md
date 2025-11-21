# 2007 AIME II Problem 7

## Problem

Given a real number $x,$ let $\lfloor x \rfloor$ denote the greatest integer less than or equal to $x.$ For a certain integer $k,$ there are exactly $70$ positive integers $n_{1}, n_{2}, \ldots, n_{70}$ such that $k=\lfloor\sqrt[3]{n_{1}}\rfloor = \lfloor\sqrt[3]{n_{2}}\rfloor = \cdots = \lfloor\sqrt[3]{n_{70}}\rfloor$ and $k$ divides $n_{i}$ for all $i$ such that $1 \leq i \leq 70.$

Find the maximum value of $\frac{n_{i}}{k}$ for $1\leq i \leq 70.$

## Solution

## Solution 1
For $x = 1$ , we see that $\sqrt[3]{1} \ldots \sqrt[3]{7}$ all work, giving 7 integers. For $x=2$ , we see that in $\sqrt[3]{8} \ldots \sqrt[3]{26}$ , all of the even numbers work, giving 10 integers. For $x = 3$ , we get 13, and so on. We can predict that at $x = 22$ we get 70.
To prove this, note that all of the numbers from $\sqrt[3]{x^3} \ldots \sqrt[3]{(x+1)^3 - 1}$ divisible by $x$ work. Thus, $\frac{(x+1)^3 - 1 - x^3}{x} + 1 = \frac{3x^2 + 3x + 1 - 1}{x} + 1 = 3x + 4$ (the one to be inclusive) integers will fit the conditions. $3k + 4 = 70 \Longrightarrow k = 22$ .
The maximum value of $n_i = (x + 1)^3 - 1$ . Therefore, the solution is $\frac{23^3 - 1}{22} = \frac{(23 - 1)(23^2 + 23 + 1)}{22} = 529 + 23 + 1 = 553$ .

## Solution 2
Obviously $k$ is positive. Then, we can let $n_1$ equal $k^3$ and similarly let $n_i$ equal $k^3 + (i - 1)k$ .
The wording of this problem (which uses "exactly") tells us that $k^3+69k<(k+1)^3 = k^3 + 3k^2 + 3k+1 \leq k^3+70k$ . Taking away $k^3$ from our inequality results in $69k<3k^2+3k+1\leq 70k$ . Since $69k$ , $3k^2+3k+1$ , and $70k$ are all integers, this inequality is equivalent to $69k\leq 3k^2+3k<70k$ . Since $k$ is positive, we can divide the inequality by $k$ to get $69 \leq 3k+3 < 70$ . Clearly the only $k$ that satisfies is $k=22$ .
Then, $\frac{n_{70}}{k}=k^2+69=484+69=\boxed{553}$ is the maximum value of $\frac{n_i}{k}$ . (Remember we set $n_i$ equal to $k^3 + (i - 1)k$ !)

## Video Solution
2007 AIME II #7
MathProblemSolvingSkills.com

## Video Solution by the Beauty of Math
https://youtu.be/42kXJgD_b-A
These problems are copyrighted © by the Mathematical Association of America.
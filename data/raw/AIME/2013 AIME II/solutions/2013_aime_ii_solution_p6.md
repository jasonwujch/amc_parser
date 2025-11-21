# 2013 AIME II Problem 6

## Problem

Find the least positive integer $N$ such that the set of $1000$ consecutive integers beginning with $1000\cdot N$ contains no square of an integer.

## Solutions

## Solution 1
The difference between consecutive integral squares must be greater than 1000. $(x+1)^2-x^2\geq1000$ , so $x\geq\frac{999}{2}\implies x\geq500$ . $x=500$ does not work, so $x>500$ . Let $n=x-500$ . By inspection, $n^2$ should end in a number close to but less than 1000 such that there exists $1000N$ within the difference of the two squares. Examine when $n^2=1000$ . Then, $n=10\sqrt{10}$ . One example way to estimate $\sqrt{10}$ follows.
Then, $n\approx 31.6$ . $n^2<1000$ , so $n$ could be $31$ . Add 500 to get the first square and 501 to get the second. Then, the two integral squares are $531^2$ and $532^2$ . Checking, $531^2=281961$ and $532^2=283024$ . $282,000$ straddles the two squares, which have a difference of 1063. The difference has been minimized, so $N$ is minimized $N=282000\implies\boxed{282}$
~BJHHar

## Solution 2
Let us first observe the difference between $x^2$ and $(x+1)^2$ , for any arbitrary $x\ge 0$ . $(x+1)^2-x^2=2x+1$ . So that means for every $x\ge 0$ , the difference between that square and the next square have a difference of $2x+1$ . Now, we need to find an $x$ such that $2x+1\ge 1000$ . Solving gives $x\ge \frac{999}{2}$ , so $x\ge 500$ . Now we need to find what range of numbers has to be square-free: $\overline{N000}\rightarrow \overline{N999}$ have to all be square-free. Let us first plug in a few values of $x$ to see if we can figure anything out. $x=500$ , $x^2=250000$ , and $(x+1)^2=251001$ . Notice that this does not fit the criteria, because $250000$ is a square, whereas $\overline{N000}$ cannot be a square. This means, we must find a square, such that the last $3$ digits are close to $1000$ , but not there, such as $961$ or $974$ . Now, the best we can do is to keep on listing squares until we hit one that fits. We do not need to solve for each square: remember that the difference between consecutive squares are $2x+1$ , so all we need to do is addition. After making a list, we find that $531^2=281961$ , while $532^2=283024$ . It skipped $282000$ , so our answer is $\boxed{282}$ .

## Solution 3
Let $x$ be the number being squared. Based on the reasoning above, we know that $N$ must be at least $250$ , so $x$ has to be at least $500$ . Let $k$ be $x-500$ . We can write $x^2$ as $(500+k)^2$ , or $250000+1000k+k^2$ . We can disregard $250000$ and $1000k$ , since they won't affect the last three digits, which determines if there are any squares between $\overline{N000}\rightarrow \overline{N999}$ . So we must find a square, $k^2$ , such that it is under $1000$ , but the next square is over $1000$ . We find that $k=31$ gives $k^2=961$ , and so $(k+1)^2=32^2=1024$ . We can be sure that this skips a thousand because the $1000k$ increments it up $1000$ each time. Now we can solve for $x$ : $(500+31)^2=281961$ , while $(500+32)^2=283024$ . We skipped $282000$ , so the answer is $\boxed{282}$ .

## Solution 4
The goal is to find the least $N \in \mathbb{N}$ such that $\exists m \in \mathbb{N}$ where $m^2 + 1 \leq 1000N, 1000N + 1000 \leq (m+1)^2$ .
Combining the two inequalities leads to $(m+1)^2 \geq m^2 + 1001, m \geq 500$ .
Let $m = k + 500$ , where $k \in \mathbb{W}$ , then the inequalities become,
$N \geq \frac{(k+500)^2 + 1}{1000} = \frac{k^2 + 1}{1000} + k + 250$ , and
$N \leq \frac{(k+501)^2}{1000} - 1 = \frac{(k+1)^2}{1000} + k + 250.$
For $k=31$ , one can verify that $N = 282$ is the unique integer satisfying the inequalities.
For $k \leq 30$ , $k + 250 < \frac{k^2 + 1}{1000} + k + 250 \leq N$ $\leq \frac{(k+1)^2}{1000} + k + 250 \leq \frac{(30+1)^2}{1000} + k + 250 < k + 251$ ,
i.e., $k + 250 < N < k + 251$ , a contradiction.
Note $k \geq 32$ leads to larger $N$ (s).
Hence, the answer is $\boxed{282}$ .
~yuxiaomatt

## Video Solution
https://youtu.be/Rjx-0hAfQ6E?si=sr0N7dWeMg1jH5Bq
~MathProblemSolvingSkills.com
### See Also
Very similar to 2016 AMC 12 A Problem 25: https://artofproblemsolving.com/wiki/index.php/2016_AMC_12A_Problems/Problem_25
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
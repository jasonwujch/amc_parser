# 2001 AIME I Problem 2

## Problem

A finite set $\mathcal{S}$ of distinct real numbers has the following properties: the mean of $\mathcal{S}\cup\{1\}$ is $13$ less than the mean of $\mathcal{S}$ , and the mean of $\mathcal{S}\cup\{2001\}$ is $27$ more than the mean of $\mathcal{S}$ . Find the mean of $\mathcal{S}$ .

## Solution
Let $x$ be the mean of $\mathcal{S}$ . Let $a$ be the number of elements in $\mathcal{S}$ . Then, the given tells us that $\frac{ax+1}{a+1}=x-13$ and $\frac{ax+2001}{a+1}=x+27$ . Subtracting, we have \begin{align*}\frac{ax+2001}{a+1}-40=\frac{ax+1}{a+1} \Longrightarrow \frac{2000}{a+1}=40 \Longrightarrow a=49\end{align*} We plug that into our very first formula, and get: \begin{align*}\frac{49x+1}{50}&=x-13 \\ 49x+1&=50x-650 \\ x&=\boxed{651}.\end{align*}

## Solution 2
Since this is a weighted average problem, the mean of $S$ is $\frac{13}{27}$ as far from $1$ as it is from $2001$ . Thus, the mean of $S$ is $1 + \frac{13}{13 + 27}(2001 - 1) = \boxed{651}$ .

## Video Solution by OmegaLearn
https://youtu.be/IziHKOubUI8?t=27
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
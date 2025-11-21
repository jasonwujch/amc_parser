# 2016 AIME II Problem 15

## Problem

For $1 \leq i \leq 215$ let $a_i = \dfrac{1}{2^{i}}$ and $a_{216} = \dfrac{1}{2^{215}}$ . Let $x_1, x_2, ..., x_{216}$ be positive real numbers such that $\sum_{i=1}^{216} x_i=1$ and $\sum_{1 \leq i < j \leq 216} x_ix_j = \dfrac{107}{215} + \sum_{i=1}^{216} \dfrac{a_i x_i^{2}}{2(1-a_i)}$ . The maximum possible value of $x_2=\dfrac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution
Note that \begin{align*}\sum_{1 \leq i < j \leq 216} x_ix_j &= \frac12\left(\left(\sum_{i=1}^{216} x_i\right)^2-\sum_{i=1}^{216} x_i^2\right)\\&=\frac12\left(1-\sum x_i^2\right).\end{align*} Substituting this into the second equation and collecting $x_i^2$ terms, we find \[\sum_{i=1}^{216}\frac{x_i^2}{1-a_i}=\frac{1}{215}.\] Conveniently, $\sum_{i=1}^{216} 1-a_i=215$ so we find \[\left(\sum_{i=1}^{216} 1-a_i\right)\left(\sum_{i=1}^{216}\frac{x_i^2}{1-a_i}\right)=1=\left(\sum_{i=1}^{216} x_i\right)^2.\] This is the equality case of the Cauchy-Schwarz Inequality, so $x_i=c(1-a_i)$ for some constant $c$ . Summing these equations and using the facts that $\sum_{i=1}^{216} x_i=1$ and $\sum_{i=1}^{216} 1-a_i=215$ , we find $c=\frac{1}{215}$ and thus $x_2=c(1-a_2)=\frac{1}{215}\cdot \left(1-\frac{1}{4}\right)=\frac{3}{860}$ . Hence the desired answer is $860+3=\boxed{863}$ .

## Video Solution
https://youtu.be/mjtM-Coav4k
~MathProblemSolvingSkills.com
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
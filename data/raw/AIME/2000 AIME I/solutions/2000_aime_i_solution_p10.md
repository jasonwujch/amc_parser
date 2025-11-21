# 2000 AIME I Problem 10

## Problem

A sequence of numbers $x_{1},x_{2},x_{3},\ldots,x_{100}$ has the property that, for every integer $k$ between $1$ and $100,$ inclusive, the number $x_{k}$ is $k$ less than the sum of the other $99$ numbers. Given that $x_{50} = m/n,$ where $m$ and $n$ are relatively prime positive integers, find $m + n$ .

## Solution
Let the sum of all of the terms in the sequence be $\mathbb{S}$ . Then for each integer $k$ , $x_k = \mathbb{S}-x_k-k \Longrightarrow \mathbb{S} - 2x_k = k$ . Summing this up for all $k$ from $1, 2, \ldots, 100$ ,
\begin{align*}100\mathbb{S}-2(x_1 + x_2 + \cdots + x_{100}) &= 1 + 2 + \cdots + 100\\ 100\mathbb{S} - 2\mathbb{S} &= \frac{100 \cdot 101}{2} = 5050\\ \mathbb{S}&=\frac{2525}{49}\end{align*}
Now, substituting for $x_{50}$ , we get $2x_{50}=\frac{2525}{49}-50=\frac{75}{49} \Longrightarrow x_{50}=\frac{75}{98}$ , and the answer is $75+98=\boxed{173}$ .

## Solution 2
Consider $x_k$ and $x_{k+1}$ . Let $S$ be the sum of the rest 98 terms. Then $x_k+k=S+x_{k+1}$ and $x_{k+1}+(k+1)=S+x_k.$ Eliminating $S$ we have $x_{k+1}-x_k=-\dfrac{1}{2}.$ So the sequence is arithmetic with common difference $-\dfrac{1}{2}.$
In terms of $x_{50},$ the sequence is $x_{50}+\dfrac{49}{2}, x_{50}+\dfrac{48}{2},\cdots,x_{50}+\dfrac{1}{2}, x_{50}, x_{50}-\dfrac{1}{2}, \cdots, x_{50}-\dfrac{49}{2}, x_{50}-\dfrac{50}{2}.$ Therefore, $x_{50}+50=99x_{50}-\dfrac{50}{2}$ .
Solving, we get $x_{50}=\dfrac{75}{98}.$ The answer is $75+98=\boxed{173}.$
- JZ
- edited by erinb28lms

## Solution 3 (Sum of equations)
Like Solution 1, let the sum of all of the terms in this sequence be $\mathbb{S}$ . By definition:
\[x_1 + 1 = x_2+x_3+x_4+...+x_{100}\] \[x_2 + 2 = x_1+x_3+x_4+...+x_{100}\] \[x_3 + 3 = x_1+x_2+x_4+...+x_{100}\] \[...\] \[x_{99} + 99 = x_1+x_2+x_3+...+x_{98}+x_{100}\] \[x_{100} + 100 = x_1+x_2+x_3+...+x_{98}+x_{99}\] .
Adding up all of these equations yields:
\[\mathbb{S} + TR(100) = 99\mathbb{S}\]
Here $TR(100)$ represents the $100$ th triangular number, which is $5050$ . Solving for $\mathbb{S}$ yields:
\[\mathbb{S} = \frac{2525}{49}\] .
$\mathbb{S}$ can also be written as $x_{50} + (x_{50} + 50)$ . Solving for $x_{50}$ ,
\[2x_{50} = \frac{2525-2450}{49}\] \[2x_{50} = \frac{75}{49}\] \[x_{50} = \frac{75}{98}\]
The requested sum is therefore $75+98 = \boxed{173}$ .
~mathwizard123123

## Video solution
https://www.youtube.com/watch?v=TdvxgrSZTQw
These problems are copyrighted © by the Mathematical Association of America.
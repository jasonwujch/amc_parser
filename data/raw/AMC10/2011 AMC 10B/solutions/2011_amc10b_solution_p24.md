# 2011 AMC 10B Problem 24

## Problem

A lattice point in an $xy$ -coordinate system is any point $(x, y)$ where both $x$ and $y$ are integers. The graph of $y = mx +2$ passes through no lattice point with $0 < x \le 100$ for all $m$ such that $\frac{1}{2} < m < a$ . What is the maximum possible value of $a$ ?

$\textbf{(A)}\ \frac{51}{101} \qquad\textbf{(B)}\ \frac{50}{99} \qquad\textbf{(C)}\ \frac{51}{100} \qquad\textbf{(D)}\ \frac{52}{101} \qquad\textbf{(E)}\ \frac{13}{25}$

## Solution 1
For $y=mx+2$ to not pass through any lattice points with $0<x\leq 100$ is the same as saying that $mx\notin\mathbb Z$ for $x\in\{1,2,\dots,100\}$ , or in other words, $m$ is not expressible as a ratio of positive integers $s/t$ with $t\leq 100$ . Hence the maximum possible value of $a$ is the first real number after $1/2$ that is so expressible.
For each $d=2,\dots,100$ , the smallest multiple of $1/d$ which exceeds $1/2$ is $1,\frac23,\frac34,\frac35,\dots,\frac{50}{98},\frac{50}{99},\frac{51}{100}$ respectively, and the smallest of these is $\boxed{\textbf{(B)}\frac{50}{99}}$ .

## Solution 1.1
Note that finding the next possible slope $m$ greater than $\frac{1}{2}$ is the same as finding the next Farey fraction of order $100$ after $\frac{1}{2}$ . Hence, we can use the Farey mediant theorem ( https://en.wikipedia.org/wiki/Farey_sequence#Farey_neighbours ), which states that if $\frac{a}{b}<\frac{c}{d}$ are neighboring Farey fractions of order $n$ , then $bc-ad=1$ where $b, d \leq n$ .
In this case, we have $a=1$ , $b=2$ , and so $2c-d=1$ . We try $d=100$ , but that doesn't give integer $c$ . We try $d=99$ , which gives us $c=50$ so the upper bound is $\boxed{\textbf{(B)}\frac{50}{99}}$ .
~Math-lover1

## Solution 2
We see that for the graph of $y=mx+2$ to not pass through any lattice points, the denominator of $m$ must be greater than $100$ , or else it would be canceled by some $0<x\le100$ which would make $y$ an integer. By using common denominators, we find that the order of the fractions from smallest to largest is $\text{(A), (B), (C), (D), (E)}$ . We can see that when $m=\frac{50}{99}$ , $y$ could be an integer, so therefore any fraction greater than $\frac{50}{99}$ would not work, as substituting our fraction $\frac{50}{99}$ for $m$ would produce an integer for $y$ . So now we are left with only $\frac{51}{101}$ and $\frac{50}{99}$ . But since $\frac{51}{101}=\frac{5049}{9999}$ and $\frac{50}{99}=\frac{5050}{9999}$ , we can be absolutely certain that there isn't a number between $\frac{51}{101}$ and $\frac{50}{99}$ that can reduce to a fraction whose denominator is less than or equal to $100$ . Since we are looking for the maximum value of $a$ , we take the larger of $\frac{51}{101}$ and $\frac{50}{99}$ , which is $\boxed{\textbf{(B)}\frac{50}{99}}$ .

## Solution 3
We want to find the smallest $m$ such that there will be an integral solution to $y=mx+2$ with $0<x\le100$ . We first test A, but since the denominator has a $101$ , $x$ must be a nonzero multiple of $101$ , but it then will be greater than $100$ . We then test B. $y=\frac{50}{99}x+2$ yields the solution $(99,52)$ which satisfies $0<x\le100$ . Checking the answer choices, we know that the largest possible $a$ must be $\frac{50}{99}\implies\boxed{\textbf{(B)}}$

## Solution 4
Notice that for $y=\frac{1}{2}x+2=\frac{50}{100}x+2$ , $x=99$ is one of the integral values of $x$ such that the value of $\frac{50}{100}x$ is the closest to its next integral value.
Thus the maximum value for $a$ is the value of $m$ when the equation $y=99m+2$ goes through its next lattice point, which occurs when $m=\frac{b}{99}$ for some positive integer $b$ .
Finding the common denominator, we have \[\frac{50}{100}=\frac{4950}{9900}, \frac{b}{99}=\frac{100b}{9900}\] Since $a>\frac{1}{2}$ , the smallest value for $b$ such that $100b>4950$ is $b=50$ .
Thus the maximum value of $a$ is $\frac{50}{99}.\boxed{\mathrm{(B)}}$
~ Nafer

## Solution 5 (MAA.org)
https://www.maa.org/sites/default/files/pdf/CurriculumInspirations/CB095_A-Line-through-Lattice-Points.pdf
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
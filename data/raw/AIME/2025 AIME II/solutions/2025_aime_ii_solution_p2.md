# 2025 AIME II Problem 2

## Problem

Find the sum of all positive integers $n$ such that $n + 2$ divides the product $3(n + 3)(n^2 + 9)$ .

## Solution 1
$\frac{3(n+3)(n^{2}+9) }{n+2} \in \mathbb{Z}$
$\Rightarrow \frac{3(n+2+1)(n^{2}+9) }{n+2} \in \mathbb{Z}$
$\Rightarrow \frac{3(n+2)(n^{2}+9) +3(n^{2}+9)}{n+2} \in \mathbb{Z}$
$\Rightarrow 3(n^{2}+9)+\frac{3(n^{2}+9)}{n+2} \in \mathbb{Z}$
$\Rightarrow \frac{3(n^{2}-4+13)}{n+2} \in \mathbb{Z}$
$\Rightarrow \frac{3(n+2)(n-2)+39}{n+2} \in \mathbb{Z}$
$\Rightarrow 3(n-2)+\frac{39}{n+2} \in \mathbb{Z}$
$\Rightarrow \frac{39}{n+2} \in \mathbb{Z}$
Since $n + 2$ is positive, the positive factors of $39$ are $1$ , $3$ , $13$ , and $39$ .
Therefore, $n = -1$ , $1$ , $11$ and $37$ .
Since $n$ is positive, $n = 1$ , $11$ and $37$ .
$1 + 11 + 37 = \framebox{049}$ is the correct answer
～ Tonyttian
~ Edited by aoum

## Solution 2
We observe that $n+2$ and $n+3$ share no common prime factor, so $n+2$ divides $3(n+3)(n^2+9)$ if and only if $n+2$ divides $3(n^2+9)$ .
By dividing $\frac{3(n^2+9)}{n+2}$ either with long division or synthetic division, one obtains $3n-6+\frac{39}{n+2}$ . This quantity is an integer if and only if $\frac{39}{n+2}$ is an integer, so $n+2$ must be a factor of 39. As in Solution 1, $n \in \{1,11,37\}$ and the sum is $\boxed{049}$ .
~scrabbler94

## Solution 3 (modular arithmetic)
Let's express the right-hand expression in terms of mod $n + 2$ .
$3 \equiv 3 \pmod{n + 2}$ .
$n + 3 \equiv 1 \pmod{n + 2}$ .
$n^2 + 9 \equiv 13 \pmod{n + 2}$ since $n^2 - 4 \equiv 0 \pmod{n + 2}$ with a quotient $n - 2$
$3(n + 3)(n^2 + 9) \equiv 3(1)(13) \pmod{n + 2} \equiv 39 \pmod{n + 2}$
This means $39 = (n + 2)k \pmod{n + 2}$ where k is some integer.
Note that $n + 2$ is positive, meaning $n + 2 \geq 3$ .
$n + 2$ is one of the factors of 39, so $n + 2 = 3, 13,$ or $39$ , so $n = 1, 11,$ or $37$ .
The sum of all possible $n$ is $1 + 11 + 37 = \boxed{049}$ .
~Sohcahtoa157

## Video Solution by Mathletes Corner
https://www.youtube.com/watch?v=WYyDe_VyvvQ
~GP102
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
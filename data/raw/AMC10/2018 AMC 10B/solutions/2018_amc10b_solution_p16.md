# 2018 AMC 10B Problem 16

## Problem

Let $a_1,a_2,\dots,a_{2018}$ be a strictly increasing sequence of positive integers such that \[a_1+a_2+\cdots+a_{2018}=2018^{2018}.\] What is the remainder when $a_1^3+a_2^3+\cdots+a_{2018}^3$ is divided by $6$ ?

$\textbf{(A)}\ 0\qquad\textbf{(B)}\ 1\qquad\textbf{(C)}\ 2\qquad\textbf{(D)}\ 3\qquad\textbf{(E)}\ 4$

## Solution 1
Verify that $a^3 \equiv a \pmod{6}$ manually for all $a\in \mathbb{Z}/6\mathbb{Z}$ . We check: $0^3 \equiv 0 \pmod{6}$ , $1^3 \equiv 1 \pmod{6}$ , $2^3 \equiv 8 \equiv 2 \pmod{6}$ , $3^3 \equiv 27 \equiv 3 \pmod{6}$ , $4^3 \equiv 64 \equiv 4 \pmod{6}$ , and $5^3 \equiv 125 \equiv 5 \pmod{6}$ . We conclude that $a^3 \equiv a \pmod{6}$ .
Therefore, \[a_1^3+a_2^3+\cdots+a_{2018}^3 \equiv a_1+a_2+\cdots+a_{2018}\pmod{6}.\]
Thus the answer is congruent to $2018^{2018} = 1009^{2018} \cdot 2^{2018} \equiv \boxed{ \text{(E)}4} \pmod{6}$ because $2^n \pmod{6}$ alternates with $2$ and $4$ when $n$ increases, and by Euler's Totient Theorem $1009^{2018} = (1009^2)^{1009} \equiv 1^{1009} \equiv 1 \pmod{6}$ .
~Dolphindesigner
~Major error correction made by akashsuresh1.22~
~Another major error correction made by YTH
~Glossed-over detail filled in by GAMER100

## Solution 2
Note that $\left(a_1+a_2+\cdots+a_{2018}\right)^3=a_1^3+a_2^3+\cdots+a_{2018}^3+3a_1^2\left(a_1+a_2\\ +\cdots+a_{2018}-a_1\right)+3a_2^2\left(a_1+a_2+\cdots+a_{2018}-a_2\right)+\cdots+3a_{2018}^2\left(a_1+a_2+\cdots+a_{2018}-a_{2018}\right)+6\sum_{i\neq j\neq k}^{2018} a_ia_ja_k$
Note that $a_1^3+a_2^3+\cdots+a_{2018}^3+3a_1^2\left(a_1+a_2+\cdots+a_{2018}-a_1\right)+3a_2^2\left(a_1+a_2+\cdots+a_{2018}-a_2\right)+\cdots+3a_{2018}^2\left(a_1+a_2+\cdots+a_{2018}-a_{2018}\right)+6\sum_{i\neq j\neq k}^{2018} a_ia_ja_k\equiv a_1^3+a_2^3+\cdots+a_{2018}^3+3a_1^2({2018}^{2018}-a_1)+3a_2^2({2018}^{2018}-a_2)+\cdots+3a_{2018}^2({2018}^{2018}-a_{2018}) \equiv -2(a_1^3+a_2^3+\cdots+a_{2018}^3)\pmod 6$ Therefore, $-2(a_1^3+a_2^3+\cdots+a_{2018}^3)\equiv \left(2018^{2018}\right)^3\equiv\left( 2^{2018}\right)^3\equiv 4^3\equiv 4\pmod{6}$ .
Thus, $a_1^3+a_2^3+\cdots+a_{2018}^3\equiv 1\pmod 3$ . However, since cubing preserves parity, and the sum of the individual terms is even, the sum of the cubes is also even, and our answer is $\boxed{\text{(E) }4}$

## Solution 3 (Partial Proof)
First, we can assume that the problem will have a consistent answer for all possible values of $a_1$ . For the purpose of this solution, we will assume that $a_1 = 1$ .
We first note that $1^3+2^3+...+n^3 = (1+2+...+n)^2$ . So what we are trying to find is what $\left(2018^{2018}\right)^2=\left(2018^{4036}\right)$ mod $6$ . We start by noting that $2018$ is congruent to $2 \pmod{6}$ . So we are trying to find $\left(2^{4036}\right) \pmod{6}$ . Instead of trying to do this with some number theory skills, we could just look for a pattern. We start with small powers of $2$ and see that $2^1$ is $2$ mod $6$ , $2^2$ is $4$ mod $6$ , $2^3$ is $2$ mod $6$ , $2^4$ is $4$ mod $6$ , and so on... So we see that since $\left(2^{4036}\right)$ has an even power, it must be congruent to $4 \pmod{6}$ , thus giving our answer $\boxed{\text{(E) }4}$ . You can prove this pattern using mods. But I thought this was easier.
-TheMagician

## Solution 4 (Lazy solution)
First, we can assume that the problem will have a consistent answer for all possible values of $a_1$ . For the purpose of this solution, assume $a_1, a_2, ... a_{2017}$ are multiples of 6 and find $2018^{2018} \pmod{6}$ (which happens to be $4$ ). Then ${a_1}^3 + ... + {a_{2018}}^3$ is congruent to $64 \pmod{6}$ or just $\boxed{\textbf{(E)} 4}$ .
-Patrick4President
~minor edit made by CatachuKetchup~
WARNING: Technique does not always work; you have been warned

## Solution 5 (Even Lazier Solution)
Due to the large amounts of variables in the problem, and the fact that the test is only 75 minutes, you can assume that the answer is probably just $2018^{2018} \pmod{6}$ , which is $\boxed{\textbf{(E)} 4}$ .
~ Zeeshan12 [Be warned that this technique is not recommended for all problems and you should use it as a last resort]
### Algebraic Insight into Given Property
Mods is a good way to prove $a^3 \equiv a \pmod6$ : residues are simply $3, \pm 2, \pm 1, 0$ . Only $2$ and $3$ are necessary to check. Another way is to observe that $a^3-a$ factors into $(a-1)a(a+1)$ . Any $k$ consecutive numbers must be a multiple of $k$ , so $a^3-a$ is both divisible by $2$ and $3$ . This provides an algebraic method for proving $a^3 \equiv a \pmod6$ for all $a$ .

## Solution 6
We are not given any other requirements than the two given in the problem, so we can assume that $a_1 + a_{2018} = a_2 + a_{2017} + \cdots + a_{1004} + a_{1005} = \frac{2018^{2018}}{2018} \cdot 2$ . Since the (theoretical) $a_{1004.5}$ averages out to be $2018^{2017}$ (lets call this constant $N$ ), we can let $(a_1, a_{2018}) = (N - x_1, N+x_1)$ , $(a_2, a_{2017}) = (N - x_2, N+x_2)$ , ... , $(a_{1004}, a_{1005}) = (N - x_{1004}, N+x_{1004})$ for the sequence of decreasing positive integers $x_1, x_2, \cdots, x_{1004}$ . Notice that for any such pair (say $(a_{n}, a_{2019-n}$ ), we have $(a_n)^3 + (a_{2019-n})^3 = (N - x_n)^3 + (N+x_n)^3 = 2N^3 + 6N\cdot x_n \equiv 2N^3 \pmod{6}$ . Thus, $a_1^3 + a_2^3 + \cdots + a_{2018}^3 \equiv 1004\cdot 2N^3 \equiv 2018(2018^{2017})^3 \equiv 2018^{6052} \equiv 2^{6052} \pmod{6}$ . Since $2^x \pmod{6}$ repeats in the pattern $2, 4, 2, 4, \cdots$ , our final answer is $\boxed{\textbf{(E)} 4}$
~ Lucas.xue
~ LaTeX corrections by Samvuong

## Video Solution 1
With Modular Arithmetic Intro https://www.youtube.com/watch?v=wbv3TArroSs
~IceMatrix

## Video Solution 2
https://www.youtube.com/watch?v=SRjZ6B5DR74
~bunny1

## Video Solution 3 by OmegaLearn
https://youtu.be/4_x1sgcQCp4?t=112
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
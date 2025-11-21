# 2020 AIME II Problem 10

## Problem

Find the sum of all positive integers $n$ such that when $1^3+2^3+3^3+\cdots +n^3$ is divided by $n+5$ , the remainder is $17$ .

## Solution 1
The formula for the sum of cubes, also known as Nicomachus's Theorem, is as follows: \[1^3+2^3+3^3+\dots+k^3=(1+2+3+\dots+k)^2=\left(\frac{k(k+1)}{2}\right)^2\] for any positive integer $k$ .
So let's apply this to this problem.
Let $m=n+5$ . Then we have \begin{align*} 1^3+2^3+3^3+\dots+(m-5)^3&\equiv 17 \mod m \\ \left(\frac{(m-5)(m-4)}{2}\right)^2&\equiv 17 \mod m \\ \left(\dfrac{m(m-9)+20}2\right)^2&\equiv 17\mod m \\ \left(m(m-9)+20\right)^2&\equiv 4\cdot 17\mod m \\ \left(20\right)^2&\equiv 68\mod m \\ 332 &\equiv 0 \mod m \\ \end{align*} So, $m\in\{83,166,332\}$ . Testing the cases, only $332$ fails. This leaves $78+161=\boxed{239}$ .
$\LaTeX$ and formatting adjustments and intermediate steps for clarification by Technodoggo.

## Solution 2 (Official MAA 1)
The sum of the cubes from 1 to $n$ is \[1^3+2^3+\cdots+n^3=\frac{n^2(n+1)^2}{4}.\] For this to be equal to $(n+5)q+17$ for some integer $q$ , it must be that \[n^2(n+1)^2=4(n+5)q+4\cdot 17,\] so \[n^2(n+1)^2 \equiv 4 \cdot 17= 68\hskip-.2cm \pmod{n+5}.\] But $n^2(n+1)^2 \equiv (-5)^2(-4)^2 = 400 \pmod{n+5}.$ Thus $n^2(n+1)^2$ is congruent to both $68$ and $400,$ which implies that $n+5$ divides $400-68 = 332=2^2 \cdot 83$ . Because $n+5 > 17$ , the only choices for $n+5$ are $83, 166,$ and $332.$ Checking all three cases verifies that $n=78$ and $n=161$ work, but $n=327$ does not. The requested sum is $78+161 = 239$ .

## Solution 3 (Official MAA 2)
The sum of the cubes of the integers from $1$ through $n$ is \[1^3+2^3+\cdots+n^3=\frac{n^2(n+1)^2}{4},\] which, when divided by $n+5$ , has quotient \[Q=\frac14n^3 -\frac34n^2+4n-20 = \frac{n^2(n-3)}4+4n-20\] with remainder $100.$ If $n$ is not congruent to $1\pmod4$ , then $Q$ is an integer, and \[\frac{n^2(n+1)^2}{4} = (n+5)Q + 100 \equiv 17\pmod{n+5},\] so $n+5$ divides $100 - 17 =83$ , and $n = 78$ . If $n \equiv 1 \pmod4$ , then $Q$ is half of an integer, and letting $n = 4k+1$ for some integer $k$ gives \[\frac{n^2(n+1)^2}{4} = 2(2k+3)Q + 100 \equiv 17\pmod{n+5}.\] Thus $2k+3$ divides $100-17 = 83$ . It follows that $k=40$ , and $n = 161$ . The requested sum is $161 + 78 = 239$ .

## Solution 4
Using the formula for $\sum_{k=1}^n k^3$ , \[1^3 + 2^3 + 3^3 + ... + n^3 = \frac{n^2(n+1)^2}{4}\] Since $1^3 + 2^3 + 3^3 + ... + n^3$ divided by $n + 5$ has a remainder of $17$ , \[\frac{n^2(n+1)^2}{4} \equiv 17\pmod {n + 5}\] Using the rules of modular arithmetic, \[n^2(n+1)^2 \equiv 68\pmod {n + 5}\] \[n^2(n+1)^2 - 68\equiv 0\pmod {n + 5}\] Expanding the left hand side, \[n^4 + 2 n^3 + n^2 - 68\equiv 0\pmod {n + 5}\] This means that $n^4 + 2 n^3 + n^2 - 68$ is divisible by ${n + 5}$ .
\[(n + 5) | (n^4 + 2 n^3 + n^2 - 68)\] Dividing polynomials, \[\frac{n^4 + 2 n^3 + n^2 - 68}{n + 5}\] \[= n^3 - 3 n^2 + 16n - 80 + \frac{332}{(n + 5)}\] $(n + 5)$ $|$ $(n^4 + 2 n^3 + n^2 - 68)$ $\iff$ $\frac{332}{(n + 5)}$ $\in$ $\mathbb{Z}$ $\frac{332}{(n + 5)}$ $\in$ $\mathbb{Z}$ $\iff$ $(n + 5) = \pm 1, \pm 2, \pm 4, \pm 83, \pm 166, \pm 332$ Note that $n$ $\in$ $\mathbb{N}$ and $n + 5 > 17$ (because the remainder when dividing by $n + 5$ is $17$ , so $n + 5$ must be greater than $17$ ), so all options $\leq 17$ can be eliminated. \[(n + 5) = 83, 166, 332\] \[n = 78, 161, 327\] Checking all 3 cases, $n = 78$ and $n = 161$ work; $n = 327$ fails. Therefore, the answer is $78 + 161 = \boxed{239}$ . ~ {TSun} ~

## Solution 5 (similar ideas to Solution 1, but faster)
As before, we note that $(5+a)^3 + (n-a)^3 \equiv (5+a)^3 - (n+5 - (n-a))^3 \equiv 0 \pmod {n+5}.$ Thus, we can pair up the terms from $5^3$ to $n^3$ and cancel them. We have to deal with two cases:
If $n$ is even, then $5^3+6^3 + \cdots + n^3 \equiv 0 \pmod {n+5},$ as there are an even number of terms and they pair and cancel. We thus get $1^2+2^3+3^3+4^3 = 100 \equiv 17 \pmod {n+5},$ or $(n+5) | 83,$ which yields $n=78.$
If $n$ is odd, then $1^3+2^3+\cdots + n^3 \equiv 1^3+2^3+3^3+4^3+\left( \frac{n+5}{2} \right)^3 \equiv 17 \pmod {n+5}.$ Letting $k = \frac{n+5}{2}$ yields $k^2 + 83 \equiv 0 \pmod {2k}.$ However, this means that $83$ is divisible by $k,$ so $k=1,83.$ Plugging this back into $n$ yields $n=2(83)-5 = 161$ in the latter case.
Thus, the sum of all possible $n$ is just $78+161 = \boxed{239}.$
- ccx09

## Video Solution by OmegaLearn
~ pi_is_3.14

## Video solution
https://www.youtube.com/watch?v=87Mp0cdUtCU ~ North America Math Contest Go Go Go

## Video Solution
https://youtu.be/bz5N-jI2e0U?t=201
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
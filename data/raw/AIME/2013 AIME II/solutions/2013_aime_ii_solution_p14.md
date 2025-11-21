# 2013 AIME II Problem 14

## Problem

For positive integers $n$ and $k$ , let $f(n, k)$ be the remainder when $n$ is divided by $k$ , and for $n > 1$ let $F(n) = \max_{\substack{1\le k\le \frac{n}{2}}} f(n, k)$ . Find the remainder when $\sum\limits_{n=20}^{100} F(n)$ is divided by $1000$ .

## Solution
### The Pattern
We can find that
$20\equiv 6 \pmod{7}$
$21\equiv 5 \pmod{8}$
$22\equiv 6 \pmod{8}$
$23\equiv 7 \pmod{8}$
$24\equiv 6 \pmod{9}$
$25\equiv 7 \pmod{9}$
$26\equiv 8 \pmod{9}$
Observing these and we can find that the reminders are in groups of three continuous integers, considering this is true, and we get
$99\equiv 31 \pmod{34}$
$100\equiv 32 \pmod{34}$
So the sum is $6+3\times(6+...+31)+31+32=1512$ ,it is also 17+20+23+...+95, so the answer is $\boxed{512}$ . By: Kris17
### The Intuition
First, let's see what happens if we remove a restriction. Let's define $G(x)$ as
$G(x):=\max_{\substack{1\le k}} f(n, k)$
Now, if you set $k$ as any number greater than $n$ , you get n, obviously the maximum possible. That's too much freedom; let's restrict it a bit. Hence $H(x)$ is defined as
$H(x):=\max_{\substack{1\le k\le n}} f(n, k)$
Now, after some thought, we find that if we set $k=\lfloor \frac{n}{2} \rfloor+1$ we get a remainder of $\lfloor \frac{n-1}{2} \rfloor$ , the max possible. Once we have gotten this far, it is easy to see that the original equation,
$F(n) = \max_{\substack{1\le k\le \frac{n}{2}}} f(n, k)$
has a solution with $k=\lfloor \frac{n}{3} \rfloor+1$ .
$W^5$ ~Rowechen
### The Proof
The solution presented above does not prove why $F(x)$ is found by dividing $x$ by $3$ . Indeed, that is the case, as rigorously shown below.
Consider the case where $x = 3k$ . We shall prove that $F(x) = f(x, k+1)$ . For all $x/2\ge n > k+1, x = 2n + q$ , where $0\le q< n$ . This is because $x < 3k + 3 < 3n$ and $x \ge 2n$ . Also, as $n$ increases, $q$ decreases. Thus, $q = f(x, n) < f(x, k+1) = k - 2$ for all $n > k+1$ . Consider all $n < k+1. f(x, k) = 0$ and $f(x, k-1) = 3$ . Also, $0 < f(x, k-2) < k-2$ . Thus, for $k > 5, f(x, k+1) > f(x, n)$ for $n < k+1$ .
Similar proofs apply for $x = 3k + 1$ and $x = 3k + 2$ . The reader should feel free to derive these proofs themself.

## Generalized Solution
$Lemma:$ Highest remainder when $n$ is divided by $1\leq k\leq n/2$ is obtained for $k_0 = (n + (3 - n \pmod{3}))/3$ and the remainder thus obtained is $(n - k_0*2) = [(n - 6)/3 + (2/3)*n \pmod{3}]$ .
$Note:$ This is the second highest remainder when $n$ is divided by $1\leq k\leq n$ and the highest remainder occurs when $n$ is divided by $k_M$ = $(n+1)/2$ for odd $n$ and $k_M$ = $(n+2)/2$ for even $n$ .
Using the lemma above:
$\sum\limits_{n=20}^{100} F(n) = \sum\limits_{n=20}^{100} [(n - 6)/3 + (2/3)*n \pmod{3}]$ $= [(120*81/2)/3 - 2*81 + (2/3)*81] = 1512$
So the answer is $\boxed{512}$
Proof of Lemma: It is similar to $The Proof$ stated above.
Kris17

## Video Solution
https://youtu.be/mQ4_1dp8Wm8?si=Ae5HAc0cZQAjdtWl
~MathProblemSolvingSkills.com
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
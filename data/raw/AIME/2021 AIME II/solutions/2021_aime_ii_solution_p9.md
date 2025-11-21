# 2021 AIME II Problem 9

## Problem

Find the number of ordered pairs $(m, n)$ such that $m$ and $n$ are positive integers in the set $\{1, 2, ..., 30\}$ and the greatest common divisor of $2^m + 1$ and $2^n - 1$ is not $1$ .

## Solution 1
This solution refers to the Remarks section.
By the Euclidean Algorithm, we have \[\gcd\left(2^m+1,2^m-1\right)=\gcd\left(2,2^m-1\right)=1.\] We are given that $\gcd\left(2^m+1,2^n-1\right)>1.$ Multiplying both sides by $\gcd\left(2^m-1,2^n-1\right)$ gives \begin{align*} \gcd\left(2^m+1,2^n-1\right)\cdot\gcd\left(2^m-1,2^n-1\right)&>\gcd\left(2^m-1,2^n-1\right) \\ \gcd\left(\left(2^m+1\right)\left(2^m-1\right),2^n-1\right)&>\gcd\left(2^m-1,2^n-1\right) \hspace{12mm} &&\text{by }\textbf{Claim 1} \\ \gcd\left(2^{2m}-1,2^n-1\right)&>\gcd\left(2^m-1,2^n-1\right) \\ 2^{\gcd(2m,n)}-1&>2^{\gcd(m,n)}-1 &&\text{by }\textbf{Claim 2} \\ \gcd(2m,n)&>\gcd(m,n), \end{align*} which implies that $n$ must have more factors of $2$ than $m$ does.
We construct the following table for the first $30$ positive integers: \[\begin{array}{c|c|c} && \\ [-2.5ex] \boldsymbol{\#}\textbf{ of Factors of }\boldsymbol{2} & \textbf{Numbers} & \textbf{Count} \\ \hline && \\ [-2.25ex] 0 & 1,3,5,7,9,11,13,15,17,19,21,23,25,27,29 & 15 \\ && \\ [-2.25ex] 1 & 2,6,10,14,18,22,26,30 & 8 \\ && \\ [-2.25ex] 2 & 4,12,20,28 & 4 \\ && \\ [-2.25ex] 3 & 8,24 & 2 \\ && \\ [-2.25ex] 4 & 16 & 1 \\ \end{array}\] To count the ordered pairs $(m,n),$ we perform casework on the number of factors of $2$ that $m$ has:
1. If $m$ has $0$ factors of $2,$ then $m$ has $15$ options and $n$ has $8+4+2+1=15$ options. So, this case has $15\cdot15=225$ ordered pairs.
1. If $m$ has $1$ factor of $2,$ then $m$ has $8$ options and $n$ has $4+2+1=7$ options. So, this case has $8\cdot7=56$ ordered pairs.
1. If $m$ has $2$ factors of $2,$ then $m$ has $4$ options and $n$ has $2+1=3$ options. So, this case has $4\cdot3=12$ ordered pairs.
1. If $m$ has $3$ factors of $2,$ then $m$ has $2$ options and $n$ has $1$ option. So, this case has $2\cdot1=2$ ordered pairs.
Together, the answer is $225+56+12+2=\boxed{295}.$
~Lcz ~MRENTHUSIASM

## Solution 2
Consider any ordered pair $(m,n)$ such that $\gcd(2^m+1, 2^n-1) > 1$ . There must exist some odd number $p\ne 1$ such that $2^m \equiv -1 \pmod{p}$ and $2^n \equiv 1 \pmod{p}$ . Let $d$ be the order of $2$ modulo $p$ . Note that $2^{2m} \equiv 1 \pmod{p}$ . From this, we can say that $2m$ and $n$ are both multiples of $d$ , but $m$ is not. Thus, we have $v_2(n) \ge v_2(d)$ and $v_2(m) + 1 = v_2(d)$ . Substituting the latter equation into the inequality before gives $v_2(n) \ge v_2(m)+1$ . Since $v_2(n)$ and $v_2(m)$ are integers, this implies $v_2(n)>v_2(m)$ . The rest of the solution now proceeds as in Solution 1.
~Sedro
### Remarks
### Claim 1 (GCD Property)
If and are positive integers such that then
As $r$ and $s$ are relatively prime (have no prime divisors in common), this property is intuitive.
~MRENTHUSIASM
### Claim 2 (Olympiad Number Theory Lemma)
If and are positive integers such that then
There are two proofs to this claim, as shown below.
~MRENTHUSIASM
### Claim 2 Proof 1 (Euclidean Algorithm)
If $a=b,$ then $\gcd(a,b)=a=b,$ from which the claim is clearly true.
Otherwise, let $a>b$ without the loss of generality. For all integers $p$ and $q$ such that $p>q>0,$ the Euclidean Algorithm states that \[\gcd(p,q)=\gcd(p-q,q)=\cdots=\gcd(p\operatorname{mod}q,q).\] We apply this result repeatedly to reduce the larger number: \[\gcd\left(u^a-1,u^b-1\right)=\gcd\left(u^a-1-u^{a-b}\left(u^b-1\right),u^b-1\right)=\gcd\left(u^{a-b}-1,u^b-1\right).\] Continuing, we have \begin{align*} \gcd\left(u^a-1,u^b-1\right)&=\gcd\left(u^{a-b}-1,u^b-1\right) \\ & \ \vdots \\ &=\gcd\left(u^{\gcd(a,b)}-1,u^{\gcd(a,b)}-1\right) \\ &=u^{\gcd(a,b)}-1, \end{align*} from which the proof is complete.
~MRENTHUSIASM
### Claim 2 Proof 2 (Bézout's Identity)
Let $d=\gcd\left(u^a-1,u^b-1\right).$ It follows that $u^a\equiv1\pmod{d}$ and $u^b\equiv1\pmod{d}.$
By Bézout's Identity, there exist integers $x$ and $y$ such that $ax+by=\gcd(a,b),$ so \[u^{\gcd(a,b)}=u^{ax+by}=(u^a)^x\cdot(u^b)^y\equiv1\pmod{d},\] from which $u^{\gcd(a,b)}-1\equiv0\pmod{d}.$ We know that $u^{\gcd(a,b)}-1\geq d.$
Next, we notice that \begin{align*} u^a-1&=\left(u^{\gcd(a,b)}-1\right)\left(u^{a-\gcd{(a,b)}}+u^{a-2\gcd{(a,b)}}+u^{a-3\gcd{(a,b)}}+\cdots+1\right), \\ u^b-1&=\left(u^{\gcd(a,b)}-1\right)\left(u^{b-\gcd{(a,b)}}+u^{b-2\gcd{(a,b)}}+u^{b-3\gcd{(a,b)}}+\cdots+1\right). \end{align*} Since $u^{\gcd(a,b)}-1$ is a common divisor of $u^a-1$ and $u^b-1,$ we conclude that $u^{\gcd(a,b)}-1=d,$ from which the proof is complete.
~MRENTHUSIASM

## Video Solution
https://youtu.be/h3awf7yhGZ4
~MathProblemSolvingSkills.com

## Video Solution by Interstigation
https://youtu.be/kasgsb0Rge4
~Interstigation
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
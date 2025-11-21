# 2014 AIME II Problem 7

## Problem

Let $f(x)=(x^2+3x+2)^{\cos(\pi x)}$ . Find the sum of all positive integers $n$ for which \[\left |\sum_{k=1}^n\log_{10}f(k)\right|=1.\]

## Solution 1
First, let's split it into two cases to get rid of the absolute value sign
$\left |\sum_{k=1}^n\log_{10}f(k)\right|=1 \iff \sum_{k=1}^n\log_{10}f(k)=1,-1$
Now we simplify using product-sum logarithmic identites:
$\log_{10}{f(1)}+\log_{10}{f(2)}+...+\log_{10}{f(n)}=\log_{10}{f(1)\cdot f(2) \cdot ... \cdot f(n)}=1,-1$
Note that the exponent $\cos{\pi(x)}$ is either $-1$ if $x$ is odd or $1$ if $x$ is even.
Writing out the first terms we have
$\frac{1}{(2)(3)}(3)(4)\frac{1}{(4)(5)} \ldots$
This product clearly telescopes (i.e. most terms cancel) and equals either $10$ or $\frac{1}{10}$ . But the resulting term after telescoping depends on parity (odd/evenness), so we split it two cases, one where $n$ is odd and another where $n$ is even.
$\textbf{Case 1: Odd n}$
For odd $n$ , it telescopes to $\frac{1}{2(n+2)}$ where $n$ is clearly $3$ .
$\textbf{Case 2: Even n}$
For even $n$ , it telescopes to $\frac{n+2}{2}$ where $18$ is the only possible $n$ value. Thus the answer is $\boxed{021}$

## Solution 2
Note that $\cos(\pi x)$ is $-1$ when $x$ is odd and $1$ when $x$ is even. Also note that $x^2+3x+2=(x+1)(x+2)$ for all $x$ . Therefore \[\log_{10}f(x)=\log_{10}(x+1)+\log_{10}(x+2)\ \ \ \text{if }x \text{ is even}\] \[\log_{10}f(x)=-\log_{10}(x+1)-\log_{10}(x+2)\ \ \ \text{if }x \text{ is odd}\] Because of this, $\sum_{k=1}^n\log_{10}f(k)$ is a telescoping series of logs, and we have \[\sum_{k=1}^n\log_{10}f(k)= \log_{10}(n+2)-\log_{10}2=\log_{10}\frac{n+2}{2}\ \ \ \text{if }n \text{ is even}\] \[\sum_{k=1}^n\log_{10}f(k)= -\log_{10}(n+2)-\log_{10}2=-\log_{10}2(n+2)\ \ \ \text{if }n \text{ is odd}\] Setting each of the above quantities to $1$ and $-1$ and solving for $n$ , we get possible values of $n=3$ and $n=18$ so our desired answer is $3+18=\boxed{021}$
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
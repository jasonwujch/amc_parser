# 2009 AIME I Problem 13

## Problem

The terms of the sequence $(a_i)$ defined by $a_{n + 2} = \frac {a_n + 2009} {1 + a_{n + 1}}$ for $n \ge 1$ are positive integers. Find the minimum possible value of $a_1 + a_2$ .

## Solution 1
Our expression is \[a_{n + 2} = \frac {a_n + 2009} {1 + a_{n + 1}}.\] Manipulate this to obtain: \[a_{n + 2}a_{n + 1}+a_{n+2}= a_n + 2009.\] Our goal is to cancel terms. If we substitute in $n+1$ for $n,$ we get: \[a_{n+3}a_{n+2}+a_{n+3}=a_{n+1}+2009.\] Subtracting these two equations and manipulating the expression yields: \[(a_{n+2}+1)(a_{n+3}-a_{n+1})=a_{n+2}-a_n.\] Notice we have the form $a_{k+2}-a_k$ on both sides. Let $b_n=a_{n+2}-a_n.$ Then: \[b_{n+1}(a_{n+2}+1)=b_n.\] Notice that since $a_n$ is always an integer, $a_{n+2}+1$ and $b_n$ must also always be an integer. It is also clear that $b_n$ is a multiple of $b_{n+1},$ implying a decreasing sequence.
However, if the decreasing factor is nonzero, we will eventually have a $b_k$ that is not an integer, contradicting our conditions for $b_n$ . Thus, we need either $a_{n+2}+1=0 \Rightarrow a_{n+2}=-1$ (impossible as $a_n$ for all indices must be positive integers) or $b_n=0 \Rightarrow a_{n+2}=a_n.$
Given this, we want to find the minimum of $a_1+a_2.$ We have, from the problem: \[\frac{a_1+2009}{1+a_2}=a_3=a_1 \Rightarrow a_1 a_2 = 2009.\] By AM-GM, to minimize this, we have to make $a_1$ and $a_2$ factors as close as possible. Hence, the smallest possible sum is $41+49=90.$
~mathboy282

## Solution 2
This question is guessable but let's prove our answer
\[a_{n + 2} = \frac {a_n + 2009} {1 + a_{n + 1}}\]
\[a_{n + 2}(1 + a_{n + 1})= a_n + 2009\]
\[a_{n + 2}+a_{n + 2} a_{n + 1}-a_n= 2009\]
lets put $n+1$ into $n$ now
\[a_{n + 3}+a_{n + 3} a_{n + 2}-a_{n+1}= 2009\]
and set them equal now
\[a_{n + 3}+a_{n + 3} a_{n + 2}-a_{n+1}= a_{n + 2}+a_{n + 2} a_{n + 1}-a_n\]
\[a_{n + 3}-a_{n+1}+a_{n + 3} a_{n + 2}-a_{n + 2} a_{n + 1}= a_{n + 2}-a_n\]
let's rewrite it
\[(a_{n + 3}-a_{n+1})(a_{n + 2}+1)= a_{n + 2}-a_n\]
Let's make it look nice and let $b_n=a_{n + 2}-a_n$
\[(b_{n+1})(a_{n + 2}+1)= b_n\]
Since $b_n$ and $b_{n+1}$ are integers, we can see $b_n$ is divisible by $b_{n+1}$
But we can't have an infinite sequence of proper factors, unless $b_n=0$
Thus, $a_{n + 2}-a_n=0$
\[a_{n + 2}=a_n\]
So now, we know $a_3=a_1$
\[a_{3} = \frac {a_1 + 2009} {1 + a_{2}}\]
\[a_{1} = \frac {a_1 + 2009} {1 + a_{2}}\]
\[a_{1}+a_{1}a_{2} = a_1 + 2009\]
\[a_{1}a_{2} = 2009\]
To minimize $a_{1}+a_{2}$ , we need $41$ and $49$
Thus, our answer $= 41+49=\boxed {090}$

## Solution 3
If $a_{n} \ne \frac {2009}{a_{n+1}}$ , then either \[a_{n} = \frac {a_{n}}{1} < \frac {a_{n} + 2009}{1 + a_{n+1}} < \frac {2009}{a_{n+1}}\]
or
\[\frac {2009}{a_{n+1}} < \frac {2009 + a_{n}}{a_{n+1} + 1} < \frac {a_{n}}{1} = a_{n}\]
All the integers between $a_{n}$ and $\frac {2009}{a_{n+1}}$ would be included in the sequence. However the sequence is infinite, so eventually there will be a non-integral term.
So $a_{n} = \frac {2009}{a_{n+1}}$ , which $a_{n} \cdot a_{n+1} = 2009$ . When $n = 1$ , $a_{1} \cdot a_{2} = 2009$ . The smallest sum of two factors which have a product of $2009$ is $41 + 49=\boxed {090}$

## Solution 4 (BS Solution)
Essentially you see that it must be an integer for infinite numbers, which doesn't quite seem probable. The most logical explanation is that the sequence repeats, and the numbers in the sequence that repeat are integers. We list out some terms. \begin{align*} a_{1} &= a \\ a_{2} &= b \\ a_{3} &=\frac{a+2009}{1+b} \\ a_{4} &=\frac{(b+1)(b+2009)}{a+b+2010} \\ \end{align*} The terms get more and more wacky, so we just solve for $a,b$ such that $a_{1}=a_{3}$ and $a_{2}=a_{4}.$
Solving we find both equations end up to the equation $ab=2009$ in which we see to minimize we see that $a = 49$ and $b=41$ or vice versa for an answer of $\boxed{90}.$ This solution is VERY non rigorous and not recommended.
These problems are copyrighted © by the Mathematical Association of America.
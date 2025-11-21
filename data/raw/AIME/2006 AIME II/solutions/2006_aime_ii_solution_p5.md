# 2006 AIME II Problem 5

## Problem

When rolling a certain unfair six-sided die with faces numbered 1, 2, 3, 4, 5, and 6, the probability of obtaining face $F$ is greater than $1/6$ , the probability of obtaining the face opposite is less than $1/6$ , the probability of obtaining any one of the other four faces is $1/6$ , and the sum of the numbers on opposite faces is 7. When two such dice are rolled, the probability of obtaining a sum of 7 is $47/288$ . Given that the probability of obtaining face $F$ is $m/n,$ where $m$ and $n$ are relatively prime positive integers, find $m+n.$

## Solution 1
Without loss of generality , assume that face $F$ has a 6, so the opposite face has a 1. Let $A(n)$ be the probability of rolling a number $n$ on one die and let $B(n)$ be the probability of rolling a number $n$ on the other die. 7 can be obtained by rolling a 2 and 5, 5 and 2, 3 and 4, or 4 and 3. Each has a probability of $\frac{1}{6} \cdot \frac{1}{6} = \frac{1}{36}$ , totaling $4 \cdot \frac{1}{36} = \frac{1}{9}$ . Subtracting all these probabilities from $\frac{47}{288}$ leaves $\frac{15}{288}=\frac{5}{96}$ chance of getting a 1 on die $A$ and a 6 on die $B$ or a 6 on die $A$ and a 1 on die $B$ :
\[A(6)\cdot B(1)+B(6)\cdot A(1)=\frac{5}{96}\]
Since the two dice are identical, $B(1)=A(1)$ and $B(6)=A(6)$ so
\begin{align*}A(1)\cdot A(6)+A(1)\cdot A(6)&=\frac{5}{96}\\ A(1)\cdot A(6)&=\frac{5}{192}\end{align*}
Also, we know that $A(2)=A(3)=A(4)=A(5)=\frac{1}{6}$ and that the total probability must be $1$ , so:
\[A(1)+4 \cdot \frac{1}{6}+A(6)=\frac{6}{6} \Longrightarrow A(1)+A(6)=\frac{1}{3}\]
Combining the equations:
\begin{align*}A(6)\left(\frac{1}{3}-A(6)\right)&=\frac{5}{192}\\ 0 &= 192 \left(A(6)\right)^2 - 64 \left(A(6)\right) + 5\\ A(6)&=\frac{64\pm\sqrt{64^2 - 4 \cdot 5 \cdot 192}}{2\cdot192} =\frac{5}{24}, \frac{1}{8}\end{align*} We know that $A(6)>\frac{1}{6}$ , so it can't be $\frac{1}{8}$ . Therefore, the probability is $\frac{5}{24}$ and the answer is $5+24=\boxed{29}$ .
Note also that the initial assumption that face $F$ was the face labelled 6 is unnecessary -- we would have carried out exactly the same steps and found exactly the same probability no matter which face it was. We could have labelled $A(6)$ as $p$ , for example, and replaced the others with variables too, but the notation would have been harder to follow.

## Solution 2
We have that the cube probabilities to land on its faces are $\frac{1}{6}$ , $\frac{1}{6}$ , $\frac{1}{6}$ , $\frac{1}{6}$ , $\frac{1}{6}+x$ , $\frac{1}{6}-x$ we also know that the sum could be 7 only when the faces in each of the two tosses are opposite hence the probability to get a 7 is: \[4 \cdot \left(\frac{1}{6} \right)^2+2 \left(\frac{1}{6}+x \right) \left(\frac{1}{6}-x \right)=\frac{47}{288}\] multiplying by 288 we get: \[32+16(1-6x)(6x+1)=47 \Longrightarrow 16(1-36x^2)=15\] dividing by 16 and rearranging we get: \[\frac{1}{16}=36x^2 \longrightarrow x=\frac{1}{24}\] so the probability F which is greater than $\frac{1}{6}$ is equal $\frac{1}{6}+\frac{1}{24}=\frac{5}{24}\longrightarrow 24+5=\boxed{29}$

## Solution 3 (Alcumus)
Let $p(a,b)$ denote the probability of obtaining $a$ on the first die and $b$ on the second. Then the probability of obtaining a sum of 7 is \[p(1,6)+p(2,5)+p(3,4)+p(4,3)+p(5,2)+p(6,1).\] Let the probability of obtaining face $F$ be $(1/6)+x$ . Then the probability of obtaining the face opposite face $F$ is $(1/6)-x$ . Therefore
\begin{align*} {{47}\over{288}}&= 4\left({1\over6}\right)^2+2\left({1\over6}+x\right) \left({1\over6}-x\right)\cr&= {4\over36}+2\left({1\over36}-x^2\right)\cr&= {1\over6}-2x^2. \end{align*}
Then $2x^2=1/288$ , and so $x=1/24$ . The probability of obtaining face $F$ is therefore $(1/6)+(1/24)=5/24$ , and $m+n=\boxed{29}$ .
These problems are copyrighted © by the Mathematical Association of America.
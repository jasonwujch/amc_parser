# 2003 AIME II Problem 9

## Problem

Consider the polynomials $P(x) = x^{6} - x^{5} - x^{3} - x^{2} - x$ and $Q(x) = x^{4} - x^{3} - x^{2} - 1.$ Given that $z_{1},z_{2},z_{3},$ and $z_{4}$ are the roots of $Q(x) = 0,$ find $P(z_{1}) + P(z_{2}) + P(z_{3}) + P(z_{4}).$

## Solution
When we use long division to divide $P(x)$ by $Q(x)$ , the remainder is $x^2-x+1$ .
So, since $z_1$ is a root, $P(z_1)=(z_1)^2-z_1+1$ .
Now this also follows for all roots of $Q(x)$ Now \[P(z_2)+P(z_1)+P(z_3)+P(z_4)=z_1^2-z_1+1+z_2^2-z_2+1+z_3^2-z_3+1+z_4^2-z_4+1\]
Now by Vieta's we know that $-z_4-z_3-z_2-z_1=-1$ , so by Newton's Sums we can find $z_1^2+z_2^2+z_3^2+z_4^2$
$a_ns_2+a_{n-1}s_1+2a_{n-2}=0$
$(1)(s_2)+(-1)(1)+2(-1)=0$
$s_2-1-2=0$
$s_2=3$
So finally $P(z_2)+P(z_1)+P(z_3)+P(z_4)=3+4-1=\boxed{006}.$

## Solution 2
Let $S_k=z_1^k+z_2^k+z_3^k+z_4^k$ then by Vieta's Formula we have \[S_{-1}=\frac{z_1z_2z_3+z_1z_3z_4+z_1z_2z_4+z_1z_2z_3}{z_1z_2z_3z_4}=0\] \[S_0=4\] \[S_1=1\] \[S_2=3\] By Newton's Sums we have \[a_4S_k+a_3S_{k-1}+a_2S_{k-2}+a_1S_{k-1}+a_0S_{k-4}=0\]
Applying the formula couples of times yields $P(z_1)+P(z_2)+P(z_3)+P(z_4)=S_6-S_5-S_3-S_2-S_1=\boxed{6}$ .
~ Nafer

## Solution 3
$P(x) = x^{2}Q(x)+x^{4}-x^{3}-x.$
So we just have to find: $\sum_{n=1}^{4} z^{4}_n - \sum_{n=1}^{4} z^{3}_n - \sum_{n=1}^{4} z_n$ .
And by Newton's Sums this computes to: $11-4-1 = \boxed{006}$ .
~ LuisFonseca123

## Solution 4
If we scale $Q(x)$ by $x^2$ , we get $x^6-x^5-x^4-x^2$ . In order to get to $P(x)$ , we add $x^4-x^3-x$ . Therefore, our answer is $\sum_{n=1}^{4} z^4_n-z^3_n-z_n$ . However, rearranging $Q(z_n) = 0$ , makes our final answer $\sum_{n=1}^{4} z^2_n-z_n+1$ . The sum of the squares of the roots is $1^2-2(-1) = 3$ and the sum of the roots is $1$ . Adding 4 to our sum, we get $3-1+4 = \boxed{006}$ .
~ Vedoral

## Solution 5
Let $S_k$ = $z_1^k+z_2^k+z_3^k+z_4^k$
By Newton's Sums ,
$S_1-1=0$
$S_2-S_1-2=0$
$S_3-S_2-S_1=0$
$S_4-S_3-S_2-4=0$
$S_5-S_4-S_3-S_1=0$
$S_6-S_5-S_4-S_2=0$
Solving for $S_1,S_2,S_3,S_4,S_5,S_6$ , we get $S_1=1, S_2=3, S_3=4, S_4=11, S_5=16, S_6=30$
$P(z_1)+P(z_2)+P(z_3)+P(z_4)=S_6-S_5-S_3-S_2-S_1=\boxed{006}$

## Solution 6 (if you don't know how to divide polynomials directly)
$P(x)$ and $Q(x)$ look very similar, so let's try subtracting $Q(x)$ multiplied with something from $P(x)$ since we know $Q(z_n) = 0$ . To make the degrees the same, let's first multiply $Q(x)$ with $x^2$ :
$Q(x) \cdot x^2 = x^6 - x^5 - x^4 - x^2$ . Subtracting this from $P(x)$ gives $x^4 - x^3 - x$ . The degrees of this polynomial and $Q(x)$ are the same, so let's subtract $Q(x)$ : $x^4 - x^3 - x - Q(x)$ = $x^4 - x^3 - x - x^4 + x^3 + x^2 + 1 = x^2 - x + 1.$
So $P(x) - (x^2 + 1) \cdot Q(x) = x^2 - x + 1$ (this is also the remainder when $P(x)$ is divided by $Q(x)$ ). This tells us that our answer is the sum of the squares of the roots of $Q(x)$ minus the sum of the roots of $Q(x)$ plus $1 \cdot 4$ .
By Newton's Sums the sum of the squares of the roots is 3, and by Vieta's Formulas the sum of the roots is 1. So our answer is $3 - 1 + 4 = \boxed{006}$ .
~ grogg007

## Video Solution by Sal Khan
https://www.youtube.com/watch?v=ZSESJ8TeGSI&list=PLSQl0a2vh4HCtW1EiNlfW_YoNAA38D0l4&index=14 - AMBRIGGS
[rule]
Nice!-sleepypuppy
These problems are copyrighted © by the Mathematical Association of America.
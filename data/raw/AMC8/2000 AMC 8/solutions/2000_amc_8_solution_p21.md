# 2000 AMC 8 Problem 21

## Problem

Keiko tosses one penny and Ephraim tosses two pennies. The probability that Ephraim gets the same number of heads that Keiko gets is

$\text{(A)}\ \frac{1}{4}\qquad\text{(B)}\ \frac{3}{8}\qquad\text{(C)}\ \frac{1}{2}\qquad\text{(D)}\ \frac{2}{3}\qquad\text{(E)}\ \frac{3}{4}$

## Solution
Divide it into $2$ cases:
1) Keiko and Ephriam both get $0$ heads: This means that they both roll all tails, so there is only $1$ way for this to happen.
2) Keiko and Ephriam both get $1$ head: For Keiko, there is only $1$ way for this to happen because he is only flipping 1 penny, but for Ephriam, there are 2 ways since there are $2$ choices for when he can flip the head. So, in total there are $2 \cdot 1 = 2$ ways for this case.
Thus, in total there are $3$ ways that work. Since there are $2$ choices for each coin flip (Heads or Tails), there are $2^3 = 8$ total ways of flipping 3 coins.
Thus, since all possible coin flips of 3 coins are equally likely, the probability is $\boxed{(B) \frac38}$ .

## Solution 2
Let $K(n)$ be the probability that Keiko gets $n$ heads, and let $E(n)$ be the probability that Ephriam gets $n$ heads.
$K(0) = \frac{1}{2}$
$K(1) = \frac{1}{2}$
$K(2) = 0$ (Keiko only has one penny!)
$E(0) = \frac{1}{2}\cdot\frac{1}{2} = \frac{1}{4}$
$E(1) = \frac{1}{2}\cdot\frac{1}{2} + \frac{1}{2}\cdot\frac{1}{2} = 2\cdot\frac{1}{4} = \frac{1}{2}$ (because Ephraim can get HT or TH)
$E(2) = \frac{1}{2}\cdot\frac{1}{2} = \frac{1}{4}$
The probability that Keiko gets $0$ heads and Ephriam gets $0$ heads is $K(0)\cdot E(0)$ . Similarly for $1$ head and $2$ heads. Thus, we have:
$P = K(0)\cdot E(0) + K(1)\cdot E(1) + K(2)\cdot E(2)$
$P = \frac{1}{2}\cdot\frac{1}{4} + \frac{1}{2}\cdot\frac{1}{2} + 0\cdot\frac{1}{4}$
$P = \frac{3}{8}$
Thus the answer is $\boxed{B}$ .

## Solution 3
Keiko can only get 1 head or one tail. That means Ephriam has to also get 1 head or one tail. There are 3 cases $HHT, HTH, TTT$ and each have a $\frac{1}{2}\cdot\frac{1}{2}\cdot\frac{1}{2}=\frac{1}{8}$ chance. Adding all 3 ways makes a total of $\boxed{(B)\frac38}$
~RandomMathGuy500

## Video Solution
https://youtu.be/a_Tfeb_6dqE Soo, DRMS, NM
https://www.youtube.com/watch?v=mLrtRuJuYI4 ~David
### See Also
# 2000 AMC 8 Problem 14

## Problem

What is the units digit of $19^{19} + 99^{99}$ ?

$\text{(A)}\ 0 \qquad \text{(B)}\ 1 \qquad \text{(C)}\ 2 \qquad \text{(D)}\ 8 \qquad \text{(E)}\ 9$

## Video Solution by OmegaLearn
https://youtu.be/7an5wU9Q5hk?t=1552

## Solution
Finding a pattern for each half of the sum, even powers of $19$ have a units digit of $1$ , and odd powers of $19$ have a units digit of $9$ . So, $19^{19}$ has a units digit of $9$ .
Powers of $99$ have the exact same property, so $99^{99}$ also has a units digit of $9$ . $9+9=18$ which has a units digit of $8$ , so the answer is $\boxed{D}$ .

## Solution 2
Using modular arithmetic: \[99 \equiv 9 \equiv -1 \pmod{10}\]
Similarly, \[19 \equiv 9 \equiv -1 \pmod{10}\]
We have \[(-1)^{19} + (-1)^{99} = -1 + -1 \equiv \boxed{(\textbf{D}) \ 8} \pmod{10}\]
-ryjs

## Solution 3
Experimentation gives \[\text{any number ending with }9^{\text{something even}} = \text{has units digit }1\]
\[\text{any number ending with }9^{\text{something odd}} = \text{has units digit }9\]
Using this we have \[19^{19} + 99^{99}\] \[9^{19} + 9^{99}\]
Both $19$ and $99$ are odd, so we are left with \[9+9=18,\] which has units digit $\boxed{(\textbf{D}) \ 8}.$ -ryjs

## Solution 4
$19^{19}+99^{99}=$ 36972963764972677265718790562880544059566876428174110243025997242355257045527752342141065001012823272794097888 9548326540119429996769494359451621570193644014418071060667659303363419435659472789623878 which ends in 8. :) If you are really stupid and have time (like about 3 hours), this is a real brainless bash.
--hefei417
### See Also
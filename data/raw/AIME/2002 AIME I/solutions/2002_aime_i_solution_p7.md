# 2002 AIME I Problem 7

## Problem

The Binomial Expansion is valid for exponents that are not integers. That is, for all real numbers $x,y$ and $r$ with $|x|>|y|$ ,

\[(x+y)^r=x^r+rx^{r-1}y+\dfrac{r(r-1)}{2}x^{r-2}y^2+\dfrac{r(r-1)(r-2)}{3!}x^{r-3}y^3 \cdots\]

What are the first three digits to the right of the decimal point in the decimal representation of $(10^{2002}+1)^{\frac{10}{7}}$ ?

## Solution 1
$1^n$ will always be 1, so we can ignore those terms, and using the definition ( $2002 / 7 = 286$ ):
\[(10^{2002} + 1)^{\frac {10}7} = 10^{2860}+\dfrac{10}{7}10^{858}+\dfrac{15}{49}10^{-1144}+\cdots\]
Since the exponent of the $10$ goes down extremely fast, it suffices to consider the first few terms. Also, the $10^{2860}$ term will not affect the digits after the decimal, so we need to find the first three digits after the decimal in
\[\dfrac{10}{7}10^{858}\] .
(The remainder after this term is positive by the Remainder Estimation Theorem. Since the repeating decimal of $\dfrac{10}{7}$ repeats every 6 digits, we can cut out a lot of 6's from $858$ to reduce the problem to finding the first three digits after the decimal of
$\dfrac{10}{7}$ .
That is the same as $1+\dfrac{3}{7}$ , and the first three digits after $\dfrac{3}{7}$ are $\boxed{428}$ .

## Solution 2
An equivalent statement is to note that we are looking for $1000 \left\{\frac{10^{859}}{7}\right\}$ , where $\{x\} = x - \lfloor x \rfloor$ is the fractional part of a number. By Fermat's Little Theorem , $10^6 \equiv 1 \pmod{7}$ , so $10^{859} \equiv 3^{6 \times 143 + 1} \equiv 3 \pmod{7}$ ; in other words, $10^{859}$ leaves a residue of $3$ after division by $7$ . Then the desired answer is the first three decimal places after $\frac 37$ , which are $\boxed{428}$ .
These problems are copyrighted © by the Mathematical Association of America.
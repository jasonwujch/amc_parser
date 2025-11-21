# 2007 AMC 10A Problem 20

## Problem

Suppose that the number $a$ satisfies the equation $4 = a + a^{ - 1}$ . What is the value of $a^{4} + a^{ - 4}$ ?

$\textbf{(A)}\ 164 \qquad \textbf{(B)}\ 172 \qquad \textbf{(C)}\ 192 \qquad \textbf{(D)}\ 194 \qquad \textbf{(E)}\ 212$

## Solution 1 (Decreases the Powers)
Note that for all real numbers $k,$ we have $a^{2k} + a^{-2k} + 2 = (a^{k} + a^{-k})^2,$ from which \[a^{2k} + a^{-2k} = (a^{k} + a^{-k})^2-2.\] We apply this result twice to get the answer: \begin{align*} a^4 + a^{-4} &= (a^2 + a^{-2})^2 - 2 \\ &= [(a + a^{-1})^2 - 2]^2 - 2 \\ &= \boxed{\textbf{(D)}\ 194}. \end{align*} ~Azjps ~MRENTHUSIASM

## Solution 2 (Increases the Powers)
Squaring both sides of $a+a^{-1}=4$ gives $a^2+a^{-2}+2=16,$ from which $a^2+a^{-2}=14.$
Squaring both sides of $a^2+a^{-2}=14$ gives $a^4+a^{-4}+2=196,$ from which $a^4+a^{-4}=\boxed{\textbf{(D)}\ 194}.$
~Rbhale12 ~MRENTHUSIASM

## Solution 3 (Detailed Explanation of Solution 2)
The detailed explanation of Solution 2 is as follows: \begin{alignat*}{8} a+a^{-1}&=4 \\ (a+a^{-1})^2&=4^2 \\ a^2+2aa^{-1}+a^{-2}&=16 \\ a^2+a^{-2}&=16-2&&=14 \\ (a^2+a^{-2})^2&=14^2 \\ a^4+2a^2a^{-2}+a^{-4}&=196 \\ a^4+a^{-4}&=196-2&&=\boxed{\textbf{(D)}\ 194}. \\ \end{alignat*} ~MathFun1000 ~MRENTHUSIASM

## Solution 4 (Binomial Theorem)
Squaring both sides of $a+a^{-1}=4$ gives $a^2+a^{-2}+2=16,$ from which $a^2+a^{-2}=14.$
Applying the Binomial Theorem, we raise both sides of $a+a^{-1}=4$ to the fourth power: \begin{align*} \binom40a^4a^0+\binom41a^3a^{-1}+\binom42a^2a^{-2}+\binom43a^1a^{-3}+\binom44a^0a^{-4}&=256 \\ a^4+4a^2+6+4a^{-2}+a^{-4}&=256 \\ \left(a^4+a^{-4}\right)+4\left(a^2+a^{-2}\right)&=250 \\ \left(a^4+a^{-4}\right)+4(14)&=250 \\ a^4+a^{-4}&=\boxed{\textbf{(D)}\ 194}. \end{align*} ~MRENTHUSIASM

## Solution 5 (Solves for a)
We multiply both sides of $4=a+a^{-1}$ by $a,$ then rearrange: \[a^2-4a+1=0.\]
We apply the Quadratic Formula to get $a=2\pm\sqrt3.$
By Vieta's Formulas, note that the roots are reciprocals of each other. Therefore, both values of $a$ produce the same value of $a^4+a^{-4}:$ \begin{align*} a^4+a^{-4}&=\left(2+\sqrt{3}\right)^4 + \left(2+\sqrt{3}\right)^{-4} \\ &=\left(2+\sqrt{3}\right)^4+\left(2-\sqrt{3}\right)^4 &&(*) \\ &=\boxed{\textbf{(D)}\ 194}. \end{align*} Remarks about
1. To find the fourth power of a sum/difference, we can first square that sum/difference, then square the result.
1. When we expand the fourth powers and combine like terms, the irrational terms will cancel.
~Azjps ~MRENTHUSIASM

## Solution 6 (Newton's Sums)
From the first sentence of Solution 4, we conclude that $a$ and $a^{-1}$ are the roots of $x^2-4x+1=0.$ Let \begin{align*} P_1&=a+a^{-1}, \\ P_2&=a^2+a^{-2}, \\ P_3&=a^3+a^{-3}, \\ P_4&=a^4+a^{-4}. \end{align*} By Newton's Sums, we have \begin{alignat*}{12} &1\cdot P_1-4\cdot 1&&=0 &&\qquad\implies\qquad P_1&&=4, \\ &1\cdot P_2-4\cdot P_1+1\cdot2 &&=0 &&\qquad\implies\qquad P_2&&=14, \\ &1\cdot P_3-4\cdot P_2+1\cdot P_1&&=0 &&\qquad\implies\qquad P_3&&=52, \\ &1\cdot P_4-4\cdot P_3+1\cdot P_2&&=0 &&\qquad\implies\qquad P_4&&=\boxed{\textbf{(D)}\ 194}. \end{alignat*} ~Albert1993 ~MRENTHUSIASM

## Solution 7 (Answer Choices)
Note that \[a^{4} + a^{-4} = (a^{2} + a^{-2})^{2} - 2.\] We guess that $a^{2} + a^{-2}$ is an integer, so the answer must be $2$ less than a perfect square. The only possibility is $\boxed{\textbf{(D)}\ 194}.$
~Thanosaops ~MRENTHUSIASM

## Video Solution
https://youtu.be/rP8_-36n1ps
~MK

## Video Solution by OmegaLearn
https://youtu.be/MhALjut3Qmw?t=484
~ pi_is_3.14
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
# 2020 AIME II Problem 1

## Problem

Find the number of ordered pairs of positive integers $(m,n)$ such that ${m^2n = 20 ^{20}}$ .

## Solution
In this problem, we want to find the number of ordered pairs $(m, n)$ such that $m^2n = 20^{20}$ . Let $x = m^2$ . Therefore, we want two numbers, $x$ and $n$ , such that their product is $20^{20}$ and $x$ is a perfect square. Note that there is exactly one valid $n$ for a unique $x$ , which is $\tfrac{20^{20}}{x}$ . This reduces the problem to finding the number of unique perfect square factors of $20^{20}$ .
$20^{20} = 2^{40} \cdot 5^{20} = \left(2^2\right)^{20}\cdot\left(5^2\right)^{10}.$ Therefore, the answer is $21 \cdot 11 = \boxed{231}.$
~superagh
~TheBeast5520

## Solution 2 (Official MAA)
Because $20^{20}=2^{40}5^{20}$ , if $m^2n = 20^{20}$ , there must be nonnegative integers $a$ , $b$ , $c$ , and $d$ such that $m = 2^a5^b$ and $n = 2^c5^d$ . Then \[2a + c = 40\] and \[2b+d = 20\] The first equation has $21$ solutions corresponding to $a = 0,1,2,\dots,20$ , and the second equation has $11$ solutions corresponding to $b = 0,1,2,\dots,10$ . Therefore there are a total of $21\cdot11 = \boxed{231}$ ordered pairs $(m,n)$ such that $m^2n = 20^{20}$ .

## Video Solution by OmegaLearn
https://youtu.be/zfChnbMGLVQ?t=4612
~ pi_is_3.14

## Video Solution
https://www.youtube.com/watch?v=VA1lReSkGXU
~ North America Math Contest Go Go Go

## Video Solution
https://www.youtube.com/watch?v=x0QznvXcwHY
~IceMatrix

## Video Solution
https://youtu.be/Va3MPyAULdU
~avn
### Purple Comet Math Meet April 2020
Notice, that this was the exact same problem (with different wording of course) as Purple Comet HS problem 3 and remembering the answer, put $\boxed{231}$ .
https://purplecomet.org/views/data/2020HSSolutions.pdf
~Lopkiloinm

## Video Solution by WhyMath
https://youtu.be/Gs27CPxRiTA
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
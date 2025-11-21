# 2002 AIME II Problem 3

## Problem

It is given that $\log_{6}a + \log_{6}b + \log_{6}c = 6,$ where $a,$ $b,$ and $c$ are positive integers that form an increasing geometric sequence and $b - a$ is the square of an integer. Find $a + b + c.$

## Solution 1
$abc=6^6$ . Since they form an increasing geometric sequence, $b$ is the geometric mean of the product $abc$ . $b=\sqrt[3]{abc}=6^2=36$ .
Since $b-a$ is the square of an integer, we can find a few values of $a$ that work: $11, 20, 27, 32,$ and $35$ . Out of these, the only value of $a$ that works is $a=27$ , from which we can deduce that $c=\dfrac{36}{27}\cdot 36=\dfrac{4}{3}\cdot 36=48$ .
Thus, $a+b+c=27+36+48=\boxed{111}$

## Solution 2(similar to Solution 1)
Let $r$ be the common ratio of the geometric sequence. Since it is increasing, that means that $b = ar$ , and $c = ar^2$ . Simplifying the logarithm, we get $\log_6(a^3 \cdot r^3) = 6$ . Therefore, $a^3 \cdot r^3 = 6^6$ . Taking the cube root of both sides, we see that $ar = 6^2 = 36$ . Now since $ar = b$ , that means $b = 36$ . Using the trial and error shown in solution 1, we get $a = 27$ , and $r = \frac{4}{3}$ . Now, $27 \cdot r^2= c = 48$ . Therefore, the answer is $27+36+48 = \boxed{111}$
~idk12345678
These problems are copyrighted © by the Mathematical Association of America.
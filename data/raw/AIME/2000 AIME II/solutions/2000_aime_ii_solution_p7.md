# 2000 AIME II Problem 7

## Problem

Given that

find the greatest integer that is less than $\frac N{100}$ .

## Solution
Multiplying both sides by $19!$ yields:
\[\frac {19!}{2!17!}+\frac {19!}{3!16!}+\frac {19!}{4!15!}+\frac {19!}{5!14!}+\frac {19!}{6!13!}+\frac {19!}{7!12!}+\frac {19!}{8!11!}+\frac {19!}{9!10!}=\frac {19!N}{1!18!}.\]
\[\binom{19}{2}+\binom{19}{3}+\binom{19}{4}+\binom{19}{5}+\binom{19}{6}+\binom{19}{7}+\binom{19}{8}+\binom{19}{9} = 19N.\]
Recall the Combinatorial Identity $2^{19} = \sum_{n=0}^{19} {19 \choose n}$ . Since ${19 \choose n} = {19 \choose 19-n}$ , it follows that $\sum_{n=0}^{9} {19 \choose n} = \frac{2^{19}}{2} = 2^{18}$ .
Thus, $19N = 2^{18}-\binom{19}{1}-\binom{19}{0}=2^{18}-19-1 = (2^9)^2-20 = (512)^2-20 = 262124$ .
So, $N=\frac{262124}{19}=13796$ and $\left\lfloor \frac{N}{100} \right\rfloor =\boxed{137}$ .

## Solution 2
Let $f(x) = (1+x)^{19}.$ Applying the binomial theorem gives us $f(x) = \binom{19}{19} x^{19} + \binom{19}{18} x^{18} + \binom{19}{17} x^{17}+ \cdots + \binom{19}{0}.$ Since $\frac 1{2!17!}+\frac 1{3!16!}+\dots+\frac 1{8!11!}+\frac 1{9!10!} = \frac{\frac{f(1)}{2} - \binom{19}{19} - \binom{19}{18}}{19!},$ $N = \frac{2^{18}-20}{19}.$ After some fairly easy bashing, we get $\boxed{137}$ as the answer.
~peelybonehead

## Solution 3 (Brute Force)
Convert each denominator to $19!$ and get the numerators to be $9,51,204,612,1428,2652,3978,4862$ (refer to note). Adding these up we have $13796$ therefore $\boxed{137}$ is the desired answer.
Note: Notice that each numerator is increased each time by a factor of $\frac{17}{3}, \frac{16}{4}, \frac{15}{5}, \frac{14}{6},$ etc. until $\frac{11}{9}$ . If you were taking the test under normal time conditions, it shouldn't be too hard to bash out all of the numbers but it is priority to be careful.
~SirAppel
These problems are copyrighted © by the Mathematical Association of America.
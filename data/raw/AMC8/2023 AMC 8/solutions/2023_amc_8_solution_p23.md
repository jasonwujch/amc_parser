# 2023 AMC 8 Problem 23

## Problem

Each square in a $3 \times 3$ grid is randomly filled with one of the $4$ gray and white tiles shown below on the right. [asy] size(5.663333333cm); draw((0,0)--(3,0)--(3,3)--(0,3)--cycle,gray); draw((1,0)--(1,3)--(2,3)--(2,0),gray); draw((0,1)--(3,1)--(3,2)--(0,2),gray); fill((6,.33)--(7,.33)--(7,1.33)--cycle,mediumgray); draw((6,.33)--(7,.33)--(7,1.33)--(6,1.33)--cycle,gray); fill((6,1.67)--(7,2.67)--(6,2.67)--cycle,mediumgray); draw((6,1.67)--(7,1.67)--(7,2.67)--(6,2.67)--cycle,gray); fill((7.33,.33)--(8.33,.33)--(7.33,1.33)--cycle,mediumgray); draw((7.33,.33)--(8.33,.33)--(8.33,1.33)--(7.33,1.33)--cycle,gray); fill((8.33,1.67)--(8.33,2.67)--(7.33,2.67)--cycle,mediumgray); draw((7.33,1.67)--(8.33,1.67)--(8.33,2.67)--(7.33,2.67)--cycle,gray); [/asy] What is the probability that the tiling will contain a large gray diamond in one of the smaller $2 \times 2$ grids? Below is an example of such tiling. [asy] size(2cm); fill((1,0)--(0,1)--(0,2)--(1,1)--cycle,mediumgray); fill((2,0)--(3,1)--(2,2)--(1,1)--cycle,mediumgray); fill((1,2)--(1,3)--(0,3)--cycle,mediumgray); fill((1,2)--(2,2)--(2,3)--cycle,mediumgray); fill((3,2)--(3,3)--(2,3)--cycle,mediumgray); draw((0,0)--(3,0)--(3,3)--(0,3)--cycle,gray); draw((1,0)--(1,3)--(2,3)--(2,0),gray); draw((0,1)--(3,1)--(3,2)--(0,2),gray); [/asy]

$\textbf{(A) } \frac{1}{1024} \qquad \textbf{(B) } \frac{1}{256} \qquad \textbf{(C) } \frac{1}{64} \qquad \textbf{(D) } \frac{1}{16} \qquad \textbf{(E) } \frac{1}{4}$

## Solution 1
There are $4$ cases that the tiling will contain a large gray diamond in one of the smaller $2 \times 2$ grids, as shown below: [asy] size(375); fill((1,1)--(2,2)--(1,3)--(0,2)--cycle,mediumgray); draw((0,0)--(3,0)--(3,3)--(0,3)--cycle,gray); draw((1,0)--(1,3)--(2,3)--(2,0),gray); draw((0,1)--(3,1)--(3,2)--(0,2),gray); fill(shift(7,0)*((1,1)--(2,2)--(1,3)--(0,2)--cycle),mediumgray); draw(shift(6,0)*((0,0)--(3,0)--(3,3)--(0,3)--cycle),gray); draw(shift(6,0)*((1,0)--(1,3)--(2,3)--(2,0)),gray); draw(shift(6,0)*((0,1)--(3,1)--(3,2)--(0,2)),gray); fill(shift(12,-1)*((1,1)--(2,2)--(1,3)--(0,2)--cycle),mediumgray); draw(shift(12,0)*((0,0)--(3,0)--(3,3)--(0,3)--cycle),gray); draw(shift(12,0)*((1,0)--(1,3)--(2,3)--(2,0)),gray); draw(shift(12,0)*((0,1)--(3,1)--(3,2)--(0,2)),gray); fill(shift(19,-1)*((1,1)--(2,2)--(1,3)--(0,2)--cycle),mediumgray); draw(shift(18,0)*((0,0)--(3,0)--(3,3)--(0,3)--cycle),gray); draw(shift(18,0)*((1,0)--(1,3)--(2,3)--(2,0)),gray); draw(shift(18,0)*((0,1)--(3,1)--(3,2)--(0,2)),gray); [/asy] There are $4^5$ ways to decide the $5$ white squares for each case, and the cases do not have any overlap.
So, the requested probability is \[\frac{4\cdot4^5}{4^9} = \frac{4^6}{4^9} = \frac{1}{4^3} = \boxed{\textbf{(C) } \frac{1}{64}}.\] ~apex304, TaeKim, MRENTHUSIASM

## Solution 2
Note that the middle tile can be any of the four tiles. The gray part of the middle tile points towards one of the corners, and for the gray diamond to appear the three adjacent tiles must all be perfect. Thus, the solution is $\frac14 \cdot \frac14 \cdot \frac14 = \boxed{\textbf{(C) } \frac{1}{64}}$ .
~aayr

## Solution 3
Note that each tile must be in its precise place. Because of that, each diamond has a $\left(\frac14\right)^4$ chance of appearing. And since there are 4 placements, our solution is $\frac{1}{4^4} \cdot 4 = \boxed{\textbf{(C) } \frac{1}{64}}$ .
~ligonmathkid2

## Solution 4 (Linearity of Expectation)
Let $S_1, S_2, S_3$ , and $S_4$ denote the $4$ smaller $2 \times 2$ squares within the $3 \times 3$ square in some order. For each $S_i$ , let $X_i = 1$ if it contains a large gray diamond tiling and $X_i = 0$ otherwise. This means that $\mathbb{E}[X_i]$ is the probability that square $S_i$ has a large gray diamond, so $\mathbb{E}[X_1 + X_2 + X_3 + X_4]$ is our desired probability. However, since there is only one possible way to arrange the squares within every $2 \times 2$ square to form such a tiling, we have $\mathbb{E}[X_i] = (\tfrac{1}{4})^4 = \tfrac{1}{256}$ for all $i$ (as each of the smallest tiles has $4$ possible arrangements), and from the linearity of expectation we get \[\mathbb{E}[X_1 + X_2 + X_3 + X_4] = \mathbb{E}[X_1] + \mathbb{E}[X_2] + \mathbb{E}[X_3] + \mathbb{E}[X_4] = \frac{1}{256} + \frac{1}{256} + \frac{1}{256} + \frac{1}{256} = \boxed{\textbf{(C) } \frac{1}{64}}.\] ~eibc
Remark 1: This method might be too advanced for the AMC 8, and is probably unnecessary (refer to the other solutions for simpler techniques).
Remark 2: Note that Probability and Expected Value are equivalent in this problem since there will never be two diamonds on one tiling. i.e. $X_1 + X_2 + X_3 + X_4 \le 1$ .
~numerophile

## Solution 5 (Simple and Quick)
We can start by finding the probability of making a diamond with the squares in ONLY the top-left corner of the square. There are $4\times 4\times 4\times 4 = 256$ total cases of putting four random tiles in the top-left corner. Since there is only one favorable case (the case of making a diamond) out of $256$ total, the probability of making a diamond is $\frac{1}{256}.$ Now, we can simply multiply this by four to account for all corners of the square to get $4\times \frac{1}{256}$ or $\boxed{\textbf{(C) } \frac{1}{64}}.$
-mathguy567

## Video Solution by Math-X (Smart and Simple)
https://youtu.be/Ku_c1YHnLt0?si=wz7F8E_c7Hxv9GQ5&t=5137
~Math-X

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/zntZrtsnyxc?si=nM5eWOwNU6HRdleZ&t=2831 ~hsnacademy

## Video Solution (THINKING CREATIVELY!!!)
https://youtu.be/B5qcEnobmEU
~Education, the Study of Everything

## Video Solution
https://youtu.be/2t_Za0Y2IqY

## Animated Video Solution
https://www.youtube.com/watch?v=wq5Ie6mUxvY&ab_channel=StarLeague
~Star League ( https://starleague.us )

## Video Solution by Magic Square
https://youtu.be/-N46BeEKaCQ?t=2405

## Video Solution by Interstigation
https://youtu.be/DBqko2xATxs&t=3115

## Video Solution by WhyMath
https://youtu.be/uJklHght9ds
~savannahsolver

## Video Solution by harungurcan
https://www.youtube.com/watch?v=Ki4tPSGAapU&t=1408s
~harungurcan

## Video Solution
https://youtu.be/YFLSh4WoZrg ~please like and subscribe

## Video Solution by Dr. David
https://youtu.be/-KGQunxiVL4
### See Also
# 2022 AIME I Problem 4

## Problem

Let $w = \dfrac{\sqrt{3} + i}{2}$ and $z = \dfrac{-1 + i\sqrt{3}}{2},$ where $i = \sqrt{-1}.$ Find the number of ordered pairs $(r,s)$ of positive integers not exceeding $100$ that satisfy the equation $i \cdot w^r = z^s.$

## Solution 1
We rewrite $w$ and $z$ in polar form: \begin{align*} w &= e^{i\cdot\frac{\pi}{6}}, \\ z &= e^{i\cdot\frac{2\pi}{3}}. \end{align*} The equation $i \cdot w^r = z^s$ becomes \begin{align*} e^{i\cdot\frac{\pi}{2}} \cdot \left(e^{i\cdot\frac{\pi}{6}}\right)^r &= \left(e^{i\cdot\frac{2\pi}{3}}\right)^s \\ e^{i\left(\frac{\pi}{2}+\frac{\pi}{6}r\right)} &= e^{i\left(\frac{2\pi}{3}s\right)} \\ \frac{\pi}{2}+\frac{\pi}{6}r &= \frac{2\pi}{3}s+2\pi k \\ 3+r &= 4s+12k \\ 3+r &= 4(s+3k). \end{align*} for some integer $k.$
Since $4\leq 3+r\leq 103$ and $4\mid 3+r,$ we conclude that \begin{align*} 3+r &\in \{4,8,12,\ldots,100\}, \\ s+3k &\in \{1,2,3,\ldots,25\}. \end{align*} Note that the values for $s+3k$ and the values for $r$ have one-to-one correspondence.
We apply casework to the values for $s+3k:$
1. $s+3k\equiv0\pmod{3}$
1. $s+3k\equiv1\pmod{3}$
1. $s+3k\equiv2\pmod{3}$
There are $8$ values for $s+3k,$ so there are $8$ values for $r.$ It follows that $s\equiv0\pmod{3},$ so there are $33$ values for $s.$
There are $8\cdot33=264$ ordered pairs $(r,s)$ in this case.
There are $9$ values for $s+3k,$ so there are $9$ values for $r.$ It follows that $s\equiv1\pmod{3},$ so there are $34$ values for $s.$
There are $9\cdot34=306$ ordered pairs $(r,s)$ in this case.
There are $8$ values for $s+3k,$ so there are $8$ values for $r.$ It follows that $s\equiv2\pmod{3},$ so there are $33$ values for $s.$
There are $8\cdot33=264$ ordered pairs $(r,s)$ in this case.
Together, the answer is $264+306+264=\boxed{834}.$
~MRENTHUSIASM

## Solution 2
First we recognize that $w = \operatorname{cis}(30^{\circ})$ and $z = \operatorname{cis}(120^{\circ})$ because the cosine and sine sums of those angles give the values of $w$ and $z$ , respectively. By De Moivre's theorem, $\operatorname{cis}(\theta)^n = \operatorname{cis}(n\theta)$ . When you multiply by $i$ , we can think of that as rotating the complex number $90^{\circ}$ counterclockwise in the complex plane. Therefore, by the equation we know that $30r + 90$ and $120s$ land on the same angle.
This means that \[30r + 90 \equiv 120s \pmod{360},\] which we can simplify to \[r+3 \equiv 4s \pmod{12}.\] Notice that this means that $r$ cycles by $12$ for every value of $s$ . This is because once $r$ hits $12$ , we get an angle of $360^{\circ}$ and the angle laps onto itself again. By a similar reasoning, $s$ laps itself every $3$ times, which is much easier to count. By listing the possible values out, we get the pairs $(r,s)$ : \[\begin{array}{cccccccc} (1,1) & (5,2) & (9,3) & (13,1) & (17,2) & (21,3) & \ldots & (97,1) \\ (1,4) & (5,5) & (9,6) & (13,4) & (17,5) & (21,6) & \ldots & (97,4) \\ (1,7) & (5,8) & (9,9) & (13,7) & (17,8) & (21,9) & \ldots & (97,7) \\ [-1ex] \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ (1,100) & (5,98) & (9,99) & (13,100) & (17,98) & (21,99) & \ldots & (97,100) \end{array}\] We have $25$ columns in total: $34$ values for the first column, $33$ for the second, $33$ for the third, and then $34$ for the fourth, $33$ for the fifth, $33$ for the sixth, etc. Therefore, this cycle repeats every $3$ columns and our total sum is $(34+33+33) \cdot 8 + 34 = 100 \cdot 8 + 34 = \boxed{834}$ .
~KingRavi

## Video Solution
2022 AIME I #4
MathProblemSolvingSkills.com

## Video Solution (Mathematical Dexterity)
https://www.youtube.com/watch?v=XiEaCq5jf5s

## Video Solution
https://www.youtube.com/watch?v=qQ0TIhHuhnI
~Steven Chen (www.professorchenedu.com)

## Video Solution
https://youtu.be/MJ_M-xvwHLk?t=933
~ThePuzzlr

## Video Solution by MRENTHUSIASM (English & Chinese)
https://www.youtube.com/watch?v=1Z6GbkBFu4Q&ab_channel=MRENTHUSIASM
~MRENTHUSIASM

## Video Solution
https://youtu.be/m1vg_DfHEX4
~AMC & AIME Training
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
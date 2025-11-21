# 2007 AIME I Problem 15

## Problem

Let $ABC$ be an equilateral triangle , and let $D$ and $F$ be points on sides $BC$ and $AB$ , respectively, with $FA = 5$ and $CD = 2$ . Point $E$ lies on side $CA$ such that angle $DEF = 60^{\circ}$ . The area of triangle $DEF$ is $14\sqrt{3}$ . The two possible values of the length of side $AB$ are $p \pm q \sqrt{r}$ , where $p$ and $q$ are rational, and $r$ is an integer not divisible by the square of a prime . Find $r$ .

## Solution
Denote the length of a side of the triangle $x$ , and of $\overline{AE}$ as $y$ . The area of the entire equilateral triangle is $\frac{x^2\sqrt{3}}{4}$ . Add up the areas of the triangles using the $\frac{1}{2}ab\sin C$ formula (notice that for the three outside triangles, $\sin 60 = \frac{\sqrt{3}}{2}$ ): $\frac{x^2\sqrt{3}}{4} = \frac{\sqrt{3}}{4}(5 \cdot y + (x - 2)(x - 5) + 2(x - y)) + 14\sqrt{3}$ . This simplifies to $\frac{x^2\sqrt{3}}{4} = \frac{\sqrt{3}}{4}(5y + x^2 - 7x + 10 + 2x - 2y + 56)$ . Some terms will cancel out, leaving $y = \frac{5}{3}x - 22$ .
$\angle FEC$ is an exterior angle to $\triangle AEF$ , from which we find that $60 + \angle CED = 60 + \angle AFE$ , so $\angle CED = \angle AFE$ . Similarly, we find that $\angle EDC = \angle AEF$ . Thus, $\triangle AEF \sim \triangle CDE$ . Setting up a ratio of sides, we get that $\frac{5}{x-y} = \frac{y}{2}$ . Using the previous relationship between $x$ and $y$ , we can solve for $x$ .
$xy - y^2 = 10$
$\frac{5}{3}x^2 - 22x - \left(\frac{5}{3}x - 22\right)^2 - 10 = 0$
$\frac{5}{3}x^2 - \frac{25}{9}x^2 - 22x + 2 \cdot \frac{5 \cdot 22}{3}x - 22^2 - 10= 0$
$10x^2 - 462x + 66^2 + 90 = 0$
Use the quadratic formula , though we only need the root of the discriminant . This is $\sqrt{(7 \cdot 66)^2 - 4 \cdot 10 \cdot (66^2 + 90)} = \sqrt{49 \cdot 66^2 - 40 \cdot 66^2 - 4 \cdot 9 \cdot 100}$ $= \sqrt{9 \cdot 4 \cdot 33^2 - 9 \cdot 4 \cdot 100} = 6\sqrt{33^2 - 100}$ . The answer is $\boxed{989}$ .

## Solution 2
First of all, assume $EC=x,BD=m, ED=a, EF=b$ , then we can find $BF=m-3, AE=2+m-x$ It is not hard to find $ab*sin60^{\circ}*\frac{1}{2}=14\sqrt{3}, ab=56$ , we apply LOC on $\triangle{DEF}, \triangle{BFD}$ , getting that $(m-3)^2+m^2-m(m-3)=a^2+b^2-ab$ , leads to $a^2+b^2=m^2-3m+65$ Apply LOC on $\triangle{CED}, \triangle{AEF}$ separately, getting $4+x^2-2x=a^2; 25+(2+m-x)^2-5(2+m-x)=b^2.$ Add those terms together and use the equality $a^2+b^2=m^2-3m+65$ , we can find: $2x^2-(2m+1)x+2m-42=0$
According to basic angle chasing, $\angle{A}=\angle{C}; \angle{AFE}=\angle{CED}$ , so $\triangle{AFE}\sim \triangle{CED}$ , the ratio makes $\frac{5}{x}=\frac{2+m-x}{2}$ , getting that $x^2-(2+m)x+10=0$ Now we have two equations with $m$ , and $x$ values for both equations must be the same, so we can solve for $x$ in two equations. $x=\frac{2m+1 \pm \sqrt{4m^2+4m+1-16m+336}}{4}; x=\frac{4+2m \pm \sqrt{4m^2+16m-144}}{4}$ , then we can just use positive sign to solve, simplifies to $3+\sqrt{4m^2+16m-144}=\sqrt{4m^2-12m+337}$ , getting $m=\frac{211-3\sqrt{989}}{10}$ , since the triangle is equilateral, $AB=BC=2+m=\frac{231-3\sqrt{989}}{10}$ , and the desired answer is $\boxed{989}$
~bluesoul

## Video Solution
2007 AIME I #15
MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
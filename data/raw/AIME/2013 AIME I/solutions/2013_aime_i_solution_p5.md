# 2013 AIME I Problem 5

## Problem

The real root of the equation $8x^3 - 3x^2 - 3x - 1 = 0$ can be written in the form $\frac{\sqrt[3]a + \sqrt[3]b + 1}{c}$ , where $a$ , $b$ , and $c$ are positive integers. Find $a+b+c$ .

## Solution 1
We note that $8x^3 - 3x^2 - 3x - 1 = 9x^3 - x^3 - 3x^2 - 3x - 1 = 9x^3 - (x + 1)^3$ . Therefore, we have that $9x^3 = (x+1)^3$ , so it follows that $x\sqrt[3]{9} = x+1$ . Solving for $x$ yields $\frac{1}{\sqrt[3]{9}-1} = \frac{\sqrt[3]{81}+\sqrt[3]{9}+1}{8}$ , so the answer is $\boxed{98}$ .

## Solution 2
Let $r$ be the real root of the given polynomial . Now define the cubic polynomial $Q(x)=-x^3-3x^2-3x+8$ . Note that $1/r$ must be a root of $Q$ . However we can simplify $Q$ as $Q(x)=9-(x+1)^3$ , so we must have that $(\frac{1}{r}+1)^3=9$ . Thus $\frac{1}{r}=\sqrt[3]{9}-1$ , and $r=\frac{1}{\sqrt[3]{9}-1}$ . We can then multiply the numerator and denominator of $r$ by $\sqrt[3]{81}+\sqrt[3]{9}+1$ to rationalize the denominator, and we therefore have $r=\frac{\sqrt[3]{81}+\sqrt[3]{9}+1}{8}$ , and the answer is $\boxed{98}$ .

## Solution 3
It is clear that for the algebraic degree of $x$ to be $3$ that there exists some cubefree integer $p$ and positive integers $m,n$ such that $a = m^3p$ and $b = n^3p^2$ (it is possible that $b = n^3p$ , but then the problem wouldn't ask for both an $a$ and $b$ ). Let $f_1$ be the automorphism over $\mathbb{Q}[\sqrt[3]{a}][\omega]$ which sends $\sqrt[3]{a} \to \omega \sqrt[3]{a}$ and $f_2$ which sends $\sqrt[3]{a} \to \omega^2 \sqrt[3]{a}$ (note : $\omega$ is a cubic root of unity ).
Letting $r$ be the root, we clearly we have $r + f_1(r) + f_2(r) = \frac{3}{8}$ by Vieta's formulas. Thus it follows $c=8$ . Now, note that $\sqrt[3]{a} + \sqrt[3]{b} + 1$ is a root of $x^3 - 3x^2 - 24x - 64 = 0$ . Thus $(x-1)^3 = 27x + 63$ so $(\sqrt[3]{a} + \sqrt[3]{b})^3 = 27(\sqrt[3]{a} + \sqrt[3]{b}) + 90$ . Checking the non-cubicroot dimension part, we get $a + b = 90$ so it follows that $a + b + c = \boxed{98}$ .

## Solution 4
We have $cx-1=\sqrt[3]{a}+\sqrt[3]{b}.$ Therefore $(cx-1)^3=(\sqrt[3]{a}+\sqrt[3]{b})^3=a+b+3\sqrt[3]{ab}(\sqrt[3]{a}+\sqrt[3]{b})=a+b+3\sqrt[3]{ab}(cx-1).$ We have \[c^3x^3-3c^2x^2-(3c\sqrt[3]{ab}-3c)x-(a+b+1-3\sqrt[3]{ab})=0.\] We will find $a,b,c$ so that the equation is equivalent to the original one. Let $\dfrac{3c^2}{c^3}=\dfrac{3}{8}, \dfrac{3c\sqrt[3]{ab}-3c}{c^3}=\dfrac{3}{8}, \dfrac{a+b+1-3\sqrt[3]{ab}}{c^3}=\dfrac{1}{8}.$ Easily, $c=8, \sqrt[3]{ab}=9,$ and $a+b=90.$ So $a + b + c = 90+8=\boxed{98}$ .

## Video Solution
https://www.youtube.com/watch?v=9way8JrtD04&t=240s
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
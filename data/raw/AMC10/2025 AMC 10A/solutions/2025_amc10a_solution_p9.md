# 2025 AMC 10A Problem 9

## Problem

Let $f(x) = 100x^3 - 300x^2 + 200x$ . For how many real numbers $a$ does the graph of $y = f(x - a)$ pass through the point $(1, 25)$ ?

(A) $1$ (B) $2$ (C) $3$ (D) $4$ (E) more than $4$

1 Video Solution

- 1 Video Solution

- 2 Solution 1 2.1 Alternative Solution

- 3 Solution 2

- 4 Solution 3 (Graphing) 4.1 Somewhat cheese (not recommended) 4.2 Super Lazy Solution

- 5 Solution 4 (Discriminant)

- 6 Chinese Video Solution

- 7 Video Solution by SpreadTheMathLove

- 8 Video Solution 2 graphig approach by SpreadTheMathLove

- 9 Video Solution (In 1 Min)

- 10 Video Solution

- 11 Video Solution by Daily Dose of Math

- 12 See Also

- 2.1 Alternative Solution

- 4.1 Somewhat cheese (not recommended)

- 4.2 Super Lazy Solution

## Video Solution
https://youtu.be/l1RY_C20Q2M

## Solution 1
Substitute $1 - a$ for $x$ and set this expression equal to $25.$ The problem boils down to finding how many real roots \[100(1-a)^3 - 300(1-a)^2 + 200(1-a) = 25\] has. We further simplify this expression and create a function $f(x):$
\[f(x) = -100a^3 + 100a - 25\]
Using Descarte's Rule of Signs we get:
Sign changes for $f(x)$ (possible number of positive roots): 2
\[f(-x) = +100a^3 - 100a - 25\]
Sign changes for $f(-x)$ (possible number of negative roots): 1
Possibilities for roots:
1) $2$ positive roots, $1$ negative root
2) $0$ positive roots, $1$ negative root, $2$ imaginary roots
So which one is it? We know if the function changes sign between an interval, then a root exists in that interval. From $a = 0$ to $\frac{1}{2},$ the function changes sign because $f(0) = -25$ while $f(\frac{1}{2}) = +\frac{25}{2}$ , so a positive root exists. This eliminates the second possibility, implying that there must be $2$ positive and $1$ negative roots. So the answer is $2 + 1 = \boxed{\textbf{(C) } 3}.$
~ grogg007

## Alternative Solution
Since we are trying to find the number of roots of $-100a^3+100a-25$ (which is the same as the number of roots of $4a^3-4a+1$ because we divided by a constant, namely $-25$ ), we can sketch a graph of this function, which we will call $g(x)$ . We find that the function is strictly decreasing when $a<-1$ , $g(0)=g(1)=1$ , and the function is strictly increasing when $a>1$ . We immediately see that since $g(-1)$ is negative, there is a root between $-1$ and $0$ by the Intermediate Value Theorem. From here, we use the first derivative test as follows. Taking the derivative, we have $g'(x)=12a^2-4$ . We solve for the roots of this equation, obtaining $\pm \frac{\sqrt{3}}{3}$ . We know that at these two values, the function will either reach a local minimum or maximum if the second derivative isn't $0$ . Proceeding by the second derivative rule, we have that $g''(x)=24a$ is positive at $a=\frac{\sqrt{3}}{3}$ and negative at $a=-\frac{\sqrt{3}}{3}$ , making them local minimums and local maximums, respectively. We don't need to care about the latter case because the local maximum doesn't give any more roots besides the one we've already found. Considering the first case when $a=\frac{\sqrt{3}}{3}$ , we must find the sign of $g(a)$ . Using some approximations, we have that \[g(\frac{\sqrt{3}}{3})\] \[=\frac{4 \sqrt{3}}{9} - \frac{4 \sqrt{3}}{3} + 1\] \[\approx \frac{6.9}{9} - \frac{6.9}{3} +1\] \[= \frac{23}{30} - \frac{69}{30} + 1\] \[= -\frac{16}{30}\] \[<0.\] By the Intermediate Value Theorem again, we see that there is one root between $0$ and $\frac{\sqrt{3}}{3}$ and one root between $\frac{\sqrt{3}}{3}$ and $1$ . Thus, we have a total of $1+2=3$ roots. Therefore, the answer is $\boxed{\textbf{(C) 3}}$
~scjh999999
~minor LaTeX edits by i_am_not_suk_at_math

## Solution 2
This problem is essentially asking how many values of $x$ satisfy $f(x)=25,$ since the graph $f(x-a)$ is a shift $a$ units right from the original graph of $f(x).$ Now we just need to determine the amount of real solutions to $100x^3-300x^2+200x=25.$
Dividing all terms by 25, we get $4x^3-12x^2+8x-1=0.$ Using the rational root theorem and testing, we find no rational roots. Our next method to determine the amount of roots is graphing. Notice how when $x$ $\to$ $+\infty,$ $f(x)$ $\to$ $+\infty.$ When $x$ $\to$ $-\infty,$ $f(x)$ $\to$ $-\infty.$ Substituting $x=0$ gives us $f(x)=-1.$ Substituting $x=1$ gives us $f(x)=-1$ also. This makes us think to see if there was any sudden bump or curve in the graph, so we test the midpoint which is $1/2.$ Substituting $x=1/2,$ we get $1/2-3+4-1=1/2.$ Aha! Connecting the dots, we see there are two solutions from $0\leq x \leq 1.$ Also, $f(x)$ must continue increasing after $x>1,$ which tells us there is a third root when $x>1.$ Now we can conclude that the problem has 3 real roots, meaning that 3 values of a satisfy the problem. The answer is $\boxed {C}.$
~ eqb5000/Esteban Q.

## Solution 3 (Graphing)
We can factor $f(x)$ as $100x(x-1)(x-2)$ . We just need to check that if the local maximum between $0$ and $1$ is below or above 25. Observe that $f(1/2)>25$ , so the graph will cross the line $y=25$ 3 times, $\boxed {C}.$
~gimmeaworkingusername
### Somewhat cheese (not recommended)
Instead of plugging in a value between $0$ and $1,$ we can assume that the equation will reach a value above $25$ between those numbers. Thus, the graph crosses $y=25$ 3 times, $\boxed {C}.$
~dodobird150

## Super Lazy Solution
Instead of using numbers, we could just remember the shape of the graph given, and that it is extremely vertically dilated. The shape of the graph is(for the y-values given) basically $3$ lines, so moving these $3$ lines left and right, we can see that the graph will intersect at 3 points, so $\boxed {C}.$
~HappyLion

## Solution 4 (Discriminant)
We start by writing $f(x-a)$ \[f(x-a)=100(x-a)^3-300(x-a)^2+200(x-a)\] Then, we substitute $25$ for $f(x-a)$ , and substitute $x=1$ \[25 = 100(1-a)^3-300(1-a)^2+200(1-a)\] Now, to make this easier, we define $p=1-a$ , and find how many real values of $p$ satisfy this \[25 = 100p^3-300p^2+200p\] \[25 = 100(p^3-3p^2+2p)\] \[0.25 = p^3-3p^2+2p\] \[0= p^3-3p^2+2p-0.25\] We use the discriminant of a cubic equation, where, assuming the form $ax^3+bx^2+cx+d$ , \[\Delta=b^2c^2-4ac^3-4b^3d-27a^2d^2+18abcd\]
When $\Delta > 0$ , there are $3$ distinct real solutions, when $\Delta =0$ , there are repeated solutions (which all belong to $\mathbb{R}$ ), and when $\Delta<0$ , there is one real solution and 2 complex-conjugate solutions.
From the expression we derived, we can see that $a=1$ , $b=-3$ , $c=2$ , and $d=-0.25$
We plug this into the discriminant formula, yielding \[\Delta=(-3)^2(2)^2-4(2)^3-4(-3)^3(-0.25)-27(-0.25)^2+18(-3)(2)(-0.25)\] \[\Delta=36-32-27-1.6875+27\] \[\Delta=4-1.6875\] \[\Delta=2.3125\] Therefore, $\Delta>0$ , meaning there are three real values of $p$ that satisfy the equation. Since $p=1-a$ , we know that there also are 3 real values of $a$ satisfying the equation. Thus, \[\Delta > 0 \implies 3 \implies \boxed{C}\] ~shockfront99

## Chinese Video Solution
https://www.bilibili.com/video/BV1bj2uBxEXo/
~metrixgo

## Video Solution by SpreadTheMathLove
https://youtu.be/dAeyV60Hu5c?t=1229

## Video Solution 2 graphig approach by SpreadTheMathLove
https://www.youtube.com/watch?v=tDclC-ojfuY

## Video Solution (In 1 Min)
https://youtu.be/zvB7LuEBbww?si=OJ9H-Wkkx3WUxTU5 ~ Pi Academy

## Video Solution
https://youtu.be/gWSZeCKrOfU?si=MPPNaoCB_Bqo918z&t=1132 ~MK

## Video Solution by Daily Dose of Math
https://youtu.be/gPh9w3X3QSw?si=FhsZ3VSzFXKEO5pf&t=749 ~Thesmartgreekmathdude
### See Also
- AMC 10
- AMC 10 Problems and Solutions
- Mathematics competitions
- Mathematics competition resources
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
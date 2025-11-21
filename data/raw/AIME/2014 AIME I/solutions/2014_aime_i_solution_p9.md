# 2014 AIME I Problem 9

## Problem

Let $x_1<x_2<x_3$ be the three real roots of the equation $\sqrt{2014}x^3-4029x^2+2=0$ . Find $x_2(x_1+x_3)$ .

## Solution 1
Substituting $n$ for $2014$ , we get \[\sqrt{n}x^3 - (1+2n)x^2 + 2 = \sqrt{n}x^3 - x^2 - 2nx^2 + 2\] \[= x^2(\sqrt{n}x - 1) - 2(nx^2 - 1) = 0\] Noting that $nx^2 - 1$ factors as a difference of squares to \[(\sqrt{n}x - 1)(\sqrt{n}x+1)\] we can factor the left side as \[(\sqrt{n}x - 1)(x^2 - 2(\sqrt{n}x+1))\] This means that $\frac{1}{\sqrt{n}}$ is a root, and the other two roots are the roots of $x^2 - 2\sqrt{n}x - 2$ . Note that the constant term of the quadratic is negative, so one of the two roots is positive and the other is negative. In addition, by Vieta's Formulas, the roots sum to $2\sqrt{n}$ , so the positive root must be greater than $2\sqrt{n}$ in order to produce this sum when added to a negative value. Since $0 < \frac{1}{\sqrt{2014}} < 2\sqrt{2014}$ is clearly true, $x_2 = \frac{1}{\sqrt{2014}}$ and $x_1 + x_3 = 2\sqrt{2014}$ . Multiplying these values together, we find that $x_2(x_1+x_3) = \boxed{002}$ .

## Solution 2
From Vieta's formulae, we know that \[x_1x_2x_3 = \dfrac{-2}{\sqrt{2014}}\] \[x_1 + x_2 + x_3 = \dfrac{4029}{\sqrt{2014}}\] and \[x_1x_2 + x_2x_3 + x_1x_3 = 0\] Thus, we know that \[x_2(x_1 + x_3) = -x_1x_3\]
Now consider the polynomial with roots $x_1x_2, x_2x_3,$ and $x_1x_3$ . Expanding the polynomial \[(x - x_1x_2)(x - x_2x_3)(x - x_1x_3)\] we get the polynomial \[x^3 - (x_1x_2 + x_2x_3 + x_1x_3)x^2 + (x_1x_2x_3)(x_1 + x_2 + x_3)x - (x_1x_2x_3)^2\] Substituting the values obtained from Vieta's formulae, we find that this polynomial is \[x^3 - \dfrac{8058}{2014}x - \dfrac{4}{2014}\] We know $x_1x_3$ is a root of this polynomial, so we set it equal to 0 and simplify the resulting expression to \[1007x^3 - 4029x - 2 = 0\]
Given the problem conditions, we know there must be at least 1 integer solution, and that it can't be very large (because the $x^3$ term quickly gets much larger/smaller than the other 2). Trying out some numbers, we quickly find that $x = -2$ is a solution. Factoring it out, we get that \[1007x^3 + 4029x - 2 = (x+2)(1007x^2 - 2014x - 1)\] Since the other quadratic factor clearly does not have any integer solutions and since the AIME has only positive integer answers, we know that this must be the answer they are looking for. Thus, \[x_1x_3 = -2\] so \[-x_1x_3 = \boxed{002}\] and we're done.

## Solution 3
Observing the equation, we notice that the coefficient for the middle term $-4029$ is equal to \[-2{\sqrt{2014}}^2-1\] .
Also notice that the coefficient for the ${x^3}$ term is $\sqrt{2014}$ . Therefore, if the original expression was to be factored into a linear binomial and a quadratic trinomial, the $x$ term of the binomial would have a coefficient of $\sqrt{2014}$ . Similarly, the $x$ term of the trinomial would also have a coefficient of $\sqrt{2014}$ . The factored form of the expression would look something like the following: \[({\sqrt{2014}}x-a)(x^2-n{\sqrt{2014}}x-b)\] where ${a, b,c}$ are all positive integers (because the ${x^2}$ term of the original expression is negative, and the constant term is positive), and \[{ab=2}\]
Multiplying this expression out gives \[{{\sqrt{2014}x^3-(2014n+a)x^2+(an{\sqrt{2014}}-b{\sqrt{2014}})x+ab}}\] Equating this with the original expression gives \[{2014n+a}=-4029\] The only positive integer solutions of this expression is $(n, a)=(1, 2015)$ or $(2, 1)$ . If $(n, a)=(1, 2015)$ then setting ${an{\sqrt{2014}}-b{\sqrt{2014}}}=0$ yields ${b=2015}$ and therefore ${ab=2015^2}$ which clearly isn't equal to $2$ as the constant term. Therefore, $(n, a)=(2, 1)$ and the factored form of the expression is: \[({\sqrt{2014}}x-1)(x^2-2{\sqrt{2014}}x-2)\] Therefore, one of the three roots of the original expression is \[{x=\dfrac{1}{\sqrt{2014}}}\] Using the quadratic formula yields the other two roots as \[{x={\sqrt{2014}}+{\sqrt{2016}}}\] and \[{x={\sqrt{2014}}-{\sqrt{2016}}}\] Arranging the roots in ascending order (in the order $x_1<x_2<x_3$ ), \[{\sqrt{2014}}-{\sqrt{2016}}<\dfrac{1}{\sqrt{2014}}<{\sqrt{2014}}+{\sqrt{2016}}\] Therefore, \[x_2(x_1+x_3)=\dfrac{1}{\sqrt{2014}}{2\sqrt{2014}}=\boxed{002}\]

## Solution 4
By Vieta's, we are seeking to find $x_2(x_1+x_3)=x_1x_2+x_2x_3=-x_1x_3=\frac{2}{\sqrt{2014}x_2}$ . Substitute $n=-x_1x_3$ and $x_2=\frac{2}{\sqrt{2014}n}$ . Substituting this back into the original equation, we have $\frac{4}{1007n^3}-\frac{8058}{1007n^2}+2=0$ , so $2n^3-\frac{8058}{1007}n+\frac{4}{1007}=2n^3-\frac{8058n-4}{1007}=0$ . Hence, $8058n-4\equiv 2n-4 \equiv 0 \pmod{1007}$ , and $n\equiv 2\pmod{1007}$ . But since $n\le 999$ because it is our desired answer, the only possible value for $n$ is $\boxed{002}$ BEST PROOOFFFF Stormersyle & mathleticguyyy

## Solution 5
Let $x =\frac{y}{\sqrt{2014}}.$ The original equation simplifies to $\frac{y^3}{2014} -\frac{4029y^2}{2014}+2 = 0 \implies y^3 - 4029y^2 + 4028=0.$ Here we clearly see that $y=1$ is a root. Dividing $y-1$ from the sum we find that $(y-1)(y^2-4028y-4028)=0.$ From simple bounding we see that $y=1$ is the middle root. Therefore $x_{2}(x_{1}+x_{3}) =\frac{1}{\sqrt{2014}} \cdot\frac{4028}{\sqrt{2014}} = \boxed{002}.$

## Solution 6
$\sqrt{2014}$ occurs multiple times, so let k = $\sqrt{2014}$ .
The equation becomes $0 = kx^3 - (2k^2 + 1)x^2 + 2$ . Since we want to relate k and x, we should solve for one of them. We can't solve for x, since that would require the cubic formula, so we solve for k, and express it in terms of a quadratic, and apply the quadratic formula.
We get the roots are:
$y = \frac{1}{x}$ , and $y = \frac{x}{2} - \frac{1}{x}$ .
In the first case, $x = \frac{1}{y} = \frac{1}{\sqrt{2014}}$ .
In the second case, $x^2 - 2\sqrt{2014} - 2 = 0$ . The solutions are $\sqrt{2014} \pm \sqrt{2016}$ . The sum of these 2 solutions is $2 \sqrt{2014}$ , and $\frac{1}{\sqrt{2014}}$ is the middle solution, and thus, $(x_1 + x_3) \cdot x_2 = 2$

## Solution 7 (Estimation and Intuitive Function Analysis)
We will estimate the roots of the polynomial. (This strategy normally doesn't work on AIME #9, but playing around with a function is often good strategy for getting an intuition for the problem. In this problem, estimation happens to be a valid solution path. It isn't a proof, but given the constraint that the answer is an integer, we can be certain that our answer is correct.)
Let $p(x) = \sqrt{2014}x^3-4029x^2+2=0$ . We start by estimating $p(-1)$ , $p(0)$ , and $p(1)$ (A natural first step for function analysis.):
$p(-1)\approx -45-4029+2 \approx -4000$
$p(0) = 2$
$p(1) \approx 45-4029+2 \approx -4000$
We conclude by Intermediate Value Theorem (or just common sense), that there is a root on $(-1, 0)$ and another root on $(0, 1)$ .
We know that $p(1) < 0$ and that $\lim_{x\to\infty} p(x) = \infty$ . We conclude that the third root is on $(1, \infty)$ . Therefore, $x_1 \in (-1, 0)$ , $x_2 \in (0, 1)$ , and $x_3 \in (1, \infty)$ .
We will estimate $x_3$ . For $x > 1$ , the constant term of $p(x)$ is negligible. We simplify and get $p(x_3) \approx \sqrt{2014}x_{3}^3 - 4029x_{3}^2 = 0$ . Solving for $x_3$ (We can divide by $x_{3}^2$ because we know $x_3 \neq 0$ ), we get $x_3 \approx \frac{4029}{\sqrt{2014}} \approx 2\sqrt{2014} \approx 90$ . We can intuitively bound $x_3$ between $88$ and $92$ .
We will now estimate $x_1$ and $x_2$ . $x_1$ and $x_2$ are close to $0$ . As a result, the $\sqrt{2014}x^3$ term is negligible. We simplify and get $p(x) \approx -4029x^2 + 2 = 0$ . Solving for $x$ , we get $x \approx \pm \sqrt{\frac{2}{4029}} \approx \pm \sqrt{\frac{1}{2014.5}} \approx \pm \frac{1}{45}$ . We can intuitively bound $x_1$ between $-\frac{1}{43}$ and $-\frac{1}{47}$ . Similarly, we can intuitively bound $x_2$ between $\frac{1}{47}$ and $\frac{1}{43}$ .
We calculate that the minimum possible value of $x_2(x_1 + x_3)$ is $\frac{88-\frac{1}{43}}{47}$ and the maximum possible value is $\frac{92-\frac{1}{47}}{43}$ . The only integer that falls is this range is $\boxed{002}$ .
~numerophile

## Solution 8
Let $a=x\sqrt{2014}$ . We have $\sqrt{2014}x^3-4029x^2+2=ax^2-2a^2-x^2+2=x^2(a-1)-2(a^2-1)=x^2(a-1)-2(a-1)(a+1)=(a-1)(x^2-2a-2)=0$ , so $a=x\sqrt{2014}=1$ or $x^2-2a-2=x^2-2\sqrt{2014}x-2=0$ . As such, the solutions are at $x=\frac{1}{\sqrt{2014}}$ and $x=\frac{2\sqrt{2014}\pm\sqrt{4\cdot2014+8}}{2}$ . Note that $\frac{2\sqrt{2014}-\sqrt{4\cdot2014+8}}{2}<0<\frac{1}{\sqrt{2014}}<\sqrt{2014}<\frac{2\sqrt{2014}+\sqrt{4\cdot2014+8}}{2}$ , so $x_2(x_1+x_3)=\frac{x_1+x_3}{\sqrt{2014}}=\frac{2\sqrt{2014}}{\sqrt{2014}}=\boxed{2}$ . ( $x_1+x_3=2\sqrt{2014}$ by vietas.)
-zhoujef000

## Solution 9 (cheese)
Rewrite the polynomial as $nx^3 - (2n^2+1)x^2 + 2 = 0$ . The answer probably holds for general $n$ , so letting $n=0$ , we have $x^2+2=0$ . We'll assume that the missing root doesn't impact the final answer, so by Vietas, we have $\boxed{002}$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
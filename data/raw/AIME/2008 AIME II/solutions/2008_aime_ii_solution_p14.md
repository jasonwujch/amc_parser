# 2008 AIME II Problem 14

## Problem

Let $a$ and $b$ be positive real numbers with $a\ge b$ . Let $\rho$ be the maximum possible value of $\frac {a}{b}$ for which the system of equations \[a^2 + y^2 = b^2 + x^2 = (a - x)^2 + (b - y)^2\] has a solution in $(x,y)$ satisfying $0\le x < a$ and $0\le y < b$ . Then $\rho^2$ can be expressed as a fraction $\frac {m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m + n$ .

## Solutions

## Solution 1
Notice that the given equation implies
We have $2by \ge y^2$ , so $2ax \le a^2 \implies x \le \frac {a}{2}$ .
Then, notice $b^2 + x^2 = a^2 + y^2 \ge a^2$ , so $b^2 \ge \frac {3}{4}a^2 \implies \rho^2 \le \frac {4}{3}$ .
The solution $(a, b, x, y) = \left(1, \frac {\sqrt {3}}{2}, \frac {1}{2}, 0\right)$ satisfies the equation, so $\rho^2 = \frac {4}{3}$ , and the answer is $3 + 4 = \boxed{007}$ .

## Solution 2
Consider the points $(a,y)$ and $(x,b)$ . They form an equilateral triangle with the origin. We let the side length be $1$ , so $a = \cos{\theta}$ and $b = \sin{\left(\theta + \frac {\pi}{3}\right)}$ .
Thus $f(\theta) = \frac {a}{b} = \frac {\cos{\theta}}{\sin{\left(\theta + \frac {\pi}{3}\right)}}$ and we need to maximize this for $0 \le \theta \le \frac {\pi}{6}$ .
Taking the derivative shows that $-f'(\theta) = \frac {\cos{\frac {\pi}{3}}}{\sin^2{\left(\theta + \frac {\pi}{3}\right)}} \ge 0$ , so the maximum is at the endpoint $\theta = 0$ . We then get
Then, $\rho^2 = \frac {4}{3}$ , and the answer is $3+4=\boxed{007}$ .
(For a non-calculus way to maximize the function above:
Let us work with degrees. Let $f(x)=\frac{\cos x}{\sin(x+60)}$ . We need to maximize $f$ on $[0,30]$ .
Suppose $k$ is an upper bound of $f$ on this range; in other words, assume $f(x)\le k$ for all $x$ in this range. Then: \[\cos x\le k\sin(x+60)=k\cdot\left(\frac{\sqrt{3}}{2}\cos x+\frac{1}{2}\sin x\right)\] \[\rightarrow 0\le \left(\frac{\sqrt{3}k}{2}-1\right)\cos x+\frac{k}{2}\sin x\rightarrow 0\le (\sqrt{3}k-2)\cos x+k\sin x\] \[\rightarrow (2-\sqrt{3}k)\cos x\le k\sin x\rightarrow \frac{2-\sqrt{3}k}{k}\le \tan x,\] for all $x$ in $[0,30]$ . In particular, for $x=0$ , $\frac{2-\sqrt{3}k}{k}$ must be less than or equal to $0$ , so $k\ge \frac{2}{\sqrt{3}}$ .
The least possible upper bound of $f$ on this interval is $k=\frac{2}{\sqrt{3}}$ . This inequality must hold by the above logic, and in fact, the inequality reaches equality when $x=0$ . Thus, $f(x)$ attains a maximum of $\frac{2}{\sqrt{3}}$ on the interval.)

## Solution 3
Consider a cyclic quadrilateral $ABCD$ with $\angle B = \angle D = 90^{\circ}$ , and $AB = y, BC = a, CD = b, AD = x$ . Then \[AC^2 = a^2 + y^2 = b^2 + x^2\] From Ptolemy's Theorem , $ax + by = AC(BD)$ , so \[AC^2 = (a - x)^2 + (b - y)^2 = a^2 + y^2 + b^2 + x^2 - 2(ax + by) = 2AC^2 - 2AC*BD\] Simplifying, we have $BD = AC/2$ .
Note the circumcircle of $ABCD$ has radius $r = AC/2$ , so $BD = r$ and has an arc of $60^{\circ}$ , so $\angle C = 30^{\circ}$ . Let $\angle BDC = \theta$ .
$\frac ab = \frac{BC}{CD} = \frac{\sin \theta}{\sin(150^{\circ} - \theta)}$ , where both $\theta$ and $150^{\circ} - \theta$ are $\leq 90^{\circ}$ since triangle $BCD$ must be acute . Since $\sin$ is an increasing function over $(0, 90^{\circ})$ , $\frac{\sin \theta}{\sin(150^{\circ} - \theta)}$ is also increasing function over $(60^{\circ}, 90^{\circ})$ .
$\frac ab$ maximizes at $\theta = 90^{\circ} \Longrightarrow \frac ab$ maximizes at $\frac 2{\sqrt {3}}$ . This squared is $(\frac 2{\sqrt {3}})^2 = \frac4{3}$ , and $4 + 3 = \boxed{007}$ .
### Note:
None of the above solutions point out clearly the importance of the restriction that $a$ , $b$ , $x$ and $y$ be positive. Indeed, larger values of p are obtained when the lower vertex of the equilateral triangle in Solution 2 dips below the x-axis. Take for example $-15= \theta$ . This yields $p = (1 + \sqrt{3})/2 > 4/3$

## Solution 4
The problem is looking for an intersection in the said range between parabola $P$ : $y = \tfrac{(x-a)^2 + b^2-a^2}{2b}$ and the hyperbola $H$ : $y^2 = x^2 + b^2 - a^2$ . The vertex of $P$ is below the x-axis and it's x-coordinate is a, which is to the right of the vertex of the $H$ , which is $\sqrt{a^2 - b^2}$ . So for the intersection to exist with $x<a$ and $y \geq 0$ , $P$ needs to cross x-axis between $\sqrt{a^2 - b^2}$ , and $a$ , meaning, \[(\sqrt{a^2 - b^2}-a)^2 + b^2-a^2 \geq 0\] Divide both side by $b^2$ , \[(\sqrt{\rho^2 - 1}-\rho)^2 + 1-\rho^2 \geq 0\] which can be easily solved by moving $1-\rho^2$ to RHS and taking square roots. Final answer $\rho^2 \leq \frac{4}{3}$ $\boxed{007}$

## Solution 5
The given system is equivalent to the points $(a,y)$ and $(x,b)$ forming an equilateral triangle with the origin. WLOG let this triangle have side length $1$ , so $x=\sqrt{1-a^2}$ . The condition $x<a$ implies $(x,b)$ lies to the left of $(a,y)$ , so $(x,b)$ is the top vertex. Now we can compute (by complex numbers, or the sine angle addition identity) that $b = \frac{\sqrt{3}}{2}a + \frac{1}{2}\sqrt{1-a^2}$ , so $\frac{a}{b} = \frac{a}{\frac{\sqrt{3}}{2}a + \frac{1}{2}\sqrt{1-a^2}} = \frac{1}{\frac{\sqrt{3}}{2} + \frac{1}{2a}\sqrt{1-a^2}}$ . Minimizing this is equivalent to minimizing the denominator, which happens when $\sqrt{1-a^2} = 0$ and thus $a=1$ , resulting in $\rho = \frac{2}{\sqrt{3}}$ , so $\rho^2 = \frac{4}{3}$ and the answer is $\boxed{007}$ .
As a remark, expressing the condition that the triangle is equilateral purely algebraically instead of using trig eliminates the need for calculus or analyzing the behavior of sine.

## Solution 6 (Geometry and Trigonometry)
Notice that by Pythagorean theorem, if we take a triangle with vertices $(0,0),$ $(a,y),$ and $(x,b)$ forming an equilateral triangle. Now, take a rectangle with vertices $(0,0), (a,0), (0,b), (a,b).$ Notice that $(a,y)$ and $(x,b)$ are on the sides. Let $\alpha$ be the angle formed by the points $(0,b), (0,0), (x,b).$ Then, we have that \[\cos \alpha = \frac{b}{s},\] where $s$ is the side of the equilateral triangle. Also, we have that $30^{\circ}-\alpha$ is the angle formed by the points $(a,0), (0,0), (a,y),$ and so \[\cos (30^{\circ}-\alpha) = \frac{a}{s}.\] Thus, we have that \[\frac{a}{b} = \frac{\cos (30^{\circ}-\alpha)}{\cos \alpha}.\] We see that this expression is maximized when $\alpha$ is maximized (at least when $\alpha$ is in the interval $(0,90^{\circ}),$ which it is). Then, $\alpha \ge 30^{\circ},$ so ew have that the maximum of $\frac{a}{b}$ is \[\frac{\cos 0}{\cos 30^{\circ}} = \frac{2}{\sqrt{3}},\] and so our answer is $4+3 = 7.$

## Solution 7 (No calc/trig)
As the previous solutions pointed out, we have that the triangle with vertices $(0,0),$ $(a,y),$ and $(x,b)$ is equilateral. Then, note that that equilateral triangle is inscribed in a rectangle with vertices $(0,0),$ $(a,0),$ $(a,b),$ and $(0,b).$ Thus, our objective is to find the most "oblique" rectangle that has an equilateral triangle inscribed in it.
This is when a side of the equilateral triangle coincides with a side of the rectangle, and therefore an axis. We see this because if we rotate it so that it is no longer the case, the longer side decreases in length while the shorter side increases in length. Rotating it to coincides with the other axis, it is just the original rectangle reflected over $y=x.$ WLOG let the side length of the equilateral triangle be $1.$ Then, by our above argument, \[(a,b)=\left(1,\dfrac{\sqrt{3}}{2}\right)\] is optimal, so our answer is \[\left(\dfrac{2}{\sqrt{3}}\right)^2=\dfrac{4}{3}\implies \boxed{007}.\]

## Video Solution
2008 AIME II #14
MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
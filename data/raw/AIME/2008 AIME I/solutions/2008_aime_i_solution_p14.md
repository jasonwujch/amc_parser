# 2008 AIME I Problem 14

## Problem

Let $\overline{AB}$ be a diameter of circle $\omega$ . Extend $\overline{AB}$ through $A$ to $C$ . Point $T$ lies on $\omega$ so that line $CT$ is tangent to $\omega$ . Point $P$ is the foot of the perpendicular from $A$ to line $CT$ . Suppose $\overline{AB} = 18$ , and let $m$ denote the maximum possible length of segment $BP$ . Find $m^{2}$ .

## Solution

## Solution 1
Let $x = OC$ . Since $OT, AP \perp TC$ , it follows easily that $\triangle APC \sim \triangle OTC$ . Thus $\frac{AP}{OT} = \frac{CA}{CO} \Longrightarrow AP = \frac{9(x-9)}{x}$ . By the Law of Cosines on $\triangle BAP$ , \begin{align*}BP^2 = AB^2 + AP^2 - 2 \cdot AB \cdot AP \cdot \cos \angle BAP \end{align*} where $\cos \angle BAP = \cos (180 - \angle TOA) = - \frac{OT}{OC} = - \frac{9}{x}$ , so: \begin{align*}BP^2 &= 18^2 + \frac{9^2(x-9)^2}{x^2} + 2(18) \cdot \frac{9(x-9)}{x} \cdot \frac 9x = 405 + 729\left(\frac{2x - 27}{x^2}\right)\end{align*} Let $k = \frac{2x-27}{x^2} \Longrightarrow kx^2 - 2x + 27 = 0$ ; this is a quadratic, and its discriminant must be nonnegative: $(-2)^2 - 4(k)(27) \ge 0 \Longleftrightarrow k \le \frac{1}{27}$ . Thus, \[BP^2 \le 405 + 729 \cdot \frac{1}{27} = \boxed{432}\] Equality holds when $x = 27$ .~Shen Kislay Kai

## Solution 1.1 (Calculus)
Proceed as follows for Solution 1.
Once you approach the function $k=(2x-27)/x^2$ , find the maximum value by setting $dk/dx=0$ .
Simplifying $k$ to take the derivative, we have $2/x-27/x^2$ , so $dk/dx=-2/x^2+54/x^3$ . Setting $dk/dx=0$ , we have $2/x^2=54/x^3$ .
Solving, we obtain $x=27$ as the critical value. Hence, $k$ has the maximum value of $(2*27-27)/27^2=1/27$ . Since $BP^2=405+729k$ , the maximum value of $\overline {BP}$ occurs at $k=1/27$ , so $BP^2$ has a maximum value of $405+729/27=\fbox{432}$ .
Note: Please edit this solution if it feels inadequate. ~Shen Kislay Kai

## Solution 2
From the diagram, we see that $BQ = OT + BO \sin\theta = 9 + 9\sin\theta = 9(1 + \sin\theta)$ , and that $QP = BA\cos\theta = 18\cos\theta$ .
\begin{align*}BP^2 &= BQ^2 + QP^2 = 9^2(1 + \sin\theta)^2 + 18^2\cos^2\theta\\ &= 9^2[1 + 2\sin\theta + \sin^2\theta + 4(1 - \sin^2\theta)]\\ BP^2 &= 9^2[5 + 2\sin\theta - 3\sin^2\theta]\end{align*}
This is a quadratic equation , maximized when $\sin\theta = \frac { - 2}{ - 6} = \frac {1}{3}$ . Thus, $m^2 = 9^2[5 + \frac {2}{3} - \frac {1}{3}] = \boxed{432}$ .

## Solution 3 (Calculus Bash)
(Diagram credit goes to Solution 2)
We let $AC=x$ . From similar triangles, we have that $PC=\frac{x\sqrt{x^2+18x}}{x+9}$ (Use Pythagorean on $\triangle\omega TC$ and then using $\triangle\omega CT\sim\triangle ACP$ ). Similarly, $TP=QT=\frac{9\sqrt{x^2+18x}}{x+9}$ . Using the Pythagorean Theorem again and $\triangle CAP\sim\triangle CBQ$ , $BQ=\sqrt{(x+18)^2-(\frac{(x+18)\sqrt{x^2+18x}}{x+9})^2}$ . Using the Pythagorean Theorem $\bold{again}$ , $BP=\sqrt{(x+18)^2-(\frac{(x+18)\sqrt{x^2+18x}}{x+9})^2+(\frac{18\sqrt{x^2+18x}}{x+9})^2}$ . After a large bashful simplification, $BP=\sqrt{405+\frac{1458x-6561}{x^2+18x+81}}$ . The fraction is equivalent to $729\frac{2x-9}{(x+9)^2}$ . Taking the derivative of the fraction and solving for x, we get that $x=18$ . Plugging $x=18$ back into the expression for $BP$ yields $\sqrt{432}$ , so the answer is $(\sqrt{432})^2=\boxed{432}$ .

## Solution 4
(Diagram credit goes to Solution 2)
Let $AC=x$ . The only constraint on $x$ is that it must be greater than $0$ . Using similar triangles, we can deduce that $PA=\frac{9x}{x+9}$ . Now, apply law of cosines on $\triangle PAB$ . \[BP^2=\left(\frac{9x^2}{x+9}\right)^2+18^2-2(18)\left(\frac{9x}{x+9}\right)\cos(\angle PAB).\] We can see that $\cos(\angle PAB)=\cos(180^{\circ}-\angle PAC)=\cos(\angle PAC -90^{\circ})=-\sin(\angle PCA)$ . We can find $-\sin(\angle PCA)=-\frac{9}{x+9}$ . Plugging this into our equation, we get: \[BP^2=\left(\frac{9x^2}{x+9}\right)^2+18^2-2(18)\left(\frac{9x}{x+9}\right)\left(-\frac{9}{x+9}\right).\] Eventually, \[BP^2 = 81\left(\frac{x^2+36x}{(x+9)^2}+4\right).\] We want to maximize $\frac{x^2+36x}{(x+9)^2}$ . There are many ways to maximize this expression, discussed here: https://artofproblemsolving.com/community/c4h2292700_maximization . The maximum result of that expression is $\frac{4}{3}$ . Finally, evaluating $BP^2$ for this value $81\left(\frac{4}{3}+4\right) = \boxed{432}$ .
~superagh

## Solution 5 (Clean)
Let $h$ be the distance from $A$ to $CT$ . Observe that $h$ takes any value from $0$ to $r$ , where $r$ is the radius of the circle.
Let $Q$ be the foot of the altitude from $B$ to $CT$ . It is clear that $T$ is the midpoint of $PQ$ , and so the length $OT$ is the average of $AP$ and $BQ$ . It follows thus that $BQ = 2r - h$ .
We compute $PT = \sqrt{r^2 - (r - h)^2} = \sqrt{h(2r - h)},$ and so $BP^2 = PQ^2 + BQ^2 = 4PT^2 + BQ^2 = 4h(2r - h) + (2r-h)^2 = (2r-h)(2r + 3h)$ . This is $\frac{1}{3}(6r - 3h)(2r + 3h) \le \frac{1}{3} \cdot \left( \frac{8r}{2} \right)^2$ . Equality is attained, so thus we extract the answer of $\frac{16 \cdot 9^2}{3} = 27 \cdot 16 = \boxed{432}.$

## Solution 6 (Calculus)
(Diagram Credits to Solution 2)
We can see that $AP = \frac{9x}{x+9}$ . From the Law of Cosines, we can now find the length of BP.
$BP^2 = (\frac{9x}{x+9})^2 + 18^2 - 2(18)(\frac{9x}{x+9})(-\frac{9}{x+9})$
$BP^2 = 81(\frac{x^2}{(x+9)^2} + 4 + \frac{36x}{(x+9)^2})$
$BP^2 = 81(\frac{x^2+36x}{(x+9)^2}+4)$
From here, we see that the value we need to maximize is $\frac{x^2+36x}{(x+9)^2}$ . We shall now do some calculus. Let $f(x) = \frac{x^2+36x}{(x+9)^2}$ . We need to find the first derivative. Using the quotient rule $(\frac{u}{v})' = \frac{u'v - uv'}{v^2}$ , we can find the derivative which is:
$f'(x) = \frac{(2x+36)(x+9)^2-(x^2+36x)(2)(x+9)}{((x+9)^2)^2}$
This simplifies to
$f'(x) = \frac{-18x+324}{(x+9)^3}$
Now we find the critical point by setting $f'(x)$ to zero and solve for x.
$-18x + 324 = 0$
$-18x = -324$
$x = 18$
We now plug this value of x back into the function to find the max value of f(x)
$f(18) = \frac{18^2+36(18)}{27^2}$
$f(18) = \frac{4}{3}$
We now go back to the formula for $BP^2$ and plug in $\frac{4}{3}$ for that ugly fraction.
$BP^2 = 81(\frac{4}{3}+4)$
$BP^2 = 81(\frac{16}{3})$
$BP^2 = 432$
Thus, the value of $m^2$ (or $BP^2$ ) with the maximum value of $m$ is $\boxed{432}$ .
~ROGER8432V3

## Video Solution
2008 AIME I #14
MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
# 2015 AIME I Problem 11

## Problem

Triangle $ABC$ has positive integer side lengths with $AB=AC$ . Let $I$ be the intersection of the bisectors of $\angle B$ and $\angle C$ . Suppose $BI=8$ . Find the smallest possible perimeter of $\triangle ABC$ .

## Solution 1
Let $D$ be the midpoint of $\overline{BC}$ . Then by SAS Congruence, $\triangle ABD \cong \triangle ACD$ , so $\angle ADB = \angle ADC = 90^o$ .
Now let $BD=y$ , $AB=x$ , and $\angle IBD = \dfrac{\angle ABD}{2} = \theta$ .
Then $\mathrm{cos}{(\theta)} = \dfrac{y}{8}$
and $\mathrm{cos}{(2\theta)} = \dfrac{y}{x} = 2\mathrm{cos^2}{(\theta)} - 1 = \dfrac{y^2-32}{32}$ .
Cross-multiplying yields $32y = x(y^2-32)$ .
Since $x,y>0$ , $y^2-32$ must be positive, so $y > 5.5$ .
Additionally, since $\triangle IBD$ has hypotenuse $\overline{IB}$ of length $8$ , $BD=y < 8$ .
Therefore, given that $BC=2y$ is an integer, the only possible values for $y$ are $6$ , $6.5$ , $7$ , and $7.5$ .
However, only one of these values, $y=6$ , yields an integral value for $AB=x$ , so we conclude that $y=6$ and $x=\dfrac{32(6)}{(6)^2-32}=48$ .
Thus the perimeter of $\triangle ABC$ must be $2(x+y) = \boxed{108}$ .

## Solution 2 (No Trig)
Let $AB=x$ and the foot of the altitude from $A$ to $BC$ be point $E$ and $BE=y$ . Since ABC is isosceles, $I$ is on $AE$ . By Pythagorean Theorem, $AE=\sqrt{x^2-y^2}$ . Let $IE=a$ and $IA=b$ . By Angle Bisector theorem, $\frac{y}{a}=\frac{x}{b}$ . Also, $a+b=\sqrt{x^2-y^2}$ . Solving for $a$ , we get $a=\frac{\sqrt{x^2-y^2}}{1+\frac{x}{y}}$ . Then, using Pythagorean Theorem on $\triangle BEI$ we have $y^2+\left(\frac{\sqrt{x^2-y^2}}{1+\frac{x}{y}}\right)^2=8^2=64$ . Simplifying, we have $y^2+y^2\frac{x^2-y^2}{(x+y)^2}=64$ . Factoring out the $y^2$ , we have $y^2\left(1+\frac{x^2-y^2}{(x+y)^2}\right)=64$ . Adding 1 to the fraction and simplifying, we have $\frac{y^2x(x+y)}{(x+y)^2}=32$ . Crossing out the $x+y$ , and solving for $x$ yields $32y = x(y^2-32)$ . Then, we continue as Solution 1 does.

## Solution 3
Let $AB=x$ , call the midpoint of $BC$ point $E$ , call the point where the incircle meets $AB$ point $D$ ,
and let $BE=y$ . We are looking for the minimum value of $2(x+y)$ . $AE$ is an altitude because the triangle
is isosceles. By Pythagoras on $BEI$ , the inradius is $\sqrt{64-y^2}$ and by Pythagoras on $ABE$ , $AE$ is
$\sqrt{x^2-y^2}$ . By equal tangents, $BE=BD=y$ , so $AD=x-y$ . Since $ID$ is an inradius, $ID=IE$ and using pythagoras on $ADI$ yields $AI=$ $\sqrt{x^2-2xy+64}$ . $ADI$ is similar to $AEB$ by $AA$ , so we
can write $\frac{x-y}{\sqrt{x^2-2xy+64}}=\frac{\sqrt{x^2-y^2}}{x}$ . Simplifying, $\frac{x}{\sqrt{x^2-2xy+64}}=\sqrt{\frac{x+y}{x-y}}$ .
Squaring, subtracting 1 from both sides, and multiplying everything out, we get $yx^2-2xy^2+64y=yx^2 -32x+32y-xy^2$ , which turns into $32y=x(y^2-32)$ . Finish as in Solution 1.

## Solution 4
Angle bisectors motivate trig bash. Define angle $IBC = x$ . Foot of perpendicular from $I$ to $BC$ is point $P$ . $\overline{BC} = 2\overline{BP} = 2(8\cos(x)) = N$ , where $N$ is an integer. Thus, $\cos(x) = \frac{N}{16}$ . Via double angle, we calculate $\overline{AB}$ to be $\frac{8\cos(x)}{2\cos(x)^2 - 1} = \frac{64N}{N^2 - 128}$ . This is to be an integer. We can bound $N$ now, as $N > 11$ to avoid negative values and $N < 16$ due to triangle inequality. Testing, $N = 12$ works, giving $\overline{AB} = 48, \overline{BC} = 12$ . Our answer is $2 * 48 + 12 = \boxed{108}$ . - whatRthose

## Solution 5
Let $M$ be midpoint $BC, BM = x, AB = y, \angle IBM = \alpha.$
$BI$ is the bisector of $\angle ABM$ in $\triangle ABM.$ $BI = \frac {2 xy \cos \alpha}{x+y} = 8, \cos \alpha = \frac {x}{8} \implies \frac {x^2 y}{x+y} = 32.$ \[y = \frac {32 x} {x^2 - 32}.\] $BC = 2x$ is integer, $5.5^2 < 32 \implies x \ge 6.$ $BM < BI \implies x =\{ 6, 6.5, 7, 7.5 \}.$
If $x > 6$ then $y$ is not integer. \[x = 6 \implies y = 48 \implies 2(x+y) = \boxed{\textbf{108}}.\] vladimir.shelomovskii@gmail.com, vvsss

## Video Solution
https://youtu.be/R8kvayz7Rtw?si=hFg4yGZO4dxyxAuG
~MathProblemSolvingSkills.com
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
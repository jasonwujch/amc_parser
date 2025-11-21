# 2024 AIME I Problem 7

## Problem

Find the largest possible real part of \[(75+117i)z+\frac{96+144i}{z}\] where $z$ is a complex number with $|z|=4$ . Here $i = \sqrt{-1}$ .

## Video Solution: Cauchy's Inequality
https://www.youtube.com/watch?v=ejmrAJ9TpvM&ab_channel=MegaMathChannel MegaMath

## Video Solution By MathTutorZhengFromSG
https://youtu.be/usEtjiPw9Hc
~MathTutorZhengFromSG

## Solution 1
Let $z=a+bi$ such that $a^2+b^2=4^2=16$ . The expression becomes:
\[(75+117i)(a+bi)+\dfrac{96+144i}{a+bi}.\]
Call this complex number $w$ . We simplify this expression.
\begin{align*} w&=(75+117i)(a+bi)+\dfrac{96+144i}{a+bi} \\ &=(75a-117b)+(117a+75b)i+48\left(\dfrac{2+3i}{a+bi}\right) \\ &=(75a-117b)+(117a+75b)i+48\left(\dfrac{(2+3i)(a-bi)}{(a+bi)(a-bi)}\right) \\ &=(75a-117b)+(117a+75b)i+48\left(\dfrac{2a+3b+(3a-2b)i}{a^2+b^2}\right) \\ &=(75a-117b)+(117a+75b)i+48\left(\dfrac{2a+3b+(3a-2b)i}{16}\right) \\ &=(75a-117b)+(117a+75b)i+3\left(2a+3b+(3a-2b)i\right) \\ &=(75a-117b)+(117a+75b)i+6a+9b+(9a-6b)i \\ &=(81a-108b)+(125a+69b)i. \\ \end{align*}
We want to maximize $\text{Re}(w)=81a-108b$ . We can use elementary calculus for this, but to do so, we must put the expression in terms of one variable. Recall that $a^2+b^2=16$ ; thus, $b=\pm\sqrt{16-a^2}$ . Notice that we have a $-108b$ in the expression; to maximize the expression, we want $b$ to be negative so that $-108b$ is positive and thus contributes more to the expression. We thus let $b=-\sqrt{16-a^2}$ . Let $f(a)=81a-108b$ . We now know that $f(a)=81a+108\sqrt{16-a^2}$ , and can proceed with normal calculus.
\begin{align*} f(a)&=81a+108\sqrt{16-a^2} \\ &=27\left(3a+4\sqrt{16-a^2}\right) \\ f'(a)&=27\left(3a+4\sqrt{16-a^2}\right)' \\ &=27\left(3+4\left(\sqrt{16-a^2}\right)'\right) \\ &=27\left(3+4\left(\dfrac{-2a}{2\sqrt{16-a^2}}\right)\right) \\ &=27\left(3-4\left(\dfrac a{\sqrt{16-a^2}}\right)\right) \\ &=27\left(3-\dfrac{4a}{\sqrt{16-a^2}}\right). \\ \end{align*}
We want $f'(a)$ to be $0$ to find the maximum.
\begin{align*} 0&=27\left(3-\dfrac{4a}{\sqrt{16-a^2}}\right) \\ &=3-\dfrac{4a}{\sqrt{16-a^2}} \\ 3&=\dfrac{4a}{\sqrt{16-a^2}} \\ 4a&=3\sqrt{16-a^2} \\ 16a^2&=9\left(16-a^2\right) \\ 16a^2&=144-9a^2 \\ 25a^2&=144 \\ a^2&=\dfrac{144}{25} \\ a&=\dfrac{12}5 \\ &=2.4. \\ \end{align*}
We also find that $b=-\sqrt{16-2.4^2}=-\sqrt{16-5.76}=-\sqrt{10.24}=-3.2$ .
Thus, the expression we wanted to maximize becomes $81\cdot2.4-108(-3.2)=81\cdot2.4+108\cdot3.2=\boxed{540}$ .
~Technodoggo

## Solution 2a (Cauchy-Schwartz and vector algebra)
Simplify rectangular form as in Solution 1 until we get $\text{Re}(w)=81a-108b = 27(3a-4b)$ .
By Cauchy-Schwartz, to maximize $\text{Re}(w)$ , the vector $z=[a,b]$ ( $|z| =4$ ) is $\frac{4}{|[3,-4]|}[3,-4]$ .
We don't need to bash the arithmetic next, because the unit vector $u$ that maximizes $v \cdot u$ is $u=v/|v|$ , so $v \cdot u= v\cdot v = |v|^2/|v| = |v|$ , which here is just $\sqrt{3^2+(-4)^2} =5$ .
Combining what remains, we get answer $= 27 |z| |v| = 27(4)(5)=\boxed{540}$ .
~oinava

## Solution 2b (Simple Analytic Geometry)
Simplify rectangular form as in Solution 1 until we get $\text{Re}(w)=81x-108y = 27(3x-4y)$ .
We also know $|z|=4$ or $x^2+y^2=16$ .
By AM-GM or Cauchy-Schwartz, b = 4a/3, so
You can also prove this like so: We want to find the line $81x-108y=k$ tangent to circle $x^2+y^2=16$ , which is perpendicular to the line connecting tangent point to circle's center $(0,0)$ .
Using the formula for (perpendicular) distance from a point to a line: $\frac{|ax+by+c|}{\sqrt{a^2+b^2}}=r$ we can substitute and get $\frac{|81(0)-108(0)-k|}{\sqrt{81^2+108^2}}=4$ \begin{align*} \frac{k}{27\sqrt{3^2+4^2}}&=4 \\\frac{k}{135}&=4 \\k&=\boxed{540} \end{align*}
~BH2019MV0

## Solution 2c (Dot product)
Let $z = a + bi.$ Simplify until we get to maximizing $81a - 108b$ given $a^2 +b^2 = 16.$ We can write $81a - 108b$ as the Dot Product of two vectors: \[81a - 108b = \langle 81 , -108 \rangle \cdot \langle a, b \rangle.\] From this, we have the line $b = -\frac{108}{81}a = -\frac{4}{3}a$ and the circle $a^2 + b^2 = 16.$ We need to find their intersection $(a,b)$ such that $a$ and $b$ are maximized. The line intersects the circle at two points, but to maximize $81a - 108b$ we want $b$ to be negative and $a$ to be positive. So the point that works has coordinates $a = 2.4$ and $b = -3.2$ . We get $81\cdot 2.4 + 108 \cdot 3.2 = \boxed{540}.$
~ grogg007

## Solution 3
Follow Solution 1 to get $81a-108b$ . We can let $a=4\cos\theta$ and $b=4\sin\theta$ as $|z|=4$ , and thus we have $324\cos\theta-432\sin\theta$ . Furthermore, we can ignore the negative sign in front of the second term as we are dealing with sine and cosine, so we finally wish to maximize $324\cos\theta+432\sin\theta$ for obviously positive $\cos\theta$ and $\sin\theta$ .
Using the previous fact, we can use the Cauchy-Schwarz Inequality to calculate the maximum. By the inequality, we have:
$(324^2+432^2)(\cos^2\theta+\sin^2\theta)\ge(324\cos\theta+432\sin\theta)^2$
$540^2\cdot1\ge(324\cos\theta+432\sin\theta)^2$
$\boxed{540}\ge324\cos\theta+432\sin\theta$
~eevee9406

## Solution 4 (Simple Quadratic Discriminant)
Similar to the solutions above, we find that $Re((75+117i)z+\frac{96+144i}{z})=81a-108b=27(3a-4b)$ , where $z=a+bi$ . To maximize this expression, we must maximize $3a-4b$ . Let this value be $x$ . Solving for $a$ yields $a=\frac{x+4b}{3}$ . From the given information we also know that $a^2+b^2=16$ . Substituting $a$ in terms of $x$ and $b$ gives us $\frac{x^2+8bx+16b^2}{9}+b^2=16$ . Combining fractions, multiplying, and rearranging, gives $25b^2+8xb+(x^2-144)=0$ . This is useful because we want the maximum value of $x$ such that this quadratic has real roots which is easy to find using the discriminant. For the roots to be real, $(8x)^2-4(25)(x^2-144) \ge 0$ . Now all that is left to do is to solve this inequality. Simplifying this expression, we get $-36x^2+14400 \ge 0$ which means $x^2 \le 400$ and $x \le 20$ . Therefore the maximum value of $x$ is $20$ and $27 \cdot 20 = \boxed{540}$
~vsinghminhas

## Solution 5 ("Completing the Triangle")
First, recognize the relationship between the reciprocal of a complex number $z$ with its conjugate $\overline{z}$ , namely:
\[\frac{1}{z} \cdot \frac{\overline{z}}{\overline{z}} = \frac{\overline{z}}{|z|^2} = \frac{\overline{z}}{16}\]
Then, let $z = 4(\cos\theta + i\sin\theta)$ and $\overline{z} = 4(\cos\theta - i\sin\theta)$ .
\begin{align*} Re \left ((75+117i)z+\frac{96+144i}{z} \right) &= Re\left ( (75+117i)z + (6+9i)\overline{z} \right ) \\ &= 4 \cdot Re\left ( (75+117i)(\cos\theta + i\sin\theta) + (6+9i)(\cos\theta - i\sin\theta) \right ) \\ &= 4 \cdot (75\cos\theta - 117\sin\theta + 6\cos\theta + 9\sin\theta) \\ &= 4 \cdot (81\cos\theta - 108\sin\theta) \\ &= 4\cdot 27 \cdot (3\cos\theta - 4\sin\theta) \end{align*}
Now, recognizing the 3 and 4 coefficients hinting at a 3-4-5 right triangle, we "complete the triangle" by rewriting our desired answer in terms of an angle of that triangle $\phi$ where $\cos\phi = \frac{3}{5}$ and $\sin\phi = \frac{4}{5}$
\begin{align*} 4\cdot 27 \cdot(3\cos\theta - 4\sin\theta) &= 4\cdot 27 \cdot 5 \cdot (\frac{3}{5}\cos\theta - \frac{4}{5}\sin\theta) \\ &= 540 \cdot (\cos\phi\cos\theta - \sin\phi\sin\theta) \\ &= 540 \cos(\theta + \phi) \end{align*}
Since the simple trig ratio is bounded above by 1, our answer is $\boxed{540}$
~ Cocoa @ https://www.corgillogical.com/ (yes i am a corgi that does math)

## Solution 6 (Cauchy-Schwarz Inequality ) (Fastest)
Follow as solution 1 would to obtain $81a + 108\sqrt{16-a^2}.$
By the Cauchy-Schwarz Inequality, we have
\[(a^2 + (\sqrt{16-a^2})^2)(81^2 + 108^2) \geq (81a + 108\sqrt{16-a^2})^2,\]
so
\[4^2 \cdot 9^2 \cdot 15^2 \geq (81a + 108\sqrt{16-a^2})^2\]
and we obtain that $81a + 108\sqrt{16-a^2} \leq 4 \cdot 9 \cdot 15 = \boxed{540}.$
- spectraldragon8

## Solution 7 (Geometry)
Follow solution 2 to get that we want to find the line $81a-108b=k$ tangent to circle $a^2+b^2=16$ . The line turns into $a=\frac{k}{81}+\frac{4b}{3}$ Connect the center of the circle to the tangency point and the y-intercept of the line. Let the tangency point be $A$ , the y-intercept be $C$ , and the center be $B$ . Drop the perpendicular from $A$ to $BC$ and call it $D$ . Let $AD=3x$ , $DC=4x$ . Then, $BD=\sqrt{AB^2-AD^2}=\sqrt{16-9x^2}$ . By similar triangles, get that $\frac{BD}{AD}=\frac{AD}{DC}$ , so $\frac{\sqrt{16-9x^2}}{3x}=\frac{3x}{4x}$ . Solve this to get that $x=\frac{16}{15}$ , so $BC=\frac{20}{3}$ and $\frac{k}{81}=\frac{20}{3}$ , so $k=\boxed{540}$ ~ryanbear

## Solution 8 (Euler's Formula and Trig Optimization)
Because $|z|=4$ , we can let $z=4e^{i\theta}$ . Then, substituting $i=e^{\frac{i\pi}{2}}$ , we get that the complex number is
\begin{align*} w&=4e^{i\theta}(75+117e^{\frac{i\pi}{2}})+\dfrac{1}{4}e^{-i\theta}(96+144e^{\frac{i\pi}{2}})\\ &=300e^{i\theta}+468e^{i(\frac{\pi}{2}+\theta)}+24e^{-i\theta}+36e^{i(\frac{\pi}{2}-\theta)}\\ \end{align*}
We know that the $\text{Re}(e^{i\alpha})=\cos(\alpha)$ from Euler's formula, so applying this and then applying trig identities yields
\begin{align*} \text{Re}(w)&=300\cos{(\theta)}+468\cos{(\dfrac{\pi}{2}+\theta)}+24\cos{(-\theta)}+36\cos{(\dfrac{\pi}{2}-\theta)}\\ &=300\cos{(\theta)}-468sin{(\theta)}+24\cos{(\theta)}+36\sin{(\theta)}\\ &=324\cos{(\theta)}-432\sin{(\theta)}\\ \implies \dfrac{1}{108}\text{Re}(w)&=3\cos{(\theta)}-4\sin{(\theta)}\\ \end{align*}
We can see that the right-hand side looks an awful lot like the sum of angles formula for cosine, but 3 and 4 don't satisfy the pythagorean identity. To make them do so, we can divide everything by $\sqrt{3^2+4^2}=5$ and set $\cos{(\alpha)}::=\frac{3}{5}$ and $\sin{(\alpha)}::=\frac{4}{5}$ . Now we have that \[\dfrac{1}{540}\text{Re}(w)=\cos{(\theta+\alpha)}\] Obviously the maximum value of the right hand side is 1, so the maximum value of the real part is $\boxed{540}$ .
~Mooshiros

## Solution 9 (Calc semi-bash)
Let $c$ denote value of the above expression such that $\mathsf{Re} (c)$ is maximized. We write $z=4e^{i\theta}$ and multiply the second term in the expression by $\overline{z} = 4e^{-i\theta},$ turning the expression into \[4e^{i\theta}(75+117i) + \frac{(96 + 144i)\cdot 4e^{-i\theta}}{4e^{i\theta}\cdot 4e^{-i\theta}} = 300e^{i\theta} + 468ie^{i\theta} + (24+ 36i)e^{-i\theta}.\] Now, we write $e^{i\theta} = \cos\theta + i\sin\theta$ . Since $\cos$ is even and $\sin$ is odd, \begin{align*} &300(\cos\theta + i\sin\theta) +468i + (24+36i)(\cos\theta -i\sin\theta) \\ \iff & \mathsf{Re}(c) = 324\cos\theta -468\sin\theta \end{align*} We want to maximize this expression, so we take its derivative and set it equal to $0$ (and quickly check the second derivative for inflection points): \begin{align*} &\mathsf{Re}(c) = 108\left(3\cos\theta - 4\sin\theta\right)\\ \frac{d}{d\theta} &\mathsf{Re}(c) = -324\sin\theta -468\cos\theta = 0, \end{align*} so $\tan\theta = -\dfrac{468}{324} = -\dfrac{4}{3},$ which is reminiscent of a $3-4-5$ right triangle in the fourth quadrant (side lengths of $3, -4, 5$ ). Since $\tan\theta = -\frac{4}{3},$ we quickly see that $\sin\theta = -\dfrac{4}{5}$ and $\cos\theta = \dfrac{3}{5}.$ Therefore, \begin{align*} \mathsf{Re}(c) &= 108\left(3\cos\theta - 4\sin\theta \right) = 108\left(\frac{9}{5} + \frac{16}{5} \right) = 108\cdot 5 = \boxed{\textbf{(540)}} \end{align*}
-Benedict T (countmath1)

## Solution 10 (Lagrange multipliers)
With $z = a + bi$ such that $a^2 + b^2 = 16,$ we have \begin{align*} (75 +117i)(a + bi) + \frac{48}{a + bi} (2 + 3i) &= 75a + 75bi + 117ai - 117b + \frac{48}{a + bi}(2 + 3i) \\ &= 75a - 117b + (117a + 75b)i + 48 (2 + 3i) \cdot \frac{a - bi}{16} \\ &= 75a - 117b + (117a + 75b)i + 3 (2 + 3i)(a - bi) \end{align*} where we use $z^{-1} = \frac{\bar z}{|z|^2}.$ With $3 (2 + 3i)(a - bi) = 3 [2a - 2bi + 3ai + 3b] = 6a +9b +9ai-6bi,$ the expression becomes $81a-108b+ (126a + 69b)i$ and we would like to maximize $81a - 108b = 9(9a - 12b) = 27(3a - 4b)$ with $a^2 + b^2 = 16.$ With $f(a, b) = 3a - 4b$ and $g(a, b) = a^2 + b^2 = 16,$ we have \begin{align*} 3 = 2\lambda a, \quad -4 = 2\lambda b \implies -\frac{3}{4} = \frac ab \implies -3b = 4a \implies b = -\frac 43 a\end{align*} so \[a^2 + \frac{16}{9}a^2 = \frac{25}{9}a^2 = 16 \implies \frac{5}{3}a = 4 \implies a = \frac {12}5, b = -\frac{16}{5}\] and we have $3a - 4b = \frac{36}{5} + \frac{64}{5} = 20,$ so the maximum is $27 \cdot 20 = \boxed{540}.$ -centslordm

## Solution 11 (basically Lagrange but easier-ish)
Proceeding as with Solution 10, we aim to maximize $27(3a-4b)$ under the constraint $a^2+b^2-16=0$ . It is a well-known result of Lagrange multipliers that a linear function is maximized under a circle when the values of the variables are proportional to their coefficients; that is, in our case, $a=3x$ and $b=-4x$ . (Technically $a=27\cdot3x$ and $b=27(-4)x$ , but it's easier to use $a=3x$ and $b=-4x$ .)
Then, $(3x)^2+(-4x)^2=25x^2=16$ , so $x=\dfrac45$ and we have $a=\dfrac{12}5$ and $b=-\dfrac{16}5$ . This yields
\[27\left(3\left(\dfrac{12}5\right)-4\left(-\dfrac{16}5\right)\right)=27\left(\dfrac{36}5+\dfrac{64}5\right)=27\cdot\dfrac{100}5=\boxed{540}~.\]
QED. $\Box$
~Technodoggo

## Solution 12 (Wave function)
Note that we can scale down the expression by a factor of $3$ , namely, we compute the maximum possible real part of ${25+39i}z+{32+48i\over z}$ for $|z|=4$ and multiply this result by 3. Write $z=4(\cos t+i\sin t)$ we have \begin{align}(25+39i)z+{32+48i\over z}\\=4(25+39i)(\cos t+i\sin t)+{32+48i\over 4(\cos t+i\sin t)\\}=(100+156i)(\cos t+i\sin t)+(8+12i)(\cos t-i\sin t)\end{align}
The real part of $(100+156i)(\cos t+i\sin t)+(8+12i)(\cos t-i\sin t)$ is then \[108\cos t-144\sin t=36(3\cos t-4\sin t)\]
The function $3\cos t-4\sin t$ oscillates with amplitude $5$ , so the maximum value of the scaled-down expression is $36\cdot 5=180$ . Hence, our requested answer is $180\cdot 3=\boxed{540}$ .

## Video Solution by MOP 2024
https://www.youtube.com/watch?v=nH7dUh0HghA
~r00tsOfUnity

## Video Solution by OmegaLearn.org
https://youtu.be/fErzDCu_utY

## Video Solution
https://youtu.be/fC6CPlQIRB8
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
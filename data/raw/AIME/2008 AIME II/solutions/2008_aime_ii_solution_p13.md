# 2008 AIME II Problem 13

## Problem

A regular hexagon with center at the origin in the complex plane has opposite pairs of sides one unit apart. One pair of sides is parallel to the imaginary axis. Let $R$ be the region outside the hexagon, and let $S = \left\lbrace\frac{1}{z}|z \in R\right\rbrace$ . Then the area of $S$ has the form $a\pi + \sqrt{b}$ , where $a$ and $b$ are positive integers. Find $a + b$ .

## Solution 1
If you're familiar with inversion, you'll see that the problem's basically asking you to invert the hexagon with respect to the unit circle in the Cartesian Plane using the Inversion Distance Formula. This works because the point in the Cartesian Plane's complex plane equivalent switches places with its conjugate but we can do that in the Cartesian plane too (just reflect a point in the Cartesian plane over the x-axis)! If you're familiar with inversion you can go plot the inverted figure's Cartesian Plane Equivalent. Then simply continue on with the figure shown in the below solution.

## Solution 2
If a point $z = r\text{cis}\,\theta$ is in $R$ , then the point $\frac{1}{z} = \frac{1}{r} \text{cis}\, \left(-\theta\right)$ is in $S$ (where cis denotes $\text{cis}\, \theta = \cos \theta + i \sin \theta$ ). Since $R$ is symmetric every $60^{\circ}$ about the origin, it suffices to consider the area of the result of the transformation when $-30 \le \theta \le 30$ , and then to multiply by $6$ to account for the entire area.
We note that if the region $S_2 = \left\lbrace\frac{1}{z}|z \in R_2\right\rbrace$ , where $R_2$ is the region (in green below) outside the circle of radius $1/\sqrt{3}$ centered at the origin, then $S_2$ is simply the region inside a circle of radius $\sqrt{3}$ centered at the origin. It now suffices to find what happens to the mapping of the region $R-R_2$ (in blue below).
The equation of the hexagon side in that region is $x = r \cos \theta = \frac{1}{2}$ , which is transformed to $\frac{1}{r} \cos (-\theta) = \frac{1}{r} \cos \theta =$ 2 . Let $r\text{cis}\,\theta = a+bi$ where $a,b \in \mathbb{R}$ ; then $r = \sqrt{a^2 + b^2}, \cos \theta = \frac{a}{\sqrt{a^2 + b^2}}$ , so the equation becomes $a^2 - 2a + b^2 = 0 \Longrightarrow (a-1)^2 + b^2 = 1$ . Hence the side is sent to an arc of the unit circle centered at $(1,0)$ , after considering the restriction that the side of the hexagon is a segment of length $1/\sqrt{3}$ .
Including $S_2$ , we find that $S$ is the union of six unit circles centered at $\text{cis}\, \frac{k\pi}{6}$ , $k = 0,1,2,3,4,5$ , as shown below.
The area of the regular hexagon is $6 \cdot \left( \frac{\left(\sqrt{3}\right)^2 \sqrt{3}}{4} \right) = \frac{9}{2}\sqrt{3}$ . The total area of the six $120^{\circ}$ sectors is $6\left(\frac{1}{3}\pi - \frac{1}{2} \cdot \frac{1}{2} \cdot \sqrt{3}\right) = 2\pi - \frac{3}{2}\sqrt{3}$ . Their sum is $2\pi + \sqrt{27}$ , and $a+b = \boxed{029}$ . - Th3Numb3rThr33

## Solution 3 (Calculus)
We can describe the line parallel to the imaginary axis $x=\frac{1}{2}$ using polar coordinates as $r(\theta)=\dfrac{1}{2\cos{\theta}},$
which rearranges to $z=\left(\dfrac{1}{2\cos{\theta}}\right)(cis{\theta})\implies \frac{1}{z}=2\cos{\theta}cis(-\theta).$
Denote the area of $S$ as $[S].$ Now, dividing the hexagon to 12 equal parts, we have the following integral:
$[S] = 12\int_{0}^{\frac{\pi}{6}}\frac{1}{2}r^2 d\theta = 12\int_{0}^{\frac{\pi}{6}}\frac{1}{2}(2\cos\theta)^2 d\theta.$
Thankfully, this is a routine computation:
$[S] = 12\int_{0}^{\frac{\pi}{6}}2(\cos\theta)^2 d\theta = 12\int_{0}^{\frac{\pi}{6}}(\cos{2\theta}+1)d\theta$
$[S] = 12\int_{0}^{\frac{\pi}{6}}(\cos{2\theta}+1)d\theta = 12\left[\frac{1}{2}\sin{2\theta}+\theta\right]_0^{\frac{\pi}{6}}=12\left(\frac{\sqrt{3}}{4}+\frac{\pi}{6}\right)=2\pi+3\sqrt{3}=2\pi + \sqrt{27}$
$a+b = \boxed{029}$ .

## Video Solution
2008 AIME II #13
MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
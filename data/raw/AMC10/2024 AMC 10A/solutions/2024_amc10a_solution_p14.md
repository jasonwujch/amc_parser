# 2024 AMC 10A Problem 14

## Problem

One side of an equilateral triangle of height $24$ lies on line $\ell$ . A circle of radius $12$ is tangent to line $\ l$ and is externally tangent to the triangle. The area of the region exterior to the triangle and the circle and bounded by the triangle, the circle, and line $\ell$ can be written as $a \sqrt{b} - c \pi$ , where $a$ , $b$ , and $c$ are positive integers and $b$ is not divisible by the square of any prime. What is $a + b + c$ ?

$\textbf{(A)}~72\qquad\textbf{(B)}~73\qquad\textbf{(C)}~74\qquad\textbf{(D)}~75\qquad\textbf{(E)}~76$

### Diagram

[asy] /* Made by MRENTHUSIASM */ size(250); pair A, B, C; path p1, p2, p3; p1 = scale(16)*polygon(3); p2 = Circle((12*sqrt(3),4),12); A = intersectionpoint(p1,p2); B = (8*sqrt(3),-8); C = (12*sqrt(3),-8); Label L1 = Label("$24$", align=(0,0), position=MidPoint, filltype=Fill(0,3,white)); fill(A--Arc((12*sqrt(3),4),A,C)--B--cycle,yellow); draw(p1^^p2); draw((8*sqrt(3),-8)--(22+8*sqrt(3),-8)); draw((-18,-8)--(-18,16), L=L1, arrow=Arrows(),bar=Bars(15)); dot((12*sqrt(3),4),linewidth(4)); draw((12*sqrt(3),4)--(12+12*sqrt(3),4)); label("$12$",(6+12*sqrt(3),4),1.5S); dot(A^^B^^C,linewidth(4)); [/asy]

~MRENTHUSIASM

## Solution 1
Call the bottom vertices of the triangle $B$ and $C$ (the one closer to the circle is $C$ ) and the top vertex $A$ . The tangency point between the circle and the side of the triangle is $D$ , and the tangency point on line $\ell$ $E$ , and the center of the circle is $O$ .
Draw radii to the tangency points, the arc is $60$ degrees because $\angle ACB$ is $60$ , and since $\angle DCE$ is supplementary, it's $120^{\circ}$ .(Using Angle of Intersecting Secants Theorem) The sum of the angles in a quadrilateral is $360$ , which means $\angle DOE$ is $60^{\circ}$
Triangle $ODC$ is $30$ - $60$ - $90$ triangle so CD is $4\sqrt{3}$ . Since we have $2$ congruent triangles ( $\triangle ODC$ and $\triangle OEC$ ), the combined area of both is $48\sqrt{3}$ . The area of the arc is $144 \cdot \frac{60}{360} \cdot \pi$ which is $24\pi$ , so the area of the region is $48\sqrt{3}-24\pi$
$a+b+c$ is $48+3+24$ which is $\boxed{\textbf{(D)}~75}$
~ASPALAPATI75 ~andy_liu766 (latex)
edits by KR
### Note
There were two possible configurations from this problem; the one described in the solution above and the configuration in which the circle is tangent to the bottom of line $\ell$ and the base of the equilateral triangle. However, since the area in this configuration is simply $0,$ we can infer that the problem is talking about the configuration in Solution 1.
~dbnl

## Solution 2 (Strategic Triangles)
For context, we want to find the area of the quadrilateral $BDCE$ and subtract the area of circular sector $BDE$ .
We are given that triangle $AMC$ is equilateral with height 24.
Through $30-60-90$ triangles, we see that length \[MF = \frac{24}{\sqrt{3}} = 8\sqrt{3}\] Therefore the side length of $AMC$ is simply $16\sqrt{3}$ .
We now pay attention to the circle. Notice how because $AMC$ is equilateral, $\angle DCE$ is $120^\circ$ .
Notice how arc $DE$ is inscribed in both $\angle DCE$ and $\angle DBE$ , therefore angles $\angle DCE$ and $\angle DBE$ are supplementary, and angle $DBE = 180^\circ - 120^\circ = 60^\circ$ .
We have that $BD = BE = 12$ . we see that $\angle BDE = \angle BED = x^\circ$ . We have that $\angle DBE = 60^\circ$ . Therefore, \[2x + 60^\circ = 180^\circ\] \[2x=120^\circ\] \[x=60^\circ\] Therefore, triangle $BDE$ is a equilateral triangle with side length 12.
Additionally, the area of sector BDE is $\frac{1}{6} \cdot (12)^2 \cdot \pi$ , or $24\pi$ .
Because $BD=BE$ , $\angle DCE + \angle DBE$ , $\angle BDC = \angle BEC = 90^\circ$ (radius-chord theorem), and $\angle BDC + \angle BEC = 180^\circ$ , quadrilateral $BDCE$ is a kite. The area of a kite is simply the diagonals $d_1$ and $d_2$ multiplied together and divided by 2.
In this case our diagonals are DE and CB. We already know DE = 12, but to find CB, we construct a triangle $ABC$ , with $AC = 16\sqrt{3}$ The diagonals of a kite bisect their respective angles. Therefore, $\angle ACB = \frac{120^\circ}{2} = 60^\circ$ .
Then, triangles $ABC$ and $BDC$ are similar through a common angle and common side (with the angle of course in-between the side).
Applying the same logic to triangle $AFC$ , one can see that quadrilateral AFCB is also a kite that is similar to kite BDCE, and therefore $\angle ABC = 90^\circ$ .
Through $30-60-90$ triangles, $BC = \frac{1}{2}AC$ , or $8\sqrt{3}$ .
The area of kite BCDE is $[BCDE] = \frac{8\sqrt{3} \cdot 12}{2}$ , or $48\sqrt{3}$ .
We need $[BCDE] - [BDE]$ , or $48\sqrt{3} - 24\pi$ .
This is in the form $a\sqrt{b} - c\pi$ , with $a=48$ , $b=3$ , and $c=24$ .
We need $a+b+c$ , which is $48+3+24 =$ $\boxed{\textbf{(D)}75}$
~Pinotation
~Diagram by Pinotation

## Solution 3 (Quick Guess)
Since this problem involves equilateral triangles, the only possible number under the square root is $3$ . Now subtracting all of the answer choices by $3$ , we get: \[\textbf{(A)}~72-3=69\qquad\textbf{(B)}~73-3=70\qquad\textbf{(C)}~74-3=71\qquad\textbf{(D)}~75-3=72\qquad\textbf{(E)}~76-3=73\]
Due to the even parity of the problem, we can safely assume that the answer is either $B$ or $D$ , but as $D$ is a multiple of $12$ and $24$ , we get the answer of $\boxed{\textbf{(D)}~75}$ .
~megaboy6679

## Solution 4
(pardon the diagrams :D)
say the area we want to find is x.
since the equilateral triangle has an internal angle of 60, the exterior angle formed by the triangle and the line is 120. simplifying the diagram you will get:
make three of these so that each circle is tangent to the other 2 circles
Since they are 3 congruent triangles, you can make an equilateral triangle using their radius(12), with each vertex at the center of each circle. This will make an equilateral triangle of side length 24. if you look now, the area within the equilateral triangle consists of 3 $60/360$ of a circle, and 3 of x.
we first find the area of the triangle, which is $24 * 12\sqrt{3}$ , we then find the area of $60/360$ of a circle, which is $60/360 * 12^2\pi$ , we subtract $24 * 12\sqrt{3}$ by $60/360 * 12^2\pi$ , and divide by 3, yielding the area of x.
_________________________________________ = $48\sqrt{3}-24\pi$
$a+b+c$ is $48+3+24$ which is $\boxed{\textbf{(D)}~75}$
~Yiguo Zhang ~Minor edit by MathCrafter314

## Solution 5 (oh no)
Setting up the problem graphically:
Define the parametric function of the circle \(r(\theta)\), centered at \((0,12)\) with radius \(12\), as: \[r(\theta) \;=\; \bigl(12\cos(\theta),\,12\sin(\theta) + 12\bigr).\]
The line \(\ell\) is taken to be the \(x\)-axis, so \(y = 0\). The circle is tangent to \(\ell\) at \((0,0)\).
We only care about the side of the triangle that is also tangent to the circle; call this line \(f(x)\). Since the triangle is equilateral of height 24, one vertex is at \((0,24)\) (directly above the tangent point), but for now we focus on the particular side tangent to the circle.
Because we expect that line to make a \(330^\circ\) angle with the positive \(x\)-axis (or a slope of \(-\sqrt{3}\)), let \[f(x) \;=\; -\sqrt{3}\,x \;+\; c.\]
We also know the perpendicular distance from the circle’s center \((0,12)\) to \(f(x)\) must be \(12\), because the circle of radius \(12\) is externally tangent to that line. The distance from a point \(\bigl(x_0,y_0\bigr)\) to a line \(Ax + By + C = 0\) is:
\[\frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}.\]
Here, \(f(x) = -\sqrt{3}\,x + c\) can be rewritten as \(\sqrt{3}\,x + y - c = 0.\) Plugging in \((x_0,y_0)=(0,12)\) and setting the distance to 12 yields:
\[\frac{|\sqrt{3}\cdot 0 \;+\; 12 \;-\; c|}{\sqrt{(\sqrt{3})^2 + 1^2}}\;=\;12.\]
Solving this and noting that \(f(x)\) has a negative \(y\)-intercept gives:
\[f(x) \;=\; -\sqrt{3}\,x \;-\; 12.\]
Next, we find the point at which \(r(\theta)\) intersects \(f(x)\). Substituting \(r(\theta) \;=\; (12\cos(\theta), \,12\sin(\theta) + 12)\) into \(f(x) = -\sqrt{3}\,x - 12,\) we set:
\[12\sin(\theta) + 12 \;=\; -\sqrt{3}\,\bigl(12\cos(\theta)\bigr) - 12.\]
One helpful approach is to note that a line perpendicular to \(f(x)\) and passing through \((0,12)\) has slope \(1/\sqrt{3}\), so that line is \(g(x) = \frac{x}{\sqrt{3}} + 12.\) Intersecting \(g(x)\) with \(f(x)\) gives:
\[\frac{x}{\sqrt{3}} + 12 \;=\; -\sqrt{3}\,x - 12,\]
which solves to \(x = -6\sqrt{3}\). Then \(y = 6.\) So the intersection point of the circle and the line is \(\bigl(-6\sqrt{3},\,6\bigr)\).
To find the corresponding \(\theta\), use: \[12\cos(\theta) = -6\sqrt{3}, \quad12\sin(\theta) + 12 = 6.\]
From the first, \(\cos(\theta) = -\sqrt{3}/2\). This corresponds to \(\theta = 5\pi/6\) or \(7\pi/6.\) Checking the \(y\)-coordinate shows \(\theta = 7\pi/6\) indeed yields \(\sin(7\pi/6) = -1/2\), so \(12\sin(7\pi/6) + 12 = 6.\)
The circle also meets \(\ell\) (the \(x\)-axis) at \((0,0)\). In polar terms, that is \(\theta = 3\pi/2\). We want the area under the circle’s parametric curve from \(\theta=7\pi/6\) to \(\theta=3\pi/2.\)
Parametrically, the area under \(y(\theta)\) from \(\theta_1\) to \(\theta_2\) can be found via:
\[\int_{\theta_1}^{\theta_2} y(\theta)\,x'(\theta)\,d\theta.\]
Here \(x(\theta) = 12\cos(\theta)\), so \(x'(\theta) = -12\sin(\theta)\). Hence the area under the circle from \(\theta = 7\pi/6\) to \(\theta = 3\pi/2\) is:
\[\int_{7\pi/6}^{3\pi/2} \bigl(12\sin(\theta) + 12\bigr) \,\bigl(-12\sin(\theta)\bigr)\,d\theta.\]
This simplifies (pulling out constants) to:
\[-12 \int_{7\pi/6}^{3\pi/2}\bigl(\sin^2(\theta) + \sin(\theta)\bigr)\, d\theta\;=\;-12 \left[\int_{7\pi/6}^{3\pi/2} \sin^2(\theta)\,d\theta\;+\;\int_{7\pi/6}^{3\pi/2} \sin(\theta)\,d\theta\right].\]
Evaluating these integrals yields:
\[54\sqrt{3} \;-\; 24\pi.\]
Next, find where \(f(x)=0\):
\[-\sqrt{3}\,x \;-\; 12 = 0\quad\Longrightarrow\quad x = -\frac{12}{\sqrt{3}} \;=\; -4\sqrt{3}.\]
However, we also need the relevant intersection interval for the region. The line and the circle intersect at \(x=-6\sqrt{3}\). So the area under \(f(x)\) from \(x=-6\sqrt{3}\) to \(x=-4\sqrt{3}\) is:
\[\int_{x=-6\sqrt{3}}^{-4\sqrt{3}} \bigl(-\sqrt{3}\,x - 12\bigr)\,dx.\]
Carrying out that integral (or carefully checking the geometry) gives \(6\sqrt{3}.\)
Subtracting this triangular “cap” (\(6\sqrt{3}\)) from the circle’s sector area (\(54\sqrt{3}-24\pi\)) gives the final region of interest:
\[\bigl(54\sqrt{3} - 24\pi\bigr) - 6\sqrt{3}\;=\;48\sqrt{3} - 24\pi.\]
Hence the area can be written as
\[a\sqrt{b} \;-\; c\pi\;=\;48\sqrt{3} - 24\pi,\]
so \(a=48\), \(b=3\), and \(c=24.\) Therefore, \[a + b + c \;=\; 48 + 3 + 24 \;=\; 75.\]
\(\boxed{D)75}\)
~meihk_neiht
P.S.: Please don’t whip out calculus like this on an AMC 10. Yes, it’s “doable” without a calculator (I speak from painful experience). Yes, I did it, but it took forever, and trust me, nobody at the AMC office expects calculus. Also, this is a terriBLE method

## Solution 6 (Pure Geometry Approach — Region DCE minus Circular Segment)
- Step 1: Area of triangle $DCE$
- Given: $DE = 12$ (radius of the circle), and the corresponding height from $C$ to $DE$ is $2\sqrt{3}$ . - The area formula for a triangle is:
- Explanation: This step finds the area of triangle $DCE$ using its base and height.
---
- Step 2: Area of sector $ODE$
- The radius is $12$ , and the central angle is $60^\circ$ . - The formula for the area of a sector is:
- Explanation: The sector's area is a fraction ( $\frac{1}{6}$ ) of the full circle's area.
---
- Step 3: Area of triangle $ODE$
- $OD = OE = 12$ , and the included angle $\angle DOE = 60^\circ$ . - The formula for an equilateral triangle's area:
- Explanation: Triangle $ODE$ is equilateral, so we use the standard area formula for such a triangle.
---
- Step 4: Area of the circular segment (arc $DE$ minus chord $DE$ )
- Explanation: The segment is the region between the arc and the chord $DE$ .
---
- Step 5: Final required region
- Explanation: The required area is the triangle $DCE$ minus the circular segment. This gives the area in the desired region bounded by the triangle, the circle, and the line.
---
- Step 6: Answer in the form $a\sqrt{b} - c\pi$
- Final Answer:
$48\sqrt{3} - 24\pi$ , and $a + b + c = \boxed{75}$
-clicksong

## Solution 7
- Step 1: Area of triangle $DCE$ (using Heron's formula)*
- By geometry, $\triangle DCE$ is a triangle with sides $DC = 12$ , $EC = 12$ , $DE = 12\sqrt{3}$ . - Let $a = 12$ , $b = 12$ , $c = 12\sqrt{3}$ . - The semi-perimeter is:
- The area by Heron's formula:
- However, the actual required region is only $\frac{4}{3}$ of this triangle (since the shaded region is less than the whole triangle). - So,
- But based on precise geometry (as in AMC standard), the correct area to use for this region is $12\sqrt{3}$ (check the triangle's effective area).
---
- Step 2: Area of sector $ODE$ *
- The radius is $12$ and the central angle is $60^\circ$ . - The formula for the area of a sector is:
---
- Step 3: Area of triangle $ODE$ *
- $OD = OE = 12$ , $\angle DOE = 60^\circ$ . - The formula for an equilateral triangle's area:
---
- Step 4: Area of the circular segment (arc $DE$ minus chord $DE$ )*
---
- Step 5: Final required region*
- Explanation: The required area is the triangle $DCE$ minus the circular segment.
---
- Step 6: Expressing the answer as $a\sqrt{b} - c\pi$ *
- Final Answer:*
$48\sqrt{3} - 24\pi$ , and $a + b + c = \boxed{75}$
also by clicksong

## Solution 8 - HEFLE (High Effort For Low Efficiency)
[asy] size(200); pair A = (-48,0); pair B = (-24,0); pair C = (-36,24); pair O = (-16.5,12); // center of the circle draw(A--B--C--cycle, linewidth(1)); draw(circle(O,12), linewidth(1)); draw((-48,0) -- (10,0)); draw((-36,24) -- (-36, 0)); dot(O); draw(O -- (-16.5,0)); pair dir = rotate(205)*(1,0); draw(O -- O + 12*dir); label("$24$", midpoint((-36,24) -- (-36, 0)), E); label("$\ell$", (10,0), E); [/asy]
So, we're here to over-complicate things. Let's start with the circle. Recognize that since the triangle is equilateral, all angles measure $60^\circ$ Observe that the two tangent lines form a $120^\circ$ angle due to the Angle Sum Theorem. Therefore, the area within the circle is the area within a $60^\circ$ arc.
Let's complicate finding the area of the circle. Now, instead of using the equation of a circle we set \[x^2 + y^2 = 144\]
then we solve for $y$ : \[y = \pm\sqrt{144 - x^2}\] then we want the bottom of this circle so we do the negative root $y$ = $-\sqrt{144 - x^2}$ Now, we define this as a function $f(x)$
\[f(x) = -\sqrt{144 - x^2}\] but hold up! waaait a minute! We can make the circle centered at $(12,0)$ because we're just like that. So, to translate it 12 right we must do $f(x - 12)$ so \[f(x - 12) = -\sqrt{144 - (x - 12)^2} = -\sqrt{-x^2 + 24x}\] and because there is a $60 ^\circ$ arc we want $\frac{1}{3}$ of this semicircle so we compute \[\frac{1}{3} \cdot \int_{0}^{24} -\sqrt{-x^2 + 24x} \ \ dx\] then we need to undo our steps and negate the integral(this is done when it's converted to polar) \[\frac{1}{3} \cdot \int_{0}^{24} -\sqrt{-x^2 + 24x} \ \ dx \rightarrow \frac{1}{3} \cdot \int_{0}^{24} -\sqrt{144-(x-12)^2}\ \ dx \rightarrow \int_0^{\pi/3} \frac{1}{2} \cdot 12^2 \ d\theta = \int_0^{\pi/3} 72 \ d\theta\] Recall that \[A= \frac{1}{2} \cdot \int_{\theta_1}^{\theta_2} [f(\theta)]^2 \ \ d\theta\] Therefore, \[\int_0^{\pi/3} 72 \ d\theta = 72 \cdot \frac{\pi}{3} = 24\pi\] Now, we must find the area enclosed by $2$ radii extending to the two points of tangency and their respective tangent lines. So, the two radii are $12$ , and they form a $60^\circ$ angle. Therefore, you have an equilateral triangle of side length $12$ , and its height is $6\sqrt{3}$ using $30^\circ \ 60^\circ \ 90^\circ$
Now, you can just see that the area is $36\sqrt{3}$ , but we won't be doing that here. We can define an absolute value function $g(x)$ such that $g(x)$ has zeros at $-6$ and $6$ , and a y-intercept at $(0, 6\sqrt{3})$ . This would create our triangle above the $x$ -axis. We can see that its slope is $\sqrt{3}$ for $x<0$ and $-\sqrt{3}$ for $x>0$ . Then, we can see that it's translated $6\sqrt{3}$ up from its parent function $h(x)=|x|$ . Therefore, the function is $g(x) = -|x\sqrt{3}|+6\sqrt{3}$ . Now, we integrate over $x\in[-6, 6]$ \[\int_{-6}^{6} -|x\sqrt{3}|+6\sqrt{3} \ \ dx\] Now, we split this into a piecewise function over two integrals \[\int_{-6}^{0} x\sqrt{3}+6\sqrt{3} \ \ dx \ + \ \int_{0}^{6} -x\sqrt{3}+6\sqrt{3} \ \ dx\] Let's apply the power rule to each term. We get \[\int_{-6}^{0} x\sqrt{3}+6\sqrt{3} \ \ dx= \left[\frac{x^2\sqrt3}{2}+6x\sqrt{3} \right]_{-6}^0 = \left(\frac{0^2\sqrt3}{2}+6\cdot0\sqrt{3}\right) - \left(\frac{(-6)^2\sqrt3}{2}+6\cdot-6\sqrt{3}\right) =\] \[0 - (18\sqrt{3} - 36\sqrt3) = 0 - (-18\sqrt{3}) = 18\sqrt{3}\] and, we could say that they are mirror images of each other, but that would make this faster (it's called inefficient for a reason) \[\int_{0}^{6} -x\sqrt{3}+6\sqrt{3} \ \ dx = \left[\frac{-x^2\sqrt3}{2}+6x\sqrt{3} \right]_{0}^6 = \left(\frac{-6^2\sqrt3}{2}+6\cdot6\sqrt{3}\right) - \left(\frac{(0)^2\sqrt3}{2}+6\cdot0\sqrt{3}\right) =\] \[(-18\sqrt{3}+36\sqrt{3}) - 0 = 18\sqrt{3}\] Therefore, by the substitution property equality, \[\int_{-6}^{0} x\sqrt{3}+6\sqrt{3} \ \ dx \ + \ \int_{0}^{6} -x\sqrt{3}+6\sqrt{3} \ \ dx = 18\sqrt{3}+18\sqrt{3}=36\sqrt{3}\] Then, there is another triangle we must define above the $x$ -axis. It is enclosed by the equilateral triangle of height $24$ , line $\ell$ , and the triangle we just found the area of. This triangle has base $12$ and height of $\frac{6}{\sqrt{3}}$ using $30^\circ \ 60^\circ \ 90^\circ$ triangle ratios, which rationalizes to $2\sqrt{3}$ . So, you can tell the area is $12\sqrt{3}$ , but that would make our solution faster.
Since half the base is $6$ , we can tell the zeros are $x= -6$ and $x=6$ , and the $y$ -intercept is $2\sqrt{3}$
We can tell the slope is $\frac{\sqrt{3}}{3}$ for $x<0$ and $-\frac{\sqrt{3}}{3}$ for $x>0$
Then, we define another function $f(x)= -|\frac{1}{3} \cdot x\sqrt{3}| + 2\sqrt{3}$
Now, we integrate over $x\in[-6, 6]$ So, we must compute \[\int_{-6}^{6} -|\frac{1}{3} \cdot x\sqrt{3}| + 2\sqrt{3} \ dx\] We split the function into a piecewise over two integrals \[\int_{-6}^{0} \ \frac{1}{3} \cdot x\sqrt{3} + 2\sqrt{3} \ dx + \int_{0}^{6} -\frac{1}{3} \cdot x\sqrt{3} + 2\sqrt{3} \ \ dx\] Now, we apply the reverse power rule to each term, we get \[\int_{-6}^{0} \ \frac{1}{3} \cdot x\sqrt{3} + 2\sqrt{3} \ \ dx = \left[ \frac{\sqrt{3}}{{3}} \cdot \frac{x^2}{2}+2x\sqrt{3} \right]_{-6}^{0} =\left[ \frac{\sqrt{3}}{{6}} \cdot{x^2}+2x\sqrt{3} \right]_{-6}^{0} =\] \[\left(\frac{\sqrt{3}}{{6}} \cdot{0^2}+2\cdot0\sqrt{3}\right)-\left(\frac{\sqrt{3}}{{6}} \cdot{6^2}+2\cdot-6\sqrt{3}\right)= 0-\left(\frac{\sqrt{3}}{{6}} \cdot{6^2}+2\cdot-6\sqrt{3}\right) =\] \[0- (6\sqrt{3}-12\sqrt{3})=6\sqrt{3}\] Then \[\int_{0}^{6} -\frac{1}{3} \cdot x\sqrt{3} + 2\sqrt{3} \ \ dx = \left[ -\frac{\sqrt{3}}{{3}} \cdot \frac{x^2}{2}+2x\sqrt{3} \right]_{0}^{6} = \left[ -\frac{\sqrt{3}}{{6}} \cdot{x^2}+2x\sqrt{3} \right]_{0}^{6} =\] \[\left(-\frac{\sqrt{3}}{{6}} \cdot{6^2}+2\cdot6\sqrt{3}\right) - \left(-\frac{\sqrt{3}}{{6}} \cdot{0^2}+2\cdot0\sqrt{3} \right)=(-6\sqrt{3} + 12\sqrt{3})-0= 6\sqrt{3}\] Now, by the substitution property of equality, \[\int_{-6}^{0} \frac{1}{3} \cdot x\sqrt{3} + 2\sqrt{3} \ \ dx + \int_{0}^{6} -\frac{1}{3} \cdot x\sqrt{3} + 2\sqrt{3} \ \ dx = 6\sqrt{3}+6\sqrt{3}=12\sqrt{3}\] Now, the total area enclosed by the two circle radii of length $12$ , line $\ell$ , and the isosceles triangle of height $24$ is simply \[36\sqrt{3}+12\sqrt{3}=48\sqrt{3}\] Now, we must subtract the circle's sector area of $24\pi$ to get the expression \[48\sqrt{3}-24\pi\] Which is in the form \[a\sqrt{b}-c\pi\] That the problem asks for. Hence, \[a=48\] \[b=3\] \[c=24\] The problem asks for $a+b+c$ , thus \[a+b+c=48+3+24=75 \implies \boxed{\textbf{(D)}~75}\] -shockfront99
PS: I've never taken calculus, so I could be pretty wrong

## Video Solution(Fast! 30-60-90 Triangle solution)
https://youtu.be/l3VrUsZkv8I
~MC

## Video Solution by Number Craft
https://youtu.be/rIF5L_-zZYQ

## Video Solution by Pi Academy
https://youtu.be/ABkKz0gS1MU?si=ZQBgDMRaJmMPSSMM

## Video Solution 1 by Power Solve
https://youtu.be/oCQ_QvXqV5s

## Video Solution by SpreadTheMathLove
https://youtu.be/UWGyPCQ9NNE?si=LHdwCyUsVeLjV8k3

## Video Solution by Just Math⚡
https://www.youtube.com/watch?v=fzXBMltyXjs&t=53s

## Video Solution by Dr. David
https://youtu.be/nuZv29pqgns

## Video solution by TheNeuralMathAcademy
https://www.youtube.com/watch?v=4b_YLnyegtw&t=2449s
### See Also
- AMC 10
- AMC 10 Problems and Solutions
- Mathematics competitions
- Mathematics competition resources
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
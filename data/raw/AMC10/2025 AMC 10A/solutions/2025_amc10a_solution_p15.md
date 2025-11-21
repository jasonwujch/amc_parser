# 2025 AMC 10A Problem 15

## Problem

In the figure below, $ABEF$ is a rectangle, $\overline{AD}\perp\overline{DE}$ , $AF=7$ , $AB=1$ , and $AD=5$ . [asy] unitsize(1cm); pair A, B, C, D, E, F; A = (5, 5); B = (5.6, 4.2); C = (5, 3.75); D = (5, 0); E = (0, 0); F = (-0.6, 0.8); fill(A--B--C--cycle, gray); dot(A); dot(B); dot(C); dot(D); dot(E); dot(F); label("$A$", A, N); label("$B$", B, (1,0)); label("$C$", C, SE); label("$D$", D, (1,0)); label("$E$", E, S); label("$F$", F, W); draw(A--D--E); draw(A--B--E--F--A); draw(rightanglemark(C, D, E)); [/asy] What is the area of $\triangle ABC$ ?

$\textbf{(A) } \frac{3}{8} \qquad\textbf{(B) } \frac{4}{9} \qquad\textbf{(C) } \frac{1}{8}\sqrt{13} \qquad\textbf{(D) } \frac{7}{15} \qquad\textbf{(E) } \frac{1}{8}\sqrt{15}$

## Video Solution
https://youtu.be/CCYoHk2Af34

## Solution 1
Because $ABEF$ is a rectangle, $\angle ABC=90°$ . We are given that $\angle ADE=90°$ , and since $\angle ECD=\angle ACB$ by vertical angles, $\triangle ECD \sim \triangle ACB$ . Let $AC=x$ . By the Pythagorean Theorem, $CB=\sqrt{x^2-1}$ . Since $AF=BE=7$ , $EC=7-\sqrt{x^2-1}$ . Because $AC=x$ and $AD=5$ , $CD=5-x$ . By similar triangles, \[\frac{7-\sqrt{x^2-1}}{x}=\frac{5-x}{\sqrt{x^2-1}}\] . Cross-multiplying, we get that \[7\sqrt{x^2-1}-x^2+1=5x-x^2\] , so \[7\sqrt{x^2-1}=5x-1\] . We square both sides, and this is simply a quadratic in $x$ : \[24x^2+10x-50=0\] , which has a positive root $x=\frac{5}{4}$ . Since $AB=1$ , we can plug this into the Pythagorean Theorem, with $\frac{5}{4}$ being the hypotenuse, to get $BC=\frac{3}{4}$ , and ${1}\cdot \frac{\frac{3}{4}}{2}$ to equal $[ABC]= \boxed{\textbf{(A)} \frac{3}{8}}$
Solution by HumblePotato, written by lhfriend,
~Corrected all incorrect side length labels and fixed typos and major errors ~Neo
Minor edit by SixthGradeBookWorm927
Minor edit by aldzandrtc
Minor edit by rcll (I fixed this, as aldzandrtc would have said)
Minor edit by pyraminx
Minor edit by wisewigglyjaguar
Minor edit by jeffyang2025

## Solution 2 (simpler)
Draw segment $AE.$ Segment $AE$ is the diagonal of rectangle $ABEF,$ and its diagonals have length $\sqrt{7^2+1^2}=\sqrt{50}=5\sqrt2.$ From right triangle $AED,$ we use pythagorean theorem to find $DE = 5.$
Now, we see similar triangles $\triangle CDE$ and $\triangle CBA$ . Let $CE = a,$ and $CD = b.$ We can find that $AC = 5-b,$ and $CB = 7-a.$ These triangles have a ratio of $\frac {AB}{DE} = \frac{1}{5}.$ So we get that $\frac {5-b}{a} = \frac{1}{5}.$ Cross multplying, we get $a =25-5b.$ And also $\frac{CB}{CD} = \frac{1}{5} = \frac{7-a}{b}.$ Cross multiplying gives $35-5a=b.$ Solving the system of equations, we find $a = 25/4,$ which means $CB = 7-25/4 = 3/4.$ $[ABC] = CB/2,$ which gives $\boxed{[ABC] = 3/8}.$
~ eqb5000/Esteban Q.

## Solution 3 (thorough)
From the diagram, $\angle BCA$ and $\angle DCE$ are vertical angles and hence congruent. Additionally, $\angle B = \angle D = 90^\circ$ , so we have by AA Similarity that $\triangle BCA \sim \triangle DCE$ .
Let $BC = x$ so $EC = 7 - x$ and $AC = y$ so $CD = 5 - y$ . Since the two triangles are similar, we have $\frac{BC}{AC} = \frac{CD}{EC}$ . Plugging in the variables gives $\frac{x}{y} = \frac{5 - y}{7 - x}$ .
Cross multiplying yields $(7 - x)(x) = (5 - y)(y) \implies 7x - x^2 = 5y - y^2 \implies 7x + (y^2 - x^2) = 5y$ .
By applying the Pythagorean Theorem on $\triangle BCA$ , we get $x^2 + 1 = y^2 \implies 1 = y^2 - x^2$ .
Therefore, $y = \frac{7x + 1}{5}$ , and plugging this back into $x^2 + 1 = y^2$ :
$x^2 + 1= (\frac{7x+1}{5})^2$
$25(x^2 + 1) = (7x+1)^2$
$25x^2 + 25 = 49x^2 + 14x + 1$
$0 = 49x^2 + 14x + 1 - 25x^2 - 25$
$0 = 24x^2 + 14x - 24$
$0 = 12x^2 + 7x - 12$
$x = \frac{-7 \pm \sqrt{7^2 - 4(12)(-12)}}{2\cdot 12}$
$= \frac{-7 \pm \sqrt{49 + 576}}{24}$
$= \frac{-7 \pm \sqrt{625}}{24}$
$= \frac{-7 \pm 25}{24}$
Therefore, $x = \frac{-7+25}{24}=\frac{18}{24}=\frac{3}{4}$ .
The area of $\triangle BCA$ is therefore $\frac{x \cdot 1}{2}=\frac{3}{8}=\boxed{A}$ . ~hxve

## Solution 4 (Trigonometry)
Using the Pythagorean theorem, I can get $AE=5 \sqrt{2}$ . Then, because $AD=5$ , $ED=5$ . Now, let $\angle FEA=a$ and $\angle AED=b$ . $\sin a=\frac{7}{5\sqrt{2}}, \sin b=\frac{1}{\sqrt{2}}, \cos a=\frac{1}{5\sqrt{2}},$ and $\cos b=\frac{1}{\sqrt{2}}$ . Then, applying the sine addition formula, I get:
$\sin(a+b)=\frac{7}{5\sqrt{2}}\times\frac{1}{\sqrt{2}}+\frac{1}{\sqrt{2}}\times\frac{1}{5\sqrt{2}}$
$=\frac{7}{10}+ \frac{1}{10}$
$=\frac{4}{5}$
Thus, $\sin(a+b)=\frac{4}{5}$ , so $\sin(180-a-b)=\frac{4}{5}$ . This indicates that if a perpendicular is dropped from point $F$ to the extension of line $DE$ , and the foot of the latitude is point $G$ , $\triangle EGF$ is a 3-4-5 triangle. Because $\triangle EGF\sim\triangle CDE$ , $\triangle CDE$ is also a 3-4-5 triangle. Using ratios,:
$CE=\frac{5}{4}\times 5$
$=\frac{25}{4}$
Therefore, $CE=\frac{25}{4}$ , so $BC=\frac{3}{4}$ , so $\triangle ABC$ has area $\frac{3}{8}$ , or $\boxed A$ .
~Lollipop316
P.S. Thank you to eqb5000 and i_am_not_suk_at_math for pointing out and helping me fix typos.

## Solution 5 (risky, but it works!)
Using a ruler (which is permitted during the exam), and assuming the diagram is to-scale, we can measure the physical lengths of $AB$ and $BC$ , and determine the scale factor in order to calculate $BC$ 's actual math length. In my specific case (potentially could vary), $AB$ was $1$ cm and $BC$ was between $0.7$ and $0.8$ cm. So, the scale with cm is $1:1$ , and the length of $BC$ is around $0.75$ , so the area is $\frac{1}{2} \cdot 0.75 \cdot 1 = \frac{3}{8}$ . To assure ourselves that $\frac{3}{8}$ is the most accurate estimation, we know that $\frac{4}{9}$ is around $0.44$ (too big), $\frac{\sqrt{13}}{8}$ even bigger (so also too big), $\frac{7}{15}$ is just under $0.5$ , and $\frac{\sqrt{15}}{8}$ is even bigger than $\frac{\sqrt{13}}{8}$ , so most likely the answer is $\boxed{\textbf{(A)} \frac{3}{8}}$ .
~vaishnav
Remark - You could also redraw the figure to scale. That way, you won't have to assume it's drawn to scale in the provided figure. You would have to draw the diagonal AE, measure it as $\sqrt{7^2+1^2}$ and use pythagorean theorem to find ED as 5. Once you have that information you could sketch the whole figure to scale.
~wisegod62 (Remark and LaTeX formatting)

## Solution 6 (another cheese)
Inspired by 2022 AMC 10B Problem 16 , another right-triangle and rectangle mashup, we can pretend that the problem uses $3-4-5$ similarity, because AMC problems do that a lot. In this case, we can verify it works by setting $BC = \frac{3}{4}, AC = \frac{5}{4}$ by $3-4-5$ similarity, so $CD = \frac{15}{4}$ and $CE = \frac{25}{4}$ . Then, we see that $BC + CE = \frac{25+3}{4} = 7 = BE = AF$ , which is our only other condition, so this setup works and we can bubble in $\frac{1}{2} \cdot \frac{3}{4} \cdot 1 = \boxed{\textbf{(A)} \frac{3}{8}}$ . of course, if it weren't $3-4-5$ , we can use any other technique.
~tiguhbabehwo

## Solution 7 (area)
Connect $AE$ , which equals $\sqrt{50}$ . Then calculate $ED$ , which equals $5$ . $\triangle ABC \sim \triangle EDC$ (AA). $\dfrac{AB}{ED} = \dfrac{1}{5}$ .
Therefore, $\dfrac{\text{Area of } \triangle ABC}{\text{Area of } \triangle EDC} = \dfrac{1}{25}$ .
Also, let the area of $\triangle ACE = x$ . The area of $\triangle ABC = \dfrac{7}{2} - x$ . The area of $\triangle EDC = \dfrac{25}{2} - x$ .
Solve: $x = \dfrac{25}{8}$
So, $\text{Area of } \triangle ABC = \dfrac{7}{2} - \dfrac{25}{8} = \boxed{\textbf{(A)} \dfrac{3}{8}}$ .
~sandpiper357

## Solution 8 (analytic geometry)
[asy] unitsize(1cm); pair _A, _B, _C, _D, _E, _F; _A = (0, 0); _B = (0, 1); _E = (7, 1); _F = (7, 0); _C = (3/4, 1); _D = extension(_A, _C, _E, _E + rotate(90)*(_A - _C)); fill(_A -- _B -- _C -- cycle, gray); draw(_A -- _B -- _E -- _D -- _A -- _F -- _E); draw((-1, 0) -- (8, 0), Arrows); draw((0, -1) -- (0, 5), Arrows); label("$A$", _A, SW); label("$B$", _B, W); label("$C$", _C, N); label("$D$", _D, N); label("$E$", _E, NE); label("$F$", _F, SE); label("$x$", (8, 0), S); label("$y$", (0, 5), E); label("$1$", _B, NE); label("$7$", _F, SW); label("$(a, 1)$", _C, SE); label(scale(0.8) * rotate(aTan(4/3)) * "$y =\frac{1}{a}x$", (_A + _D)/2, NW); label(scale(0.8) * rotate(-aTan(3/4)) * "$y - 1 = -a(x - 7)$", (_D + _E)/2, NE); [/asy] As shown in the figure, establish a coordinate system with point A as the origin.
Suppose $C = (a, 1)$ , then the equation of $AC$ is $y = \dfrac{1}{a}x$ . Since $DE \perp AC$ , the slope of $DE$ is $-a$ , the equation of $DE$ is $y - 1 = -a(x - 7) \to ax + y - 7a - 1 = 0$ .
Notice that the length of $AD$ is the distance between point $A$ and line $DE$ , due to the distance formula, we get: \[\frac{|a \cdot 0 + 0 - 7a - 1|}{\sqrt{a^2 + 1}} = 5\] \[(7a + 1)^2 = 25(a^2 + 1)\] \[(4a - 3)(3a + 4) = 0\] \[a = \frac{3}{4}\]
The area of $\triangle BCA$ is therefore $\frac{a \cdot 1}{2}=\frac{3}{8}=\boxed{A}$ .
~ reda_mandymath

## Solution 9
From the Pythagorean Theorem, $AE=5\sqrt{2}$ and we also discover $\triangle ADE$ is a $45°-45°-90°$ right triangle. This means that $DE=5$ . As $\triangle ABC \sim \triangle EDC$ by AA similarity and $AB=1$ , we can set up a system of linear equations in terms of $a$ and $b$ where they represent $BC$ and $AC$ respectively. Since $CD=5CB$ and $CE=5AC$ , we have \[5a+b=5\] and \[a+5b=7\] and solving the equations results in $a=\frac{3}{4}$ . The area of $\triangle ABC$ is $\boxed{\textbf{(A)} \frac{3}{8}}$ . $b$ is unnecessary to find.
Note that $\triangle ABC$ is a $3-4-5$ triangle.
~ruihl123

## Chinese Video Solution
https://www.bilibili.com/video/BV1nhkUByE3V/
~metrixgo

## Video Solution (Fast and Easy to Understand)
https://youtu.be/RvU1P9qRu84?si=Ynf6wWPNB1EuF_mq ~ Pi Academy

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=dAeyV60Hu5c

## Video Solution
https://youtu.be/gWSZeCKrOfU
~MK

## Video Solution by Daily Dose of Math
https://youtu.be/5Fjos1vBt0A
~Thesmartgreekmathdude
### See Also
- AMC 10
- AMC 10 Problems and Solutions
- Mathematics competitions
- Mathematics competition resources
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
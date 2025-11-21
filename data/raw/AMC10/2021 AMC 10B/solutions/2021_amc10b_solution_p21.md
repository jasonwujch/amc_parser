# 2021 AMC 10B Problem 21

## Problem

A square piece of paper has side length $1$ and vertices $A,B,C,$ and $D$ in that order. As shown in the figure, the paper is folded so that vertex $C$ meets edge $\overline{AD}$ at point $C'$ , and edge $\overline{BC}$ intersects edge $\overline{AB}$ at point $E$ . Suppose that $C'D = \frac{1}{3}$ . What is the perimeter of triangle $\bigtriangleup AEC' ?$

$\textbf{(A)} ~2 \qquad\textbf{(B)} ~1+\frac{2}{3}\sqrt{3} \qquad\textbf{(C)} ~\frac{13}{6} \qquad\textbf{(D)} ~1 + \frac{3}{4}\sqrt{3} \qquad\textbf{(E)} ~\frac{7}{3}$ [asy] /* Made by samrocksnature */ pair A=(0,1); pair CC=(0.666666666666,1); pair D=(1,1); pair F=(1,0.62); pair C=(1,0); pair B=(0,0); pair G=(0,0.25); pair H=(-0.13,0.41); pair E=(0,0.5); dot(A^^CC^^D^^C^^B^^E); draw(E--A--D--F); draw(G--B--C--F, dashed); fill(E--CC--F--G--H--E--CC--cycle, gray); draw(E--CC--F--G--H--E--CC); label("A",A,NW); label("B",B,SW); label("C",C,SE); label("D",D,NE); label("E",E,NW); label("C'",CC,N); dot(C); dot(E); [/asy]

## Solution 1
We can set the point on $CD$ where the fold occurs as point $F$ . Then, we can set $FD$ as $x$ , and $CF$ as $1-x$ because of symmetry due to the fold. It can be recognized that this is a right triangle, and solving for $x$ , we get,
\[x^2 + \left(\frac{1}{3}\right)^2 = (1-x)^2 \rightarrow x^2 + \frac{1}{9} = x^2 - 2x + 1 \rightarrow x=\frac{4}{9}\]
We know this is a 3-4-5 triangle because the side lengths are $\frac{3}{9}, \frac{4}{9}, \frac{5}{9}$ . We also know that $EAC'$ is similar to $C'DF$ because angle $EC'F$ is a right angle. Now, we can use similarity to find out that the perimeter is just the perimeter of $C'DF \times \frac{AC'}{DF}$ . That's just $\frac{4}{3} \times \frac{\frac{2}{3}}{\frac{4}{9}} = \frac{4}{3} \times \frac{3}{2} = 2$ . Therefore, the final answer is $\boxed{\textbf{(A)} ~2}$
~Tony_Li2007

## Solution 2
Let the line we're reflecting over be $\ell$ , and let the points where it hits $AB$ and $CD$ , be $M$ and $N$ , respectively. Notice, to reflect over a line we find the perpendicular passing through the midpoint of the two points (which are the reflected and the original). So, we first find the equation of the line $\ell$ . The segment $CC'$ has slope $\frac{0 - 1}{1 - 2/3} = -3$ , implying line $\ell$ has a slope of $\frac{1}{3}$ . Also, the midpoint of segment $CC'$ is $\left( \frac{5}{6}, \frac{1}{2} \right)$ , so line $\ell$ passes through this point. Then, we get the equation of line $\ell$ is simply $y = \frac{1}{3} x + \frac{2}{9}$ . Then, if the point where $B$ is reflected over line $\ell$ is $B'$ , then we get $BB'$ is the line $y = -3x$ . The intersection of $\ell$ and segment $BB'$ is $\left( - \frac{1}{15}, \frac{1}{5} \right)$ . So, we get $B' = \left(- \frac{2}{15}, \frac{2}{5} \right)$ . Then, line segment $B'C'$ has equation $y = \frac{3}{4} x + \frac{1}{2}$ , so the point $E$ is the $y$ -intercept, or $\left(0, \frac{1}{2} \right)$ . This implies that $AE = \frac{1}{2}, AC' = \frac{2}{3}$ , and by the Pythagorean Theorem, $EC' = \frac{5}{6}$ (or you could notice $\triangle AEC'$ is a $3-4-5$ right triangle). Then, the perimeter is $\frac{1}{2} + \frac{2}{3} + \frac{5}{6} = 2$ , so our answer is $\boxed{\textbf{(A)} ~2}$ . ~rocketsri

## Solution 3 (Fakesolve):
Assume that E is the midpoint of $\overline{AB}$ . Then, $\overline{AE}=\frac{1}{2}$ and since $C'D=\frac{1}{3}$ , $\overline{AC'}=\frac{2}{3}$ . By the Pythagorean Theorem, $\overline{EC'}=\frac{5}{6}$ . It easily follows that our desired perimeter is $\boxed{\textbf{(A)} ~2}$ ~samrocksnature
Note: This method is only correct because it turns out that $AE$ does in fact equal $\frac{1}{2}$ . However, since it is already given that $C'D$ is $\frac{1}{3}$ . all points are fized and we cannot make any assumptions on $AE'$ s length.
~flyingkinder123

## Solution 4
As described in Solution 1, we can find that $DF=\frac{4}{9}$ , and $C'F = \frac{5}{9}.$
Then, we can find we can find the length of $\overline{AE}$ by expressing the length of $\overline{EF}$ in two different ways, in terms of $AE$ . If let $AE = a$ , by the Pythagorean Theorem we have that $EC' = \sqrt{a^2 + \left(\frac{2}{3}\right)^2} = \sqrt{a^2 + \frac{4}{9}}.$ Therefore, since we know that $\angle EC'F$ is right, by Pythagoras again we have that $EF = \sqrt{\left(\sqrt{a^2+\frac{4}{9}}\right)^2 + \left(\frac{5}{9}\right)^2} = \sqrt{a^2 + \frac{61}{81}}.$
Another way we can express $EF$ is by using Pythagoras on $\triangle XEF$ , where $X$ is the foot of the perpendicular from $F$ to $\overline{AE}.$ We see that $ADFX$ is a rectangle, so we know that $AD = 1 = FX$ . Secondly, since $FD = \frac{4}{9}, EX = a - \frac{4}{9}$ . Therefore, through the Pythagorean Theorem, we find that $EF = \sqrt{\left(a-\frac{4}{9}\right)^2 + 1^2} = \sqrt{a^2 - \frac{8}{9}a +\frac{97}{81}}.$
Since we have found two expressions for the same length, we have the equation $\sqrt{a^2 + \frac{61}{81}} = \sqrt{a^2 - \frac{8}{9}a +\frac{97}{81}}.$ Solving this, we find that $a=\frac{1}{2}$ .
Finally, we see that the perimeter of $\triangle AEC'$ is $\frac{1}{2} + \frac{2}{3} + \sqrt{\left(\frac{1}{2}\right)^2 + \frac{4}{9}},$ which we can simplify to be $2$ . Thus, the answer is $\boxed{\textbf{(A)} ~2}.$ ~laffytaffy

## Solution 5 (Trig)
Draw a perpendicular line from $\overline{AB}$ at $E$ , and let it intersect $\overline{DC}$ at $E'$ . The angle between $\overline{AB}$ and $\overline{EE'}$ is $2\theta$ , where $\theta$ is the angle between the fold and a line perpendicular to $\overline{AD}$ . The slope of the fold is $\frac{1}{3}$ because it is perpendicular to $\overline{CC'}$ ( $\overline{CC'}$ has a slope of $-3$ using points $C'$ and $C$ , and perpendicular lines have slopes negative inverses of each other). Using tangent double angle formula, the slope of $\overline{EC'}$ is $\frac{3}{4}$ , which implies $\overline{AE}$ = $\frac{1}{2}$ . By the Pythagorean Theorem, $\overline{EC'}=\frac{5}{6}$ . It easily follows that our desired perimeter is $\boxed{\textbf{(A)} ~2}$ ~forrestc

## Solution 6
It is easy to prove that the ratio of the sum of the larger leg and hypotenuse to the smaller leg depends monotonically on the angle of a right triangle, which means: \[C' F + DF = CF + DF = CD = AD = 3 C'D \implies C' D : DF : C' F = 3 : 4 : 5.\]
For a similar triangle, the ratio of the perimeter to the larger leg is $\frac {3 + 4 +5}{4} = 3.$
$\triangle AEC' \sim \triangle DC'F \implies$ the perimeter of triangle $\bigtriangleup AEC'$ is $3 AC' = \boxed{\textbf{(A)} ~ 2}.$
vladimir.shelomovskii@gmail.com, vvsss

## Video Solution by OmegaLearn (Using Pythagoras Theorem and Similar Triangles)
https://youtu.be/cagzLmdbqYQ
~ pi_is_3.14

## Video Solution by Interstigation
https://youtu.be/0sEQOjLG-V4
~Interstigation

## Video Solution by The Power of Logic
https://www.youtube.com/watch?v=5kbQHcx1FfE
~The Power of Logic
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
# 2021 AIME II Problem 5

## Problem

For positive real numbers $s$ , let $\tau(s)$ denote the set of all obtuse triangles that have area $s$ and two sides with lengths $4$ and $10$ . The set of all $s$ for which $\tau(s)$ is nonempty, but all triangles in $\tau(s)$ are congruent, is an interval $[a,b)$ . Find $a^2+b^2$ .

## Solution 1
We start by defining a triangle. The two small sides MUST add to a larger sum than the long side. We are given $4$ and $10$ as the sides, so we know that the $3$ rd side is between $6$ and $14$ , exclusive. We also have to consider the word OBTUSE triangles. That means that the two small sides squared is less than the $3$ rd side. So the triangles' sides are between $6$ and $\sqrt{84}$ exclusive, and the larger bound is between $\sqrt{116}$ and $14$ , exclusive. The area of these triangles are from $0$ (straight line) to $2\sqrt{84}$ on the first "small bound" and the larger bound is between $0$ and $20$ . $0 < s < 2\sqrt{84}$ is our first equation, and $0 < s < 20$ is our $2$ nd equation. Therefore, the area is between $\sqrt{336}$ and $\sqrt{400}$ , so our final answer is $\boxed{736}$ .
~ARCTICTURN

## Solution 2 (Inequalities and Casework)
If $a,b,$ and $c$ are the side-lengths of an obtuse triangle with $a\leq b\leq c,$ then both of the following must be satisfied:
- Triangle Inequality Theorem: $a+b>c$
- Pythagorean Inequality Theorem: $a^2+b^2<c^2$
For one such obtuse triangle, let $4,10,$ and $x$ be its side-lengths and $K$ be its area. We apply casework to its longest side:
Case (1): The longest side has length so
By the Triangle Inequality Theorem, we have $4+x>10,$ from which $x>6.$
By the Pythagorean Inequality Theorem, we have $4^2+x^2<10^2,$ from which $x<\sqrt{84}.$
Taking the intersection produces $6<x<\sqrt{84}$ for this case.
At $x=6,$ the obtuse triangle degenerates into a straight line with area $K=0;$ at $x=\sqrt{84},$ the obtuse triangle degenerates into a right triangle with area $K=\frac12\cdot4\cdot\sqrt{84}=2\sqrt{84}.$ Together, we obtain $0<K<2\sqrt{84},$ or $K\in\left(0,2\sqrt{84}\right).$
Case (2): The longest side has length so
By the Triangle Inequality Theorem, we have $4+10>x,$ from which $x<14.$
By the Pythagorean Inequality Theorem, we have $4^2+10^2<x^2,$ from which $x>\sqrt{116}.$
Taking the intersection produces $\sqrt{116}<x<14$ for this case.
At $x=14,$ the obtuse triangle degenerates into a straight line with area $K=0;$ at $x=\sqrt{116},$ the obtuse triangle degenerates into a right triangle with area $K=\frac12\cdot4\cdot10=20.$ Together, we obtain $0<K<20,$ or $K\in\left(0,20\right).$
Answer
It is possible for noncongruent obtuse triangles to have the same area. Therefore, all such positive real numbers $s$ are in exactly one of $\left(0,2\sqrt{84}\right)$ or $\left(0,20\right).$ By the exclusive disjunction, the set of all such $s$ is \[[a,b)=\left(0,2\sqrt{84}\right)\oplus\left(0,20\right)=\left[2\sqrt{84},20\right),\] from which $a^2+b^2=\boxed{736}.$
~MRENTHUSIASM

## Solution 3
We have the diagram below.
[asy] draw((0,0)--(1,2*sqrt(3))); draw((1,2*sqrt(3))--(10,0)); draw((10,0)--(0,0)); label("$A$",(0,0),SW); label("$B$",(1,2*sqrt(3)),N); label("$C$",(10,0),SE); label("$\theta$",(0,0),NE); label("$\alpha$",(1,2*sqrt(3)),SSE); label("$4$",(0,0)--(1,2*sqrt(3)),WNW); label("$10$",(0,0)--(10,0),S); [/asy]
We proceed by taking cases on the angles that can be obtuse, and finding the ranges for $s$ that they yield .
If angle $\theta$ is obtuse, then we have that $s \in (0,20)$ . This is because $s=20$ is attained at $\theta = 90^{\circ}$ , and the area of the triangle is strictly decreasing as $\theta$ increases beyond $90^{\circ}$ . This can be observed from \[s=\frac{1}{2}(4)(10)\sin\theta\] by noting that $\sin\theta$ is decreasing in $\theta \in (90^{\circ},180^{\circ})$ .
Then, we note that if $\alpha$ is obtuse, we have $s \in (0,4\sqrt{21})$ . This is because we get $x=\sqrt{10^2-4^2}=\sqrt{84}=2\sqrt{21}$ when $\alpha=90^{\circ}$ , yileding $s=4\sqrt{21}$ . Then, $s$ is decreasing as $\alpha$ increases by the same argument as before.
$\angle{ACB}$ cannot be obtuse since $AC>AB$ .
Now we have the intervals $s \in (0,20)$ and $s \in (0,4\sqrt{21})$ for the cases where $\theta$ and $\alpha$ are obtuse, respectively. We are looking for the $s$ that are in exactly one of these intervals, and because $4\sqrt{21}<20$ , the desired range is \[s\in [4\sqrt{21},20)\] giving \[a^2+b^2=\boxed{736}\Box\]

## Solution 4
Note: Archimedes15 Solution which I added an answer here are two cases. Either the $4$ and $10$ are around an obtuse angle or the $4$ and $10$ are around an acute triangle. If they are around the obtuse angle, the area of that triangle is $<20$ as we have $\frac{1}{2} \cdot 40 \cdot \sin{\alpha}$ and $\sin$ is at most $1$ . Note that for the other case, the side lengths around the obtuse angle must be $4$ and $x$ where we have $16+x^2 < 100 \rightarrow x < 2\sqrt{21}$ . Using the same logic as the other case, the area is at most $4\sqrt{21}$ . Square and add $4\sqrt{21}$ and $20$ to get the right answer \[a^2+b^2= \boxed{736}\Box\]

## Solution 5 (Circles)
For $\triangle ABC,$ we fix $AB=10$ and $BC=4.$ Without the loss of generality, we consider $C$ on only one side of $\overline{AB}.$
As shown below, all locations for $C$ at which $\triangle ABC$ is an obtuse triangle are indicated in red, excluding the endpoints. [asy] /* Made by MRENTHUSIASM */ size(300); pair A, B, O, P, Q, C1, C2, D; A = origin; B = (10,0); O = midpoint(A--B); P = B - (4,0); Q = B + (4,0); C1 = intersectionpoints(D--D+(100,0),Arc(B,Q,P))[1]; C2 = B + (0,4); D = intersectionpoint(Arc(O,B,A),Arc(B,Q,P)); draw(Arc(O,B,A)^^Arc(B,C2,D)^^A--Q); draw(Arc(B,Q,C2)^^Arc(B,D,P),red); dot("$A$", A, 1.5*S, linewidth(4.5)); dot("$B$", B, 1.5*S, linewidth(4.5)); dot(O, linewidth(4.5)); dot(P^^C2^^D^^Q, linewidth(0.8), UnFill); Label L1 = Label("$10$", align=(0,0), position=MidPoint, filltype=Fill(3,0,white)); Label L2 = Label("$4$", align=(0,0), position=MidPoint, filltype=Fill(3,0,white)); draw(A-(0,2)--B-(0,2), L=L1, arrow=Arrows(),bar=Bars(15)); draw(B-(0,2)--Q-(0,2), L=L2, arrow=Arrows(),bar=Bars(15)); label("$\angle C$ obtuse",(midpoint(Arc(B,D,P)).x,2),2.5*W,red); label("$\angle B$ obtuse",(midpoint(Arc(B,Q,C2)).x,2),5*E,red); [/asy] Note that:
1. The region in which $\angle B$ is obtuse is determined by construction.
1. The region in which $\angle C$ is obtuse is determined by the corollaries of the Inscribed Angle Theorem.
For any fixed value of $s,$ the height from $C$ is fixed. We need obtuse $\triangle ABC$ to be unique, so there can only be one possible location for $C.$ As shown below, all possible locations for $C$ are on minor arc $\widehat{C_1C_2},$ including $C_1$ but excluding $C_2.$ [asy] /* Made by MRENTHUSIASM */ size(250); pair A, B, O, P, Q, C1, C2, D; A = origin; B = (10,0); O = midpoint(A--B); P = B - (4,0); Q = B + (4,0); C2 = B + (0,4); D = intersectionpoint(Arc(O,B,A),Arc(B,Q,P)); C1 = intersectionpoint(D--D+(100,0),Arc(B,Q,C2)); draw(Arc(O,B,A)^^Arc(B,C2,D)^^A--Q); draw(Arc(B,Q,C1)^^Arc(B,D,P),red); draw(Arc(B,C1,C2),green); draw((A.x,D.y)--(Q.x,D.y),dashed); dot("$A$", A, 1.5*S, linewidth(4.5)); dot("$B$", B, 1.5*S, linewidth(4.5)); dot("$D$", D, 1.5*dir(75), linewidth(0.8), UnFill); dot("$C_2$", C2, 1.5*N, linewidth(4.5)); dot("$C_1$", C1, 1.5*dir(C1-B), linewidth(4.5)); dot(O, linewidth(4.5)); dot(P^^C2^^Q, linewidth(0.8), UnFill); dot(C1, green+linewidth(4.5)); Label L1 = Label("$10$", align=(0,0), position=MidPoint, filltype=Fill(3,0,white)); Label L2 = Label("$4$", align=(0,0), position=MidPoint, filltype=Fill(3,0,white)); draw(A-(0,2)--B-(0,2), L=L1, arrow=Arrows(),bar=Bars(15)); draw(B-(0,2)--Q-(0,2), L=L2, arrow=Arrows(),bar=Bars(15)); [/asy] Let the brackets denote areas:
- If $C=C_1,$ then $[ABC]$ will be minimized (attainable). By the same base and height and the Inscribed Angle Theorem, we have \begin{align*} [ABC]&=[ABD] \\ &=\frac12\cdot BD\cdot DA \\ &=\frac12\cdot BD\cdot \sqrt{AB^2-BD^2} \\ &=\frac12\cdot 4\cdot \sqrt{10^2-4^2} \\ &=2\sqrt{84}. \end{align*}
- If $C=C_2,$ then $[ABC]$ will be maximized (unattainable). For this right triangle, we have \begin{align*} [ABC]&=\frac12\cdot AB\cdot BC \\ &=\frac12\cdot 10\cdot 4 \\ &=20. \end{align*}
Finally, the set of all such $s$ is $[a,b)=\left[2\sqrt{84},20\right),$ from which $a^2+b^2=\boxed{736}.$
~MRENTHUSIASM (credit given to Snowfan)

## Solution 6
Let a triangle in $\tau(s)$ be $ABC$ , where $AB = 4$ and $BC = 10$ . We will proceed with two cases:
Case 1: $\angle ABC$ is obtuse. If $\angle ABC$ is obtuse, then, if we imagine $AB$ as the base of our triangle, the height can be anything in the range $(0,10)$ ; therefore, the area of the triangle will fall in the range of $(0, 20)$ .
Case 2: $\angle BAC$ is obtuse. Then, if we imagine $AB$ as the base of our triangle, the height can be anything in the range $\left(0, \sqrt{10^{2} - 4^{2}}\right)$ . Therefore, the area of the triangle will fall in the range of $\left(0, 2 \sqrt{84}\right)$ .
If $s < 2 \sqrt{84}$ , there will exist two types of triangles in $\tau(s)$ - one type with $\angle ABC$ obtuse; the other type with $\angle BAC$ obtuse. If $s \geq 2 \sqrt{84}$ , as we just found, $\angle BAC$ cannot be obtuse, so therefore, there is only one type of triangle - the one in which $\angle ABC$ is obtuse. Also, if $s > 20$ , no triangle exists with lengths $4$ and $10$ . Therefore, $s$ is in the range $\left[ 2 \sqrt{84}, 20\right)$ , so our answer is $\left(2 \sqrt{84}\right)^{2} + 20^{2} = \boxed{736}$ .
Alternatively, refer to Solution 5 for the geometric interpretation.
~ihatemath123

## Solution 7
Let's rephrase the condition. It is required to find such values of the area of an obtuse triangle with sides $4$ and $10,$ when there is exactly one such obtuse triangle. In the diagram, $AB = 4, AC = 10.$
The largest area of triangle with sides $4$ and $10$ is $20$ for a right triangle with legs $4$ and $10$ ( $AC\perp AB$ ).
The diagram shows triangles with equal heights. The yellow triangle $ABC'$ has the longest side $BC',$ the blue triangle $ABC$ has the longest side $AC.$ If $BC\perp AB,$ then $BC = \sqrt {AC^2 – AB^2} = 2 \sqrt{21}$ the area is equal to $4\sqrt{21}.$ In the interval, the blue triangle $ABC$ is acute-angled, the yellow triangle $ABC'$ is obtuse-angled. Their heights and areas are equal. The condition is met.
If the area is less than $4\sqrt{21},$ both triangles are obtuse, not equal, so the condition is not met.
Therefore, $s$ is in the range $\left[ 4 \sqrt{21}, 20\right)$ , so answer is $\left(4 \sqrt{21}\right)^{2} + 20^{2} = \boxed{736}$
vladimir.shelomovskii@gmail.com, vvsss

## Solution 8
If $4$ and $10$ are the shortest sides and $\angle C$ is the included angle, then the area is \[\frac{4\cdot10\cdot\sin\angle C}{2} = 20\sin\angle C.\] Because $0\leq\sin\angle C\leq1$ , the maximum value of $20\sin\angle C$ is $20$ , so $s\leq20$ .
If $4$ is a shortest side and $10$ is the longest side, the length of the other short side is $4\cos\angle C+2\sqrt{4\cos^2 \angle C+21}$ by law of cosines, and the area is $2\left(4\cos\angle C+2\sqrt{4\cos^2\angle C+21}\right)\sqrt{1-\cos\angle C}$ . Because $-1\le \cos\angle C\le 0$ , this is minimized if $\cos\angle C=0$ , where $s=4\sqrt{21}$ .
So, the answer is $20^2+\left(4\sqrt{21}\right)^2=\boxed{736}$ .
~ryanbear

## Video Solution by Interstigation
https://youtu.be/ODokTEt3EVA
~Interstigation
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
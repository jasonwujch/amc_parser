# 2021 AIME II Problem 2

## Problem

Equilateral triangle $ABC$ has side length $840$ . Point $D$ lies on the same side of line $BC$ as $A$ such that $\overline{BD} \perp \overline{BC}$ . The line $\ell$ through $D$ parallel to line $BC$ intersects sides $\overline{AB}$ and $\overline{AC}$ at points $E$ and $F$ , respectively. Point $G$ lies on $\ell$ such that $F$ is between $E$ and $G$ , $\triangle AFG$ is isosceles, and the ratio of the area of $\triangle AFG$ to the area of $\triangle BED$ is $8:9$ . Find $AF$ . [asy] pair A,B,C,D,E,F,G; B=origin; A=5*dir(60); C=(5,0); E=0.6*A+0.4*B; F=0.6*A+0.4*C; G=rotate(240,F)*A; D=extension(E,F,B,dir(90)); draw(D--G--A,grey); draw(B--0.5*A+rotate(60,B)*A*0.5,grey); draw(A--B--C--cycle,linewidth(1.5)); dot(A^^B^^C^^D^^E^^F^^G); label("$A$",A,dir(90)); label("$B$",B,dir(225)); label("$C$",C,dir(-45)); label("$D$",D,dir(180)); label("$E$",E,dir(-45)); label("$F$",F,dir(225)); label("$G$",G,dir(0)); label("$\ell$",midpoint(E--F),dir(90)); [/asy]

## Solution 1 (Area Formulas for Triangles)
By angle chasing, we conclude that $\triangle AGF$ is a $30^\circ\text{-}30^\circ\text{-}120^\circ$ triangle, and $\triangle BED$ is a $30^\circ\text{-}60^\circ\text{-}90^\circ$ triangle.
Let $AF=x.$ It follows that $FG=x$ and $EB=FC=840-x.$ By the side-length ratios in $\triangle BED,$ we have $DE=\frac{840-x}{2}$ and $DB=\frac{840-x}{2}\cdot\sqrt3.$
Let the brackets denote areas. We have \[[AFG]=\frac12\cdot AF\cdot FG\cdot\sin{\angle AFG}=\frac12\cdot x\cdot x\cdot\sin{120^\circ}=\frac12\cdot x^2\cdot\frac{\sqrt3}{2}\] and \[[BED]=\frac12\cdot DE\cdot DB=\frac12\cdot\frac{840-x}{2}\cdot\left(\frac{840-x}{2}\cdot\sqrt3\right).\]
We set up and solve an equation for $x:$ \begin{align*} \frac{[AFG]}{[BED]}&=\frac89 \\ \frac{\frac12\cdot x^2\cdot\frac{\sqrt3}{2}}{\frac12\cdot\frac{840-x}{2}\cdot\left(\frac{840-x}{2}\cdot\sqrt3\right)}&=\frac89 \\ \frac{2x^2}{(840-x)^2}&=\frac89 \\ \frac{x^2}{(840-x)^2}&=\frac49. \end{align*} Since $0<x<840,$ it is clear that $\frac{x}{840-x}>0.$ Therefore, we take the positive square root for both sides: \begin{align*} \frac{x}{840-x}&=\frac23 \\ 3x&=1680-2x \\ 5x&=1680 \\ x&=\boxed{336}. \end{align*}
~MRENTHUSIASM

## Solution 2
We express the areas of $\triangle BED$ and $\triangle AFG$ in terms of $AF$ in order to solve for $AF.$
We let $x = AF.$ Because $\triangle AFG$ is isosceles and $\triangle AEF$ is equilateral, $AF = FG = EF = AE = x.$
Let the height of $\triangle ABC$ be $h$ and the height of $\triangle AEF$ be $h'.$ Then we have that $h = \frac{\sqrt{3}}{2}(840) = 420\sqrt{3}$ and $h' = \frac{\sqrt{3}}{2}(EF) = \frac{\sqrt{3}}{2}x.$
Now we can find $DB$ and $BE$ in terms of $x.$ $DB = h - h' = 420\sqrt{3} - \frac{\sqrt{3}}{2}x,$ $BE = AB - AE = 840 - x.$ Because we are given that $\angle DBC = 90,$ $\angle DBE = 30.$ This allows us to use the sin formula for triangle area: the area of $\triangle BED$ is $\frac{1}{2}(\sin 30)\left(420\sqrt{3} - \frac{\sqrt{3}}{2}x\right)(840-x).$ Similarly, because $\angle AFG = 120,$ the area of $\triangle AFG$ is $\frac{1}{2}(\sin 120)(x^2).$
Now we can make an equation: \begin{align*} \frac{\triangle AFG}{\triangle BED} &= \frac{8}{9} \\ \frac{\frac{1}{2}(\sin 120)(x^2)}{\frac{1}{2}(\sin 30)\left(420\sqrt{3} - \frac{\sqrt{3}}{2}x\right)(840-x)} &= \frac{8}{9} \\ \frac{x^2}{\left(420 - \frac{x}{2}\right)(840-x)} &= \frac{8}{9}. \end{align*} To make further calculations easier, we scale everything down by $420$ (while keeping the same variable names, so keep that in mind). \begin{align*} \frac{x^2}{\left(1-\frac{x}{2}\right)(2-x)} &= \frac{8}{9} \\ 8\left(1-\frac{x}{2}\right)(2-x) &= 9x^2 \\ 16-16x + 4x^2 &= 9x^2 \\ 5x^2 + 16x -16 &= 0 \\ (5x-4)(x+4) &= 0. \end{align*} Thus $x = \frac{4}{5}.$ Because we scaled down everything by $420,$ the actual value of $AF$ is $\frac{4}{5}(420) = \boxed{336}.$
~JimY

## Solution 3 (Pretty Straightforward)
$\angle AFE = \angle AEF = \angle EAF = 60^{0} \Rightarrow \angle AFG = 120^{0}$ So, If $\Delta AFG$ is isosceles, it means that $AF = FG$ .
Let $AF = FG = AE = EF = x$
So, $[\Delta AFG] = \frac{1}{2} \cdot x^{2} \textup{sin} 120^{0} = \frac{\sqrt{3}}{4}x^{2}$
In $\Delta BED$ , $BE = 840 - x$ , Hence $DE = \frac{840 - x}{2}$ (because $\textup{sin} 30^{0} = \frac{1}{2}$ )
Therefore, $[\Delta BED] = \frac{1}{2} (840 - x) \left (\frac{840-x}{2} \right) \textup{sin} 60^{0}$
So, $[\Delta BED] = \frac{\sqrt{3}}{4} (840 - x) \left (\frac{840-x}{2} \right) = \frac{\sqrt{3}}{8} (840 - x)^{2}$
Now, as we know that the ratio of the areas of $\Delta AFG$ and $\Delta BED$ is $8:9$
Substituting the values, we get
$\frac{\frac{\sqrt{3}}{4}x^{2}}{\frac{\sqrt{3}}{8} (840 - x)^{2}} = \frac{8}{9} \Rightarrow \left (\frac{x}{840 - x} \right)^{2} = \frac{4}{9}$ Hence, $\frac{x}{840 - x} = \frac{2}{3}$ . Solving this, we easily get $x = 336$
We have taken $AF = x$ , Hence, $AF = \boxed{336}$
-Arnav Nigam

## Solution 4 (Similar Triangles)
Since $\triangle AFG$ is isosceles, $AF = FG$ , and since $\triangle AEF$ is equilateral, $AF = EF$ . Thus, $EF = FG$ , and since these triangles share an altitude, they must have the same area.
Drop perpendiculars from $E$ and $F$ to line $BC$ ; call the meeting points $P$ and $Q$ , respectively. $\triangle BEP$ is clearly congruent to both $\triangle BED$ and $\triangle FQC$ , and thus each of these new triangles has the same area as $\triangle BED$ . But we can "slide" $\triangle BEP$ over to make it adjacent to $\triangle FQC$ , thus creating an equilateral triangle whose area has a ratio of $18:8$ when compared to $\triangle AEF$ (based on our conclusion from the first paragraph). Since these triangles are both equilateral, they are similar, and since the area ratio $18:8$ reduces to $9:4$ , the ratio of their sides must be $3:2$ . So, because $FC$ and $AF$ represent sides of these triangles, and they add to $840$ , $AF$ must equal two-fifths of $840$ , or $\boxed{336}$ .

## Solution 5 (No Trig, Straightforward)
Draw the perpendicular segment from $A$ to $BC$ . Call its intersection with $EF$ as point $H$ and its intersection with $BC$ as point $I$ . Because $AFH$ is a $30-60-90$ triangle, $AH = \frac{\sqrt{3}}{2}x$ . Call $DB = HI$ as $h$ . Because $ABI$ is a $30-60-90$ triangle, $AI = \frac{\sqrt{3}}{2}x + h = 420\sqrt{3}$ . $DE = \frac{h}{\sqrt{3}}$ because $DBE$ is a $30-60-90$ triangle. We know from the problem statement that $9[AFG]= \frac{9}{2}(\frac{\sqrt{3}}{2}x^2) = \frac{8}{2\sqrt{3}}h^2 = 8[BED]$ . By simplifying this equation, $h = \frac{3\sqrt{3}x}{4}$ . Substituting $h$ into the first equation yields $x = \boxed{336}$ .
-unhappyfarmer

## Video Solution
https://www.youtube.com/watch?v=ol-Nl-t9X04

## Video Solution by Interstigation (Similar Triangles)
https://youtu.be/qjiOhBEfpWY
~Interstigation
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
# 2004 AIME II Problem 7

## Problem

$ABCD$ is a rectangular sheet of paper that has been folded so that corner $B$ is matched with point $B'$ on edge $AD.$ The crease is $EF,$ where $E$ is on $AB$ and $F$ is on $CD.$ The dimensions $AE=8, BE=17,$ and $CF=3$ are given. The perimeter of rectangle $ABCD$ is $m/n,$ where $m$ and $n$ are relatively prime positive integers. Find $m+n.$

[asy] size(200); defaultpen(linewidth(0.7)+fontsize(10)); pair A=origin, B=(25,0), C=(25,70/3), D=(0,70/3), E=(8,0), F=(22,70/3), Bp=reflect(E,F)*B, Cp=reflect(E,F)*C; draw(F--D--A--E); draw(E--B--C--F, linetype("4 4")); filldraw(E--F--Cp--Bp--cycle, white, black); pair point=( 12.5, 35/3 ); label("$A$", A, dir(point--A)); label("$B$", B, dir(point--B)); label("$C$", C, dir(point--C)); label("$D$", D, dir(point--D)); label("$E$", E, dir(point--E)); label("$F$", F, dir(point--F)); label("$B^\prime$", Bp, dir(point--Bp)); label("$C^\prime$", Cp, dir(point--Cp));[/asy]

## Solutions

## Solution 1 (Synthetic)
Since $EF$ is the perpendicular bisector of $\overline{BB'}$ , it follows that $BE = B'E$ (by SAS). By the Pythagorean Theorem , we have $AB' = 15$ . Similarly, from $BF = B'F$ , we have \begin{align*} BC^2 + CF^2 = B'D^2 + DF^2 &\Longrightarrow BC^2 + 9 = (BC - 15)^2 + 484 \\ BC &= \frac{70}{3} \end{align*} Thus the perimeter of $ABCD$ is $2\left(25 + \frac{70}{3}\right) = \frac{290}{3}$ , and our answer is $m+n=\boxed{293}$ .

## Solution 2 (analytic)
Let $A = (0,0), B=(0,25)$ , so $E = (0,8)$ and $F = (l,22)$ , and let $l = AD$ be the length of the rectangle. The slope of $EF$ is $\frac{14}{l}$ and so the equation of $EF$ is $y -8 = \frac{14}{l}x$ . We know that $EF$ is perpendicular to and bisects $BB'$ . The slope of $BB'$ is thus $\frac{-l}{14}$ , and so the equation of $BB'$ is $y -25 = \frac{-l}{14}x$ . Let the point of intersection of $EF, BB'$ be $G$ . Then the y-coordinate of $G$ is $\frac{25}{2}$ , so \begin{align*} \frac{14}{l}x &= y-8 = \frac{9}{2}\\ \frac{-l}{14}x &= y-25 = -\frac{25}{2}\\ \end{align*} Dividing the two equations yields
The answer is $\boxed{293}$ as above.

## Solution 3 (Coordinate Bashing)
Firstly, observe that if we are given that $AE=8$ and $BE=17$ , the length of the triangle is given and the height depends solely on the length of $CF$ . Let Point $A = (0,0)$ . Since $AE=8$ , point E is at (8,0). Next, point $B$ is at $(25,0)$ since $BE=17$ and point $B'$ is at $(0,15)$ since $BE=AE$ by symmetry. Draw line segment $BB'$ . Notice that this is perpendicular to $EF$ by symmetry. Next, find the slope of EB, which is $\frac{15}{25}=\frac{3}{5}$ . Then, the slope of $EF$ is - $\frac{5}{3}$ .
Line EF can be written as y= $-\frac{5}{3}x+b$ . Plug in the point $(8,0)$ , and we get the equation of EF to be y= $_\frac{5}{3}x+\frac{40}{3}$ . Since the length of $AB$ =25, a point on line $EF$ lies on $DC$ when $x=25-3=22$ . Plug in $x=22$ into our equation to get $y=-\frac{70}{3}$ . $|y|=BC=\frac{70}{3}$ . Therefore, our answer is $2(AB+BC)=2\left(25+\frac{70}{3}\right)=2\left(\frac{145}{3}\right)=\frac{290}{3}= \boxed{293}$ .

## Solution 4 (Trig)
Firstly, note that $B'E=BE=17$ , so $AB'=\sqrt{17^2-8^2}=15$ . Then let $\angle BEF=\angle B'EF=\theta$ , so $\angle B'EA = \pi-2\theta$ . Then $\tan(\pi-2\theta)=\frac{15}{8}$ , or
\[\frac{2\tan(\theta)}{\tan^2(\theta)-1}=\frac{15}{8}\] using supplementary and double angle identities. Multiplying though and factoring yields
\[(3\tan(\theta)-5)(5\tan(\theta)+3)=0\]
It is clear from the problem setup that $0<\theta<\frac\pi2$ , so the correct value is $\tan(\theta)=\frac53$ . Next, extend rays $\overrightarrow{BC}$ and $\overrightarrow{EF}$ to intersect at $C'$ . Then $\tan(\theta)=\frac{BC'}{17}=\frac53$ , so $BC'=\frac{85}{3}$ . By similar triangles, $CC'=\frac{3}{17}BC'=\frac{15}{3}$ , so $BC=\frac{70}{3}$ . The perimeter is $\frac{140}{3}+50=\frac{290}{3}\Longrightarrow \boxed{293}$
An even faster way to finish is, to draw a line segment $FF'$ where $F'$ is a point on $EB$ such that $FF'$ is perpendicular to $EB$ . This makes right triangle $FF'E$ , Also, note that $F'B$ has length of $3$ (draw the diagram out, and note the $F'B =FC$ ). From here, through $\tan \theta = \frac{5}{3}$ , we can note that $\frac{FF'}{EF'} = \frac{5}{3} \implies \frac{FF'}{14} = \frac{5}{3} \implies FF' = \frac{70}{3}$ . $FF'$ is parallel and congrurent to $CB$ and $AD$ , and hence we can use this to calculate the perimeter. The perimeter is simply $\frac{70}{3} + \frac{70}{3} + 25 + 25 = \frac{290}{3} \Longrightarrow \boxed{293}$

## Solution 5 (Fast, Pythagorean)
Use the prepared diagram for this solution.
Call the intersection of DF and B'C' G. AB'E is an 8-15-17 right triangle, and so are B'DG and C'FG. Since C'F is 3, then using the properties of similar triangles GF is 51/8. DF is 22, so DG is 125/8. Finally, DB can to calculated to be 25/3. Add all the sides together to get $\boxed{293}$ .
-jackshi2006

## Solution 6(fast as wind[rufeng])
Call the intersection of $B'C'$ , $BC$ , and $EF$ $G$ . Since $FCBE$ and $FC'B'E$ are congruent, we know that the three lines intersect. We already know $AB$ so we just need to find $CB$ , call it $x$ . Drop an altitude from $F$ to $AB$ and call it $H$ . $EH=EB-FC=14$ . Using Pythagorean Theorem, we have $EF=\sqrt{x^2+14^2}$ . Triangles $EFH$ and $EGB$ are similar (AA), so we get \[\frac{HF}{BG}=\frac{EH}{EB}\] \[\frac{x}{x+GC}=\frac{14}{17}\] Simplify and we get $GC=\frac{3x}{14}$ .
We find the area of $FCBE$ by using the fact that it is a trapezoid. $[FCBE]=\frac{(3+17)x}{2}=10x$
A different way to find the area: $[FCBE]=\frac{1}{2} EG\cdot($ height of $EGB$ with $EG$ as base $)-[FGC]$
Since $GBE$ and $G'B'E$ are congruent(SAS), their height from $EG$ is the same. $B'B=\sqrt{AB'^2+AB^2}=5\sqrt{34}$ . $EG=\sqrt{EB^2+BG^2}=\sqrt{(\frac{17x}{14})^2+17^2}=17\sqrt{\frac{x^2}{196}+1}$
\[[FCBE]=\frac{1}{2} \cdot 17 \cdot \sqrt{\frac{x^2}{196}+1} \cdot \frac{5\sqrt{34}}{2}-\frac{9x}{28}\] \[280x+9x=7\cdot 5 \cdot \sqrt{34} \cdot 17 \cdot \sqrt{\frac{x^2}{196}+1}\] \[17^4 x^2=49 \cdot 25 \cdot 34 \cdot 17^2 \cdot (\frac{x^2}{196}+1)\] \[17x^2=\frac{25}{2}x^2+2450\] \[x=\frac{70}{3}\]
The perimeter is $\frac{140}{3}+50=\frac{290}{3},$ so our answer is $\boxed{293}$ .

## Solution 7 (Similar to solution 5, more in depth)
Let the endpoint of the intersection of the fold near $F$ be $G$ . Since trapezoid $BCFE$ is folded, it is congruent to trapezoid $B'C'FE$ . Therefore, $BE=B'E=17$ . Since $\triangle AB'E$ is a right triangle, $AB'=15$ from the pythagorean theorem. From here, we can see that triangles $\triangle AEB \sim \triangle DGB' \sim \triangle C'GF$ by AA similarity. From here, we find $BC$ from a lot of similarities. Let $BC=x$ .
Since $\triangle ABE' \sim \triangle DGB'$ :
\[\frac {AE}{AB'} = \frac{DB}{DG}\]
\[\frac {8}{15} = \frac {x-15}{DG}\]
\[DG = \frac {15(x-15)}{8}\]
\[GF = DC-DG-FC\]
\[GF = \frac{-15x+401}{8}\]
Since $\triangle ABE' \sim \triangle C'GF'$ ,
\[\frac {AE}{B'E} = \frac {C'F}{GF}\]
\[\frac {8}{17} = \frac{3}{\frac {-15x+401}{8}}\]
from which we get $x= \frac {70}{3}$ .
Finally, our answer is $2(\frac {70}{3}) + 2(25)=\frac {290}{3}$ , which is $290+3=\boxed{293}$ .
~ Wesserwessey7254
These problems are copyrighted © by the Mathematical Association of America.
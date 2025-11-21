# 2021 Fall AMC 10B Problem 25

## Problem

A rectangle with side lengths $1{ }$ and $3,$ a square with side length $1,$ and a rectangle $R$ are inscribed inside a larger square as shown. The sum of all possible values for the area of $R$ can be written in the form $\tfrac mn$ , where $m$ and $n$ are relatively prime positive integers. What is $m+n?$ [asy] size(8cm); draw((0,0)--(10,0)); draw((0,0)--(0,10)); draw((10,0)--(10,10)); draw((0,10)--(10,10)); draw((1,6)--(0,9)); draw((0,9)--(3,10)); draw((3,10)--(4,7)); draw((4,7)--(1,6)); draw((0,3)--(1,6)); draw((1,6)--(10,3)); draw((10,3)--(9,0)); draw((9,0)--(0,3)); draw((6,13/3)--(10,22/3)); draw((10,22/3)--(8,10)); draw((8,10)--(4,7)); draw((4,7)--(6,13/3)); label("$3$",(9/2,3/2),N); label("$3$",(11/2,9/2),S); label("$1$",(1/2,9/2),E); label("$1$",(19/2,3/2),W); label("$1$",(1/2,15/2),E); label("$1$",(3/2,19/2),S); label("$1$",(5/2,13/2),N); label("$1$",(7/2,17/2),W); label("$R$",(7,43/6),W); [/asy] $(\textbf{A})\: 14\qquad(\textbf{B}) \: 23\qquad(\textbf{C}) \: 46\qquad(\textbf{D}) \: 59\qquad(\textbf{E}) \: 67$

## Solution 1
We see that the polygon bounded by the small square, large square, and rectangle of known lengths is an isosceles triangle. Let’s draw a perpendicular from the vertex of this triangle to its opposing side;
[asy] size(8cm); draw((0,0)--(10,0)); draw((0,0)--(0,10)); draw((10,0)--(10,10)); draw((0,10)--(10,10)); draw((1,6)--(0,9)); draw((1,6)--(0,6)); draw((1,6)--(4,6)); draw((4,6)--(4,10)); draw((0,9)--(3,10)); draw((3,10)--(4,7)); draw((4,7)--(1,6)); draw((0,3)--(1,6)); draw((1,6)--(10,3)); draw((10,3)--(9,0)); draw((9,0)--(0,3)); draw((6,13/3)--(10,22/3)); draw((10,22/3)--(8,10)); draw((8,10)--(4,7)); draw((4,7)--(6,13/3)); label("$3$",(9/2,3/2),N); label("$3$",(11/2,9/2),S); label("$1$",(1/2,9/2),E); label("$1$",(19/2,3/2),W); label("$1$",(1/2,15/2),E); label("$1$",(3/2,19/2),S); label("$1$",(5/2,13/2),N); label("$1$",(7/2,17/2),W); label("$R$",(7,43/6),W); label("$b$",(-1/8,9/2),W); label("$b$",(-1/8,7),W); label("$a$",(1/3,6),N); label("$a$",(-1/8,28/3),W); label("$b$",(1,81/8),N); label("$b$",(3,6),N); label("$a$",(401/100,13/2),W); label("$b$",(401/100,17/2),E); label("$a$",(7/2,81/8),N); [/asy]
We see that this creates two congruent triangles. Let the smaller side of the triangle have length $a$ and let the larger side of the triangle have length $b$ . Now we see by AAS congruency that if we draw perpendiculars that surround the smaller square, each outer triangle will be congruent to these two triangles.
Now notice that these small triangles are also similar to the large triangle bounded by the bigger square and the rectangle by AA, and the ratio of the sides are 1:3, so we can fill in the lengths of that triangle. Similarly, the small triangle on the right bounded by the rectangle and the square is also congruent to the other small triangles by AAS, so we can fill in those sides;
[asy] size(8cm); draw((0,0)--(10,0)); draw((0,0)--(0,10)); draw((10,0)--(10,10)); draw((0,10)--(10,10)); draw((1,6)--(0,9)); draw((1,6)--(0,6)); draw((1,6)--(4,6)); draw((4,6)--(4,10)); draw((0,9)--(3,10)); draw((3,10)--(4,7)); draw((4,7)--(1,6)); draw((0,3)--(1,6)); draw((1,6)--(10,3)); draw((10,3)--(9,0)); draw((9,0)--(0,3)); draw((6,13/3)--(10,22/3)); draw((10,22/3)--(8,10)); draw((8,10)--(4,7)); draw((4,7)--(6,13/3)); label("$3$",(9/2,3/2),N); label("$3$",(11/2,9/2),S); label("$1$",(1/2,9/2),E); label("$1$",(19/2,3/2),W); label("$1$",(1/2,15/2),E); label("$1$",(3/2,19/2),S); label("$1$",(5/2,13/2),N); label("$1$",(7/2,17/2),W); label("$R$",(7,43/6),W); label("$b$",(-1/8,9/2),W); label("$b$",(-1/8,7),W); label("$a$",(1/3,6),N); label("$a$",(-1/8,28/3),W); label("$b$",(1,81/8),N); label("$b$",(3,6),N); label("$a$",(401/100,13/2),W); label("$b$",(401/100,17/2),E); label("$a$",(7/2,81/8),N); label("$3a$",(-1/8,1),W); label("$3b$",(4,-1/8),S); label("$a$",(19/2,-1/8),S); label("$b$",(81/8,1),E); [/asy]
Since the larger square by definition has all equal sides, we can set the sum of the lengths of the sides equal to each other. $3a+b+b+a = 3b+a \implies 3a = b$ . Now let's draw some more perpendiculars and rename the side lengths.
[asy] size(8cm); draw((0,0)--(10,0)); draw((0,0)--(0,10)); draw((10,0)--(10,10)); draw((0,10)--(10,10)); draw((1,6)--(0,9)); draw((1,6)--(0,6)); draw((1,6)--(4,6)); draw((4,6)--(4,10)); draw((0,9)--(3,10)); draw((3,10)--(4,7)); draw((4,7)--(1,6)); draw((0,3)--(1,6)); draw((1,6)--(10,3)); draw((10,3)--(9,0)); draw((9,0)--(0,3)); draw((6,13/3)--(10,22/3)); draw((10,22/3)--(8,10)); draw((8,10)--(4,7)); draw((4,7)--(6,13/3)); draw((6,13/3)--(10,13/3)); label("$3$",(9/2,3/2),N); label("$3$",(11/2,9/2),S); label("$1$",(1/2,9/2),E); label("$1$",(19/2,3/2),W); label("$1$",(1/2,15/2),E); label("$1$",(3/2,19/2),S); label("$1$",(5/2,13/2),N); label("$1$",(7/2,17/2),W); label("$R$",(7,43/6),W); label("$3a$",(-1/8,9/2),W); label("$3a$",(-1/8,7),W); label("$a$",(1/3,6),N); label("$a$",(-1/8,28/3),W); label("$3a$",(1,81/8),N); label("$3a$",(3,6),N); label("$a$",(401/100,13/2),W); label("$3a$",(401/100,17/2),E); label("$a$",(7/2,81/8),N); label("$3a$",(-1/8,1),W); label("$9a$",(4,-1/8),S); label("$a$",(19/2,-1/8),S); label("$3a$",(81/8,1),E); label("$c$",(81/8,15/4),E); label("$3a$",(81/8,35/6),E); label("$3c$",(9,17/4),N); [/asy]
By AA similarity, when we draw a perpendicular from the intersection of the two rectangles to the large square, we create a triangle below that is similar to the small congruent triangles with length $a,3a$ . Since we don't know its scale, we'll label its sides $c,3c$ .
The triangle that is created above the perpendicular is congruent to the triangle on the opposite of the rectangle with unknown dimensions because they share the same hypotenuse and have two angles in common. Thus we can label these two triangles accordingly.
The side length of the big square is $10a$ , so we can find the remaining dimensions of the triangle bounded by the rectangle with unknown dimensions and the large square in terms of $a$ and $c$ :
[asy] size(8cm); draw((0,0)--(10,0)); draw((0,0)--(0,10)); draw((10,0)--(10,10)); draw((0,10)--(10,10)); draw((1,6)--(0,9)); draw((1,6)--(0,6)); draw((1,6)--(4,6)); draw((4,6)--(4,10)); draw((0,9)--(3,10)); draw((3,10)--(4,7)); draw((4,7)--(1,6)); draw((0,3)--(1,6)); draw((1,6)--(10,3)); draw((10,3)--(9,0)); draw((9,0)--(0,3)); draw((6,13/3)--(10,22/3)); draw((10,22/3)--(8,10)); draw((8,10)--(4,7)); draw((4,7)--(6,13/3)); draw((6,13/3)--(10,13/3)); label("$3$",(9/2,3/2),N); label("$3$",(11/2,9/2),S); label("$1$",(1/2,9/2),E); label("$1$",(19/2,3/2),W); label("$1$",(1/2,15/2),E); label("$1$",(3/2,19/2),S); label("$1$",(5/2,13/2),N); label("$1$",(7/2,17/2),W); label("$R$",(7,43/6),W); label("$3a$",(-1/8,9/2),W); label("$3a$",(-1/8,7),W); label("$a$",(1/3,6),N); label("$a$",(-1/8,28/3),W); label("$3a$",(1,81/8),N); label("$3a$",(3,6),N); label("$a$",(401/100,13/2),W); label("$3a$",(401/100,17/2),E); label("$a$",(7/2,81/8),N); label("$3a$",(-1/8,1),W); label("$9a$",(4,-1/8),S); label("$a$",(19/2,-1/8),S); label("$3a$",(81/8,1),E); label("$c$",(81/8,15/4),E); label("$3a$",(81/8,35/6),E); label("$3c$",(9,17/4),N); label("$3c$",(6,81/8),N); label("$6a-3c$",(9,81/8),N); label("$4a-c$",(81/8,9),E); [/asy]
This triangle with side lengths $4a-c$ and $6a-3c$ is similar to the triangle directly below it with side lengths $3a$ and $3c$ by AA similarity, so we can set up a ratio equation: $\frac{3a}{3c} = \frac{6a-3c}{4a-c} \implies 4a^2-ac = -3c^2 + 6ac \implies 4a^2 - 7ac + 3c^2 = 0 \implies (4a-3c)(a-c) = 0$ . There are two solutions to this equation; $c = \frac{4}{3}a$ and $c = a$ . For the first solution, the triangle in the corner has sides $2a$ and $\frac{8}{3}a$ . Using Pythagorean theorem on that triangle, the hypotenuse has length $\frac{10}{3}a$ . The triangle directly below has side lengths $3a$ and $4a$ in this case, so special right triangle yields the hypotenuse to be $5a$ . The area of the rectangle is thus $5a\cdot\frac{10}{3}a = \frac{50}{3}a^2$ . For the second solution, the side lengths of the corner triangle are $3a$ and $3a$ , so the hypotenuse of the triangle is $3\sqrt{2}a$ . The triangle below that also has side lengths $3a$ and $3a$ , so its hypotenuse is the same. Then the area of the rectangle is $(3\sqrt{2}a)^2 = 18a^2$ .
The sum of the possible areas of the rectangle is therefore $18a^2+\frac{50}{3}a^2 = \frac{104}{3}a^2$ .
Using Pythagorean theorem on the original small congruent triangles, $a^2+9a^2 = 1$ or $a^2 = \frac{1}{10}$ . Therefore the sum of the possible areas of the rectangle is $\frac{104}{3}\cdot\frac{1}{10} = \frac{52}{15}$ . Therefore $m = 52$ , $n = 15$ , and $m + n = 67 = \boxed{E}$
~KingRavi

## Solution 2
We use Image:2021_AMC_10B_(Nov)_Problem_25,_sol.png to facilitate our analysis.
Denote $\angle AFE = \theta$ . Thus, $\angle FIB = \angle CEF = \angle EKG = \angle KLC = \theta$ .
Hence, \begin{align*} AB & = AF + FB \\ & = EF \cos \angle EFA + IF \sin \angle FIB \\ & = 3 \cos \theta + \sin \theta , \end{align*} and \begin{align*} AC & = AE + EK + KC \\ & = EF \sin \angle EFA + EG \cos \angle CEG + KG \cos \angle EKG + KL \sin \angle CLK \\ & = 3 \sin \theta + \cos \theta + \cos \theta + \sin \theta \\ & = 2 \cos \theta + 4 \sin \theta . \end{align*}
Because $AB = AC$ , $3 \cos \theta + \sin \theta = 2 \cos \theta + 4 \sin \theta$ . Hence, $\tan \theta = \frac{1}{3}$ . Hence, $\sin \theta = \frac{1}{\sqrt{10}}$ and $\cos \theta = \frac{3}{\sqrt{10}}$ .
Hence, $AB = AC = BD = CD = \sqrt{10}$ .
Now, we put the graph to a coordinate plane by setting point $A$ as the origin, putting $AB$ in the $x$ -axis and $AC$ on the $y$ -axis.
Hence, $A = \left( 0 , 0 \right)$ , $B = \left( \sqrt{10} , 0 \right)$ , $C = \left( 0 , \sqrt{10} \right)$ , $D = \left( \sqrt{10} , \sqrt{10} \right)$ , $E = \left( 0 , \frac{3}{\sqrt{10}} \right)$ , $F = \left( \frac{9}{\sqrt{10}} , 0 \right)$ , $G = \left( \frac{1}{\sqrt{10}} , \frac{6}{\sqrt{10}} \right)$ , $H = \left( \frac{4}{\sqrt{10}} , \frac{7}{\sqrt{10}} \right)$ , $I = \left( \sqrt{10} , \frac{3}{\sqrt{10}} \right)$ .
Denote $P = \left( \frac{10 - u}{\sqrt{10}} , \sqrt{10} \right)$ , $Q = \left( \sqrt{10} , \frac{10 - v}{\sqrt{10}} \right)$ .
Because $HPQJ$ is a rectangle, $HP \perp PQ$ . Hence, $m_{HP} m_{PQ} = -1$ . We have $m_{HP} = \frac{3}{6 - u}$ and $m_{PQ} = - \frac{v}{u}$ . Hence, \[ \frac{3}{6 - u} \cdot \left( - \frac{v}{u} \right) = - 1 . \hspace{1cm} (1) \]
Because $HPQJ$ is a rectangle, $x_J + x_P = x_H + x_Q$ and $y_J + y_P = y_H + y_Q$ . Hence, $J = \left( \frac{4 + u}{\sqrt{10}} , \frac{7 - v}{\sqrt{10}} \right)$ .
The equation of line $GI$ is \begin{align*} y & = \frac{\frac{3}{\sqrt{10}} - \frac{6}{\sqrt{10}}}{\sqrt{10} - \frac{1}{\sqrt{10}}} \left( x - \frac{1}{\sqrt{10}} \right) + \frac{6}{\sqrt{10}} \\ & = - \frac{x}{3} + \frac{19}{3 \sqrt{10}} . \end{align*} Because point $J$ is on line $GI$ , plugging the coordinates of $J$ into the equation of line $GI$ , we get \[ \frac{7 - v}{\sqrt{10}} = - \frac{\frac{4 + u}{\sqrt{10}}}{3} + \frac{19}{3 \sqrt{10}} . \hspace{1cm} (2) \]
By solving Equations (1) and (2), we get $\left( u , v \right) = \left( 2 , \frac{8}{3} \right)$ or $\left( 3 , 3 \right)$ .
Case 1: $\left( u , v \right) = \left( 2 , \frac{8}{3} \right)$ .
We have $P = \left( \frac{8}{\sqrt{10}} , \sqrt{10} \right)$ and $Q = \left( \sqrt{10} , \frac{22}{3 \sqrt{10}} \right)$ . Thus, $HP = \frac{5}{\sqrt{10}}$ and $PQ = \frac{10}{3\sqrt{10}}$ .
Therefore, ${\rm Area} \ R = HP \cdot PQ = \frac{5}{3}$ .
Case 2: $\left( u , v \right) = \left( 3 , 3 \right)$ .
We have $P = \left( \frac{7}{\sqrt{10}} , \sqrt{10} \right)$ and $Q = \left( \sqrt{10} , \frac{7}{ \sqrt{10}} \right)$ . Thus, $HP = \frac{3 \sqrt{2}}{\sqrt{10}}$ and $PQ = \frac{3 \sqrt{2}}{\sqrt{10}}$ .
Therefore, ${\rm Area} \ R = HP \cdot PQ = \frac{9}{5}$ .
Putting these two cases together, the sum of all possible values of the area of $R$ is $\frac{5}{3} + \frac{9}{5} = \frac{52}{15}$ .
Therefore, the answer is $\boxed{\textbf{(E) }67}$ .
~Steven Chen (www.professorchenedu.com)

## Solution 3
[asy] size(8cm); label("D",(0,0),SW); label("A",(0,10),NW); label("B",(10,10),NE); label("C",(10,0),SE); label("H",(1,5.7),SE); label("O",(0,6),W); label("I",(0,3),W); draw((0,0)--(10,0)); draw((0,0)--(0,10)); draw((10,0)--(10,10)); draw((0,10)--(10,10)); draw((1,6)--(0,9)); draw((0,9)--(3,10)); draw((3,10)--(4,7)); draw((4,7)--(1,6)); draw((0,3)--(1,6)); draw((1,6)--(10,3)); draw((10,3)--(9,0)); draw((9,0)--(0,3)); draw((6,13/3)--(10,22/3)); draw((10,22/3)--(8,10)); draw((8,10)--(4,7)); draw((4,7)--(6,13/3)); draw((1,6)--(0,6)); label("$3$",(9/2,3/2),N); label("$3$",(11/2,9/2),S); label("$1$",(1/2,9/2),E); label("$1$",(19/2,3/2),W); label("$1$",(1/2,15/2),E); draw((0.3,6)--(0.3,5.7)--(0,5.7)); label("$1$",(3/2,19/2),S); label("$1$",(5/2,13/2),N); label("$1$",(7/2,17/2),W); label("$R$",(7,43/6),W); label("E",(0,9),W); label("F",(3,10),N); label("P",(4,10),N); label("L",(8,10),N); draw((4,7)--(4,10)); draw((4,9.7)--(4.3,9.7)--(4.3,10)); label("G",(3.9,6.8),S); label("N",(6.2,4.1),S); label("M",(10,22/3),E); label("Q",(10,13/3),E); draw((10,13/3)--(6,13/3)); draw((9.7,13/3)--(9.7,4.033333333333333333333333)--(10,4.03333333333333333333333333)); label("K",(10,3),E); label("J",(9,0),S); [/asy] We will scale every number up by a factor of $\sqrt{10}.$ This implies our final area will be $\frac{1}{10}$ of the answer we receive.
We have \[FAE\sim EOH \sim IOH\sim JDI\sim KCJ \sim NQK\sim GPF.\] Let $AE=a$ and $FA=b.$ We have \[FP=AE=OH=JC=\frac13ID=a\] and \[PG=AF=EO=OI=KC=\frac13 DJ=b\] As $ABCD$ is a square, we have $AD=DC$ or \[a+2b+3a=3b+a \Rightarrow 3a=b.\] Since $a^2+b^2=10,$ we have \[a=1,b=3.\] We have $\triangle GPL\cong \triangle MQN$ which implies \[MQ=GP=3.\] Denote $QK=x.$ As $\triangle NQK\sim \triangle JDI,$ we have $NQ=3x.$
We have \begin{align*}BM&=BC-(CK+QK+MQ)\\ &=4-x.\end{align*}
In addition, \begin{align*}LB&=AB-(AF+FP+PL)\\&=6-3x.\end{align*}
Since $\triangle LBM\sim \triangle MQN,$ we have \[\frac{LB}{BM}=\frac{MQ}{QN}\Rightarrow \frac{6-3x}{4-x}=\frac{3}{3x}=\frac{1}{x}.\] Simplifying we have \[3x^2-7x+4=0 \Rightarrow x=\frac43, 1.\] We have \begin{align*}[GLMN]&=MN\cdot LM\\ &= 3\sqrt{x^2+1}\cdot \sqrt{10x^2-44x+52}.\end{align*}
Plugging in $x=1,$ we have $[GLMN]=18.$
Plugging in $x=\frac43,$ we have $[GLMN]=\frac{50}{3}.$
The sum of the two possible $R$ s is \[\frac{1}{10}\cdot\frac{104}{3}=\frac{52}{15}.\] Hence, $52+15=\boxed{\textbf{(E) }67}.$
~ASAB

## Solution 4
We use the same diagram as solution 3, without scaling by $\sqrt{10}$ . Denote $S$ the foot from $G$ to $HN$ . Using the same method, obtain $JC=\frac{1}{\sqrt{10}}$ and $KC=\frac{3}{\sqrt{10}}$ .
We have $\angle GHS = 2 \angle HIO \Longrightarrow \sin \angle GHS = 2 \sin \angle HIO \cos \angle HIO = \frac{3}{5}$ , so $GS = \frac{3}{5}$ , and $HS=\frac{4}{5}$ .
Denote $x=KN$ , then $SN=HK-HS-NK=\frac{11-5x}{5}$ , and $NQ=\frac{3x}{\sqrt{10}}$ .
Also, $\triangle NQM \cong \triangle LPG$ because they're similar by $AA$ , and then $LG=NM$ , so $MQ=PG=\frac{3}{\sqrt{10}}$ .
Thus $\tan \angle KNQ = \frac{1}{3}$ and $\tan \angle QNM = \frac{1}{x}$ . Then $\cot \angle GNS = \tan (90 ^{\circ} - \angle GNS) = \tan \angle KNM = \tan (\angle KNQ + \angle QNM) = \frac{\tan \angle KNQ + \tan \angle QNM}{1-\tan \angle KNQ \tan \angle QNM}$
which simplifies to
$\frac{11-5x}{3}=\frac{3+x}{3x-1}$
Cross multiplying gives
$3x^2-7x+4=0$ , with solutions $x=1,\frac{4}{3}$ .
Plugging these back into the setup gives areas of $\frac{9}{5}$ and $\frac{5}{3}$ , respectively, which have sum $\frac{52}{15}$ , and thus the answer is $52+15=\boxed{\textbf{(E) }67}.$
~mathfan2020

## Video Solution
https://www.youtube.com/watch?v=5mPvkipCvhE

## Video Solution by Interstigation
https://www.youtube.com/watch?v=o3_1GF11A2A
~Interstigation

## Video Solution by WhyMath
https://youtu.be/xc9-Wl_1n9k
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
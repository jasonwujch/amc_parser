# 2019 AMC 8 Problem 24

## Problem

In triangle $\triangle ABC$ , point $D$ divides side $\overline{AC}$ so that $AD:DC=1:2$ . Let $E$ be the midpoint of $\overline{BD}$ and let $F$ be the point of intersection of line $\overline{BC}$ and line $\overline{AE}$ . Given that the area of $\triangle ABC$ is $360$ , what is the area of $\triangle EBF$ ?

[asy] unitsize(2cm); pair A,B,C,DD,EE,FF; B = (0,0); C = (3,0); A = (1.2,1.7); DD = (2/3)*A+(1/3)*C; EE = (B+DD)/2; FF = intersectionpoint(B--C,A--A+2*(EE-A)); draw(A--B--C--cycle); draw(A--FF); draw(B--DD);dot(A); label("$A$",A,N); dot(B); label("$B$", B,SW);dot(C); label("$C$",C,SE); dot(DD); label("$D$",DD,NE); dot(EE); label("$E$",EE,NW); dot(FF); label("$F$",FF,S); [/asy]

$\textbf{(A) }24\qquad\textbf{(B) }30\qquad\textbf{(C) }32\qquad\textbf{(D) }36\qquad\textbf{(E) }40$

## Solution 1
We use the line-segment ratios to infer area ratios and height ratios.
Areas:
$AD:DC = 1:2 \implies AD:AC = 1:3 \implies [ABD] =\frac{[ABC]}{3} = 120$ .
$BE:BD = 1:2 \text{ (midpoint)} \implies [ABE] = \frac{[ABD]}{2} = \frac{120}{2} = 60$ .
Heights:
Let $h_A$ = height (of altitude) from $\overline{BC}$ to $A$ .
$AD:DC = 1:2 \implies CD:CA = 2:3 \implies \text{height } h_D$ from $\overline{BC}$ to $D$ is $\frac{2}{3}h_A$ .
$BE:BD = 1:2 \text{ (midpoint)} \implies \text{height } h_E$ from $\overline{BC}$ to $E$ is $\frac{1}{2} h_D = \frac{1}{2}(\frac{2}{3} h_A) = \frac{1}{3} h_A$ .
Conclusion:
$\frac{[EBF]} {[ABF]} = \frac{[EBF]} {[EBF] + [ABE]} = \frac{[EBF]} {[EBF]+60}$ , and also $\frac{[EBF]} {[ABF]} = \frac{h_E}{h_A} = \frac{1}{3}$ .
So, $\frac{[EBF]} {[EBF] + 60} = \frac{1}{3}$ , and thus, $[EBF] = \boxed{\textbf{(B) }30}$

## Solution 2
Draw $X$ on $\overline{AF}$ such that $\overline{XD}$ is parallel to $\overline{BC}$ .
Triangles $BEF$ and $EXD$ are similar, and since $BE = ED$ , they are also congruent, and so $XE=EF$ and $XD=BF$ .
$AC:AD = 3$ implies $\frac{AF}{AX} = 3 = \frac{FC}{XD} = \frac{FC}{BF}$ , so $BC=BF + 3BF = 4BF$ , $BF=\frac{BC}{4}$ .
Since $XE=EF$ , $AX = XE = EF$ , and since $AX + XE + EF = AF$ , all of these are equal to $\frac{AF}{3}$ , and so the altitude of triangle $BEF$ is equal to $\frac{1}{3}$ of the altitude of $ABC$ .
The area of $ABC$ is $360$ , so the area of $\triangle EBF=\frac{1}{3} \cdot \frac{1}{4} \cdot 360=\boxed{\textbf{(B) }30}$ .

## Solution 3(Mass point method, AMC10 tricks)
[asy] /* Geogebra to Asymptote conversion, documentation at artofproblemsolving.com/Wiki go to User:Azjps/geogebra */ import graph; size(7cm); real labelscalefactor = 0.5; /* changes label-to-point distance */ pen dps = linewidth(0.7) + fontsize(10); defaultpen(dps); /* default pen style */ pen dotstyle = black; /* point style */ real xmin = -6.28, xmax = 6.28, ymin = -5.49, ymax = 5.73; /* image dimensions */ pen wrwrwr = rgb(0.3803921568627451,0.3803921568627451,0.3803921568627451); /* draw figures */ draw((0.28,2.39)--(-2.8,-1.17), linewidth(2) + wrwrwr); draw((-2.8,-1.17)--(3.78,-1.05), linewidth(2) + wrwrwr); draw((3.78,-1.05)--(0.28,2.39), linewidth(2) + wrwrwr); draw((-2.8,-1.17)--(1.2887445398528459,1.3985482236874887), linewidth(2) + wrwrwr); draw((0.28,2.39)--(-0.7199623188673492,-1.1320661821070033), linewidth(2) + wrwrwr); draw(circle((-0.1,2.93), 0.46818799642878495), linewidth(2) + wrwrwr); draw(circle((-0.1,2.93), 0.46818799642878495), linewidth(2) + wrwrwr); draw(circle((4.48,-1.28), 0.46818799642878506), linewidth(2) + wrwrwr); draw(circle((1.98,1.56), 0.46818799642878495), linewidth(2) + wrwrwr); draw(circle((-3.36,-1.62), 0.46818799642878517), linewidth(2) + wrwrwr); draw(circle((0.16,0.14), 0.46818799642878495), linewidth(2) + wrwrwr); draw(circle((-0.74,-1.81), 0.46818799642878495), linewidth(2) + wrwrwr); /* dots and labels */ dot((0.28,2.39),dotstyle); label("$A$", (0.36,2.59), NE * labelscalefactor); dot((-2.8,-1.17),dotstyle); label("$B$", (-2.72,-0.97), NE * labelscalefactor); dot((3.78,-1.05),dotstyle); label("$C$", (3.86,-0.85), NE * labelscalefactor); dot((1.2887445398528459,1.3985482236874887),dotstyle); label("$D$", (1.36,1.59), NE * labelscalefactor); dot((-0.7199623188673492,-1.1320661821070033),dotstyle); label("$F$", (-0.64,-0.93), NE * labelscalefactor); dot((-0.2815567696989588,0.41208536204620183),linewidth(4pt) + dotstyle); label("$E$", (-0.2,0.57), NE * labelscalefactor); label("2", (-0.18,2.81), NE * labelscalefactor,wrwrwr); label("1", (4.4,-1.39), NE * labelscalefactor,wrwrwr); label("3", (1.9,1.45), NE * labelscalefactor,wrwrwr); label("3", (-3.44,-1.73), NE * labelscalefactor,wrwrwr); label("6", (0.08,0.03), NE * labelscalefactor,wrwrwr); label("4", (-0.82,-1.93), NE * labelscalefactor,wrwrwr); clip((xmin,ymin)--(xmin,ymax)--(xmax,ymax)--(xmax,ymin)--cycle); /* end of picture */ [/asy]
First, when we see the problem, we see ratios, and we see that this triangle basically has no special properties (right, has medians, etc.) and this screams mass points at us.
The triangle we will consider is $\triangle ABC$ (obviously), and we will let $E$ be the center of mass, so that $D$ balances $A$ and $C$ (this is true since $E$ balances $B$ and $D$ , but $E$ also balances $A$ and $B$ and $C$ so $D$ balances $A$ and $C$ ), and $F$ balances $B$ and $C$ .
We know that $AD:CD=1:2$ and $D$ balances $A$ and $C$ so we assign $2$ to $A$ and $1$ to $C$ . Then, since $D$ balances $A$ and $C$ , we get $D = A + C = 2 + 1 = 3$ (by mass points addition).
Next, since $E$ balances $B$ and $D$ in a ratio of $BE:DE=1:1$ , we know that $B=D=3$ . Similarly, by mass points addition, $E=B+D=3+3=6$ .
Finally, $F$ balances $B$ and $C$ so $F=B+C=3+1=4$ . We can confirm we have done everything right by noting that $E$ balances $A$ and $F$ , so $E$ should equal $A+F$ , which it does.
Now that our points have weights, we can solve the problem. $BF:FC=1:3$ so $BF:BC=1:4$ so $[ABF]=\frac{1}{4}[ABC]=90$ . Also, $EF:EA=2:4=1:2$ so $EF:AF=1:3$ so $[EBF]=\frac{1}{3}[ABF]=\boxed{\textbf{(B) }30}$ .
-Firebolt360 and Brudder
Note: We can also find the ratios of the areas using the reciprocal of the product of the mass points of $EBF$ over the product of the mass points of $ABC$ which is $\frac{2\times3\times1}{3\times6\times4}\times360$ which also yields $\boxed{\textbf{(B) }30}$ .
-Brudder

## Solution 4
$\frac{BF}{FC}$ is equal to $\frac{\textrm{The area of triangle ABE}}{\textrm{The area of triangle ACE}}$ . The area of triangle $ABE$ is equal to $60$ because it is equal to one-half of the area of triangle $ABD$ , which is equal to one-third of the area of triangle $ABC$ , which is $360$ . The area of triangle $ACE$ is the sum of the areas of triangles $AED$ and $CED$ , which is respectively $60$ and $120$ . So, $\frac{BF}{FC}$ is equal to $\frac{60}{180}$ = $\frac{1}{3}$ , so the area of triangle $ABF$ is $90$ . That minus the area of triangle $ABE$ is $\boxed{\textbf{(B) }30}$ .
~~SmileKat32

## Solution 5 (Similar Triangles)
Extend $\overline{BD}$ to $G$ such that $\overline{AG} \parallel \overline{BC}$ as shown: [asy] size(8cm); pair A, B, C, D, E, F, G; B = (0,0); A = (2, 3); C = (5, 0); D = (3, 2); E = (1.5, 1); F = (1.25, 0); G = (4.5, 3); draw(A--B--C--A--G--B); draw(A--F); label("$A$", A, N); label("$B$", B, WSW); label("$C$", C, ESE); label("$D$", D, dir(0)*1.5); label("$E$", E, SE); label("$F$", F, S); label("$G$", G, ENE); [/asy] Then, $\triangle ADG \sim \triangle CDB$ and $\triangle AEG \sim \triangle FEB$ . Since $CD = 2AD$ , triangle $CDB$ has four times the area of triangle $ADG$ . Since $[CDB] = 240$ , we get $[ADG] = 60$ .
Since $[AED]$ is also $60$ , we have $ED = DG$ because triangles $AED$ and $ADG$ have the same height and same areas and so their bases must be the congruent. Thus, triangle $AEG$ has twice the side lengths and therefore four times the area of triangle $BEF$ , giving $[BEF] = (60+60)/4 = \boxed{\textbf{(B) }30}$ .
[asy] size(8cm); pair A, B, C, D, E, F, G; B = (0,0); A = (2, 3); C = (5, 0); D = (3, 2); E = (1.5, 1); F = (1.25, 0); G = (4.5, 3); draw(A--B--C--A--G--B); draw(A--F); label("$A$", A, N); label("$B$", B, WSW); label("$C$", C, ESE); label("$D$", D, dir(0)*1.5); label("$E$", E, SE); label("$F$", F, S); label("$G$", G, ENE); label("$60$", (A+E+D)/3); label("$60$", (A+E+B)/3); label("$60$", (A+G+D)/3); label("$30$", (B+E+F)/3); [/asy] (Credit to MP8148 for the idea)

## Solution 6 (Area Ratios)
[asy] size(8cm); pair A, B, C, D, E, F; B = (0,0); A = (2, 3); C = (5, 0); D = (3, 2); E = (1.5, 1); F = (1.25, 0); draw(A--B--C--A--D--B); draw(A--F); draw(E--C); label("$A$", A, N); label("$B$", B, WSW); label("$C$", C, ESE); label("$D$", D, dir(0)*1.5); label("$E$", E, SSE); label("$F$", F, S); label("$60$", (A+E+D)/3); label("$60$", (A+E+B)/3); label("$120$", (D+E+C)/3); label("$x$", (B+E+F)/3); label("$120-x$", (F+E+C)/3); [/asy] As before, we figure out the areas labeled in the diagram. Then, we note that \[\dfrac{EF}{AE} = \dfrac{x}{60} = \dfrac{120-x}{180}\] Even simpler: \[\dfrac{EF}{AE} = \dfrac{x}{60} = \dfrac{120}{240}\] Solving gives $x = \boxed{\textbf{(B) }30}$ . (Credit to scrabbler94 for the idea)

## Solution 7 (Coordinate Bashing)
Let $ADB$ be a right triangle, and $BD=CD$
Let $A=(-2\sqrt{30}, 0)$
$B=(0, 4\sqrt{30})$
$C=(4\sqrt{30}, 0)$
$D=(0, 0)$
$E=(0, 2\sqrt{30})$
$F=(\sqrt{30}, 3\sqrt{30})$
The line $\overleftrightarrow{AE}$ can be described with the equation $y=x-2\sqrt{30}$
The line $\overleftrightarrow{BC}$ can be described with $x+y=4\sqrt{30}$
Solving, we get $x=3\sqrt{30}$ and $y=\sqrt{30}$
Now we can find $EF=BF=2\sqrt{15}$
$[\bigtriangleup EBF]=\frac{(2\sqrt{15})^2}{2}=\boxed{\textbf{(B) }30}$
-Trex4days

## Solution 8
[asy] /* Geogebra to Asymptote conversion, documentation at artofproblemsolving.com/Wiki go to User:Azjps/geogebra */ import graph; size(15cm); real labelscalefactor = 0.5; /* changes label-to-point distance */ pen dps = linewidth(0.7) + fontsize(10); defaultpen(dps); /* default pen style */ pen dotstyle = black; /* point style */ real xmin = -6.61, xmax = 16.13, ymin = -6.4, ymax = 6.42; /* image dimensions */ /* draw figures */ draw(circle((0,0), 5), linewidth(2)); draw((-4,-3)--(4,3), linewidth(2)); draw((-4,-3)--(0,5), linewidth(2)); draw((0,5)--(4,3), linewidth(2)); draw((12,-1)--(-4,-3), linewidth(2)); draw((0,5)--(0,-5), linewidth(2)); draw((-4,-3)--(0,-5), linewidth(2)); draw((4,3)--(0,2.48), linewidth(2)); draw((4,3)--(12,-1), linewidth(2)); draw((-4,-3)--(4,3), linewidth(2)); /* dots and labels */ dot((0,0),dotstyle); label("E", (0.27,-0.24), NE * labelscalefactor); dot((-5,0),dotstyle); dot((-4,-3),dotstyle); label("B", (-4.45,-3.38), NE * labelscalefactor); dot((4,3),dotstyle); label("$D$", (4.15,3.2), NE * labelscalefactor); dot((0,5),dotstyle); label("A", (-0.09,5.26), NE * labelscalefactor); dot((12,-1),dotstyle); label("C", (12.23,-1.24), NE * labelscalefactor); dot((0,-5),dotstyle); label("$G$", (0.19,-4.82), NE * labelscalefactor); dot((0,2.48),dotstyle); label("I", (-0.33,2.2), NE * labelscalefactor); dot((0,0),dotstyle); label("E", (0.27,-0.24), NE * labelscalefactor); dot((0,-2.5),dotstyle); label("F", (0.23,-2.2), NE * labelscalefactor); clip((xmin,ymin)--(xmin,ymax)--(xmax,ymax)--(xmax,ymin)--cycle); /* end of picture */ [/asy]
Let $A[\Delta XYZ]$ = $\text{Area of Triangle XYZ}$
$A[\Delta ABD]: A[\Delta DBC] :: 1:2 :: 120:240$
$A[\Delta ABE] = A[\Delta AED] = 60$ (the median divides the area of the triangle into two equal parts)
Construction: Draw a circumcircle around $\Delta ABD$ with $BD$ as is diameter. Extend $AF$ to $G$ such that it meets the circle at $G$ . Draw line $BG$ .
$A[\Delta ABD] = A[\Delta ABG] = 120$ (Since $\square ABGD$ is cyclic)
But $A[\Delta ABE]$ is common in both with an area of 60. So, $A[\Delta AED] = A[\Delta BEG]$ .
Therefore $A[\Delta AED] \cong A[\Delta BEG]$ (SAS Congruency Theorem).
In $\Delta AED$ , let $DI$ be the median of $\Delta AED$ ,
which means $A[\Delta AID] = 30 = A[\Delta EID]$ .
Rotate $\Delta DEA$ to meet $D$ at $B$ and $A$ at $G$ . $DE$ will fit exactly in $BE$ (both are radii of the circle). From the above solutions, $\frac{AE}{EF} = 2:1$ .
$AE$ is a radius and $EF$ is half of it implies $EF$ = $\frac{radius}{2}$ ,
which means $A[\Delta BEF] \cong A[\Delta DEI]$ .
Thus, $A[\Delta BEF] = \boxed{\textbf{(B) }30}$ .
~phoenixfire & flamewavelight

## Solution 9
[asy] import geometry; unitsize(2cm); pair A,B,C,DD,EE,FF, M; B = (0,0); C = (3,0); M = (1.45,0); A = (1.2,1.7); DD = (2/3)*A+(1/3)*C; EE = (B+DD)/2; FF = intersectionpoint(B--C,A--A+2*(EE-A)); draw(A--B--C--cycle); draw(A--FF); draw(B--DD);dot(A); label("$A$",A,N); dot(B); label("$B$", B,SW);dot(C); label("$C$",C,SE); dot(DD); label("$D$",DD,NE); dot(EE); label("$E$",EE,NW); dot(FF); label("$F$",FF,S); draw(EE--M,StickIntervalMarker(1,1)); label("$M$",M,S); draw(A--DD,invisible,StickIntervalMarker(1,1)); dot((DD+C)/2); draw(DD--C,invisible,StickIntervalMarker(2,1)); [/asy] Using the ratio of $\overline{AD}$ and $\overline{CD}$ , we find the area of $\triangle ADB$ is $120$ and the area of $\triangle BDC$ is $240$ . Also using the fact that $E$ is the midpoint of $\overline{BD}$ , we know $\triangle ADE = \triangle ABE = 60$ . Let $M$ be a point such $\overline{EM}$ is parellel to $\overline{CD}$ . We immediatley know that $\triangle BEM \sim BDC$ by $2$ . Using that we can conclude $EM$ has ratio $1$ . Using $\triangle EFM \sim \triangle AFC$ , we get $EF:AE = 1:2$ . Therefore using the fact that $\triangle EBF$ is in $\triangle ABF$ , the area has ratio $\triangle BEF : \triangle ABE=1:2$ and we know $\triangle ABE$ has area $60$ so $\triangle BEF$ is $\boxed{\textbf{(B) }30}$ .
- fath2012

## Solution 10 (Menelaus's Theorem)
[asy] unitsize(2cm); pair A,B,C,DD,EE,FF; B = (0,0); C = (3,0); A = (1.2,1.7); DD = (2/3)*A+(1/3)*C; EE = (B+DD)/2; FF = intersectionpoint(B--C,A--A+2*(EE-A)); draw(A--B--C--cycle); draw(A--FF); draw(B--DD);dot(A); label("$A$",A,N); dot(B); label("$B$", B,SW);dot(C); label("$C$",C,SE); dot(DD); label("$D$",DD,NE); dot(EE); label("$E$",EE,NW); dot(FF); label("$F$",FF,S); [/asy] By Menelaus's Theorem on triangle $BCD$ , we have \[\dfrac{BF}{FC} \cdot \dfrac{CA}{DA} \cdot \dfrac{DE}{BE} = 3\dfrac{BF}{FC} = 1 \implies \dfrac{BF}{FC} = \dfrac13 \implies \dfrac{BF}{BC} = \dfrac14.\] Therefore, \[[EBF] = \dfrac{BE}{BD}\cdot\dfrac{BF}{BC}\cdot [BCD] = \dfrac12 \cdot \dfrac 14 \cdot \left( \dfrac23 \cdot [ABC]\right) = \boxed{\textbf{(B) }30}.\]
Note: This is AMC 10-12 level, please do not learn this for the AMC 8.

## Solution 11 (Graph Paper)
[asy] unitsize(2cm); pair A,B,C,D,E,F,a,b,c,d,e,f; A = (2,3); B = (0,2); C = (2,0); D = (2/3)*A+(1/3)*C; E = (B+D)/2; F = intersectionpoint(B--C,A--A+2*(E-A)); a = (0,0); b = (1,0); c = (2,1); d = (1,3); e = (0,3); f = (0,1); draw(a--C,dashed); draw(f--c,dashed); draw(e--A,dashed); draw(a--e,dashed); draw(b--d,dashed); draw(A--B--C--cycle); draw(A--F); draw(B--D); dot(A); label("$A$",A,NE); dot(B); label("$B$",B,dir(180)); dot(C); label("$C$",C,SE); dot(D); label("$D$",D,dir(0)); dot(E); label("$E$",E,SE); dot(F); label("$F$",F,SW); [/asy] Note: If graph paper is unavailable, this solution can still be used by constructing a small grid on a sheet of blank paper. As triangle $ABC$ is loosely defined, we can arrange its points such that the diagram fits nicely on a coordinate plane. By doing so, we can construct it on graph paper and be able to visually determine the relative sizes of the triangles. As point $D$ splits line segment $\overline{AC}$ in a $1:2$ ratio, we draw $\overline{AC}$ as a vertical line segment $3$ units long. Point $D$ is thus $1$ unit below point $A$ and $2$ units above point $C$ . By definition, Point $E$ splits line segment $\overline{BD}$ in a $1:1$ ratio, so we draw $\overline{BD}$ $2$ units long directly left of $D$ and draw $E$ directly between $B$ and $D$ , $1$ unit away from both. We then draw line segments $\overline{AB}$ and $\overline{BC}$ . We can easily tell that triangle $ABC$ occupies $3$ square units of space. Constructing line $AE$ and drawing $F$ at the intersection of $AE$ and $BC$ , we can easily see that triangle $EBF$ forms a right triangle occupying $\frac{1}{4}$ of a square unit of space. The ratio of the areas of triangle $EBF$ and triangle $ABC$ is thus $\frac{1}{4}\div3=\frac{1}{12}$ , and since the area of triangle $ABC$ is $360$ , this means that the area of triangle $EBF$ is $\frac{1}{12}\times360=\boxed{\textbf{(B) }30}$ .
~ emerald_block Additional note: There are many subtle variations of this triangle; this method is one of the more compact ones.
~ i_equal_tan_90

## Solution 12
[asy] unitsize(2cm); pair A,B,C,DD,EE,FF,G; B = (0,0); C = (3,0); A = (1.2,1.7); DD = (2/3)*A+(1/3)*C; EE = (B+DD)/2; FF = intersectionpoint(B--C,A--A+2*(EE-A)); G = (1.5,0); draw(A--B--C--cycle); draw(A--FF); draw(B--DD); draw(G--DD); label("$A$",A,N); label("$B$", B,SW); label("$C$",C,SE); label("$D$",DD,NE); label("$E$",EE,NW); label("$F$",FF,S); label("$G$",G,S); [/asy] We know that $AD = \dfrac{1}{3} AC$ , so $[ABD] = \dfrac{1}{3} [ABC] = 120$ . Using the same method, since $BE = \dfrac{1}{2} BD$ , $[ABE] = \dfrac{1}{2} [ABD] = 60$ . Next, we draw $G$ on $\overline{BC}$ such that $\overline{DG}$ is parallel to $\overline{AF}$ and create segment $DG$ . We then observe that $\triangle AFC \sim \triangle DGC$ , and since $AD:DC = 1:2$ , $FG:GC$ is also equal to $1:2$ . Similarly (no pun intended), $\triangle DBG \sim \triangle EBF$ , and since $BE:ED = 1:1$ , $BF:FG$ is also equal to $1:1$ . Combining the information in these two ratios, we find that $BF:FG:GC = 1:1:2$ , or equivalently, $BF = \dfrac{1}{4} BC$ . Thus, $[BFA] = \dfrac{1}{4} [BCA] = 90$ . We already know that $[ABE] = 60$ , so the area of $\triangle EBF$ is $[BFA] - [ABE] = \boxed{\textbf{(B) }30}$ .
~ i_equal_tan_90

## Solution 13 (Fastest Solution if you have no time)
The picture is misleading. Assume that the triangle ABC is a right triangle.
Then, find two factors of $720$ that are the closest together so that the picture becomes easier in your mind. Quickly searching for squares near $720$ to use difference of squares, we find $24$ and $30$ as our numbers. Then, the coordinates of D are $(10,16)$ (note, A=0,0). E is then $(5,8)$ . Then the equation of the line AE is $-16x/5+24=y$ . Plugging in $y=0$ , we have $x=\dfrac{15}{2}$ . Now notice that we have both the height and the base of EBF.
Solving for the area, we have $(8)(15/2)(1/2)=30$ .

## Solution 14
$AD : DC = 1:2$ , so $ADB$ has area $120$ and $CDB$ has area $240$ . $BE = ED$ so the area of $ABE$ is equal to the area of $ADE = 60$ . Draw $\overline{DG}$ parallel to $\overline{AF}$ . Set area of BEF = $x$ . BEF is similar to BDG in ratio of 1:2 so area of BDG = $4x$ , area of EFDG= $3x$ , and area of CDG $=240-4x$ . CDG is similar to CAF in ratio of 2:3 so area CDG = $4/9$ area CAF, and area AFDG= $5/4$ area CDG. Thus, $60+3x=5/4(240-4x)$ and $x=30$ .
~EFrame

## Solution 15 - Geometry & Algebra
[asy] unitsize(2cm); pair A,B,C,DD,EE,FF; B = (0,0); C = (3,0); A = (1.2,1.7); DD = (2/3)*A+(1/3)*C; EE = (B+DD)/2; FF = intersectionpoint(B--C,A--A+2*(EE-A)); draw(A--B--C--cycle); draw(A--FF); draw(DD--FF,blue); draw(B--DD);dot(A); label("$A$",A,N); dot(B); label("$B$", B,SW);dot(C); label("$C$",C,SE); dot(DD); label("$D$",DD,NE); dot(EE); label("$E$",EE,NW); dot(FF); label("$F$",FF,S); [/asy]
We draw line $FD$ so that we can define a variable $x$ for the area of $\triangle BEF = \triangle DEF$ . Knowing that $\triangle ABE$ and $\triangle ADE$ share both their height and base, we get that $ABE = ADE = 60$ .
Since we have a rule where 2 triangles, ( $\triangle A$ which has base $a$ and vertex $c$ ), and ( $\triangle B$ which has Base $b$ and vertex $c$ )who share the same vertex (which is vertex $c$ in this case), and share a common height, their relationship is : Area of $A : B = a : b$ (the length of the two bases), we can list the equation where $\frac{ \triangle ABF}{\triangle ACF} = \frac{\triangle DBF}{\triangle DCF}$ . Substituting $x$ into the equation we get:
\[\frac{x+60}{300-x} = \frac{2x}{240-2x}\] \[(2x)(300-x) = (60+x)(240-x)\] \[600-2x^2 = 14400 - 120x + 240x - 2x^2\] \[480x = 14400\] and we now have that $\triangle BEF=30$ .
~ $\bold{\color{blue}{onionheadjr}}$

## Solution 16 (Straightfoward & Simple Solution)
[asy] size(8cm); pair A, B, C, D, E, F; B = (0,0); A = (2, 3); C = (5, 0); D = (3, 2); E = (1.5, 1); F = (1.25, 0); draw(A--B--C--A--D--B); draw(A--F); draw(E--C); label("$A$", A, N); label("$B$", B, WSW); label("$C$", C, ESE); label("$D$", D, dir(0)*1.5); label("$E$", E, SSE); label("$F$", F, S); label("$60$", (A+E+D)/3); label("$60$", (A+E+B)/3); label("$120$", (D+E+C)/3); label("$x$", (B+E+F)/3); label("$120-x$", (F+E+C)/3); [/asy] Since $AD:DC=1:2$ thus $\triangle ABD=\frac{1}{3} \cdot 360 = 120.$
Similarly, $\triangle DBC = \frac{2}{3} \cdot 360 = 240.$
Now, since $E$ is a midpoint of $BD$ , $\triangle ABE = \triangle AED = 120 \div 2 = 60.$
We can use the fact that $E$ is a midpoint of $BD$ even further. Connect lines $E$ and $C$ so that $\triangle BEC$ and $\triangle DEC$ share 2 sides.
We know that $\triangle BEC=\triangle DEC=240 \div 2 = 120$ since $E$ is a midpoint of $BD.$
Let's label $\triangle BEF$ $x$ . We know that $\triangle EFC$ is $120-x$ since $\triangle BEC = 120.$
Note that with this information now, we can deduct more things that are needed to finish the solution.
Note that $\frac{EF}{AE} = \frac{120-x}{180} = \frac{x}{60}.$ because of triangles $EBF, ABE, AEC,$ and $EFC.$
We want to find $x.$
This is a simple equation, and solving we get $x=\boxed{\textbf{(B)}30}.$
~mathboy282, an expanded solution of Solution 5, credit to scrabbler94 for the idea.

## Solution 17
[asy] size(8cm); pair A, B, C, D, E, F; B = (0,0); A = (2, 3); C = (5, 0); D = (3, 2); E = (1.5, 1); F = (1.25, 0); draw(A--B--C--A--D--B); draw(A--F); draw(E--C); label("$A$", A, N); label("$B$", B, WSW); label("$C$", C, ESE); label("$D$", D, dir(0)*1.5); label("$E$", E, SSE); label("$F$", F, S); label("$60$", (A+E+D)/3); label("$60$", (A+E+B)/3); label("$120$", (D+E+C)/3); [/asy]
Because $AD:DC=1:2$ and $E$ is the midpoint of $BD$ , we know that the areas of $ABE$ and $AED$ are $60$ and the areas of $DEC$ and $EBC$ are $120$ . \[\frac{[EBF]}{[EFC]} = \frac{[ABF]}{[AFC]} = \frac{ [ABE]}{[AEC]} = \frac{60}{180}\] $[EBF] = \frac{120}{4} = \boxed{\textbf{(B) }30}$
### Note
This question is extremely similar to 1971 AHSME Problems/Problem 26 .

## Video Solutions

## Video Solution by Math-X (Let's do this step by step!!!)
https://youtu.be/IgpayYB48C4?si=ypjLOH-vfgQr8Neu&t=7358
~Math-X
https://www.youtube.com/watch?v=AY4mByrL8v0
Associated video
https://www.youtube.com/watch?v=DMNbExrK2oo
https://www.youtube.com/watch?v=nm-Vj_fsXt4
- Happytwin (Another video solution)
https://www.youtube.com/watch?v=nyevg9w-CCI&list=PLLCzevlMcsWNBsdpItBT4r7Pa8cZb6Viu&index=6
~ MathEx
https://www.youtube.com/watch?v=m04K0Q2SNXY&t=1s
https://youtu.be/vZjPUW_ZupA
~savannahsolver

## Video Solution by The Power of Logic(1 to 25 Full Solution)
https://youtu.be/Xm4ZGND9WoY
~Hayabusa1

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=AY4mByrL8v0&feature=youtu.be
### See Also
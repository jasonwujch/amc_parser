# 2019 AIME I Problem 13

## Problem

Triangle $ABC$ has side lengths $AB=4$ , $BC=5$ , and $CA=6$ . Points $D$ and $E$ are on ray $AB$ with $AB<AD<AE$ . The point $F \neq C$ is a point of intersection of the circumcircles of $\triangle ACD$ and $\triangle EBC$ satisfying $DF=2$ and $EF=7$ . Then $BE$ can be expressed as $\tfrac{a+b\sqrt{c}}{d}$ , where $a$ , $b$ , $c$ , and $d$ are positive integers such that $a$ and $d$ are relatively prime, and $c$ is not divisible by the square of any prime. Find $a+b+c+d$ .

## Solution 1
[asy] unitsize(20); pair A, B, C, D, E, F, X, O1, O2; A = (0, 0); B = (4, 0); C = intersectionpoints(circle(A, 6), circle(B, 5))[0]; D = B + (5/4 * (1 + sqrt(2)), 0); E = D + (4 * sqrt(2), 0); F = intersectionpoints(circle(D, 2), circle(E, 7))[1]; X = extension(A, E, C, F); O1 = circumcenter(C, A, D); O2 = circumcenter(C, B, E); filldraw(A--B--C--cycle, lightcyan, deepcyan); filldraw(D--E--F--cycle, lightmagenta, deepmagenta); draw(B--D, gray(0.6)); draw(C--F, gray(0.6)); draw(circumcircle(C, A, D), dashed); draw(circumcircle(C, B, E), dashed); dot("$A$", A, dir(A-O1)); dot("$B$", B, dir(240)); dot("$C$", C, dir(120)); dot("$D$", D, dir(40)); dot("$E$", E, dir(E-O2)); dot("$F$", F, dir(270)); dot("$X$", X, dir(140)); label("$6$", (C+A)/2, dir(C-A)*I, deepcyan); label("$5$", (C+B)/2, dir(B-C)*I, deepcyan); label("$4$", (A+B)/2, dir(A-B)*I, deepcyan); label("$7$", (F+E)/2, dir(F-E)*I, deepmagenta); label("$2$", (F+D)/2, dir(D-F)*I, deepmagenta); label("$4\sqrt{2}$", (D+E)/2, dir(E-D)*I, deepmagenta); label("$a$", (B+X)/2, dir(B-X)*I, gray(0.3)); label("$a\sqrt{2}$", (D+X)/2, dir(D-X)*I, gray(0.3)); [/asy]
Notice that \[\angle DFE=\angle CFE-\angle CFD=\angle CBE-\angle CAD=180-B-A=C.\] By the Law of Cosines, \[\cos C=\frac{AC^2+BC^2-AB^2}{2\cdot AC\cdot BC}=\frac34.\] Then, \[DE^2=DF^2+EF^2-2\cdot DF\cdot EF\cos C=32\implies DE=4\sqrt2.\] Let $X=\overline{AB}\cap\overline{CF}$ , $a=XB$ , and $b=XD$ . Then, \[XA\cdot XD=XC\cdot XF=XB\cdot XE\implies b(a+4)=a(b+4\sqrt2)\implies b=a\sqrt2.\] However, since $\triangle XFD\sim\triangle XAC$ , $XF=\tfrac{4+a}3$ , but since $\triangle XFE\sim\triangle XBC$ , \[\frac75=\frac{4+a}{3a}\implies a=\frac54\implies BE=a+a\sqrt2+4\sqrt2=\frac{5+21\sqrt2}4,\] and the requested sum is $5+21+2+4=\boxed{032}$ .
(Solution by TheUltimate123)

## Solution 2
Define $\omega_1$ to be the circumcircle of $\triangle ACD$ and $\omega_2$ to be the circumcircle of $\triangle EBC$ .
Because of exterior angles,
$\angle ACB = \angle CBE - \angle CAD$
But $\angle CBE = \angle CFE$ because $CBFE$ is cyclic. In addition, $\angle CAD = \angle CFD$ because $CAFD$ is cyclic. Therefore, $\angle ACB = \angle CFE - \angle CFD$ . But $\angle CFE - \angle CFD = \angle DFE$ , so $\angle ACB = \angle DFE$ . Using Law of Cosines on $\triangle ABC$ , we can figure out that $\cos(\angle ACB) = \frac{3}{4}$ . Since $\angle ACB = \angle DFE$ , $\cos(\angle DFE) = \frac{3}{4}$ . We are given that $DF = 2$ and $FE = 7$ , so we can use Law of Cosines on $\triangle DEF$ to find that $DE = 4\sqrt{2}$ .
Let $G$ be the intersection of segment $\overline{AE}$ and $\overline{CF}$ . Using Power of a Point with respect to $G$ within $\omega_1$ , we find that $AG \cdot GD = CG \cdot GF$ . We can also apply Power of a Point with respect to $G$ within $\omega_2$ to find that $CG \cdot GF = BG \cdot GE$ . Therefore, $AG \cdot GD = BG \cdot GE$ .
\[AG \cdot GD = BG \cdot GE\] \[(AB + BG) \cdot GD = BG \cdot (GD + DE)\] \[AB \cdot GD + BG \cdot GD = BG \cdot GD + BG \cdot DE\] \[AB \cdot GD = BG \cdot DE\] \[4 \cdot GD = BG \cdot 4\sqrt{2}\] \[GD = BG \cdot \sqrt{2}\]
Note that $\triangle GAC$ is similar to $\triangle GFD$ . $GF = \frac{BG + 4}{3}$ . Also note that $\triangle GBC$ is similar to $\triangle GFE$ , which gives us $GF = \frac{7 \cdot BG}{5}$ . Solving this system of linear equations, we get $BG = \frac{5}{4}$ . Now, we can solve for $BE$ , which is equal to $BG(\sqrt{2} + 1) + 4\sqrt{2}$ . This simplifies to $\frac{5 + 21\sqrt{2}}{4}$ , which means our answer is $\boxed{032}$ .

## Solution 3
Construct $FC$ and let $FC\cap AE=K$ . Let $FK=x$ . Using $\triangle FKE\sim \triangle BKC$ , \[BK=\frac{5}{7}x\] Using $\triangle FDK\sim ACK$ , it can be found that \[3x=AK=4+\frac{5}{7}x\to x=\frac{7}{4}\] This also means that $BK=\frac{21}{4}-4=\frac{5}{4}$ . It suffices to find $KE$ . It is easy to see the following: \[180-\angle ABC=\angle KBC=\angle KFE\] Using reverse Law of Cosines on $\triangle ABC$ , $\cos{\angle ABC}=\frac{1}{8}\to \cos{180-\angle ABC}=\frac{-1}{8}$ . Using Law of Cosines on $\triangle EFK$ gives $KE=\frac{21\sqrt 2}{4}$ , so $BE=\frac{5+21\sqrt 2}{4}\to \boxed{\textbf{032}}$ . -franchester

## Solution 4 (No <C = <DFE, no LoC)
Let $P=AE\cap CF$ . Let $CP=5x$ and $BP=5y$ ; from $\triangle{CBP}\sim\triangle{EFP}$ we have $EP=7x$ and $FP=7y$ . From $\triangle{CAP}\sim\triangle{DFP}$ we have $\frac{6}{4+5y}=\frac{2}{7y}$ giving $y=\frac{1}{4}$ . So $BP=\frac{5}{4}$ and $FP=\frac{7}{4}$ . These similar triangles also gives us $DP=\frac{5}{3}x$ so $DE=\frac{16}{3}x$ . Now, Stewart's Theorem on $\triangle{FEP}$ and cevian $FD$ tells us that \[\frac{560}{9}x^3+28x=\frac{49}{3}x+\frac{245}{3}x,\] so $x=\frac{3\sqrt{2}}{4}$ . Then $BE=\frac{5}{4}+7x=\frac{5+21\sqrt{2}}{4}$ so the answer is $\boxed{032}$ as desired. (Solution by Trumpeter, but not added to the Wiki by Trumpeter)

## Solution 5
Connect $CF$ meeting $AE$ at $J$ . We can observe that $\triangle{ACJ}\sim \triangle{FJD}$ Getting that $\frac{AJ}{FJ}=\frac{AC}{FD}=3$ . We can also observe that $\triangle{CBJ}\sim \triangle{EFJ}$ , getting that $\frac{CB}{EF}=\frac{BJ}{FJ}=\frac{CJ}{EJ}=\frac{5}{7}$
Assume that $BJ=5x;FJ=7x$ , since $\frac{AJ}{FJ}=3$ , we can get that $\frac{AJ}{FJ}=\frac{AB+BJ}{FJ}=\frac{4+5x}{7x}=3$ , getting that $x=\frac{1}{4}; BJ=\frac{5}{4}; FJ=\frac{7}{4}$
Using Power of Point, we can get that $BJ * EJ=CJ*FJ; DJ * AJ=CJ * FJ$ Assume that $DJ=5k,CJ=15k$ , getting that $JE=21k, DE=16k$
Now applying Law of Cosine on two triangles, $\triangle{ACJ};\triangle{FJE}$ separately, we can get two equations
$(1): (15k)^2+(\frac{21}{4})^2-2*15k *\frac{21}{4} * cos\angle{CJA}=36$
$(2):(21k)^2+(\frac{7}{4})^2-2*\frac{7}{4} * 21k*cos\angle{FJE}=49$
Since $\angle{CJA}=\angle{FJE}$ , we can use $15(2)-7(1)$ to eliminate the $cos$ term
Then we can get that $5040k^2=630$ , getting $k=\frac{\sqrt{2}}{4}$
$BE=21k=\frac{21\sqrt{2}}{4}; BJ=\frac{5}{4}$ , so the desired answer is $\frac{21\sqrt{2}+5}{4}$ , which leads to the answer $\boxed{032}$
~bluesoul

## Solution 6
First, let $AE$ and $CF$ intersect at $X$ . Our motivation here is to introduce cyclic quadrilaterals and find useful relationships in terms of angles. Observe that \[\angle DFE = \angle XFE - \angle XFD = \angle CBE - \angle CAB = 180 - \angle ABC - \angle CAB = \angle BAC\] By the so-called "Reverse Law of Cosines" on $\triangle ABC$ we have \[\cos(\angle BAC) = \frac{4^2 - 5^2 - 6^2}{-2 \cdot 5 \cdot 6} = \frac{3}{4}\] Applying on $\triangle DFE$ gives \[DE^2 = 2^2 + 7^2 - 2 \cdot 2 \cdot 7 \cos(\angle DFE)\] \[= 2^2 + 7^2 - 2 \cdot 2 \cdot 7 \cdot \frac{3}{4}\] \[=32\] So $DE = 4 \sqrt{2}$ , now by our cyclic quadrilaterals again, we are motivated by the multiple appearances of similar triangles throughout the figure. We want some that are related to $BX$ and $XD$ , which are crucial lengths in the problem. Suppose $BX = r, XD = s$ for simplicity. We have:
\[\triangle AXC \sim \triangle FXD\] and \[\triangle BXC \sim \triangle FXE\]
So \[\frac{AX}{FX} = \frac{XC}{XD} = \frac{AC}{FD} \implies \frac{4 + r}{FX} = \frac{XC}{s} = 3\] \[\frac{BX}{FX} = \frac{XC}{XE} = \frac{BC}{FE} \implies \frac{r}{FX} = \frac{XC}{s + 4 \sqrt{2}} = \frac{5}{7}\] \[\implies \frac{4 + r}{r} = \frac{s + 4 \sqrt{2}}{s} = \frac{21}{5}\] \[\implies r = \frac{5}{4}, s = \frac{5 \sqrt{2}}{4}\] So $BE = r + s + 4 \sqrt{2} = \frac{5 + 21 \sqrt{2}}{4}$ . The requested sum is $5 + 21 + 2 + 4 = \boxed{032}$ .
~CoolJupiter

## Video Solution by MOP 2024
https://youtube.com/watch?v=B7rFw05AYQ0
~r00tsOfUnity
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
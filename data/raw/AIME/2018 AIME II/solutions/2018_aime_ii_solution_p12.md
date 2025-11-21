# 2018 AIME II Problem 12

## Problem

Let $ABCD$ be a convex quadrilateral with $AB = CD = 10$ , $BC = 14$ , and $AD = 2\sqrt{65}$ . Assume that the diagonals of $ABCD$ intersect at point $P$ , and that the sum of the areas of triangles $APB$ and $CPD$ equals the sum of the areas of triangles $BPC$ and $APD$ . Find the area of quadrilateral $ABCD$ .

### Diagram

Let $AP=x$ and let $PC=\rho x$ . Let $[ABP]=\Delta$ and let $[ADP]=\Lambda$ . [asy] defaultpen(fontsize(14)+0.6); unitsize(12); real x=11.25; pair B1=origin, D1=(x,0), C1=IP(CR(B1,14),CR(D1,10)), A1=OP(CR(B1,10),CR(D1,2*sqrt(65))), P1=extension(A1,C1,B1,D1); pair A=origin, C=(length(C1-A1),0), B=IP(CR(A,10),CR(C,14)), D=OP(CR(A,2*sqrt(65)),CR(C,10)), P=extension(A,C,B,D); draw(A--B--C--D--A); draw(A--C^^B--D,gray+0.4); dot("$A$",A,dir(A-P)); dot("$B$",B,dir(B-P)); dot("$C$",C,dir(C-P)); dot("$D$",D,dir(D-P)); dot("$P$",P,dir(230)); pen p=fontsize(10); label("$10$",A--B,up,p); label("$10$", C--D, 2*right,p); label("$14$", B--C, N,p); label("$2\sqrt{65}$", A--D, SW,p); label("$x$", A--P,down,p); label("$\rho x$", P--C,down,p); label("$\Delta$",(A+B+P)/3, right,p); label("$\Lambda$",(A+D+P)/3, right,p); [/asy]

## Solution 1
Let $AP=x$ and let $PC=\rho x$ . Let $[ABP]=\Delta$ and let $[ADP]=\Lambda$ . We easily get $[PBC]=\rho \Delta$ and $[PCD]=\rho\Lambda$ .
We are given that $[ABP] +[PCD] = [PBC]+[ADP]$ , which we can now write as \[\Delta + \rho\Lambda = \rho\Delta + \Lambda \qquad \Longrightarrow \qquad \Delta -\Lambda = \rho (\Delta -\Lambda).\] Either $\Delta = \Lambda$ or $\rho=1$ . The former would imply that $ABCD$ is a parallelogram, which it isn't; therefore we conclude $\rho=1$ and $P$ is the midpoint of $AC$ . Let $\angle BAD = \theta$ and $\angle BCD = \phi$ . Then $[ABCD]=2\cdot [BCD]=140\sin\phi$ . On one hand, since $[ABD]=[BCD]$ , we have \begin{align}\sqrt{65}\sin\theta = 7\sin\phi \quad \implies \quad 16+49\cos^2\phi = 65\cos^2\theta\end{align} whereas, on the other hand, using cosine formula to get the length of $BD$ , we get \[10^2+4\cdot 65 - 40\sqrt{65}\cos\theta = 10^2+14^2-280\cos\phi\] \begin{align}\tag{2}\implies \qquad 65\cos^2\theta = \left(7\cos\phi+ \frac{8}{5}\right)^2\end{align} Eliminating $\cos\theta$ in the above two equations and solving for $\cos\phi$ we get \[\cos\phi = \frac{3}{5}\qquad \implies \qquad \sin\phi = \frac{4}{5}\] which finally yields $[ABCD]=2\cdot [BCD] = 140\sin\phi = 112$ .

## Solution 2
For reference, $2\sqrt{65} \approx 16$ , so $\overline{AD}$ is the longest of the four sides of $ABCD$ . Let $h_1$ be the length of the altitude from $B$ to $\overline{AC}$ , and let $h_2$ be the length of the altitude from $D$ to $\overline{AC}$ . Then, the triangle area equation becomes
\[\frac{h_1}{2}AP + \frac{h_2}{2}CP = \frac{h_1}{2}CP + \frac{h_2}{2}AP \rightarrow \left(h_1 - h_2\right)AP = \left(h_1 - h_2\right)CP \rightarrow AP = CP\]
What an important finding! Note that the opposite sides $\overline{AB}$ and $\overline{CD}$ have equal length, and note that diagonal $\overline{DB}$ bisects diagonal $\overline{AC}$ . This is very similar to what happens if $ABCD$ were a parallelogram with $AB = CD = 10$ , so let's extend $\overline{DB}$ to point $E$ , such that $AECD$ is a parallelogram. In other words, \[AE = CD = 10\] and \[EC = DA = 2\sqrt{65}\] Now, let's examine $\triangle ABE$ . Since $AB = AE = 10$ , the triangle is isosceles, and $\angle ABE \cong \angle AEB$ . Note that in parallelogram $AECD$ , $\angle AED$ and $\angle CDE$ are congruent, so $\angle ABE \cong \angle CDE$ and thus \[\text{m}\angle ABD = 180^\circ - \text{m}\angle CDB\] Define $\alpha := \text{m}\angle CDB$ , so $180^\circ - \alpha = \text{m}\angle ABD$ .
We use the Law of Cosines on $\triangle DAB$ and $\triangle CDB$ :
\[\left(2\sqrt{65}\right)^2 = 10^2 + BD^2 - 20BD\cos\left(180^\circ - \alpha\right) = 100 + BD^2 + 20BD\cos\alpha\]
\[14^2 = 10^2 + BD^2 - 20BD\cos\alpha\]
Subtracting the second equation from the first yields
\[260 - 196 = 40BD\cos\alpha \rightarrow BD\cos\alpha = \frac{8}{5}\]
This means that dropping an altitude from $B$ to some foot $Q$ on $\overline{CD}$ gives $DQ = \frac{8}{5}$ and therefore $CQ = \frac{42}{5}$ . Seeing that $CQ = \frac{3}{5}\cdot BC$ , we conclude that $\triangle QCB$ is a 3-4-5 right triangle, so $BQ = \frac{56}{5}$ . Then, the area of $\triangle BCD$ is $\frac{1}{2}\cdot 10 \cdot \frac{56}{5} = 56$ . Since $AP = CP$ , points $A$ and $C$ are equidistant from $\overline{BD}$ , so \[\left[\triangle ABD\right] = \left[\triangle CBD\right] = 56\] and hence \[\left[ABCD\right] = 56 + 56 = \boxed{112}\] -kgator
Just to be complete -- $h_1$ and $h_2$ can actually be equal. In this case, $AP \neq CP$ , but $BP$ must be equal to $DP$ . We get the same result. -Mathdummy.

## Solution 3 (Another way to get the middle point)
So, let the area of $4$ triangles $\triangle {ABP}=S_{1}$ , $\triangle {BCP}=S_{2}$ , $\triangle {CDP}=S_{3}$ , $\triangle {DAP}=S_{4}$ . Suppose $S_{1}>S_{3}$ and $S_{2}>S_{4}$ , then it is easy to show that \[S_{1}\cdot S_{3}=S_{2}\cdot S_{4}.\] Also, because \[S_{1}+S_{3}=S_{2}+S_{4},\] we will have \[(S_{1}+S_{3})^2=(S_{2}+S_{4})^2.\] So \[(S_{1}+S_{3})^2=S_{1}^2+S_{3}^2+2\cdot S_{1}\cdot S_{3}=(S_{2}+S_{4})^2=S_{2}^2+S_{4}^2+2\cdot S_{2}\cdot S_{4}.\] So \[S_{1}^2+S_{3}^2=S_{2}^2+S_{4}^2.\] So \[S_{1}^2+S_{3}^2-2\cdot S_{1}\cdot S_{3}=S_{2}^2+S_{4}^2-2\cdot S_{2}\cdot S_{4}.\] So \[(S_{1}-S_{3})^2=(S_{2}-S_{4})^2.\] As a result, \[S_{1}-S_{3}=S_{2}-S_{4}.\] Then, we have \[S_{1}+S_{4}=S_{2}+S_{3}.\] Combine the condition \[S_{1}+S_{3}=S_{2}+S_{4},\] we can find out that \[S_{3}=S_{4},\] so $P$ is the midpoint of $\overline {AC}$
~Solution by $BladeRunnerAUG$ (Frank FYC)

## Solution 4 (With yet another way to get the middle point)
Denote $\angle APB$ by $\alpha$ . Then $\sin(\angle APB)=\sin \alpha = \sin(\angle APD)$ . Using the formula for the area of a triangle, we get \[\frac{1}{2} (AP\cdot BP+ CP\cdot DP)\sin\alpha=\frac{1}{2}(AP\cdot DP+ CP\cdot BP)\sin\alpha ,\] so \[(AP-CP)(BP-DP)=0\] Hence $AP=CP$ (note that $BP=DP$ makes no difference here). Now, assume that $AP=CP=x$ , $BP=y$ , and $DP=z$ . Using the cosine rule for $\triangle APB$ and $\triangle BPC$ , it is clear that \[x^2+y^2-100=2 xy \cdot \cos{APB}=-(2 xy \cdot \cos{(\pi-CPB)})=-(x^2+y^2-196)\] or \begin{align}x^2+y^2=148\end{align}. Likewise, using the cosine rule for triangles $APD$ and $CPD$ , \begin{align}\tag{2}x^2+z^2=180\end{align}. It follows that \begin{align}\tag{3}z^2-y^2=32\end{align}. Since $\sin\alpha=\sqrt{1-\cos^2\alpha}$ , \[\sqrt{1-\frac{(x^2+y^2-100)^2}{4x^2y^2}}=\sqrt{1-\frac{(x^2+z^2-260)^2}{4x^2z^2}}\] which simplifies to \[\frac{48^2}{y^2}=\frac{80^2}{z^2} \qquad \Longrightarrow \qquad 5y=3z.\] Plugging this back to equations $(1)$ , $(2)$ , and $(3)$ , it can be solved that $x=\sqrt{130},y=3\sqrt{2},z=5\sqrt{2}$ . Then, the area of the quadrilateral is \[x(y+z)\sin\alpha=\sqrt{130}\cdot8\sqrt{2}\cdot\frac{14}{\sqrt{260}}=\boxed{112}\] --Solution by MicGu

## Solution 5
As in all other solutions, we can first find that either $AP=CP$ or $BP=DP$ , but it's an AIME problem, we can take $AP=CP$ , and assume the other choice will lead to the same result (which is true).
From $AP=CP$ , we have $[DAP]=[DCP]$ , and $[BAP]=[BCP] \implies [ABD] = [CBD]$ , therefore, \begin{align} \nonumber \frac 12 \cdot AB\cdot AD\sin A &= \frac 12 \cdot BC\cdot CD\sin C \\ \Longrightarrow \hspace{1in} 7\sin C &= \sqrt{65}\sin A \end{align} By Law of Cosines, \begin{align} \nonumber 10^2+14^2-2\cdot 10\cdot 14\cos C &= 10^2+4\cdot 65-2\cdot 10\cdot 2\sqrt{65}\cos A \\ \Longrightarrow \hspace{1in} -\frac 85 - 7\cos C &= \sqrt{65}\cos A \tag{2} \end{align} Square $(1)$ and $(2)$ , and add them, to get \[\left(\frac 85\right)^2 + 2\cdot \frac 85 \cdot 7\cos C + 7^2 = 65\] Solve, $\cos C = 3/5 \implies \sin C = 4/5$ , \[[ABCD] = 2[BCD] = BC\cdot CD\cdot \sin C = 14\cdot 10\cdot \frac 45 = \boxed{112}\] -Mathdummy

## Solution 6
Either $PA=PC$ or $PD=PB$ . Let $PD=PB=s$ . Applying Stewart's Theorem on $\triangle ABD$ and $\triangle BCD$ , dividing by $2s$ and rearranging, \[\tag{1}CP^2+s^2=148\] \[\tag{2}AP^2+s^2=180\] Applying Stewart on $\triangle CAB$ and $\triangle CAD$ , \[\tag{3} 5CP^2=3AP^2\] Substituting equations 1 and 2 into 3 and rearranging, $s=BP=PD\sqrt{130}, CP=3\sqrt{2}, PA=5\sqrt{2}$ . By Law of Cosines on $\triangle APB$ , $\cos(\angle APB)=\frac{4\sqrt{65}}{65}$ so $\sin(\angle APB)=\sin(\angle BPC)=\sin(\angle CPD)=\sin(\angle DPA)=\frac{7\sqrt{65}}{65}$ . Using $[\triangle ABC]=\frac{ab\sin(\angle C)}{2}$ to find unknown areas, $[ABCD]=[\triangle APB]+[\triangle BPC]+[\triangle CPD]+[\triangle DPA]=\boxed{112}$ .
-Solution by Garrett

## Solution 7
Now we prove P is the midpoint of $BD$ . Denote the height from $B$ to $AC$ as $h_1$ , height from $D$ to $AC$ as $h_2$ .According to the problem, $AP* h_1 +CP* h_2 =CP* h_1 +AP* h_2$ implies $h_1 (AP-CP)= h_2 (AP-CP), h_1 = h_2$ . Then according to basic congruent triangles we get $BP=DP$ Firstly, denote that $CP=a,BP=b,CP=c,AP=d$ . Applying Stewart theorem, getting that $100c+196b=(b+c)(bc+a^2); 100b+260c=(b+c)(bc+c^2); 100c+196b=100b+260c, 3b=5c$ , denote $b=5x,c=3x$ Applying Stewart Theorem, getting $260a+100a=2a(a^2+25x^2); 196a+100a=2a(9x^2+a^2)$ solve for a, getting $a=\sqrt{130},AP=5\sqrt{2}; CP=3\sqrt{2}$ Now everything is clear, we can find $cos\angle{BPA}=\frac{4}{\sqrt{65}}$ using LOC, $sin\angle{BPA}=\frac{7\sqrt{65}}{65}$ , the whole area is $\sqrt{130}*8\sqrt{2}*\frac{7\sqrt{65}}{65}=\boxed{112}$
~bluesoul

## Solution 8 (Simple Geometry)
$BP = PD$ as in another solutions.
Let $D'$ be the reflection of $D$ across $C$ . Let points $E, E',$ and $H$ be the foot of perpendiculars on $AC$ from $D,D'$ , and $B$ respectively. \begin{align*} &\qquad AB = CD = CD', \quad \textrm{and} \quad BH = DE = D'E' \\ \Rightarrow &\qquad \triangle ABH = \triangle CDE = \triangle CD'E' \\ \Rightarrow &\qquad \angle BAC = \angle ACD' \\ \Rightarrow &\qquad \triangle ABC = \triangle AD'C \\ \Rightarrow &\qquad BC = AD'. \end{align*} The area of quadrilateral $ABCD$ is equal to the area of triangle $ADD'$ with sides $AD' = 14, AD = 2\sqrt{65}, DD' = 2 \cdot 10 = 20$ . The semiperimeter is $s = 17 + \sqrt{65},$ the area \[[ADD'] = \sqrt {(17 + \sqrt{65}) (17 - \sqrt{65})(3 + \sqrt{65})(\sqrt{65}-3)} = \sqrt{(289 – 65)\cdot(65-9)} =\sqrt{56 \cdot 4 \cdot 56} = \boxed{112}.\]
vladimir.shelomovskii@gmail.com, vvsss

## Solution 9 (Mindless Law of Cosines Bash)
Use your favorite method to get that $P$ is the midpoint of one of the two diagonals (suppose it's the midpoint of $\overline{AC}$ ). From here, let $x=AP=PC, y=BP, z=PD, a=\cos\theta$ where $\theta$ is the angle that the diagonals make. Then we have a system of four equations:
\begin{align*} x^2+y^2+2xya &= 100 \\ z^2+x^2+2xza &= 100 \\ x^2+y^2-2xya &= 196 \\ x^2+z^2-2xza &= 260 \\ \end{align*}
From these equations we get that \begin{align*} xya &= -24 \\ xza &= -40 \\ x^2+y^2-48 &= 10 \\ x^2+z^2-80 &= 10 \end{align*}
From here we can see that $\frac{z}{y}=\frac{5}{3}, z^2-y^2=32,$ so $z=5\sqrt{2}, y=3\sqrt{2}.$ Furthermore, this implies $x=\sqrt{130}$ and $xa=-4\sqrt{2},$ which implies $a=\cos\theta=\frac{4}{\sqrt{65}}.$ Then note that the area of the quadrilateral is \[\frac{1}{2}\sin\theta (xy+xz+xz+xy)=\sin\theta (\sqrt{130}\cdot 3\sqrt{2}+\sqrt{130} \cdot 5\sqrt{2})=7\cdot (3\cdot 2+5\cdot 2)=7(6+10)=7\cdot 16=\boxed{112}.\]
~Dhillonr25

## Solution 10
Note that $\angle APB = \angle CPD = 180-\angle APD = 180-\angle BPC.$ (All angles are in degrees) Since $\sin(\theta)=\sin(180-\theta),$ we can use sine area formula to get the following(after some simplifying steps): \begin{align*} BP \times AP + CP \times DP = BP \times PC + AP \times PD. \end{align*} For convenience, let $AP=a, BP=b, CP=c,DP=d.$ The above equation simplifies to: \begin{align*} ab + cd = bc + ad \\ab-ad+cd-bc=0 \\a(b-d)-c(b-d)=0 \\(a-c)(b-d)=0 \end{align*} From here, we see that $a=c$ or $b=d$ . Without loss of generality, let $a=c$ . Since triangles $ABP$ and $CDP$ are obviously not congruent, we see that one triangle is obtuse and the other one is acute.(Refer to the diagram) However, if we drop perpendiculars from $B$ to $AC$ and $D$ to $AC$ , we do get congruent triangles. If the foot of the perpendicular from $B$ is $M$ , and the foot of the perpendicular from $D$ is $N$ , then right triangle $BMP$ is congruent to right triangle $DNP$ . From here, we see that the altitudes of triangles $ABC$ and $ADC$ to $AC$ are equal. Since they share base $AC$ , their areas are equal. We can use Heron's formula. To not have any fractions, let $AC=2x.$ \begin{align*} \sqrt{(12+x)(12-x)(x+2)(x-2)}=\sqrt{5+\sqrt{65}+x)(5+\sqrt{65}-x)(5-\sqrt{65}+x)(\sqrt{65}-5+x)} \end{align*} Even though this looks bad at first, it actually isn't too complicated to simplify. Expanding the differences of squares and simplifying completely, we get $x^2=32.$ Plugging this $x$ back into the Heron's formula, we get that the area of $ABC$ (or $ADC$ ) is $56$ . Since these triangles have equal area, the area of the quadrilateral is $2 \times 56 = \boxed{112}$ , and we are done. $\blacksquare$
~ewei12

## Solution 11
Use any method to derive that $P$ is the midpoint of $A$ and $C$ . Now, either construct a parallelogram with as shown in the diagram to the right, or use law of sines. We will take the parallelogram route here, but the same thing can be done with law of sines on triangles $\triangle \textnormal{ABP}$ and $\triangle \textnormal{CPD}$ . Reflect $D$ across $P$ to get $D'$ . Since $CD = AD' = AB = 10$ , $\triangle \textnormal{ABD'}$ is isosceles. Thus, $\angle AD'B = \angle ABD'$ , and because $ADCD'$ is a parallelogram (since $AP = PC$ and $DP = PD'$ ), $\angle AD'B = \angle BDC = \angle ABD'$ . So, $\angle ABD = 180 - \angle ABD' = 180 - \angle BDC$ . Now, apply law of cosines on $\triangle \textnormal{ABD}$ and $\triangle \textnormal{CDB}$ . We get: \begin{align} 100 + BD^2 - 20BD \cos{\angle ABD} &= 100 + BD^2 - 20 BD \cos {(180 - \angle BDC)} = \\ 100 + BD^2 + 20 BD \cos{\angle BDC} &= 260 \\ &\textnormal{and} \\ 100 + BD^2 - 20 BD \cos{\angle BDC} &= 196 \\ \textnormal{summing }&\textnormal{and simplifying,} \\ BD &= 8\sqrt{2} \end{align} Then, applying law of cosines on $\triangle \textnormal{BCD}$ again, we obtain \[100 + 196 - 280 \cos{\angle BCD} = BD^2 = 128 \implies \cos{\angle BCD} = \frac{3}{5} \implies \sin{\angle BCD} = \frac{4}{5}\] Since $AP = PD$ , $[ABD] = [BCD] \implies [ABCD] = [ABD] + [BCD] = 2[BCD]$ . Thus, $[ABCD] = 2[BCD] = 2 \cdot \frac{1}{2} \cdot 10 \cdot 14 \sin{\angle BCD} = 140 \cdot \frac{4}{5} = \boxed{112}$ .
~ CrazyVideoGamez

## Solution 12(LoC Bash)
Let $AP = a, CP = b, BP = c, DP = d$ . Also, let $\angle APB = \theta$ and the other angles will follow by Supplementary Angle Theorem and Vertical Angle Theorem.
Using Law of Cosines we get
$a^2 + d^2 + 2ad\cos(\theta) = 260 \textbf{(1)}$
$b^2 + c^2 + 2bc\cos(\theta) = 196 \textbf{(2)}$
$a^2 + c^2 - 2ac\cos(\theta) = 100 \textbf{(3)}$
$b^2 + d^2 - 2bd\cos(\theta) = 100 \textbf{(4)}$
By sine area formula
$\frac{1}{2} \sin(\theta) ac + \frac{1}{2} \sin(\theta) bd = \frac{1}{2} \sin(180 - \theta) bc + \frac{1}{2} \sin(180 - \theta) ad \implies ac + bd = bc + ad \implies c(a - b) = d(a - b) \implies \text{Either a = b or c = d}$
We will assume $a = b$ for this solution.
Now we subtract equations (1) and (2)
$a^2 - b^2 + d^2 - c^2 + 2\cos(\theta)(ad - bc) = 64$
We also subtract equations (3) and (4)
$a^2 - b^2 + c^2 - d^2 + 2\cos(\theta)(bd - ac) = 0$
We will add these equations to get
$2a^2 - 2b^2 + 2\cos(\theta)((d - c)(a + b)) = 64$
Then factoring an $a - b$ out from each of the factors and dividing by $2$
$(a + b)(a - b + \cos(\theta)(d - c)) = 32 \textbf{(5)}$
Now we will subtract equations (1) and (3)
$d^2 - c^2 + 2\cos(\theta)(ac + ad) = 160$
We will also subtract equations (2) and (4)
$c^2 - d^2 + 2\cos(\theta)(bc + bd) = 96$
We subtract these equations to get
$2d^2 - 2c^2 + 2\cos(\theta)(ad - bc - bd + ac) = 64$
Factoring we have
$(d + c)(d - c + \cos(\theta)(a - b)) = 32 \textbf{(6)}$
Now remember that $a = b$ . So we can plug that in for both equations (5) and (6)
$(2a)((d - c)\cos(\theta)) = 32$
$(d + c)(d - c) = 32$
We know $d - c = \frac{16}{a\cos(\theta)}$ from the first equation and $d - c = \frac{32}{d + c}$ . Setting them equal and solving for $\cos(\theta)$ gives
$\cos(\theta) = \frac{c + d}{2a}$
Now we will subtract equations (1) and (4)
$a^2 - b^2 + 2\cos(\theta)(ad + bd) = 160$
Factoring we have
$(a + b)(a - b + 2d\cos(\theta)) = 160$
Substituting $a = b$ we get
$(a + b)(2d\cos(\theta) = 160 \implies \cos(\theta) = \frac{80}{d(a + b)}$
Now we will subtract equations (2) and (3)
$b^2 - a^2 + 2\cos(\theta)(bc + ac) = 96$
Factoring we get
$(a + b)(b - a + 2c\cos(\theta)) = 96$
We can substitute $a = b$ to get
$(a + b)(2c\cos(\theta)) = 96 \implies \cos(\theta) = \frac{48}{c(a + b)}$
Now setting these two representations of cosines equal, we have
$\frac{80}{d} = \frac{48}{c}$ after cancelling the $a + b$ 's.
Solving, we have $d = \frac{5c}{3}$ .
Note that $\cos(\theta) = \frac{c + d}{2a}$ from earlier. Plugging in $d = \frac{5c}{3}$ , we get
$\cos(\theta) = \frac{4c}{3a}$
We have from equation 6
$(d + c)(d - c + \cos(\theta)(a - b)) = 32$
We can plug in $a = b$ to get
$d^2 - c^2 = 32$ following difference of squares.
Now $d = \frac{5c}{3}$ so we can substitute that in to have
$\frac{25c^2}{9} - \frac{9c^2}{9} = 32 \implies \frac{16c^2}{9} = 32 \implies c^2 = 18 \implies c = 3\sqrt{2}$ because $c$ has to be positive as it is a side length.
Now $d = \frac{5c}{3} = \frac{5 \cdot 3\sqrt{2}}{3} = 5\sqrt{2}$ .
Now from the sine area formula, the area of the quadrilateral is just $\frac{1}{2} \sin(\theta) ac + \frac{1}{2} \sin(\theta) bd + \frac{1}{2} \sin(180 - \theta) bc + \frac{1}{2} \sin(180 - \theta) ad = \frac{1}{2} \sin(\theta)(ac + bd + bc + ad) = \frac{1}{2} \sin(\theta)(a + b)(c + d) = \sin(\theta) \cdot a \cdot (c + d)$ where the last steps follow from $a = b$ . Now $c + d = 3\sqrt{2} + 5\sqrt{2} = 8\sqrt{2}$ . We need to find $a$ and $\sin(\theta)$ .
We can go back to equation (3) to find $a$ . We have
$a^2 + c^2 - 2ac\cos(\theta) = 100$
Plugging in $c = 3\sqrt{2}$ and $\cos(\theta) = \frac{4c}{3a} = \frac{4 \cdot 3\sqrt{2}}{3a} = \frac{4\sqrt{2}}{a}$ we get
$a^2 + 18 - 6\sqrt{2} \cdot a \cdot \frac{4\sqrt{2}}{a} = 100 \implies a^2 + 18 - 48 = 100 \implies a^2 = 130$
Now $\sin(\theta) = \sqrt{1 - \frac{32}{a^2}}$ following the Pythagorean Identity. Now $a^2 = 130$ so we have
$\sin(\theta) = \sqrt{1 - \frac{32}{130}} = \sqrt{\frac{98}{130}} = \frac{7\sqrt{2}}{\sqrt{130}}$ . Hence the answer is
$\frac{7\sqrt{2}}{\sqrt{130}} \cdot 8\sqrt{2} \cdot \sqrt{130} = 7\sqrt{2} \cdot 8\sqrt{2} = 56 \cdot 2 = \boxed{112}$ .
~ilikemath247365

## Video Solution by MOP 2024
https://youtube.com/watch?v=2BsYR1dJn9c
~r00tsOfUnity
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
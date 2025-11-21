# 2016 AIME II Problem 10

## Problem

Triangle $ABC$ is inscribed in circle $\omega$ . Points $P$ and $Q$ are on side $\overline{AB}$ with $AP<AQ$ . Rays $CP$ and $CQ$ meet $\omega$ again at $S$ and $T$ (other than $C$ ), respectively. If $AP=4,PQ=3,QB=6,BT=5,$ and $AS=7$ , then $ST=\frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution 1
[asy] import cse5; pathpen = black; pointpen = black; pointfontsize = 9; size(8cm); pair A = origin, B = (13,0), P = (4,0), Q = (7,0), T = B + 5 dir(220), C = IP(circumcircle(A,B,T),Line(T,Q,-0.1,10)), S = IP(circumcircle(A,B,C),Line(C,P,-0.1,10)); Drawing(A--B--C--cycle); D(circumcircle(A,B,C),rgb(0,0.6,1)); DrawPathArray(C--S^^C--T,rgb(1,0.4,0.1)); DrawPathArray(A--S^^B--T,rgb(0,0.4,0)); D(S--T,rgb(1,0.2,0.4)); D("A",A,dir(215)); D("B",B,dir(330)); D("P",P,dir(240)); D("Q",Q,dir(240)); D("T",T,dir(290)); D("C",C,dir(120)); D("S",S,dir(250)); MP("4",(A+P)/2,dir(90)); MP("3",(P+Q)/2,dir(90)); MP("6",(Q+B)/2,dir(90)); MP("5",(B+T)/2,dir(140)); MP("7",(A+S)/2,dir(40)); [/asy] Let $\angle ACP=\alpha$ , $\angle PCQ=\beta$ , and $\angle QCB=\gamma$ . Note that since $\triangle ACQ\sim\triangle TBQ$ we have $\tfrac{AC}{CQ}=\tfrac56$ , so by the Ratio Lemma \[\dfrac{AP}{PQ}=\dfrac{AC}{CQ}\cdot\dfrac{\sin\alpha}{\sin\beta}\quad\implies\quad \dfrac{\sin\alpha}{\sin\beta}=\dfrac{24}{15}.\] Similarly, we can deduce $\tfrac{PC}{CB}=\tfrac47$ and hence $\tfrac{\sin\beta}{\sin\gamma}=\tfrac{21}{24}$ .
Now Law of Sines on $\triangle ACS$ , $\triangle SCT$ , and $\triangle TCB$ yields \[\dfrac{AS}{\sin\alpha}=\dfrac{ST}{\sin\beta}=\dfrac{TB}{\sin\gamma}.\] Hence \[\dfrac{ST^2}{\sin^2\beta}=\dfrac{TB\cdot AS}{\sin\alpha\sin\gamma},\] so \[TS^2=TB\cdot AS\left(\dfrac{\sin\beta}{\sin\alpha}\dfrac{\sin\beta}{\sin\gamma}\right)=\dfrac{15\cdot 21}{24^2}\cdot 5\cdot 7=\dfrac{35^2}{8^2}.\] Hence $ST=\tfrac{35}8$ and the requested answer is $35+8=\boxed{43}$ .
Edit: Note that the finish is much simpler. Once you get $\dfrac{AS}{\sin\alpha}=\dfrac{ST}{\sin\beta}$ , you can solve quickly from there getting $ST=\dfrac{AS \sin(\beta)}{\sin(\alpha)}=7\cdot \dfrac{15}{24}=\dfrac{35}{8}$ .

## Solution 2 (Projective Geometry)
Projecting through $C$ we have \[\frac{3}{4}\times \frac{13}{6}=(A,Q;P,B)\stackrel{C}{=}(A,T;S,B)=\frac{ST}{7}\times \frac{13}{5}\] which easily gives $ST=\frac{35}{8}\Longrightarrow 35+8=\boxed{043}$ .

## Solution 3
By Ptolemy's Theorem applied to quadrilateral $ASTB$ , we find \[5\cdot 7+13\cdot ST=AT\cdot BS.\] Therefore, in order to find $ST$ , it suffices to find $AT\cdot BS$ . We do this using similar triangles, which can be found by using Power of a Point theorem.
As $\triangle APS\sim \triangle CPB$ , we find \[\frac{4}{PC}=\frac{7}{BC}.\] Therefore, $\frac{BC}{PC}=\frac{7}{4}$ .
As $\triangle BQT\sim\triangle CQA$ , we find \[\frac{6}{CQ}=\frac{5}{AC}.\] Therefore, $\frac{AC}{CQ}=\frac{5}{6}$ .
As $\triangle ATQ\sim\triangle CBQ$ , we find \[\frac{AT}{BC}=\frac{7}{CQ}.\] Therefore, $AT=\frac{7\cdot BC}{CQ}$ .
As $\triangle BPS\sim \triangle CPA$ , we find \[\frac{9}{PC}=\frac{BS}{AC}.\] Therefore, $BS=\frac{9\cdot AC}{PC}$ . Thus we find \[AT\cdot BS=\left(\frac{7\cdot BC}{CQ}\right)\left(\frac{9\cdot AC}{PC}\right).\] But now we can substitute in our previously found values for $\frac{BC}{PC}$ and $\frac{AC}{CQ}$ , finding \[AT\cdot BS=63\cdot \frac{7}{4}\cdot \frac{5}{6}=\frac{21\cdot 35}{8}.\] Substituting this into our original expression from Ptolemy's Theorem, we find \begin{align*}35+13ST&=\frac{21\cdot 35}{8}\\13ST&=\frac{13\cdot 35}{8}\\ST&=\frac{35}{8}.\end{align*} Thus the answer is $\boxed{43}$ .

## Solution 4
Extend $\overline{AB}$ past $B$ to point $X$ so that $CPTX$ is cyclic. Then, by Power of a Point on $CPTX$ , $(CQ)(QT) = (PQ)(QX)$ . By Power of a Point on $CATB$ , $(CQ)(QT) = (AQ)(QB) = 42$ . Thus, $(PQ)(QX) = 42$ , so $BX = 8$ .
By the Inscribed Angle Theorem on $CPTX$ , $\angle SCT = \angle BXT$ . By the Inscribed Angle Theorem on $ASTC$ , $\angle SCT = \angle SAT$ , so $\angle BXT = \angle SAT$ . Since $ASTB$ is cyclic, $\angle AST = \angle TBX$ . Thus, $\triangle AST \sim \triangle XBT$ , so $AS/XB = ST/BT$ . Solving for $ST$ yields $ST = \frac{35}{8}$ , for a final answer of $35+8 = \boxed{043}$ .
~ Leo.Euler

## Solution 5 (5 = 2 + 3)
By Ptolemy's Theorem applied to quadrilateral $ASTB$ , we find \[AS\cdot BT+AB\cdot ST=AT\cdot BS.\] Projecting through $C$ we have \[\frac{AQ \cdot PB}{PQ \cdot AB} = (A,Q; P,B)\stackrel{C}{=}(A,T; S,B)=\frac{AT \cdot BS}{ST \cdot AB}.\] Therefore \[AT \cdot BS = \frac {AQ \cdot PB}{PQ} \times ST \implies\] \[\left(\frac {AQ \cdot PB}{PQ} - AB\right)\times ST = AS \cdot BT \implies\] \[ST = \frac {AS \cdot BT \cdot PQ}{AQ \cdot PB – AB \cdot PQ}\] \[ST = \frac {7\cdot 5 \cdot 3}{7\cdot 9 – 13 \cdot 3 } = \frac {35}{8} \implies 35 + 8 = \boxed {43}.\]
vladimir.shelomovskii@gmail.com, vvsss

## Solution 6
Connect $AT$ and $\angle{SCT}=\angle{SAT}, \angle{ACS}=\angle{ATS}, \frac{ST}{\sin \angle{SAT}}=\frac{AS}{\sin \angle{ATS}}$
So we need to get the ratio of $\frac{\sin \angle{ACS}}{\sin \angle{SCT}}$
By clear observation $\triangle{CAQ}\sim \triangle{BTQ}$ , we have $\frac{CQ}{AC}=\frac{6}{5}$ , LOS tells $\frac{AC}{\sin \angle{CPA}}=\frac{4}{\sin \angle{ACS}}; \frac{CQ}{\sin \angle{CPQ}}=\frac{3}{\sin \angle{PCQ}}$ so we get $\frac{\sin \angle{PCQ}}{\sin \angle{ACS}}=\frac{5}{8}$ , the desired answer is $7\cdot \frac{\sin \angle{SAT}}{\sin \angle{ATS}}=\frac{35}{8}$ leads to $\boxed{043}$
~blusoul

## Solution 7 (no trig or projections)
Note that since $\triangle SAP~\triangle BCP$ , $\frac{9}{SP}=\frac{BC}{7}=\frac{PC}{4}$ . Furthermore, since $\triangle ACQ~\triangle TBQ$ , we have $\frac{7}{TQ}=\frac{AC}{5}=\frac{QC}{6}$ . From Stewart's on triangle $BCP$ , we have $25CQ+BC^2\cdot TQ=TQ\cdot CQ\cdot TC+36TC$ , and since $TQ\cdot CQ=6\cdot7=42$ by power of a point, this simplifies to $25CQ+BC^2\cdot TQ=78TC$ . Similarly, $49CP+AC^2\cdot SP=52SC$ . Finally, using Ptolemy's on quadrilateral $ACBS$ yields $13SC=7BC+SB\cdot AC$ , and using Ptolemy's on quadrilateral $ACBT$ yields $13TC=5AC+TA\cdot BC$ . From Ptolemy's on $ABTS$ , we find $SB\cdot TA=13ST+35$ , which is nice because it contains $ST$ . We return to our first Stewart's equation: $25CQ+BC^2\cdot TQ=78TC$ , and we notice that $CQ$ and $TQ$ can be related to $AC$ using our similar triangle conditions. Substituting gives us $30AC+\frac{35BC^2}{AC}=78TC$ , which by four times our first Ptolemy's equation also equals $30AC+6TA\cdot BC$ . Thus, $\frac{35BC^2}{AC}=6TA\cdot BC$ and $TA=\frac{35}{6}\cdot\frac{BC}{AC}$ . Similarly, from our other Stewart's equation, we find $28BC+\frac{63AC^2}{BC}=52SC=28BC+4SB\cdot AC$ , or $SB=\frac{63}{4}\cdot\frac{AC}{BC}$ . Plugging this into our final Ptolemy's equation, we find \[SB\cdot TA=13ST+35\Longrightarrow\frac{35\cdot63}{6\cdot4}=13ST+35\Longrightarrow ST=\frac{\frac{35\cdot21}{8}-35}{13}=\frac{35\cdot\frac{13}{8}}{13}=\frac{35}{8},\] giving us our final answer of $\boxed{043}$ .
~wuwang2002
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
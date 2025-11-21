# 2010 AIME II Problem 15

## Problem

In triangle $ABC$ , $AC = 13$ , $BC = 14$ , and $AB=15$ . Points $M$ and $D$ lie on $AC$ with $AM=MC$ and $\angle ABD = \angle DBC$ . Points $N$ and $E$ lie on $AB$ with $AN=NB$ and $\angle ACE = \angle ECB$ . Let $P$ be the point, other than $A$ , of intersection of the circumcircles of $\triangle AMN$ and $\triangle ADE$ . Ray $AP$ meets $BC$ at $Q$ . The ratio $\frac{BQ}{CQ}$ can be written in the form $\frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m-n$ .

### Diagram

[asy] size(250); defaultpen(fontsize(9pt)); picture pic; pair A,B,C,D,E,M,N,P,Q; B=MP("B",origin, SW); C=MP("C", (12.5,0), SE); A=MP("A", IP(CR(C,10),CR(B,15)), dir(90)); N=MP("N", (A+B)/2, dir(180)); M=MP("M", midpoint(C--A), dir(70)); D=MP("D", extension(B,incenter(A,B,C),A,C), dir(C-B)); E=MP("E", extension(C,incenter(A,B,C),A,B), dir(90)); P=MP("P", OP(circumcircle(A,M,N),circumcircle(A,D,E)), dir(-70)); Q = MP("Q", extension(A,P,B,C),dir(-90)); draw(B--C--A--B^^M--P--N^^D--P--E^^A--Q); draw(circumcircle(A,M,N), gray); draw(circumcircle(A,D,E), heavygreen); dot(A);dot(B);dot(C);dot(D);dot(E);dot(P);dot(Q);dot(M);dot(N); [/asy]

## Solution 1 (Linearity)
Define the function $f:\mathbb{R}^{2}\rightarrow\mathbb{R}$ by \[f(X)=\text{Pow}_{(AMN)}(X)-\text{Pow}_{(ADE)}(X)\] for points $X$ in the plane. Then $f$ is linear, so $\frac{BQ}{CQ}=\frac{f(B)-f(Q)}{f(Q)-f(C)}$ . But $f(Q)=0$ since $Q$ lies on the radical axis of $(AMN)$ , $(ADE)$ thus \[\frac{BQ}{CQ}=-\frac{f(B)}{f(C)}=-\frac{BN\cdot BA-BE\cdot BA}{CM\cdot CA-CD\cdot CA}\] Let $AC=b$ , $BC=a$ and $AB=c$ . Note that $BN=\tfrac{c}{2}$ and $CM=\tfrac{b}{2}$ because they are midpoints, while $BE=\frac{ac}{a+b}$ and $CD=\frac{ab}{a+c}$ by Angle Bisector Theorem. Thus we can rewrite this expression as \begin{align*}&-\frac{\tfrac{c^{2}}{2}-\tfrac{ac^{2}}{a+b}}{\tfrac{b^{2}}{2}-\tfrac{ab^{2}}{a+c}} \\ =&-\left(\frac{c^{2}}{b^{2}}\right)\left(\frac{\tfrac{1}{2}-\tfrac{a}{a+b}}{\tfrac{1}{2}-\tfrac{a}{a+c}}\right) \\ =&\left(\frac{c^{2}}{b^{2}}\right)\left(\frac{a+c}{a+b}\right) \\ =&\left(\frac{225}{169}\right)\left(\frac{29}{27}\right) \\ =&~\frac{725}{507}\end{align*} so $m-n=\boxed{218}$ .

## Official Solution (MAA)
The Angle Bisector Theorem implies that $E$ lies on $\overline{AN}$ and $D$ lies on $\overline{MC}$ because $AE/EB = AC/BC < 1$ and $AD/DC = AB/CB > 1$ . The Angle Bisector Theorem furthermore implies \[NE=AN-AE=\frac 12\cdot AB - \frac{AC}{AC+BC}\cdot AB=\frac 5{18}\] and \[MD = CM - CD = \frac 12\cdot AC - \frac{BC}{BC+BA}\cdot AC = \frac{13}{58}.\] Because $ANPM$ is cyclic, $\angle ENP = \angle ANP = \angle PMD$ . Because $AEPD$ is cyclic, $\angle NEP = 180^\circ-\angle AEP = \angle MDP$ . Because $\angle ENP =\angle PMD$ and $\angle NEP = \angle MDP$ , triangles $NEP$ and $MDP$ are similar. Hence \[\frac{NE}{MD}=\frac{NP}{MP}.\] Applying the Law of Sines to $\triangle ANP$ and $\triangle AMP$ gives \[\frac{NE}{MD} = \frac{NP}{MP} = \frac{\sin \angle NAP}{\sin \angle PAM} = \frac{\sin \angle BAQ}{\sin \angle QAC}\] and thus \[\frac{\sin \angle BAQ}{\sin \angle QAC} = \frac{(\frac{5}{18})}{(\frac{13}{58})} = \frac{145}{117}.\] Thus \[\frac{BQ}{QC} = \frac{\textrm{Area}(ABQ)}{\textrm{Area}(ACQ)} = \frac{\frac{1}{2}\cdot AB \cdot AQ \cdot \sin \angle BAQ}{\frac{1}{2}\cdot AC \cdot AQ \cdot \sin \angle QAC}= \frac{15}{13} \cdot \frac{145}{117} = \frac{725}{507},\] and $m - n = 218$ .

## Solution 2
Let $Y = MN \cap AQ$ . $\frac {BQ}{QC} = \frac {NY}{MY}$ since $\triangle AMN \sim \triangle ACB$ . Since quadrilateral $AMPN$ is cyclic, $\triangle MYA \sim \triangle PYN$ and $\triangle MYP \sim \triangle AYN$ , yielding $\frac {YM}{YA} = \frac {MP}{AN}$ and $\frac {YA}{YN} = \frac {AM}{PN}$ . Multiplying these together yields * $\frac {YN}{YM} = \left(\frac {AN}{AM}\right) \left(\frac {PN}{PM}\right)$ .
$\frac {AN}{AM} = \frac {\frac {AB}{2}}{\frac {AC}{2}} = \frac {15}{13}$ .
Now we claim that $\triangle PMD \sim \triangle PNE$ . To prove this, we can use cyclic quadrilaterals.
From $AMPN$ , $\angle PNY \cong \angle PAM$ and $\angle ANM \cong \angle APM$ . So, $m\angle PNA = m\angle PNY + m\angle ANM = m\angle PAM + m\angle APM = 180-m\angle PMA$ and $\angle PNA \cong \angle PMD$ .
From $ADPE$ , $\angle PDE \cong \angle PAE$ and $\angle EDA \cong \angle EPA$ . Thus, $m\angle MDP = m\angle PDE + m\angle EDA = m\angle PAE + m\angle EPA = 180-m\angle PEA$ and $\angle PDM \cong \angle PEN$ .
Thus, from AA similarity, $\triangle PMD \sim \triangle PNE$ .
Therefore, $\frac {PN}{PM} = \frac {NE}{MD}$ , which can easily be computed by the angle bisector theorem to be $\frac {145}{117}$ . It follows that * $\frac {BQ}{CQ} = \frac {15}{13} \cdot \frac {145}{117} = \frac {725}{507}$ , giving us an answer of $725 - 507 = \boxed{218}$ .
- These two ratios are the same thing and can also be derived from the Ratio Lemma.
Ratio Lemma : $\frac{BD}{DC} = \frac{AB}{AC} \cdot \frac{\sin \angle BAD}{\sin \angle CAD}$ , for any cevian AD of a triangle ABC. For the sine ratios use Law of Sines on triangles APM and APN, \[\frac{PM}{\sin \angle PAM}=\frac{AP}{\sin \angle AMP}=\frac{AP}{\sin \angle ANP}=\frac{PN}{\sin \angle PAN}\] . The information needed to use the Ratio Lemma can be found from the similar triangle section above.
Source: [1] by Zhero
### Extension
The work done in this problem leads to a nice extension of this problem:
Given a $\triangle ABC$ and points $A_1$ , $A_2$ , $B_1$ , $B_2$ , $C_1$ , $C_2$ , such that $A_1$ , $A_2$ $\in BC$ , $B_1$ , $B_2$ $\in AC$ , and $C_1$ , $C_2$ $\in AB$ , then let $\omega_1$ be the circumcircle of $\triangle AB_1C_1$ and $\omega_2$ be the circumcircle of $\triangle AB_2C_2$ . Let $A'$ be the intersection point of $\omega_1$ and $\omega_2$ distinct from $A$ . Define $B'$ and $C'$ similarly. Then $AA'$ , $BB'$ , and $CC'$ concur.
This can be proven using Ceva's theorem and the work done in this problem, which effectively allows us to compute the ratio that line $AA'$ divides the opposite side $BC$ into and similarly for the other two sides.

## Solution 3
This problem can be solved with barycentric coordinates. Let triangle $ABC$ be the reference triangle with $A=(1,0,0)$ , $B=(0,1,0)$ , and $C=(0,0,1)$ . Thus, $N=(1:1:0)$ and $M=(1:0:1)$ . Using the Angle Bisector Theorem, we can deduce that $D=(14:0:15)$ and $E = (14:13:0)$ . Plugging the coordinates for triangles $ANM$ and $AED$ into the circle formula, we deduce that the equation for triangle $ANM$ is $-a^2yz-b^2zx-c^2xy+(\frac{c^2}{2}y+\frac{b^2}{2}z)(x+y+z)=0$ and the equation for triangle $AED$ is $-a^2yz-b^2zx-c^2xy+(\frac{14c^2}{27}y+\frac{14b^2}{29}z)(x+y+z)=0$ . Solving the system of equations, we get that $\frac{c^2y}{54}=\frac{b^2z}{58}$ . This equation determines the radical axis of circles $ANM$ and $AED$ , on which points $P$ and $Q$ lie. Thus, solving for $\frac{z}{y}$ gets the desired ratio of lengths, and $\frac{z}{y}=\frac{58c^2}{54b^2}$ and plugging in the lengths $b=13$ and $c=15$ gets $\frac{725}{507}$ . From this we get the desired answer of $725-507=\boxed{218}$ . -wertguk

## Solution 4 (Fast)
Observe that $P$ is the center of spiral symmetry of segments $DM$ and $EN$ .
Using the angle bisector theorem, we compute $DM = \frac{13}{58}$ and $EN = \frac{5}{18}$ . Hence, it follows that the side-length ratio of triangles $DMP$ to $ENP$ is $\frac{117}{145}$ (note that the two triangles are similar by the spiral symmetry). This implies that the ratio of the height from $P$ to $AC$ to the height from $P$ to $AB$ is $\frac{117}{145}$ , so we compute the area ratio $\frac{APC}{APB} = \frac{507}{725}$ .
From the above, we see that the barycentric coordinates of $P$ are of the form $(x : 507 : 725)$ . Hence, it follows that the point $Q$ has the coordinates $(0 : 507 : 725)$ , so $\frac{BQ}{CQ} = \frac{725}{507}$ and our answer is $\boxed{218}$ .
~hgomamogh

## Video Solution by the SpreadTheMathLove
https://www.youtube.com/watch?v=gzmY6nbbphw
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
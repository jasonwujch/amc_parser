# 2001 AIME I Problem 7

## Problem

Triangle $ABC$ has $AB=21$ , $AC=22$ and $BC=20$ . Points $D$ and $E$ are located on $\overline{AB}$ and $\overline{AC}$ , respectively, such that $\overline{DE}$ is parallel to $\overline{BC}$ and contains the center of the inscribed circle of triangle $ABC$ . Then $DE=m/n$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

1 Problem

- 1 Problem

- 2 Solution 1

- 3 Solution 2

- 4 Solution 3 (mass points)

- 5 Solution 4 (Faster)

- 6 Solution 5

- 7 Solution 6

- 8 Solution 7

- 9 Solution 8 (vectors)

- 10 See also

## Solution 1
Let $I$ be the incenter of $\triangle ABC$ , so that $BI$ and $CI$ are angle bisectors of $\angle ABC$ and $\angle ACB$ respectively. Then, $\angle BID = \angle CBI = \angle DBI,$ so $\triangle BDI$ is isosceles , and similarly $\triangle CEI$ is isosceles. It follows that $DE = DB + EC$ , so the perimeter of $\triangle ADE$ is $AD + AE + DE = AB + AC = 43$ . Hence, the ratio of the perimeters of $\triangle ADE$ and $\triangle ABC$ is $\frac{43}{63}$ , which is the scale factor between the two similar triangles, and thus $DE = \frac{43}{63} \times 20 = \frac{860}{63}$ . Thus, $m + n = \boxed{923}$ .

## Solution 2
The semiperimeter of $ABC$ is $s = \frac{20 + 21 + 22}{2} = \frac{63}{2}$ . By Heron's formula , the area of the whole triangle is $A = \sqrt{s(s-a)(s-b)(s-c)} = \frac{21\sqrt{1311}}{4}$ . Using the formula $A = rs$ , we find that the inradius is $r = \frac{A}{s} = \frac{\sqrt{1311}}6$ . Since $\triangle ADE \sim \triangle ABC$ , the ratio of the heights of triangles $ADE$ and $ABC$ is equal to the ratio between sides $DE$ and $BC$ . From $A=\frac{1}{2}bh$ , we find $h_{ABC} = \frac{21\sqrt{1311}}{40}$ . Thus, we have
Solving for $DE$ gives $DE=\frac{860}{63},$ so the answer is $m+n=\boxed{923}$ .
Or we have the area of the triangle as $S$ . Using the ratio of heights to ratio of bases of $ADE$ and $ABC$ $\frac {\frac {2S}{20}-\frac {2S}{63}}{\frac {2S}{20}}= \frac {DE}{BC(20)}$ from that it is easy to deduce that $DE=\frac{860}{63}$ .

## Solution 3 (mass points)
Let $P$ be the incenter ; then it is be the intersection of all three angle bisectors . Draw the bisector $AP$ to where it intersects $BC$ , and name the intersection $F$ .
Using the angle bisector theorem , we know the ratio $BF:CF$ is $21:22$ , thus we shall assign a weight of $22$ to point $B$ and a weight of $21$ to point $C$ , giving $F$ a weight of $43$ . In the same manner, using another bisector, we find that $A$ has a weight of $20$ . So, now we know $P$ has a weight of $63$ , and the ratio of $FP:PA$ is $20:43$ . Therefore, the smaller similar triangle $ADE$ is $43/63$ the height of the original triangle $ABC$ . So, $DE$ is $43/63$ the size of $BC$ . Multiplying this ratio by the length of $BC$ , we find $DE$ is $860/63 = m/n$ . Therefore, $m+n=\boxed{923}$ .

## Solution 4 (Faster)
More directly than Solution 2, we have \[DE=BC\left(\frac{h_a-r}{h_a}\right)=20\left(1-\frac{r}{\frac{[ABC]}{\frac{BC}{2}}}\right)=20\left(1-\frac{10r}{sr}\right)=20\left(1-\frac{10}{\frac{63}{2}}\right)=\frac{860}{63}\implies \boxed{923}.\]

## Solution 5
Diagram borrowed from Solution 3.
Let the angle bisector of $\angle{A}$ intersects $BC$ at $F$ .
Applying the Angle Bisector Theorem on $\angle{A}$ we have \[\frac{AB}{BF}=\frac{AC}{CF}\] \[BF=BC\cdot(\frac{AB}{AB+AC})\] \[BF=\frac{420}{43}\] Since $BP$ is the angle bisector of $\angle{B}$ , we can once again apply the Angle Bisector Theorem on $\angle{B}$ which gives \[\frac{BA}{AP}=\frac{BF}{FP}\] \[\frac{AP}{PF}=\frac{AB}{BF}=\frac{41}{20}\] Since $\bigtriangleup ADE\sim\bigtriangleup ABC$ we have \[\frac{DE}{BC}=\frac{AP}{AF}\] \[DE=BC\cdot(\frac{AP}{(\frac{61}{41})\cdot AP})\] Solving gets $DE=\frac{860}{63}$ . Thus $m+n=860+63=\boxed{923}$ .
~ Nafer

## Solution 6
Let $A'$ be the foot of the altitude from $A$ to $\overline {BC}$ and $K$ be the foot of the altitude from $A$ to $\overline{DE}$ . Evidently, \[\frac{AK}{AA'} = 1- \frac{r}{AA'} = 1 - \frac{T/s}{T/BC}\] where $r$ is the inradius, $T = [ABC]$ , and $s$ is the semiperimeter. So, \[\frac{AK}{AA'} = 1 - \frac{BC}{s} = 1 - \frac{20}{63}= \frac{43}{63}\] Therefore, by similar triangles, we have $DE = BC * \frac{AK}{AA'} = 20 * \frac{AK}{AA'}= \boxed{\frac{860}{63}}$ .

## Solution 7
Label $P$ the point the angle bisector of $A$ intersects ${BC}$ . First we find ${BP}$ and ${PC}$ . By the Angle Bisector Theorem, $\frac{BP}{PC} = \frac{21}{22}$ and solving for each using the fact that ${BC} = 20$ , we see that ${BP} = \frac{420}{43}$ and $PC = \frac{440}{43}$ .
\[{AP} = 21*22 - \frac{440}{43}\cdot\frac{420}{43}\] \[{AP} = 21*22 - \frac{440\cdot420}{43^2}\]
Now we can calculate what ${AO}$ is. Using the formula to find the distance from a vertex to the incenter, ${AO} = \frac{43}{63} \cdot[21\cdot22 - \frac{420*440}{43^2}] = \frac{43^2\cdot22 - 20\cdot440}{43\cdot3}$ .
Now because $\triangle{APE} ~ \triangle{ABC}$ , we can find ${DE}$ by $\frac{AO}{AP} \cdot 20$ . Dividing and simplifying, we see that $\frac{1}{21}\cdot\frac{43}{3}\cdot20 = \frac{860}{63}$ . So the answer is $\boxed{923}$
~YBSuburbanTea

## Solution 8 (vectors)
To solve this problem, we can use the fact that, in $\triangle ABC$ , the vector representation of the incenter is $\overrightarrow I = \frac{a\overrightarrow A + b\overrightarrow B + c\overrightarrow C}{a+b+c}$ and that that the vector of the foot of the bisector of $\angle BAC$ on $\overline{BC}$ is $\overrightarrow P = \frac{b\overrightarrow B + c\overrightarrow C}{b+c}$ , where $a=BC,$ $b=AC,$ and $c=AB$ .
Let point $A$ be the origin of the coordinate plane. Then, $\overrightarrow A$ is the zero vector, so we can simplify our expression for $\overrightarrow I$ to $\frac{b\overrightarrow B + c\overrightarrow C}{a+b+c}$ . Now, note that the vector components of $\overrightarrow I$ and $\overrightarrow P$ are the same, but they are multiplied by different scalars. Thus, the ratio of these scalars is the ratio of these vectors' magnitudes. Thus, we have $\frac{|\overrightarrow I|}{|\overrightarrow P|}=\frac{\tfrac1{a+b+c}}{\tfrac1{b+c}}=\frac{b+c}{a+b+c}=\frac{43}{63}$ .
Let $D \in \overline{AB}$ and $E \in \overline{AC}$ . Because $\triangle AIE \sim \triangle APC$ , we have $\frac{AI}{AP}=\frac{AE}{AC}$ . Further, because $\triangle ADE \sim \triangle ABC$ , we have $\frac{AE}{AC}=\frac{DE}{BC}$ . Thus, by transitivity, $\frac{AI}{AP}=\frac{DE}{BC}$ . We know that $\frac{AI}{AP}=\frac{43}{63}$ , so $DE=\frac{AI}{AD}\cdot BC = \frac{43}{63}\cdot 20 = \frac{860}{63}$ .
Thus, our answer is $860+63=\boxed{923}$ .
These problems are copyrighted © by the Mathematical Association of America.
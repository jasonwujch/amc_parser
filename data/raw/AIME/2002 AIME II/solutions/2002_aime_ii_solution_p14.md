# 2002 AIME II Problem 14

## Problem

The perimeter of triangle $APM$ is $152$ , and the angle $PAM$ is a right angle . A circle of radius $19$ with center $O$ on $\overline{AP}$ is drawn so that it is tangent to $\overline{AM}$ and $\overline{PM}$ . Given that $OP=m/n$ where $m$ and $n$ are relatively prime positive integers, find $m+n$ .

## Solution 1
Let the circle intersect $\overline{PM}$ at $B$ . Then note $\triangle OPB$ and $\triangle MPA$ are similar. Also note that $AM = BM$ by power of a point . Using the fact that the ratio of corresponding sides in similar triangles is equal to the ratio of their perimeters, we have \[\frac{19}{AM} = \frac{152-2AM-19+19}{152} = \frac{152-2AM}{152}\] Solving, $AM = 38$ . So the ratio of the side lengths of the triangles is 2. Therefore, \[\frac{PB+38}{OP}= 2 \text{ and } \frac{OP+19}{PB} = 2\] so $2OP = PB+38$ and $2PB = OP+19.$ Substituting for $PB$ , we see that $4OP-76 = OP+19$ , so $OP = \frac{95}3$ and the answer is $\boxed{098}$ .

## Solution 2
Reflect triangle $PAM$ across line $AP$ , creating an isoceles triangle. Let $x$ be the distance from the top of the circle to point $P$ , with $x + 38$ as $AP$ . Given the perimeter is 152, subtracting the altitude yields the semiperimeter $s$ of the isoceles triangle, as $114 - x$ . The area of the isoceles triangle is:
$[PAM] = r \cdot s$
$[PAM] = 19 \cdot (114 - x)$
Now use similarity, draw perpendicular from $O$ to $PM$ , name the new point $D$ . Triangle $PDO$ is similar to triangle $PAM$ , by AA Similarity. Equating the legs, we get:
$\frac{\sqrt{x}}{19} = \frac{\sqrt{x + 38}}{AM}$
Solving for $AM$ , it yields $19 \cdot \sqrt{\frac{x + 38}{x}}$ .
$19 \cdot (114 - x) = AM \cdot AP = 19 \cdot (x + 38) \cdot \sqrt{\frac{x + 38}{x}}$
The $x^3$ cancels, yielding a quadratic. Solving yields $x = \frac{38}{3}$ . Add $19$ to find $OP$ , yielding $\frac{95}{3}$ or $\boxed{098}$ .

## Solution 3
Let the foot of the perpendicular from $O$ to $PM$ be $D;$ now $OD=19.$ Also let $AM=x$ and $PM=y.$ This means that $OP=\frac{y}{x}\cdot 19$ , since $O$ is on the angle bisector of $\angle M.$
We have that $\tan(\angle AMO)=\frac{19}{x},$ so \[\tan(\angle M)=\tan (2\cdot \angle AMO)=\frac{38x}{x^{2}-361}.\]
However $\tan(\angle M)=\frac{PA}{AM}=\frac{PO+OA}{AM}=\frac{\frac{y}{x}\cdot 19 + 19}{x}$ , so \[\frac{38x}{x^{2}-361}=19\cdot \frac{\frac{y}{x}+1}{x}\] \[\frac{2x^{2}}{x^{2}-361}=\frac{y}{x}+1\] \[\frac{x^{2}+361}{x^{2}-361}=\frac{y}{x}.\] \[x\cdot \frac{x^{2}+361}{x^{2}-361}=y\]
We now use the fact that the perimeter of $\triangle PAM$ is $152$ : \[PO+OA+AM+MP=152\] \[\frac{y}{x}\cdot 19+19+x+y=152\] \[19\left(\frac{x^{2}+361}{x^{2}-361}\right)+x\cdot \left(\frac{x^{2}+361}{x^{2}-361}\right)+x+19=152\] \[(x+19)\left(\frac{x^{2}+361}{x^{2}-361}+\frac{x^{2}-361}{x^{2}-361}\right)=152\] \[\frac{2x^{2}}{x-19}=152\] \[x^{2}-76x+19\cdot 76=0.\] This quadratic factors as $(x-38)^{2}=0,$ so $x=38$ , and \[\frac{y}{x}=\frac{38^{2}+361}{38^{2}-361}=\frac{5}{3}\] \[OP=\frac{y}{x}\cdot 19=\frac{95}{3}\to \boxed{98.}\]

## Solution 4
Let $K$ be the foot of the altitude from $O$ to $PM,$ and notice how $OK$ is a radius of the circle. Also, we have that $\angle OKM=\angle OAM=90^\circ,$ $OK=OA=90,$ and $OM=OM,$ so $\triangle OKM$ is congruent to $\triangle OAM.$ This means that because $\angle PMO=\angle KMO=\angle AMO,$ $O$ is the foot of the angle bisector from $M.$
Then, let $k=\angle AMO=\angle PMO.$ We have that \[\angle POK=180^\circ-\angle KOM-\angle AOM=2k=\angle PMA,\] so $\triangle PKO$ is similar to $\triangle PAM.$ Let $a=AM=KM,$ and let $p=152$ be the perimeter of $\triangle PAM.$ By similarity, we have that the perimeter of $\triangle PKO$ is $\frac{19}{a}\cdot p,$ so \[PK+PO=\dfrac{19}{a}\cdot p-19,\] so \[p=PK+PO+OA+AM+MK=\dfrac{19}{a}\cdot p-19+19+2a.\] Solving for $p,$ we have that \[p=\dfrac{2a}{1-\frac{19}{a}}\] and using $p=152$ we find that \[a^2-76a+38^2=(a-38)^2=0\] so $a=38.$
Finally, let $b=PO.$ We have by the angle bisector theorem that $PM=2b,$ so using the perimeter information one more time we get $3b+57=152$ and solving gives us \[b=\dfrac{95}{3}\implies \boxed{098}.\]
~BS2012
These problems are copyrighted © by the Mathematical Association of America.
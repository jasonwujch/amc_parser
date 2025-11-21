# 2010 AIME II Problem 9

## Problem

Let $ABCDEF$ be a regular hexagon . Let $G$ , $H$ , $I$ , $J$ , $K$ , and $L$ be the midpoints of sides $AB$ , $BC$ , $CD$ , $DE$ , $EF$ , and $AF$ , respectively. The segments $\overline{AH}$ , $\overline{BI}$ , $\overline{CJ}$ , $\overline{DK}$ , $\overline{EL}$ , and $\overline{FG}$ bound a smaller regular hexagon. Let the ratio of the area of the smaller hexagon to the area of $ABCDEF$ be expressed as a fraction $\frac {m}{n}$ where $m$ and $n$ are relatively prime positive integers. Find $m + n$ .

### Diagram

Let $M$ be the intersection of $\overline{AH}$ and $\overline{BI}$ .

Let $N$ be the intersection of $\overline{BI}$ and $\overline{CJ}$ .

Let $O$ be the center.

## Solution 1
Without loss of generality, let $BC=2.$
Note that $\angle BMH$ is the vertical angle to an angle of the regular hexagon, so it has a measure of $120^\circ$ .
Because $\triangle ABH$ and $\triangle BCI$ are rotational images of one another, we get that $\angle{MBH}=\angle{HAB}$ and hence $\triangle ABH \sim \triangle BMH \sim \triangle BCI$ .
Using a similar argument, $NI=MH$ , and
\[MN=BI-NI-BM=BI-(BM+MH).\]
Applying the Law of cosines on $\triangle BCI$ , $BI=\sqrt{2^2+1^2-2(2)(1)(\cos(120^\circ))}=\sqrt{7}$
\begin{align*}\frac{BC+CI}{BI}&=\frac{3}{\sqrt{7}}=\frac{BM+MH}{BH} \\ BM+MH&=\frac{3BH}{\sqrt{7}}=\frac{3}{\sqrt{7}} \\ MN&=BI-(BM+MH)=\sqrt{7}-\frac{3}{\sqrt{7}}=\frac{4}{\sqrt{7}} \\ \frac{\text{Area of smaller hexagon}}{\text{Area of bigger hexagon}}&=\left(\frac{MN}{BC}\right)^2=\left(\frac{2}{\sqrt{7}}\right)^2=\frac{4}{7}\end{align*}
Thus, the answer is $4 + 7 = \boxed{011}.$

## Solution 2 (Coordinate Bash)
We can use coordinates. Let $O$ be at $(0,0)$ with $A$ at $(1,0)$ ,
then $B$ is at $(\cos(60^\circ),\sin(60^\circ))=\left(\frac{1}{2},\frac{\sqrt{3}}{2}\right)$ ,
$C$ is at $(\cos(120^\circ),\sin(120^\circ))=\left(-\frac{1}{2},\frac{\sqrt{3}}{2}\right)$ ,
$D$ is at $(\cos(180^\circ),\sin(180^\circ))=(-1,0)$ ,
\begin{align*}&H=\frac{B+C}{2}=\left(0,\frac{\sqrt{3}}{2}\right) \\ &I=\frac{C+D}{2}=\left(-\frac{3}{4},\frac{\sqrt{3}}{4}\right)\end{align*}
Line $AH$ has the slope of $-\frac{\sqrt{3}}{2}$ and the equation of $y=-\frac{\sqrt{3}}{2}(x-1)$
Line $BI$ has the slope of $\frac{\sqrt{3}}{5}$ and the equation $y-\frac{3}{2}=\frac{\sqrt{3}}{5}\left(x-\frac{1}{2}\right)$
Let's solve the system of equation to find $M$
\begin{align*}-\frac{\sqrt{3}}{2}(x-1)-\frac{3}{2}&=\frac{\sqrt{3}}{5}\left(x-\frac{1}{2}\right) \\ -5\sqrt{3}x&=2\sqrt{3}x-\sqrt{3} \\ x&=\frac{1}{7} \\ y&=-\frac{\sqrt{3}}{2}(x-1)=\frac{3\sqrt{3}}{7}\end{align*}
Finally,
\begin{align*}&\sqrt{x^2+y^2}=OM=\frac{1}{7}\sqrt{1^2+(3\sqrt{3})^2}=\frac{1}{7}\sqrt{28}=\frac{2}{\sqrt{7}} \\ &\frac{\text{Area of smaller hexagon}}{\text{Area of bigger hexagon}}=\left(\frac{OM}{OA}\right)^2=\left(\frac{2}{\sqrt{7}}\right)^2=\frac{4}{7}\end{align*}
Thus, the answer is $\boxed{011}$ .
Diagram (by dragoon) https://services.artofproblemsolving.com/download.php?id=YXR0YWNobWVudHMvZC82L2ZiNDljZmZiNjUzYWE4NGRmNmIwYTljMWQxZDU2ZDc1ZmNiMDQ3LmpwZWc=&rn=RDQ3ODA2RjUtMzlDNi00QzQ3LUE2OTYtMjlCQkE4NThDNkRBLmpwZWc=

## Solution 3
Use the diagram. Now notice that all of the "overlapping triangles" are congruent. You can use the AA similarity to see that the small triangles are similar to the large triangles. Now you can proceed as in Solution 1.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
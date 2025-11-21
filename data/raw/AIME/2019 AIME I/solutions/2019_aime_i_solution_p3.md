# 2019 AIME I Problem 3

## Problem

In $\triangle PQR$ , $PR=15$ , $QR=20$ , and $PQ=25$ . Points $A$ and $B$ lie on $\overline{PQ}$ , points $C$ and $D$ lie on $\overline{QR}$ , and points $E$ and $F$ lie on $\overline{PR}$ , with $PA=QB=QC=RD=RE=PF=5$ . Find the area of hexagon $ABCDEF$ .

### Diagram

[asy] dot((0,0)); dot((15,0)); dot((15,20)); draw((0,0)--(15,0)--(15,20)--cycle); dot((5,0)); dot((10,0)); dot((15,5)); dot((15,15)); dot((3,4)); dot((12,16)); draw((5,0)--(3,4)); draw((10,0)--(15,5)); draw((12,16)--(15,15)); [/asy]

## Solution 1
We know the area of the hexagon $ABCDEF$ to be $\triangle PQR- \triangle PAF- \triangle BCQ- \triangle RED$ . Since $PR^2+RQ^2=PQ^2$ , we know that $\triangle PRQ$ is a right triangle. Thus the area of $\triangle PQR$ is $150$ . Another way to compute the area is \[\frac12 \cdot PQ\cdot RQ \sin \angle PQR = \frac12 \cdot 500 \cdot \sin \angle PQR=150 \implies \sin \angle PQR = \frac35.\] Then the area of $\triangle BCQ = \frac12 \cdot BQ \cdot CQ \cdot \sin \angle PQR= \frac{25}{2}\cdot \frac{3}{5}=\frac{15}{2}$ . Preceding in a similar fashion for $\triangle PAF$ , the area of $\triangle PAF$ is $10$ . Since $\angle ERD = 90^{\circ}$ , the area of $\triangle RED=\frac{25}{2}$ . Thus our desired answer is $150-\frac{15}{2}-10-\frac{25}{2}=\boxed{120}$

## Solution 2
Let $R$ be the origin. Noticing that the triangle is a 3-4-5 right triangle, we can see that $A=(4,12), B=(16,3), C=(15,0), D=(5,0), E=(0,5)$ , and $F=(0,10)$ . Using the shoelace theorem, the area is $\boxed{120}$ . Shoelace theorem:Suppose the polygon $P$ has vertices $(a_1, b_1)$ , $(a_2, b_2)$ , ... , $(a_n, b_n)$ , listed in clockwise order. Then the area of $P$ is
\[\dfrac{1}{2} |(a_1b_2 + a_2b_3 + \cdots + a_nb_1) - (b_1a_2 + b_2a_3 + \cdots + b_na_1)|\] You can also go counterclockwise order, as long as you find the absolute value of the answer.
.

## Solution 3 (Easiest, uses only basic geometry too)
Note that $\triangle{PQR}$ has area $150$ and is a $3$ - $4$ - $5$ right triangle. Then, by similar triangles, the altitude from $B$ to $QC$ has length $3$ and the altitude from $A$ to $FP$ has length $4$ , so $[QBC]+[DRE]+[AFP]=\frac{15}{2}+\frac{25}{2}+\frac{20}{2}=30$ , meaning that $[ABCDEF]=\boxed{120}$ . -Stormersyle

## Solution 4
Knowing that $\triangle{PQR}$ has area $150$ and is a $3$ - $4$ - $5$ triangle, we can find the area of the smaller triangles $\triangle{DRE}$ , $\triangle{APF}$ , and $\triangle{CQB}$ and subtract them from $\triangle{PQR}$ to obtain our answer. First off, we know $\triangle{DRE}$ has area $12.5$ since it is a right triangle. To the find the areas of $\triangle{APF}$ and $\triangle{CQB}$ , we can use Law of Cosines ( $c^2 = a^2 + b^2 - 2ab\cos C$ ) to find the lengths of $AF$ and $CB$ , respectively. Computing gives $AF = \sqrt{20}$ and $CB = \sqrt{10}$ . Now, using Heron's Formula, we find $\triangle{APF} = 10$ and $\triangle{CQB} = 7.5$ . Adding these and subtracting from $\triangle{PQR}$ , we get $150 - (10 + 7.5 + 12.5) = \boxed{120}$ -Starsher

## Solution 5 (Official MAA)
Triangle $PQR$ is a right triangle with are $\tfrac12\cdot15\cdot20=150$ . Each of $\triangle PAF,\triangle QCB,$ and $\triangle RED$ shares an angle with $\triangle PQR$ . Because the area of a triangle with sides $a,\,b,$ and included angle $\gamma$ is $\tfrac12a\cdot b\cdot \sin\gamma,$ it follows that the areas of $\triangle PAF,\triangle QCB,$ and $\triangle RED$ are each $5\cdot5\cdot\tfrac{150}{ab},$ where $a$ and $b$ are the lengths of the sides of $\triangle PQR$ adjacent to the shared angle. Thus the sum of the areas of $\triangle PAF,\triangle QCB,$ and $\triangle RED$ is \[5\cdot5\cdot\frac{150}{15\cdot25}+5\cdot5\cdot\frac{150}{25\cdot20}+5\cdot5\cdot\frac{150}{20\cdot15}=25\left(\frac25+\frac3{10}+\frac12\right)=30.\] Therefore $ABCDEF$ has area $150-30=\boxed{120}$ .

## Solution 6 (Using simple trigonometry)
Let's say that $\angle APF$ = $u$ . Then, we know that $\sin(u) = 20/25 = 4/5$ . Therefore, the area of $\triangle{APF}$ is $0.5*5*5*\sin(u)=10$ . Now, let's do the same thing with $\triangle{BQC}$ . If we name $\angle BQC$ as $w$ , we know that $\sin(w) = 15/25 = 3/5$ . Therefore, the area of $\triangle{BQC}$ is $0.5*5*5*\sin(w)=7.5$ . Since $\triangle{ERD}$ is a right-angled isosceles triangle, the area of $\triangle{ERD} = 12.5$ . In conclusion, the area of $ABCDEF$ is $\triangle{PRQ}-(\triangle{APF}+\triangle{BQC}+\triangle{ERD})=150-(10+7.5+12.5)=\boxed{120}$ .

## Video Solution #1(Complementary Area Counting?)
https://youtu.be/JQdad7APQG8?t=417

## Video Solution
https://www.youtube.com/watch?v=4jOfXNiQ6WM

## Video Solution 2
https://youtu.be/TSKcjht8Rfk?t=941
~IceMatrix

## Video Solution 3
https://youtu.be/9X18wCiYw9M
~Shreyas S
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
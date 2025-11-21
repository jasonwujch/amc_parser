# 2003 AIME II Problem 11

## Problem

Triangle $ABC$ is a right triangle with $AC = 7,$ $BC = 24,$ and right angle at $C.$ Point $M$ is the midpoint of $AB,$ and $D$ is on the same side of line $AB$ as $C$ so that $AD = BD = 15.$ Given that the area of triangle $CDM$ may be expressed as $\frac {m\sqrt {n}}{p},$ where $m,$ $n,$ and $p$ are positive integers, $m$ and $p$ are relatively prime, and $n$ is not divisible by the square of any prime, find $m + n + p.$

## Solution

## Solution 1
We use the Pythagorean Theorem on $ABC$ to determine that $AB=25.$
Let $N$ be the orthogonal projection from $C$ to $AB.$ Thus, $[CDM]=\frac{(DM)(MN)} {2}$ , $MN=BN-BM$ , and $[ABC]=\frac{24 \cdot 7} {2} =\frac{25 \cdot (CN)} {2}.$
From the third equation, we get $CN=\frac{168} {25}.$
By the Pythagorean Theorem in $\Delta BCN,$ we have
$BN=\sqrt{\left(\frac{24 \cdot 25} {25}\right)^2-\left(\frac{24 \cdot 7} {25}\right)^2}=\frac{24} {25}\sqrt{25^2-7^2}=\frac{576} {25}.$
Thus, $MN=\frac{576} {25}-\frac{25} {2}=\frac{527} {50}.$
In $\Delta ADM$ , we use the Pythagorean Theorem to get $DM=\sqrt{15^2-\left(\frac{25} {2}\right)^2}=\frac{5} {2} \sqrt{11}.$
Thus, $[CDM]=\frac{527 \cdot 5\sqrt{11}} {50 \cdot 2 \cdot 2}= \frac{527\sqrt{11}} {40}.$
Hence, the answer is $527+11+40=\boxed{578}.$
~ minor edits by kundusne000

## Solution 2
By the Pythagorean Theorem in $\Delta AMD$ , we get $DM=\frac{5\sqrt{11}} {2}$ . Since $ABC$ is a right triangle, $M$ is the circumcenter and thus, $CM=\frac{25} {2}$ . We let $\angle CMD=\theta$ . By the Law of Cosines ,
$24^2 = 2 \cdot (12.5)^2-2 \cdot (12.5)^2 * \cos (90+\theta).$
It follows that $\sin \theta = \frac{527} {625}$ . Thus, $[CMD]=\frac{1} {2} (12.5) \left(\frac{5\sqrt{11}} {2}\right)\left(\frac{527} {625}\right)=\frac{527\sqrt{11}} {40}$ .

## Solution 3
Suppose $ABC$ is plotted on the cartesian plane with $C$ at $(0,0)$ , $A$ at $(0,7)$ , and $B$ at $(24,0)$ . Then $M$ is at $(12,3.5)$ . Since $\Delta ABD$ is isosceles, $MD$ is perpendicular to $AM$ , and since $AM=12.5$ and $AD=15, MD=2.5\sqrt{11}$ . The slope of $AM$ is $-\frac{7}{24}$ so the slope of $MD$ is $\frac{24}{7}$ . Draw a vertical line through $M$ and a horizontal line through $D$ . Suppose these two lines meet at $X$ . then $MX=\frac{24}{7}DX$ so $MD=\frac{25}{7}DX=\frac{25}{24}MD$ by the pythagorean theorem. So $MX=2.4\sqrt{11}$ and $DX=.7\sqrt{11}$ so the coordinates of D are $(12-.7\sqrt{11},\, 3.5-2.4\sqrt{11})$ . Since we know the coordinates of each of the vertices of $\Delta CMD$ , we can apply the Shoelace Theorem to find the area of $\Delta CMD, \frac{527 \sqrt{11}}{40}$ .
~ minor edit by kundusne000

## Solution 4
Let $E$ be the intersection of lines $BC$ and $DM$ . Since triangles $\Delta CME$ and $\Delta CMD$ share a side and height, the area of $\Delta CDM$ is equal to $\frac{DM}{EM}$ times the area of $\Delta CME$ . By AA similarity, $\Delta EMB$ is similar to $\Delta ACB$ , $\frac{EM}{AC}=\frac{MB}{CB}$ . Solving yields $EM=\frac{175}{48}$ . Using the same method but for $EB$ yields $EB=\frac{625}{48}$ . As in previous solutions, by the Pythagorean Theorem , $DM=\frac{5\sqrt{11}}{2}$ . So, $\frac{DM}{EM}=\frac{24\sqrt{11}}{35}$ . Now, since we know both $CB$ and $EB$ , we can find that $CE=\frac{527}{48}$ . The height of $\Delta CME$ is the length from point $M$ to $CB$ . Since $M$ is the midpoint of $AB$ , the height is just $\frac{1}{2}\cdot7=\frac{7}{2}$ . Using this, we can find that the area of $\Delta CMD$ is $\frac{1}{2}\cdot\frac{7}{2}\cdot\frac{527}{48}\cdot\frac{24\sqrt{11}}{35}=\frac{527\sqrt{11}}{40}$ , giving our answer of $\boxed{578}$ .
Solution by someonenumber011.
Video Solution from Khan Academy: https://www.youtube.com/watch?v=smtrrefmC40
These problems are copyrighted © by the Mathematical Association of America.
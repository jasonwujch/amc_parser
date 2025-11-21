# 2013 AIME I Problem 9

## Problem

A paper equilateral triangle $ABC$ has side length $12$ . The paper triangle is folded so that vertex $A$ touches a point on side $\overline{BC}$ a distance $9$ from point $B$ . The length of the line segment along which the triangle is folded can be written as $\frac{m\sqrt{p}}{n}$ , where $m$ , $n$ , and $p$ are positive integers, $m$ and $n$ are relatively prime, and $p$ is not divisible by the square of any prime. Find $m+n+p$ .

[asy] import cse5; size(12cm); pen tpen = defaultpen + 1.337; real a = 39/5.0; real b = 39/7.0; pair B = MP("B", (0,0), dir(200)); pair A = MP("A", (9,0), dir(-80)); pair C = MP("C", (12,0), dir(-20)); pair K = (6,10.392); pair M = (a*B+(12-a)*K) / 12; pair N = (b*C+(12-b)*K) / 12; draw(B--M--N--C--cycle, tpen); draw(M--A--N--cycle); fill(M--A--N--cycle, mediumgrey); pair shift = (-20.13, 0); pair B1 = MP("B", B+shift, dir(200)); pair A1 = MP("A", K+shift, dir(90)); pair C1 = MP("C", C+shift, dir(-20)); draw(A1--B1--C1--cycle, tpen);[/asy]

## Solution 1
Let $M$ and $N$ be the points on $\overline{AB}$ and $\overline{AC}$ , respectively, where the paper is folded. Let $D$ be the point on $\overline{BC}$ where the folded $A$ touches it. [asy] import cse5; size(8cm); pen tpen = defaultpen + 1.337; real a = 39/5.0; real b = 39/7.0; pair B = MP("B", (0,0), dir(200)); pair A = MP("A", 12*dir(60), dir(90)); pair C = MP("C", (12,0), dir(-20)); pair D = MP("D", (9,0), dir(-80)); pair Y = MP("Y", midpoint(A--D), dir(-50)); pair M = MP("M", extension(A,B,Y,Y+(dir(90)*(D-A))), dir(180)); pair N = MP("N", extension(A,C,M,Y), dir(20)); pair F = MP("F", foot(A,B,C), dir(-90)); pair X = MP("X", extension(A,F,M,N), dir(-120)); draw(B--A--C--cycle, tpen); draw(M--N^^F--A--D); draw(rightanglemark(D,F,A,15)); draw(rightanglemark(A,Y,M,15)); MA("\theta",F,A,D,1.8); [/asy] We have $AF=6\sqrt{3}$ and $FD=3$ , so $AD=3\sqrt{13}$ . Denote $\angle DAF = \theta$ ; we get $\cos\theta = 2\sqrt{3}/\sqrt{13}$ .
In triangle $AXY$ , $AY=\tfrac 12 AD = \tfrac 32 \sqrt{13}$ , and $AX=AY\sec\theta =\tfrac{13}{4}\sqrt{3}$ .
In triangle $AMX$ , we get $\angle AMX=60^\circ-\theta$ and then use sine-law to get $MX=\tfrac 12 AX\csc(60^\circ-\theta)$ ; similarly, from triangle $ANX$ we get $NX=\tfrac 12 AX\csc(60^\circ+\theta)$ . Thus \[MN=\tfrac 12 AX(\csc(60^\circ-\theta) +\csc(60^\circ+\theta)).\] Since $\sin(60^\circ\pm \theta) = \tfrac 12 (\sqrt{3}\cos\theta \pm \sin\theta)$ , we get \begin{align*} \csc(60^\circ-\theta) +\csc(60^\circ+\theta) &= \frac{\sqrt{3}\cos\theta}{\cos^2\theta - \tfrac 14} = \frac{24 \cdot \sqrt{13}}{35} \end{align*} Then \[MN = \frac 12 AX \cdot \frac{24 \cdot \sqrt{13}}{35} = \frac{39\sqrt{39}}{35}\]
The answer is $39 + 39 + 35 = \boxed{113}$ .

## Solution 2
Let $P$ and $Q$ be the points on $\overline{AB}$ and $\overline{AC}$ , respectively, where the paper is folded.
Let $D$ be the point on $\overline{BC}$ where the folded $A$ touches it.
Let $a$ , $b$ , and $x$ be the lengths $AP$ , $AQ$ , and $PQ$ , respectively.
We have $PD = a$ , $QD = b$ , $BP = 12 - a$ , $CQ = 12 - b$ , $BD = 9$ , and $CD = 3$ .
Using the Law of Cosines on $BPD$ :
$a^{2} = (12 - a)^{2} + 9^{2} - 2 \times (12 - a) \times 9 \times \cos{60}$
$a^{2} = 144 - 24a + a^{2} + 81 - 108 + 9a$
$a = \frac{39}{5}$
Using the Law of Cosines on $CQD$ :
$b^{2} = (12 - b)^{2} +3^{2} - 2 \times (12 - b) \times 3 \times \cos{60}$
$b^{2} = 144 - 24b + b^{2} + 9 - 36 + 3b$
$b = \frac{39}{7}$
Using the Law of Cosines on $DPQ$ :
$x^{2} = a^{2} + b^{2} - 2ab \cos{60}$
$x^{2} = (\frac{39}{5})^2 + (\frac{39}{7})^2 - (\frac{39}{5} \times \frac{39}{7})$
$x = \frac{39 \sqrt{39}}{35}$
The solution is $39 + 39 + 35 = \boxed{113}$ .

## Solution 3
Proceed with the same labeling as in Solution 1.
$\angle B = \angle C = \angle A = \angle PDQ = 60^\circ$
$\angle PDB + \angle PDQ + \angle QDC = \angle QDC + \angle CQD + \angle C = 180^\circ$
Therefore, $\angle PDB = \angle CQD$ .
Similarly, $\angle BPD = \angle QDC$ .
Now, $\bigtriangleup BPD$ and $\bigtriangleup CDQ$ are similar triangles, so
$\frac{3}{12-a} = \frac{12-b}{9} = \frac{b}{a}$ .
Solving this system of equations yields $a = \frac{39}{5}$ and $b = \frac{39}{7}$ .
Using the Law of Cosines on $APQ$ :
$x^{2} = a^{2} + b^{2} - 2ab \cos{60}$
$x^{2} = (\frac{39}{5})^2 + (\frac{39}{7})^2 - (\frac{39}{5} \times \frac{39}{7})$
$x = \frac{39 \sqrt{39}}{35}$
The solution is $39 + 39 + 35 = \boxed{113}$ .
### Note
Once you find $DP$ and $DQ$ , you can scale down the triangle by a factor of $\frac{39}{35}$ so that all sides are integers. Applying Law of cosines becomes easier, you just need to remember to scale back up.

## Solution 4 (Coordinate Bash)
We let the original position of $A$ be $A$ , and the position of $A$ after folding be $D$ . Also, we put the triangle on the coordinate plane such that $A=(0,0)$ , $B=(-6,-6\sqrt3)$ , $C=(6,-6\sqrt3)$ , and $D=(3,-6\sqrt3)$ .
[asy] size(10cm); pen tpen = defaultpen + 1.337; real a = 39/5.0; real b = 39/7.0; pair B = MP("B", (0,0), dir(200)); pair A = (9,0); pair C = MP("C", (12,0), dir(-20)); pair K = (6,10.392); pair M = (a*B+(12-a)*K) / 12; pair N = (b*C+(12-b)*K) / 12; draw(B--M--N--C--cycle); draw(M--A--N--cycle); label("$D$", A, S); pair X = (6,6*sqrt(3)); draw(B--X--C); label("$A$",X,dir(90)); draw(A--X); [/asy]
Note that since $A$ is reflected over the fold line to $D$ , the fold line is the perpendicular bisector of $AD$ . We know $A=(0,0)$ and $D=(3,-6\sqrt3)$ . The midpoint of $AD$ (which is a point on the fold line) is $(\tfrac32, -3\sqrt3)$ . Also, the slope of $AD$ is $\frac{-6\sqrt3}{3}=-2\sqrt3$ , so the slope of the fold line (which is perpendicular), is the negative of the reciprocal of the slope of $AD$ , or $\frac{1}{2\sqrt3}=\frac{\sqrt3}{6}$ . Then, using point slope form, the equation of the fold line is \[y+3\sqrt3=\frac{\sqrt3}{6}\left(x-\frac32\right)\] \[y=\frac{\sqrt3}{6}x-\frac{13\sqrt3}{4}\] Note that the equations of lines $AB$ and $AC$ are $y=\sqrt3x$ and $y=-\sqrt3x$ , respectively. We will first find the intersection of $AB$ and the fold line by substituting for $y$ : \[\sqrt3 x=\frac{\sqrt3}{6}x-\frac{13\sqrt3}{4}\] \[\frac{5\sqrt3}{6}x=-\frac{13\sqrt3}{4} \implies x=-\frac{39}{10}\] Therefore, the point of intersection is $\left(-\tfrac{39}{10},-\tfrac{39\sqrt3}{10}\right)$ . Now, lets find the intersection with $AC$ . Substituting for $y$ yields \[-\sqrt3 x=\frac{\sqrt3}{6}x-\frac{13\sqrt3}{4}\] \[\frac{-7\sqrt3}{6}x=-\frac{13\sqrt3}{4} \implies x=\frac{39}{14}\] Therefore, the point of intersection is $\left(\tfrac{39}{14},-\tfrac{39\sqrt3}{14}\right)$ . Now, we just need to use the distance formula to find the distance between $\left(-\tfrac{39}{10},-\tfrac{39\sqrt3}{10}\right)$ and $\left(\tfrac{39}{14},-\tfrac{39\sqrt3}{14}\right)$ . \[\sqrt{\left(\frac{39}{14}+\frac{39}{10}\right)^2+\left(-\frac{39\sqrt3}{14}+\frac{39\sqrt3}{10}\right)^2}\] The number 39 is in all of the terms, so let's factor it out: \[39\sqrt{\left(\frac{1}{14}+\frac{1}{10}\right)^2+\left(-\frac{\sqrt3}{14}+\frac{\sqrt3}{10}\right)^2}=39\sqrt{\left(\frac{6}{35}\right)^2+\left(\frac{\sqrt3}{35}\right)^2}\] \[\frac{39}{35}\sqrt{6^2+\sqrt3^2}=\frac{39\sqrt{39}}{35}\] Therefore, our answer is $39+39+35=\boxed{113}$ , and we are done.
Solution by nosaj.

## Solution 5
Note: this requires lots of calculations that increase your chance of errors, but it only requires simple understanding of areas, similar triangles, and Heron's formula. I'll just put the strategy here because I am too lazy to calculate it myself right now.
1. notice that the two triangles on the sides of the folded corner are similar. using this, we can find that the side lengths of them are 9,7.8,4.2 and 3, 45/7, 39/7 2. use heron's formula to find the areas of those two triangles. remember that it is sqrt[s(s-a)(s-b)(s-c)] 3. using the area of these triangles, we can find the area of the triangle with the length we need. 4. use heron's formula again, with the unknown length as x, and since we know the area and the other two side lengths, we can just solve for x with this equation.
-EmilyQ

## Solution 6(Easy)
Thanks to Solution 1 for the diagram below:
[asy] import cse5; size(8cm); pen tpen = defaultpen + 1.337; real a = 39/5.0; real b = 39/7.0; pair B = MP("B", (0,0), dir(200)); pair A = MP("A", 12*dir(60), dir(90)); pair C = MP("C", (12,0), dir(-20)); pair D = MP("D", (9,0), dir(-80)); pair Y = MP("Y", midpoint(A--D), dir(-50)); pair M = MP("M", extension(A,B,Y,Y+(dir(90)*(D-A))), dir(180)); pair N = MP("N", extension(A,C,M,Y), dir(20)); pair F = MP("F", foot(A,B,C), dir(-90)); pair X = MP("X", extension(A,F,M,N), dir(-120)); draw(B--A--C--cycle, tpen); draw(M--N^^F--A--D); draw(rightanglemark(D,F,A,15)); draw(rightanglemark(A,Y,M,15)); MA("\theta",F,A,D,1.8); [/asy]
We will use the notation already on the diagram, but our solution is slightly different.
We will only need M and N.
Let NC be length a, which implies NA be 12-a.
Also, AC = 3 because AB = 9
By the Law of Cosines on NCA,
$(12-a)^2=a^2+3^2-2(a)(3)(cos60)$
which simplifies to:
$a=\frac{45}{7}$
Which means that NC = 45/7 and NA = 39/7.
We can do the same thing for MBA.
This time, MB = b.
$(12-b)^2=b^2+81-2(9)(b)(cos60)$
Which gives:
$b=\frac{21}{5}$ Which implies that MA = $\frac{39}{5}$ Now, since MAN is 60 degrees, we can apply the Law of Cosines again(I know, I don't like bashy things too) to get:
$c^2=(\frac{39}{5})^2+39/7^2-2(39/7)(39/5)(cos60)$
Which leads us to our answer => 113
~MC

## Video Solution
https://www.youtube.com/watch?v=581ZtcQFCaE&t=98s
This video is private for some reason ~get-rickrolled
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
# 2021 Fall AMC 10B Problem 18

## Problem

Three identical square sheets of paper each with side length $6{ }$ are stacked on top of each other. The middle sheet is rotated clockwise $30^\circ$ about its center and the top sheet is rotated clockwise $60^\circ$ about its center, resulting in the $24$ -sided polygon shown in the figure below. The area of this polygon can be expressed in the form $a-b\sqrt{c}$ , where $a$ , $b$ , and $c$ are positive integers, and $c$ is not divisible by the square of any prime. What is $a+b+c?$

$(\textbf{A})\: 75\qquad(\textbf{B}) \: 93\qquad(\textbf{C}) \: 96\qquad(\textbf{D}) \: 129\qquad(\textbf{E}) \: 147$

## Solution 1
[asy] defaultpen(fontsize(8)+0.8); size(100); pair A=(0,0); pair B=(1.732,3); pair C=(3,3); pair D=(3,1.732); draw(A--(0,3)--C--(3,0)--A, lightgray+dashed); draw(A--B--C--A); draw(A--D--C, gray); label("$A$",A,W); label("$B$",B,N); label("$C$",C,NE); label("$D$",D,E); label("$E$",(0,3),NW); label("$F$",(3,0),E); [/asy] The $24$ -sided polygon is made out of $24$ shapes like $\triangle ABC$ . Then $\angle BAC=360^\circ/24=15^\circ$ , and $\angle EAC = 45^\circ$ , so $\angle{EAB} = 30^{\circ}$ . Then $EB=AE\tan 30^\circ = \sqrt{3}$ ; therefore $BC=EC-EB=3-\sqrt{3}$ . Thus \[[ABC] = \frac{BC}{EC}\cdot [ACE] = \frac{3-\sqrt{3}}{3}\cdot \frac 92\] and the required area is $24\cdot[ABC] =108-36\sqrt{3}$ . Finally $108+36+3=\boxed{(\textbf{E})\ 147}$ . ~lopkiloinm

## Solution 2 (15-75-90 triangles)
Break the $24$ -gon as shown so that there are $12$ copies of quadrilateral $OBAC$ . We can find the area of this quadrilateral by finding the area of triangle $OBC$ and subtracting the area of triangle $ABC$ .
The angle from $O$ to one of the vertices of the original square is $45^\circ{}$ , and this point rotates $30^\circ{}$ , so the angle that $OC$ makes with the horizontal is $75^\circ{}$ .
Let $D$ be the intersection of $OA$ with $BC$ . Since $ABC$ and $OBC$ are both isosceles, $OD$ forms a right angle with $BC$ . Furthermore, $\angle DOC = 90^\circ{}-75^\circ{} = 15^\circ{}$ .
Note that $OC$ is equal to $3\sqrt{2}$ because it is half the diagonal of the square with side length $6$ . We can now split up the $15-75-90$ into $30-60-90$ and $15-15-150$ triangles to find the height and length of the triangle:
Now we have use Pythagorean: $x^2+(x \cdot (2+\sqrt{3}))^2 = 3\sqrt{2}^2 \implies x^2+x^2 \cdot (7+4\sqrt{3}) = 18$ $\implies x^2 = \frac{18}{8+4\sqrt{3}} = \frac{9}{4+2\sqrt{3}} \implies x^2 = \frac{36-18\sqrt{3}}{4}$
Now note that $x$ must be in the form of $\frac{a\sqrt{3}-b}{2}$ . Therefore, $-2ab = -18 \implies ab=9$ . We can guess that $a=b=3$ . Sure enough, $3\sqrt{3}^2 +3^2= 36$ , so $x = \frac{3\sqrt{3}-3}{2}$ . Then the height of the triangle is $x \cdot (2+\sqrt{3}) = \frac{3\sqrt{3}+3}{2}$ .
The area of triangle $OBC$ is equal to the length times the height of triangle $ODC$ since this triangle has half the area of the full triangle. Therefore the area of triangle $OBC = \frac{3\sqrt{3}-3}{2} \cdot \frac{3\sqrt{3}+3}{2} = \frac{18}{4}$ .
Now we look at triangle $ABC$ . $\angle OCA = 45^\circ{}$ because $OC$ is the diagonal of a square, and $\angle COA$ is $15^\circ{}$ as we saw earlier. Therefore, $\angle OAC = \angle OAB = 120^\circ{}$ . Because both these angles are $120$ , $\angle BAC = 360-240 = 120$ .
We can now split triangle $ABC$ into two congruent $30-60-90$ triangles, and we know the base of each since $BC = 3\sqrt{3}-3$ .
The height of these triangles is $\frac{\frac{3\sqrt{3}-3}{2}}{\sqrt{3}} = \frac{3-\sqrt{3}}{2}$ . Therefore the area of this triangle is $\frac{3\sqrt{3}-3}{2} \cdot \frac{3-\sqrt{3}}{2} = \frac{12\sqrt{3}-18}{4}$
Therefore the total area of this segment is $\frac{18}{4}-(\frac{12\sqrt{3}-18}{4}) = \frac{36-12\sqrt{3}}{4} = 9-3\sqrt{3}$ . Multiplying by $12$ to find the entire area, the area of the figure is $108-36\sqrt{3}$ and the answer is $108+36+3 = 147 = \boxed{E}$
~KingRavi

## Solution 3
First note the useful fact that if $R$ is the circumradius of a dodecagon ( $12$ -gon) the area of the figure is $3R^2.$ If we connect the vertices of the $3$ squares we get a dodecagon. The radius of circumcircle of the dodecagon is simply half the diagonal of the square, which is $3\sqrt{2}.$ Thus the area of the dodecagon is $3 \cdot (3\sqrt{2})^2 = 3 \cdot 18 = 54.$ But, the problem asked for the area of the combined figure which was made from the rotated squares. This area is the area of the dodecagon, which was found, subtracting the $12$ isosceles triangles, which are formed when connecting the vertices of the squares to created the dodecagon. To find this area, we need to know the base of the isosceles triangle, call this $x.$ Then, we can use the Law of Cosines on the triangle that is formed from the two vertices of the square and the center of the square. After computing, we get that $x = 3\sqrt{3} -3.$ Realize that the $12$ isosceles are congruent with an angle measure of $120^{\circ},$ this means that we can create $4$ congruent equilateral triangles with side length of $3\sqrt3 - 3.$ The area of the equilateral triangle is $\frac{\sqrt{3}}{4} \cdot (3\sqrt{3} -3)^2 = \frac{\sqrt{3}}{4} \cdot (36 - 18\sqrt{3}) = \frac{36\sqrt{3} - 54}{4}.$ Thus, the area of all the twelve small equilateral traingles are $4 \cdot \frac{36\sqrt{3} - 54}{4} = 36\sqrt{3} - 54$ . Thus, the requested area is $54 - (36\sqrt{3} - 54) = 108 - 36\sqrt{3}.$ Thus, $a+b+c = 108 + 36 + 3 = 147,$ so the answer is $\boxed{(\textbf{E})\textbf{147}}.$
~NH14

## Solution 4 (30-60-90 Triangles)
To make things simpler, let's take only the original sheet and the 30 degree rotated sheet. Then the diagram is this;
[asy] size(10cm,0); path p = box((0,0), (1,1)); draw(p, black + linewidth(2.0pt)); draw(rotate(30,(1/2,1/2))*p,black + linewidth(2.0pt)); /*Rotate 60 degrees*/ [/asy]
The area of this diagram is the original square plus the area of the four triangles that 'jut' out of the square. Because the square is rotated $30^{\circ}$ , each triangle is a 30-60-90 triangle. Similarly, the triangles that are bounded on the inside of the original square outside of the rotated square are also congruent 30-60-90 triangles. Noting this, we can do some labelling:
[asy] size(10cm,0); path p = box((0,0), (1,1)); draw(p, black + linewidth(2.0pt)); draw(rotate(30,(1/2,1/2))*p,black + linewidth(2.0pt)); /*Rotate 60 degrees*/ label("$y$",(0.1,-0.05)); label("$x$",(0.4,0.05)); label("$y\sqrt{3}$",(0.8,-0.05)); label("$\frac{x}{2}$",(0.22,-0.12)); label("$\frac{x\sqrt{3}}{2}$",(0.5,-0.15)); label("$2y$",(0.8,0.15)); label("$y$",(1.05,0.1)); label("$\frac{x}{2}$",(1.12,0.22)); [/asy]
Since the side lengths of the squares must be the same, and they are both 6, we have a system of equations; \[y+x+y\sqrt{3} = 6\] \[\frac{x\sqrt{3}}{2} + 2y + \frac{x}{2} = 6\]
We solve this to get $x = 6-2\sqrt{3}$ and $y = 3-\sqrt{3}$ .
The area of each triangle is $\frac{x}{2} \cdot \frac{x\sqrt{3}}{2} \cdot \frac{1}{2} = 6\sqrt{3} - 9$ by plugging in $x$ .
The rotated 60 degree square is the same thing as rotating it 30 degrees counterclockwise, so it's triangles that jut out of the square will be congruent to the triangles we have found, and therefore they will have the same area.
Unfortunately, when drawing all three squares, we see the two triangles overlap; take the very top for example.
[asy] import olympiad; size(10cm); pair A,B,C,D,E,F,G; A = (0.211,0); B=(0.3657,0); C = (0.63397,0); D = (0.789,0); E = (0.31666,0.1823); F=(0.5,0.077); G=(0.68334,0.1823); draw((0,0)--(1,0),black+linewidth(2pt)); draw(A--E--C--cycle); draw(B--D--G--cycle); label("$A$",A,S); label("$B$",B,S); label("$C$",C,S); label("$D$",D,S); label("$E$",E,N); label("$F$",F,N); label("$G$",G,N); [/asy]
The area of this shape is twice the area of each of the triangles that we have already found minus the area of the small triangle that is overlapped by the two by PIE. Now we only need to find the area of $\bigtriangleup BCF$ .
$\angle GBD \cong \angle ECA \cong 30^{\circ}$ and by symmetry $\bigtriangleup BCF$ is isosceles, so it is a 30-30-120 triangle. If we draw a perpendicular, we split it into two 30-60-90 triangles;
[asy] import olympiad; size(10cm); pair A,B,C,D,E,F,G; A = (0.211,0); B=(0.3657,0); C = (0.63397,0); D = (0.789,0); E = (0.31666,0.1823); F=(0.5,0.077); G=(0.68334,0.1823); draw((0,0)--(1,0),black+linewidth(2pt)); draw(A--E--C--cycle); draw(B--D--G--cycle); draw(F--(0.5,0)); label("$A$",A,S); label("$B$",B,S); label("$C$",C,S); label("$D$",D,S); label("$E$",E,N); label("$F$",F,N); label("$G$",G,N); label("$H$",(0.5,0),S); [/asy]
By symmetry, the distance from A to the edge of the square is equal to the distance from D to the edge of the square is equal to $y$ . AC = BD = $x$ , and the side length of the square is 6, so we use PIE to obtain \[x+x-BC = 6-y-y \implies BC = 12 - 6\sqrt{3}\] To find the height of $\bigtriangleup BFC$ , we see that $HC = \frac{BC}{2} = 6-3\sqrt{3}$ . Then by 30-60-90 triangles, $HF = \frac{HC}{\sqrt{3}} = 2\sqrt{3} - 3$ . Finally, the area of $\bigtriangleup BFC = \frac{BC \cdot HF}{2} = 21\sqrt{3}-36$ .
Putting it all together, the area of the entire diagram is the area of the square plus four of these triangle-triangle intersections. The area of these intersections by PIE is $2 \cdot [ACE] - [BFC] = 12\sqrt{3}-18-(21\sqrt{3}-36) = 18-9\sqrt{3}$ . Therefore the total area is $36 + 4 \cdot(18-9\sqrt{3}) = 36 + 72 - 36 \sqrt{3} = 108 - 36\sqrt{3}$ .
Thus $a + b + c = 108+36+3 = 147 = \boxed{\textbf{(E) }147}$ .
~KingRavi

## Solution 5
As shown in Image:2021_AMC_12B_(Nov)_Problem_15,_sol.png , all 12 vertices of three squares form a regular dodecagon (12-gon). Denote by $O$ the center of this dodecagon.
Hence, $\angle AOB = \frac{360^\circ}{12} = 30^\circ$ .
Because the length of a side of a square is 6, $AO = 3 \sqrt{2}$ .
Hence, $AB = 2 AO \sin \frac{\angle AOB}{2} = 3 \left( \sqrt{3} - 1 \right)$ .
We notice that $\angle MAB = \angle MBA = 30^\circ$ . Hence, $AM = \frac{AB}{2\cos \angle MAB} = 3 - \sqrt{3}$ .
Therefore, the area of the region that three squares cover is \begin{align*} & \ [ABCDEFGHIJKL] - 12[MAB] \\ & = 12 [OAB] - 12 [MAB] \\ & = 12 \cdot \frac{1}{2} OA \cdot OB \sin \angle AOB - 12 \cdot \frac{1}{2} MA \cdot MB \sin \angle AMB \\ & = 6 OA^2 \sin \angle AOB - 6 MA^2 \sin \angle AMB \\ & = 108 - 36\sqrt{3} \end{align*}
Therefore, the answer is $\boxed{\textbf{(E) }147}$ .
~Steven Chen (www.professorchenedu.com)
~stjwyl (adjusted for readability aka minor edits)
Note: If you have square brackets around a specified polygon (i.e. [ABCD]), it means the writer is referring to the area of that polygon.
~flyingkinder123 (minor spelling edits)

## Solution 6
First, we can separate the shape into 12 congruent kites. The area of the figure can be determined by finding the area of one kite and multiplying it by 12. In order to to get the area of one kite, we need to find its diagonals, shown in blue.
We notice that angle FCE is $\frac{360^\circ}{12} = 30^\circ$ . Also, we know that CD is half of AB, so it has a length of 3. Now, we can find the lengths of FC and FD using the 30-60-90 triangle. We find that FC is $2\sqrt{3}$ and FD is $\sqrt{3}$ . Since FC is congruent to CE, CE is also $2\sqrt{3}$ . Using this information, we can conclude that ED is $2\sqrt{3}-3$ .
Now, we can find the shorter diagonal by using the Pythagorean theorem: \begin{align*} & {\rm FC}^2 = \sqrt{3}^2 + (2\sqrt{3}-3)^2 \\ & {\rm FC} = \sqrt{24- 12\sqrt{3}} \end{align*}
We can find the longer diagonal of the kite by looking at one of the square sheets of paper. We know that the side of the square has a length of 6, so the diagonal of the square must be $6\sqrt{2}$ . The longer diagonal of the kite is half of this length, so it has a length of $3\sqrt{2}$ .
The area of the entire figure is \begin{align*} & = 12 \cdot\frac{{\rm d_1*d_2}}{2} \\ & = 12 \cdot\frac{3\sqrt{2}\cdot\sqrt{24- 12\sqrt{3}}}{2} \\ & = 12 \cdot\frac{6\sqrt{12- 6\sqrt{3}}}{2} \\ & = 36 \sqrt{12- 6\sqrt{3}} \end{align*}
Now we can use algebra to make our answer look a little nicer. \begin{align*} & a-\sqrt{b} = \sqrt{12- 6\sqrt{3}} \\ & (a-\sqrt{b})^2 = (\sqrt{12- 6\sqrt{3}})^2 \\ & a^2-2a\sqrt{b}+b = 12 - 6\sqrt{3}\\ &\\ &a^2+b = 12 \\ &2a\sqrt{b} = 6\sqrt{3} \\ & a = 3, b = 3 \\ &\\ & a-\sqrt{b} = \sqrt{12- 6\sqrt{3}} = 3 - \sqrt{3} \end{align*}
The area of the entire region is $36(3 - \sqrt{3})$ , or $108 - 36\sqrt{3}$ .
Therefore, $a + b + c = 108 + 36+ 3 = 147 = \boxed{E}$ .
~JavaWhiz12

## Solution 7
Let $O$ be the center of the polygon, $A$ be the bottom right corner of the first square, $C$ be the next vertex to the left of $A$ , and $M$ be the midpoint between $A$ and $B$ , where $B$ is the bottom left corner of the first square. Note that because there are three $90^{\circ}$ squares separated by $\frac{90^{\circ}}{3} = 30^{\circ}$ , each side of the 24-sided polygon is equal in length, meaning to calculate the area of the whole polygon, we find the area of $\bigtriangleup OAC$ and multiply by 24.
To find $[\bigtriangleup OAC]$ , we already know the height $\overline{OM}$ is the sidelength of the square over $2$ , or $\frac{6}{2}=3$ , so we just need the length of the base $\overline{AC}$ . Notice that $\bigtriangleup OCM$ is a $30-60-90$ triangle since $\angle COM = \frac{360^{\circ}}{12} = 30^{\circ}$ , so $\overline{CM} = \frac{\overline{OM}}{\sqrt{3}} = \frac{3}{\sqrt{3}} = \sqrt{3}$ . Then $\overline{AC} = \overline{AM} - \overline{CM} = \frac{6}{2} - \sqrt{3} = 3 - \sqrt{3}$ , so \begin{align*} & [\bigtriangleup AOC] = \frac{1}{2} \cdot \overline{OM} \cdot \overline{AC} \\ & = \frac{1}{2} (3)(3 - \sqrt{3}) \\ & = \frac{9 - 3\sqrt{3}}{2} \end{align*}
Then the whole area of the polygon is $\frac{9 - 3\sqrt{3}}{2} \cdot 24 = 108 - 36\sqrt{3}$ . The desired solution is then $108 + 36 + 3 = 147$ , so the answer is $\boxed{\textbf{(E) 147}}$ .
~Tacozxyt

## Solution 8
Using the diagram from Solution 2, we observe two isosceles triangles. The larger triangle has angles of 75°, 75°, and 30°.
To find the angle measures of the smaller triangle \(BCO\), note that the congruent sides of \(\triangle BCO\) are each half of the diagonals of two squares. Since a diagonal of a square bisects the right angle (45°), we have \(75 - 45 = 30^\circ\) for each base angle, making the remaining vertex angle \(120^\circ\).
Because both triangles are isosceles, we have \(BO = CO\) and \(AB = AC\).
Using the formula for the area of a square, $A = \frac{d^2}{2}$ , we find
so $BO = 3\sqrt{2}.$
Let $[BCO]$ denote the area of \(\triangle BCO\). Using the area formula $\frac{1}{2}ab\sin C$ , we find
Next, to find the side lengths of \(\triangle ABC\), we apply the Law of Cosines to \(\triangle BCO\):
Now, let $AB = x.$ Applying the Law of Cosines to \(\triangle ABC\):
Simplifying,
We can now find the area of \(\triangle ABC\) using the same area formula:
Subtracting the two areas gives the area of the quadrilateral \(OBAC\):
Since there are 12 such regions in the figure, the total area is
The problem asks for \(a + b + c,\) so
~Voidling

## Video Solution 1 by Power of Logic
~math2718281828459

## Video Solution 2 by Interstigation (with some trigonometry)
https://www.youtube.com/watch?v=8GgGXsB3yjU
~Interstigation

## Video Solution 3 by WhyMath
https://youtu.be/kP3jD1-aVzY
~savannahsolver

## Video Solution 4 (1 min)
https://youtu.be/oKPQh9lU0X4

## Video Solution by TheBeautyofMath
https://youtu.be/YD9J394zeig
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
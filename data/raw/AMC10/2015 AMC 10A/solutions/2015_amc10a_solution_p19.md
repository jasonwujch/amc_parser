# 2015 AMC 10A Problem 19

## Problem

The isosceles right triangle $ABC$ has right angle at $C$ and area $12.5$ . The rays trisecting $\angle ACB$ intersect $AB$ at $D$ and $E$ . What is the area of $\bigtriangleup CDE$ ?

$\textbf{(A) }\dfrac{5\sqrt{2}}{3}\qquad\textbf{(B) }\dfrac{50\sqrt{3}-75}{4}\qquad\textbf{(C) }\dfrac{15\sqrt{3}}{8}\qquad\textbf{(D) }\dfrac{50-25\sqrt{3}}{2}\qquad\textbf{(E) }\dfrac{25}{6}$

## Solution 1 (No Trigonometry)
$\triangle ADC$ can be split into a $45-45-90$ right triangle and a $30-60-90$ right triangle by dropping a perpendicular from $D$ to side $AC$ . Let $F$ be where that perpendicular intersects $AC$ .
Because the side lengths of a $45-45-90$ right triangle are in ratio $a:a:a\sqrt{2}$ , $DF = AF$ .
Because the side lengths of a $30-60-90$ right triangle are in ratio $a:a\sqrt{3}:2a$ and $AF + FC = 5$ , $DF = \frac{5 - AF}{\sqrt{3}}$ .
Setting the two equations for $DF$ equal to each other, $AF = \frac{5 - AF}{\sqrt{3}}$ .
Solving gives $AF = DF = \frac{5\sqrt{3} - 5}{2}$ .
The area of $\triangle ADC =\frac12 \cdot DF \cdot AC = \frac{25\sqrt{3} - 25}{4}$ .
$\triangle ADC$ is congruent to $\triangle BEC$ , so their areas are equal.
A triangle's area can be written as the sum of the figures that make it up, so $[ABC] = [ADC] + [BEC] + [CDE]$ .
$\frac{25}{2} = \frac{25\sqrt{3} - 25}{4} + \frac{25\sqrt{3} - 25}{4} + [CDE]$ .
Solving gives $[CDE] = \frac{50 - 25\sqrt{3}}{2}$ , so the answer is $\boxed{\textbf{(D) }\frac{50 - 25\sqrt{3}}{2}}$
### Note
Another way to get $DF$ is to assume that $AF=DF$ is equal to $a$ , as previously mentioned, and $CF$ is equal to $a\sqrt{3}$ . $AF+DF=5=a+a\sqrt{3}$

## Solution 2 (Trigonometry)
The area of $\triangle ABC$ is $12.5$ , and so the leg length of $45 - 45 - 90$ $\triangle ABC$ is $5.$ Thus, the altitude to hypotenuse $AB$ , $CF$ , has length $\dfrac{5}{\sqrt{2}}$ by $45 - 45 - 90$ right triangles. Now, it is clear that $\angle{ACD} = \angle{BCE} = 30^\circ$ , and so by the Exterior Angle Theorem, $\triangle{CDE}$ is an isosceles $30 - 75 - 75$ triangle. Thus, $DF = CF \tan 15^\circ = \dfrac{5}{\sqrt{2}} (2 - \sqrt{3})$ by the Half-Angle formula, and so the area of $\triangle CDE$ is $DF \cdot CF = \dfrac{25}{2} (2 - \sqrt{3})$ . The answer is thus $\boxed{\textbf{(D) } \frac{50 - 25\sqrt{3}}{2}}$

## Solution 3 (Analytical Geometry)
Because the area of triangle $ABC$ is $12.5$ , and the triangle is right and isosceles, we can quickly see that the leg length of the triangle $ABC$ is 5. If we put the triangle on the coordinate plane, with vertex $C$ at the origin, and the hypotenuse in the first quadrant, we can use slope-intercept form and tangents to get three lines that intersect at the origin, $D$ , and $E$ . Then, you can use the distance formula to get the length of $DE$ . The height is just $\frac{5}{\sqrt{2}}$ , so the area is just $DE \cdot \frac{5}{\sqrt{2}} \cdot \frac{1}{2}=\boxed{\textbf{(D) } \frac{50 - 25\sqrt{3}}{2}}$

## Solution 4 (Weak Trigonometry)
Just like with Solution 1, we drop a perpendicular from $D$ onto $AC$ , splitting it into a $30$ - $60$ - $90$ triangle and a $45$ - $45$ - $90$ triangle. We find that $AF=\frac{5\sqrt{3}-5}{2}$ .
Now, since $\triangle AEC\cong \triangle BDC$ by ASA, $CE=CD$ . Since, $DF=\frac{5\sqrt{3}-5}{2}$ , $DC=2\cdot \frac{5\sqrt{3}-5}{2}=5\sqrt{3}-5$ . By the sine area formula, $[CDE]=\frac{1}{2}\cdot \sin 30\cdot CD^2=\frac{1}{4}\cdot (100-50\sqrt{3})=\frac{50-25\sqrt{3}}{2}\implies \boxed{\textbf{(D)}}$

## Solution 5 (Basic Trigonometry)
Prerequisite knowledge for this solution: the side ratios of a 30-60-90, and 45-45-90 right triangle.
We let point C be the origin. Since $\overline{CD}$ and $\overline{CE}$ trisect $\angle ACB = 90^{\circ}$ , this means $m\angle CEB = 30^{\circ}$ and the equation of $\overline{CE}$ is $y=\frac{\sqrt{3}}{3}$ (you can figure out that the tangent of 30 degrees gives $\frac{\sqrt{3}}{3}$ ). Next, we can find A to be at $(0, 5)$ and B at $(5, 0)$ , so the equation of $\overline{AB}$ is $y=-x+5$ . So we have the system:
\[\begin{cases}y=\frac{\sqrt{3}}{3}x\\y=-x+5\end{cases}\]
By substituting values, we can arrive at $\frac{3+\sqrt{3}}{3}x=5$ , or $x=5\cdot\frac{3}{3+\sqrt{3}}=\frac{15}{3+\sqrt{3}}$ . We multiply $x=\frac{15}{3+\sqrt{3}}\cdot\frac{3-\sqrt{3}}{3-\sqrt{3}}=\frac{45-15\sqrt{3}}{6}=\frac{15-5\sqrt{3}}{2}$ .
Dropping an altitude from E onto $\overline{CB}$ , and calling the intersection point G, we find that $\triangle EGB$ is a 45-45-90 triangle with a leg of $\frac{15-5\sqrt{3}}{2}\cdot\frac{\sqrt{3}}{3}=\frac{15\sqrt{3}-15}{6}=\frac{5\sqrt{3}-5}{2}$ . Thus, $EB=\frac{5\sqrt{3}-5}{2}\sqrt{2}=\frac{5\sqrt{6}-5\sqrt{2}}{2}$ .
Dropping an altitude from C onto $\overline{AB}$ , and calling the intersection point H, we find that $CH=\frac{5\sqrt{2}}{2}=BH$ , and by the theorem of betweenness applied to H, E, and B, we get $HE=HB-EB=\frac{5\sqrt{2}}{2}-\frac{5\sqrt{6}-5\sqrt{2}}{2}=\frac{10\sqrt{2}-5\sqrt{6}}{2}$ .
We are almost done. By symmetry, $HD=HE$ , so to find the area of the triangle CED, we only need to multiply HE by CH, $\frac{10\sqrt{2}-5\sqrt{6}}{2}\cdot\frac{5\sqrt{2}}{2}=\frac{100-50\sqrt{3}}{4}=\frac{50-25\sqrt{3}}{2}$ . This is answer choice $\boxed{\textbf{(D) } \frac{50-25\sqrt{3}}{2}}$ ~JH. L

## Solution 6 (Law of Sines)
We know that the area of the right triangle is $\frac{25}{2}$ and that the two legs are equal, so we can easily tell that the length of the two legs is $5$ . Thus, the hypotenuse $AB = 5\sqrt{2}$ and $\angle{CAB} = \angle{ABC} = 45^{\circ}.$ Let's quickly define $F$ as the point that bisects $\angle{ACB}$ and $\overline{AB}$ . Then, we can say that the area of the desired triangle is $DF \cdot AF$ . Let $\overline{AD} = \overline{BE} = n.$ Since $D$ is one of the trisecting points of $\angle{ACB}, \angle{ACD} = 30^{\circ}.$ Because \[\angle{ADC} = 180^{\circ}-\angle{ACD}-\angle{CAB},\] \[\angle{ADC} = 180^{\circ} - 45^{\circ} - 30^{\circ} = 105^{\circ}.\] Now, we can employ the Law of Sines. It tells us that $\frac{\sin(\angle{ADC})}{5} = \frac{\sin(\angle{ACD})}{n}$ . Plugging in our angle values, we get that \[\frac{\sin(105^{\circ})}{5} = \frac{\sin(30^{\circ})}{n}.\] It's easy to find that $\sin(105^{\circ}) = \sin(75^{\circ}) = \frac{\sqrt{2}+\sqrt{6}}{4},$ and that $\sin(30^{\circ}) = \frac{1}{2}$ . Plugging in these values into our previous equation, we get \[\frac{\sqrt{2}+\sqrt{6}}{20} = \frac{1}{2n}.\] Cross multiplying gets us \[2n\sqrt{2}+2n\sqrt{6} = 20,\] and then we simplify like so: \[2n(\sqrt{2}+\sqrt{6}) = 20\rightarrow\] \[n(\sqrt{2}+\sqrt{6}) = 10\rightarrow\] \[n = \frac{10}{\sqrt{2}+\sqrt{6}}.\] Now, using our definition of $n$ , we know that $DF$ = $\frac{AB}{2} - n = \frac{5\sqrt{2}}{2} - \frac{10}{\sqrt{2}+\sqrt{6}}$ . We want to put this under one common denominator, which is pretty simple to execute. That leaves us with \[\frac{5\sqrt{2} \cdot \sqrt{2}+5\sqrt{2} \cdot \sqrt{6} - 20}{2\sqrt{2} + 2\sqrt{6}}=\] \[\frac{10+10\sqrt{3} - 20}{2\sqrt{2} + 2\sqrt{6}}=\] \[\frac{10\sqrt{3} - 10}{2(\sqrt{2} + \sqrt{6})}=\] \[\frac{2(5\sqrt{3} - 5)}{2(\sqrt{2} + \sqrt{6})}=\] \[\frac{5\sqrt{3} - 5}{\sqrt{2} + \sqrt{6}}.\] Whew. That was longer than expected. Anyways, quick inspection tells us that $AF = \frac{5\sqrt{2}}{2},$ so now we just have to do some simplifying to find the desired, $[CDE]$ . Let's do that now. \[[CDE] = \frac{5\sqrt{3} - 5}{\sqrt{2} + \sqrt{6}} \cdot \frac{5\sqrt{2}}{2}=\] \[[CDE] = \frac{25\sqrt{6} - 25\sqrt{2}}{2(\sqrt{2} + \sqrt{6})}=\] \[[CDE] = \frac{25(\sqrt{2} - \sqrt{6})}{2(\sqrt{2} + \sqrt{6})}=\] (We need to take a quick conjugation break. Note that $(\sqrt{2} - \sqrt{6})^2 = 8 - 4\sqrt{3}.$ ) \[[CDE] = \frac{25(\sqrt{2} - \sqrt{6})}{2(\sqrt{2} + \sqrt{6})} \cdot \frac{(\sqrt{2} - \sqrt{6})}{(\sqrt{2} - \sqrt{6})}=\] \[[CDE] = \frac{200 - 100\sqrt{3}}{2(4)}=\] \[[CDE] =\boxed{\frac{50 - 25\sqrt{3}}{2} \text{(D)}.}\] ~Nickelslordm

## Solution 7(Ratio of 15,75,90 triangle)
Drawing the two rays, we get triangles CAD, CDE, and CBE. Notice that triangles CAD and CBE are identical, and triangle CDE is an isosceles triangle with angles CDE=CED=75 and angle DEC=15.
We draw the height of triangle ABC, which is also the height of triangle CDE. Because triangle CDE is an isosceles triangle, we know the height spilt base DE into 2 equal parts, and triangle CDE into 2 identical 15,75,90 triangle. From the ratio of 15,75,90 triangles,we know that the ratio of the height and half of line DE is equal to the ratio of areas.

## Video Solution:
https://www.youtube.com/watch?v=JWMIsCS0Ksk
https://www.youtube.com/watch?v=_LPz_i4Cwv4
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
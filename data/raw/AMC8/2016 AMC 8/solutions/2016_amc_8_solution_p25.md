# 2016 AMC 8 Problem 25

## Problem

A semicircle is inscribed in an isosceles triangle with base $16$ and height $15$ so that the diameter of the semicircle is contained in the base of the triangle as shown. What is the radius of the semicircle?

[asy]draw((0,0)--(8,15)--(16,0)--(0,0)); draw(arc((8,0),7.0588,0,180));[/asy]

$\textbf{(A) }4 \sqrt{3}\qquad\textbf{(B) } \dfrac{120}{17}\qquad\textbf{(C) }10\qquad\textbf{(D) }\dfrac{17\sqrt{2}}{2}\qquad \textbf{(E)} \dfrac{17\sqrt{3}}{2}$

### Note

There are many solutions here, and all of them are equally good. For your own benefit, look at all of the solutions, as they employ many unique techniques to get to the final answer.

## Solution 1
[asy] pair A, B, C, D; A=(0,0); B=(16,0); C=(8,15); D=B/2; draw(A--B--C--cycle); draw(C--D); draw(arc(D,120/17,0,180)); draw(rightanglemark(B,D,C,25)); label("$A$",A,SW); label("$B$",B,SE); label("$C$",C,N); label("$D$",D,S); label("$8$",(A+D)/2,S); label("$15$",(C+D)/2,NE); label("$17$",(A+C)/2,W); [/asy]
First, we drop a perpendicular, shown above, to the base of the triangle, cutting the triangle into two congruent right triangles. This triangle is isosceles, which means perpendiculars are medians and vice versa. The base of the resulting right triangle is $8$ for both sides, and the height is $15,$ as given. Using the Pythagorean theorem, we can find the length of the hypotenuse, or $17.$ Using the two legs of the right triangle, we find the area of the right triangle, $60$ . $\frac{60}{17}$ times $2$ results in the radius, which is the height of the right triangle when using the hypotenuse as the base. Hence, the answer is $\boxed{\textbf{(B) }\frac{120}{17}}$ .

## Solution 2: Similar Triangles
[asy] pair A, B, C, D, E; A=(0,0); B=(16,0); C=(8,15); D=B/2; E=(64/17*8/17, 64/17*15/17); draw(A--B--C--cycle); draw(C--D); draw(D--E); draw(arc(D,120/17,0,180)); draw(rightanglemark(B,D,C,25)); draw(rightanglemark(A,E,D,25)); label("$A$",A,SW); label("$B$",B,SE); label("$C$",C,N); label("$D$",D,S); label("$E$",E,NW);[/asy] Let's call the triangle $\triangle ABC,$ where $AB=16$ and $AC=BC.$ Let's say that $D$ is the midpoint of $AB$ and $E$ is the point where $AC$ is tangent to the semicircle. We could also use $BC$ instead of $AC$ because of symmetry.
Notice that $\triangle ACD \cong \triangle BCD,$ and are both 8-15-17 right triangles. We also know that we create a right angle with the intersection of the radius and a tangent line of a circle (or part of a circle). So, by $AA$ similarity, $\triangle AED \sim \triangle ADC,$ with $\angle EAD \cong \angle DAC$ and $\angle CDA \cong \angle DEA.$ This similarity means that we can create a proportion: $\frac{AD}{AC}=\frac{DE}{CD}.$ We plug in $AD=\frac{AB}{2}=8, AC=17,$ and $CD=15.$ After we multiply both sides by $15,$ we get $DE=\frac{8}{17} \cdot 15= \boxed{\textbf{(B) }\frac{120}{17}}.$
(By the way, we could also use $\triangle DEC \sim \triangle ADC.$ )

## Solution 3: Inscribed Circle
[asy] pair A, B, C, D, M; B=(0,0); D=(16,0); A=(8,15); C=(8,-15); M=D/2; draw(B--D--A--cycle); draw(A--M); draw(arc(M,120/17,0,180)); draw(rightanglemark(D,M,A,25)); draw(rightanglemark(B,M,25)); label("$B$",B,SW); label("$D$",D,SE); label("$A$",A,N); label("$M$",M,S); label("$C$",C,S); draw((0,0)--(8,-15)--(16,0)--(0,0)); draw(arc((8,0),7.0588,0,360));[/asy]
We'll call this triangle $\triangle ABD$ . Let the midpoint of base $BD$ be $M$ . Divide the triangle in half by drawing a line from $A$ to $M$ . Half the base of $\triangle ABD$ is $\frac{16}{2} = 8$ . The height is $15$ , which is given in the question. Using the Pythagorean Triple $8$ - $15$ - $17$ , the length of each of the legs ( $AB$ and $DA$ ) is 17.
Reflect the triangle over its base. This will create an inscribed circle in a rhombus $ABCD$ . Because $AB \cong DA$ , $BC \cong CD$ . Therefore $AB = BC = CD = DA$ .
The semiperimeter $s$ of the rhombus is $\frac{AB + BC + CD + DA}{2} = \frac{(17)(4)}{2} = 34$ . Since the area of $\triangle ABD$ is $\frac{bh}{2}$ , the area $[ABCD]$ of the rhombus is twice that, which is $bh = (16)(15) = 240$ .
The Formula for the Incircle of a Quadrilateral is $s$ $r$ = $[ABCD]$ . Substituting the semiperimeter and area into the equation, $34r = 240$ . Solving this, $r = \frac{240}{34}$ = $\boxed{\textbf{(B) }\frac{120}{17}}$ .

## Solution 4: Inscribed Circle
Noting that we have a 8-15-17 triangle, we can find $AE$ and $CE.$ Let $AE=x$ , $CE=17-x.$ Then by similar triangles (or "Altitude on Hypotenuse") we have $15^2=x*17.$ Thus, $AE=x=225/17, CE=64/17.$ Now again by "Altitude on Hypotenuse”, $r=\sqrt{AE*CE}.$ Therefore $r=\boxed{\textbf{(B) }\frac{120}{17}}$ .

## Solution 5: Simple Trigonometry
Note: This solution uses Trigonometric Concepts [asy] pair A, B, C, D; A=(0,0); B=(16,0); C=(8,15); D=B/2; draw(A--B--C--cycle); draw(C--D); draw(arc(D,120/17,0,180)); draw(rightanglemark(B,D,C,25)); label("$A$",A,SW); label("$B$",B,SE); label("$C$",C,N); label("$D$",D,S); [/asy]
Denote the bottom left vertex of the isosceles triangle to be $8$
Denote the bottom right vertex of the isosceles triangle to be $8$
Denote the top vertex of the isosceles triangle to be $x$
Drop an altitude from $x$ to side $AB$ . Denote the foot of the intersection to be $D$ .
By the Pythagorean Theorem, $AC=17$ .
Now, we see that by sin(x), $\sin{A}=\frac{15}{17}$ .
This implies that $\sin{A}=\frac{r}{8}$ (r=radius of semicircle).
Hence, $r=\boxed{\textbf{(B) }\frac{120}{17}}$ .

## Solution 6: Area
[asy] pair A, B, C, D, E; A=(0,0); B=(16,0); C=(8,15); D=B/2; E=(64/17*8/17, 64/17*15/17); draw(A--B--C--cycle); draw(C--D); draw(D--E); draw(arc(D,120/17,0,180)); draw(rightanglemark(B,D,C,25)); draw(rightanglemark(A,E,D,25)); label("$A$",A,SW); label("$B$",B,SE); label("$C$",C,N); label("$D$",D,S); label("$E$",E,NW);[/asy] Credits for Asymptote go to whoever wrote this diagram up in Solution 2.
There are two ways to find the area of $\triangle ABC$ . The first way is the most obvious, and that is to multiply the base times the height ( $16\cdot15$ ) and then divide it by two. The second way is, in a way, a little more complex. Note that $\triangle ACD$ and $\triangle BCD$ are congruent. This means that if we find the area of one triangle, we can just multiply it's area by 2 and we've found the area of the larger triangle $ABC$ . But since we always divide by two, as it is in the formula for finding the area of a triangle, the multiply by two and divide by two cancel out, giving us that if we just multiply base times height of $\triangle ACD$ , we will get the area of $\triangle ABC$ .
Now you might think: "But what is the other way of finding the area". Well that is $AC$ , which would be the base, times $DE$ , the radius, which would be the height.
The first way to find the area gives us the area of the $\triangle ABC$ , $\frac{15\cdot16}{2}=120$ . This gives us $120=AC\cdot r$ ( $r$ signifies radius). We can find $AC$ using the Pythagorean Theorem on $\triangle ACD$ . The two legs are $8$ and $15$ , which gives us that the hypotenuse, $AC$ , is equal to $17$ .
Now that we have an equation with only one variable for the radius, $120=17r$ , we can just solve for the radius. We get $r=\boxed{\textbf{(B) }\frac{120}{17}}$ .
This may seem like a lengthy explanation, but doing it yourself when you know what to do, it actually takes very little time. Try it yourself!

## Solution 7
Let us draw altitude $\overline{CD}.$ This cuts our base into line segments with length $\dfrac{16}{2}=8.$ Finding the area of the resulting triangles gives $[\triangle ADC] = [\triangle BDC] = \dfrac{8 \cdot 15}{2} = 60.$ Since $m\angle CDB = m\angle CDA = 90^\circ,$ we use the Pythagorean Theorem to find length $\overline{AC}$ : \begin{align*} (\overline{AD})^2+(\overline{CD})^2 &= (\overline{AC})^2 \\ 8^2+15^2 &= (\overline{AC})^2 \\ 64+225 &= (\overline{AC})^2 \\ 289 &= (\overline{AC})^2 \\ \sqrt{289} &= \sqrt{(\overline{AC})^2} \\ 17 &= AC. \end{align*} Thus we have $\overline{AC}=\overline{BC}=17.$
[asy] pair A, B, C, D; A=(0,0); B=(16,0); C=(8,15); D=B/2; draw(A--B--C--cycle); draw(C--D); draw(arc(D,120/17,0,180)); draw(rightanglemark(B,D,C,25)); label("$A$",A,SW); label("$B$",B,SE); label("$C$",C,N); label("$D$",D,S); label("$8$",(A+D)/2,S); label("$8$",(B+D)/2,S); label("$15$",(C+D)/2,NE); label("$17$",(A+C)/2,W); label("$17$",(B+C)/2,E); [/asy]
Letting $17$ be the base of the triangle makes our height the radius of the semicircle: [asy] pair A, B, C, D, EE; A=(0,0); B=(16,0); C=(8,15); D=B/2; EE=(64/17*8/17, 64/17*15/17); draw(A--B--C--cycle); draw(C--D); draw(D--EE); draw(arc(D,120/17,0,180)); draw(rightanglemark(B,D,C,25)); draw(rightanglemark(A,EE,D,25)); label("$A$",A,SW); label("$B$",B,SE); label("$C$",C,N); label("$D$",D,S); label("$8$",(A+D)/2,S); label("$8$",(B+D)/2,S); label("$15$",(C+D)/2,NE); label("$17$",(A+C)/2,W); label("$17$",(B+C)/2,E); label("$r$",D--EE, N); [/asy]
Let $r$ be the radius of the semicircle. Then we have $\dfrac{17 \cdot r}{2}=60 \implies 17 \cdot r = 120 \implies \dfrac{17r}{17} = \dfrac{120}{17} \implies r = \boxed{\textbf{(B) }\dfrac{120}{17}}.$
$\textbf{Remember: Area can help in places where you least expect it!}$
\[\definecolor{salmon}{rgb}{.918, .6, .6}\colorbox{salmon}{\color{white}{solution by \textbf{pog}}}\]

## Solution 8: equations
Draw tangent lines to connect the centre of the circle to the equal sides. Since the angle is 90 degrees and the height is perpendicular to the side not equal with any of the other side lengths, the two triangles(Not the big one but the two smaller ones) are similar. We've got one common side that gives us the ratio is $\frac{8}{15}$ . We've got a system of equations!
1. 8/15=x(the radius)/y(the side that is similar) 2. $x^2 + y^2 = 225$ (by the pythagorean theorem).
Solving the equations we get $\boxed{\frac{120}{17}}$
\[\definecolor{salmon}{rgb}{.789, .6, .6}\colorbox{salmon}{\color{black}{created by \textbf{justin6688}}}\]

## Solution 9: Process of Elimination
Not a true solution, but in the interest of creativity and alternative methods, here is a way to cheese the solution in seconds.
[asy] pair A, B, C, D, E; A=(0,0); B=(16,0); C=(8,15); D=B/2; E=(64/17*8/17, 64/17*15/17); draw(A--B--C--cycle); draw(C--D); draw(D--E); draw(arc(D,120/17,0,180)); draw(rightanglemark(B,D,C,25)); draw(rightanglemark(A,E,D,25)); label("$A$",A,SW); label("$B$",B,SE); label("$C$",C,N); label("$D$",D,S); label("$E$",E,NW);[/asy]
First, notice that $AC=17$ (Pythagorean triple $8$ - $15$ - $17$ ). Since all the side lengths of $\triangle ADC$ are integers, and $\triangle AED \sim \triangle ADC \sim \triangle DEC$ , all of the side length ratios are rational, and therefore, $DE$ must be a rational value. We eliminate answer choices A, D, and E.
Finally, notice that answer choice C is impossible because that would mean that in $\triangle AED$ , the leg $DE = 10$ would be bigger than the hypotenuse $AD = 8$ . The only answer choice remaining is $\boxed{\textbf{(B) }\dfrac{120}{17}}$ .

## Video Solution

## Video Solution 1
https://youtu.be/fMXtuMXfAcE - Happytwin

## Video Solution 2
https://www.youtube.com/watch?v=jfGc3hHPu2w&feature=youtu.be
~IceMatrix2
### See Also
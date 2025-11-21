# 2009 AMC 10A Problem 10

## Problem

Triangle $ABC$ has a right angle at $B$ . Point $D$ is the foot of the altitude from $B$ , $AD=3$ , and $DC=4$ . What is the area of $\triangle ABC$ ?

[asy] unitsize(5mm); defaultpen(linewidth(.8pt)+fontsize(8pt)); dotfactor=4; pair B=(0,0), C=(sqrt(28),0), A=(0,sqrt(21)); pair D=foot(B,A,C); pair[] ps={B,C,A,D}; draw(A--B--C--cycle); draw(B--D); draw(rightanglemark(B,D,C)); dot(ps); label("$A$",A,NW); label("$B$",B,SW); label("$C$",C,SE); label("$D$",D,NE); label("$3$",midpoint(A--D),NE); label("$4$",midpoint(D--C),NE); [/asy]

$\mathrm{(A)}\ 4\sqrt3 \qquad \mathrm{(B)}\ 7\sqrt3 \qquad \mathrm{(C)}\ 21 \qquad \mathrm{(D)}\ 14\sqrt3 \qquad \mathrm{(E)}\ 42$

## Solution 1
It is a well-known fact that in any right triangle $ABC$ with the right angle at $B$ and $D$ the foot of the altitude from $B$ onto $AC$ we have $BD^2 = AD\cdot CD$ . (See below for a proof.) Then $BD = \sqrt{ 3\cdot 4 } = 2\sqrt 3$ , and the area of the triangle $ABC$ is $\frac{AC\cdot BD}2 = 7\sqrt3\Rightarrow\boxed{\text{(B)}}$ .
Proof : Consider the Pythagorean theorem for each of the triangles $ABC$ , $ABD$ , and $CBD$ . We get:
1. $AB^2 + BC^2 = AC^2 = (AD+DC)^2 = AD^2 + DC^2 + 2 \cdot AD \cdot DC$ .
1. $AB^2 = AD^2 + BD^2$
1. $BC^2 = BD^2 + CD^2$
Substituting equations 2 and 3 into the left hand side of equation 1, we get $BD^2 = AD \cdot DC$ .
Alternatively, note that $\triangle ABD \sim \triangle BCD \Longrightarrow \frac{AD}{BD} = \frac{BD}{CD}$ .

## Solution 2
For those looking for a dumber solution, we can use Pythagoras and manipulation of area formulas to solve the problem.
Assume the length of $BD$ is equal to $h$ . Then, by Pythagoras, we have,
\[AB^2 = h^2 + 9 \Rightarrow AB = \sqrt{h^2 + 9}\] \[BC^2 = h^2 + 16 \Rightarrow BC = \sqrt{h^2 + 16}\]
Then, by area formulas, we know:
\[\frac{1}{2}\sqrt{(h^2+9)(h^2+16)} = \frac{1}{2}(7)(h)\]
Squaring and solving the above equation yields our solution that $h^2 = 12 \Rightarrow h = 2\sqrt{3}.$ Since the area of the triangle is half of this quantity multiplied by the base, we have \[\text{area} = \frac{1}{2}(7)(2\sqrt{3})\Rightarrow \boxed{7\sqrt{3}}\]

## Solution 3 (Power of a point)
Draw the circumcircle $\omega$ of the $\Delta ABC$ . Because $\Delta ABC$ is a right angle triangle, AC is the diameter of the circumcircle. And we know that AC is the diameter because of Perpendicular Chord Bisector Theorem. By applying Power of a Point Theorem , we can have $BD=DE$ and $AD\cdot CD=BD^2$ $\Rightarrow BD=\sqrt{3\times 4}=2\sqrt{3}$ . Then we have $S_{[ABC]}=\frac{1}{2}(7)(2\sqrt{3})=\boxed{7\sqrt{3}}$
[asy] unitsize(6mm); defaultpen(linewidth(.8pt)+fontsize(8pt)); dotfactor=4; pair B=(0,0), C=(sqrt(28),0), A=(0,sqrt(21)), E=(6*sqrt(28)/7,8*sqrt(21)/7); pair D=foot(B,A,C); pair[] ps={B,C,A,D}; filldraw(Circle((sqrt(28)/2,sqrt(21)/2),sqrt(49)/2),white,black); draw(A--B--C--cycle); draw(B--D); draw(E--D); draw(rightanglemark(B,D,C)); dot(ps); label("$A$",A,NW); label("$B$",B,SW); label("$E$",E,NE); label("$C$",C,SE); label("$D$",D,NE); label("$3$",midpoint(A--D),NE); label("$4$",midpoint(D--C),NE); [/asy] ~Bran_Qin
~twosetisdabest (Just proving that AC is diameter of the circle)

## Solution 4 (Fakesolve)/Answer Choices
Suppose that $BD=x$ . Then, the area of the triangle is $\frac{7x}{2}$ . We want to find what $x$ is. Now, we try each answer choice.
$A): 4 \sqrt{3}$ . I am too lazy to go over this, but we immediately see that this is very improbably due to the area being $\frac{7x}{2}$ . This does not work. $B): 7 \sqrt{3}$ . This is promising. This means that $x = 2\sqrt{3}$ . Now, applying Pythagorean Theorem, we have the vertical sides is $\sqrt {21}$ and the horizontal side is $\sqrt {28}$ . Multiplying these and dividing by $2$ indeed gives us $7 \sqrt {3}$ as desired. Therefore, the answer is $\boxed{7 \sqrt{3}}$
~Arcticturn

## Solution 5
Let $\overline{BD} = x$ , and $\angle ABD = \theta$ . Since $m\angle ABC = 90, DBC = 90 - \theta$ . $\tan{\theta} = \frac{3}{x}$ , and $\tan{90-\theta} = \frac{4}{x}$ . Using trig identities, we can simplify the second one to $\cot{\theta} = \frac{4}{x}$ . Let $y = \tan{\theta}$ . We get $xy = 3$ , and using the fact that $\cot{a} = \frac{1}{\tan{a}}$ , $\frac{x}{y} = 4$ . Solving for x and y(using substitution), we get $y^2 = \frac{3}{4}$ . We could substitute back in and solve, but there is an easier way. Squaring $xy = 3$ , we get $x^2y^2 = 9$ . Since we know $y^2 = \frac{3}{4}$ , $x = \sqrt{12}$ . Using the Pythagorean Theorem in the original triangle, we get the legs of the triangle to be $\sqrt{9+x^2}$ and $\sqrt{16+x^2}$ . Putting in $x$ , we get the equation for the area, which is $\frac{\sqrt{28} \cdot \sqrt{21}}{2} = \frac{14\sqrt{3}}{2} = \boxed{\textbf{(B) } 7\sqrt{3}}$
~idk12345678

## Video Solution by OmegaLearn
https://youtu.be/4_x1sgcQCp4?t=1195
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
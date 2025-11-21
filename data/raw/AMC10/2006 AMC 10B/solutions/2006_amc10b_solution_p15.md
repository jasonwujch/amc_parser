# 2006 AMC 10B Problem 15

## Problem

Rhombus $ABCD$ is similar to rhombus $BFDE$ . The area of rhombus $ABCD$ is $24$ and $\angle BAD = 60^\circ$ . What is the area of rhombus $BFDE$ ?

[asy] defaultpen(linewidth(0.7)+fontsize(10)); size(120); pair A=origin, B=(2,0), C=(3, sqrt(3)), D=(1, sqrt(3)), E=(1, 1/sqrt(3)), F=(2, 2/sqrt(3)); pair point=(3/2, sqrt(3)/2); draw(B--C--D--A--B--F--D--E--B); label("$A$", A, dir(point--A)); label("$B$", B, dir(point--B)); label("$C$", C, dir(point--C)); label("$D$", D, dir(point--D)); label("$E$", E, dir(point--E)); label("$F$", F, dir(point--F)); [/asy]

$\textbf{(A) } 6\qquad \textbf{(B) } 4\sqrt{3}\qquad \textbf{(C) } 8\qquad \textbf{(D) } 9\qquad \textbf{(E) } 6\sqrt{3}$

## Solution 1
Using the property that opposite angles are equal in a rhombus , $\angle DAB = \angle DCB = 60 ^\circ$ and $\angle ADC = \angle ABC = 120 ^\circ$ . It is easy to see that rhombus $ABCD$ is made up of equilateral triangles $DAB$ and $DCB$ . Let the lengths of the sides of rhombus $ABCD$ be $s$ .
The longer diagonal of rhombus $BFDE$ is $BD$ . Since $BD$ is a side of an equilateral triangle with a side length of $s$ , $BD = s$ . The longer diagonal of rhombus $ABCD$ is $AC$ . Since $AC$ is twice the length of an altitude of of an equilateral triangle with a side length of $s$ , $AC = 2 \cdot \frac{s\sqrt{3}}{2} = s\sqrt{3}$ .
The ratio of the longer diagonal of rhombus $BFDE$ to rhombus $ABCD$ is $\frac{s}{s\sqrt{3}} = \frac{\sqrt{3}}{3}$ . Therefore, the ratio of the area of rhombus $BFDE$ to rhombus $ABCD$ is $\left( \frac{\sqrt{3}}{3} \right) ^2 = \frac{1}{3}$ .
Let $x$ be the area of rhombus $BFDE$ . Then $\frac{x}{24} = \frac{1}{3}$ , so $x = \boxed{\textbf{(C) }8}$ .

## Solution 2
Triangle DAB is equilateral so triangles $DEA$ , $AEB$ , $BED$ , $BFD$ , $BFC$ and $CFD$ are all congruent with angles $30^\circ$ , $30^\circ$ and $120^\circ$ from which it follows that rhombus $BFDE$ has one third the area of rhombus $ABCD$ i.e. $8 \Longrightarrow \boxed{\textbf{(C) }8}$ . Note: A quick way to visualize this method is to draw the line $DB$ and notice the two equilateral triangles $\triangle ADB$ and $\triangle DBC$ .

## Solution 3 (A bit more math involved)
We can extend line $DE$ , meeting line $AB$ at $G$ . Similarly, we can extend line $DF$ to meet line $BC$ at $H$ . We can see with some simple math that triangle $ADG$ is a $30$ - $60$ - $90$ triangle, so we can call line $AG$ as $x$ , line $DG$ as $x\sqrt{3}$ , and line $AD$ as $2x$ (because of the $30$ - $60$ - $90$ triangle side proportions).
We can also see that line $AD$ is a base of rhombus $ABCD$ , and line $DH$ is a height. Since triangle $DHC$ is also a $30$ - $60$ - $90$ triangle, line $DH$ is also $x\sqrt{3}$ . Since the question told us that the area of rhombus $ABCD$ is $24$ , we can make the following equation:
$2x \cdot x\sqrt{3} = 24$
Solving for x:
$2x^2\sqrt{3} = 24$
$x^2\sqrt{3} = 12$
$x^2 = \frac{12}{\sqrt{3}}$
$x^2 = 4\sqrt{3}$
$x = 2\sqrt{\sqrt{3}}$
Since the question is to find the area of rhombus $BFDE$ , to find the answer, we can just multiply base $DE$ with the rhombus's height. We'll start by finding the height: instantly we can see that $GB$ is the height. Since all the sides of a rhombus are equal, and we found earlier that the side length is $2x$ , if $AG$ is $x$ , that means $GB$ is the same length as $AG$ - that is to say,
$GB = AG = 2\sqrt{\sqrt{3}}$
Now to find the base. We can see that to find the base, we can simply just subtract the length of line $EG$ from the length of line $DG$ . Since $DG$ is $x\sqrt{3}$ , and $x$ is $2\sqrt{\sqrt{3}}$ , that makes
$DG = 2\sqrt{\sqrt{3}} \cdot \sqrt{3} = 2\sqrt{3\sqrt{3}}$
Now to find $EG$ : We can see with simple math that triangle $EGB$ is also a $30$ - $60$ - $90$ triangle, which means that $EG = \frac{GB}{\sqrt{3}}$ . Previously, we found out that $GB$ is $2\sqrt{\sqrt{3}}$ , so:
$EG = \frac{2\sqrt{\sqrt{3}}}{\sqrt{3}} = \frac{2\sqrt{3\sqrt{3}}}{3}$
Now we can find the base:
$DG - EG = 2\sqrt{3\sqrt{3}} - \frac{2\sqrt{3\sqrt{3}}}{3} = \frac{4\sqrt{3\sqrt{3}}}{3}$
Multiplying the newly found base by the height we found earlier:
$\frac{4\sqrt{3\sqrt{3}}}{3} \cdot 2\sqrt{\sqrt{3}} = \frac{8\sqrt{9}}{3} = \frac{24}{3} = \boxed{\textbf{(C) }8}$
~ilee0820
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
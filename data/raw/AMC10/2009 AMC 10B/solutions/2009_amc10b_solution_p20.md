# 2009 AMC 10B Problem 20

## Problem

Triangle $ABC$ has a right angle at $B$ , $AB=1$ , and $BC=2$ . The bisector of $\angle BAC$ meets $\overline{BC}$ at $D$ . What is $BD$ ?

[asy] unitsize(2cm); defaultpen(linewidth(.8pt)+fontsize(8pt)); dotfactor=4; pair A=(0,1), B=(0,0), C=(2,0); pair D=extension(A,bisectorpoint(B,A,C),B,C); pair[] ds={A,B,C,D}; dot(ds); draw(A--B--C--A--D); label("$1$",midpoint(A--B),W); label("$B$",B,SW); label("$D$",D,S); label("$C$",C,SE); label("$A$",A,NW); draw(rightanglemark(C,B,A,2)); [/asy]

$\text{(A) } \frac {\sqrt3 - 1}{2} \qquad \text{(B) } \frac {\sqrt5 - 1}{2} \qquad \text{(C) } \frac {\sqrt5 + 1}{2} \qquad \text{(D) } \frac {\sqrt6 + \sqrt2}{2} \qquad \text{(E) } 2\sqrt 3 - 1$

## Solution 1
By the Pythagorean Theorem, $AC=\sqrt5$ . Then, from the Angle Bisector Theorem, we have:
\[\frac{BD}{1}=\frac{2-BD}{\sqrt5}\] \[BD\left(1+\frac{1}{\sqrt5}\right)=\frac{2}{\sqrt5}\] \[BD(\sqrt5+1)=2\] \[BD=\frac{2}{\sqrt5+1}=\boxed{\frac{\sqrt5-1}{2}} \implies {B}\]

## Solution 2
Let $\theta = \angle BAD = \angle DAC$ . Notice $\tan \theta = BD$ and $\tan 2 \theta = 2$ . By the double angle identity, \[2 = \frac{2 BD}{1 - BD^2} \implies BD = \boxed{\frac{\sqrt5 - 1}{2} \implies B}.\]
Remarks: You could also use tangent half angle formula

## Solution 3
Let $BD=y$ .
Make $DE$ a line so that it is perpendicular to $AC$ . Since $AD$ is an angle bisector, $\triangle AED$ is congruent to $\triangle ABD$ . Using the Pythagorean Theorem:
$AC^2=1^2+2^2$
$AC^2=5$
$AC=\sqrt{5}$
We know that $AE=1$ by the congruent triangles, so $EC=\sqrt{5}-1$ . We know that $DE=y$ , $EC=\sqrt{5}-1$ , and $DC=2-y$ . We now have right triangle $DEC$ and its 3 sides. Using the Pythagorean Thereom, we get:
$y^2+(\sqrt{5}-1)^2=(2-y)^2$
$-4y=2-2\sqrt{5}$
So, $y=BD=\boxed{\frac{\sqrt5-1}{2} \implies B}.$
~HelloWorld21

## Video Solution by OmegaLearn
https://youtu.be/4_x1sgcQCp4?t=4816
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
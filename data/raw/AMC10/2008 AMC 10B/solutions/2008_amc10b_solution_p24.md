# 2008 AMC 10B Problem 24

## Problem

Quadrilateral $ABCD$ has $AB = BC = CD$ , $m\angle ABC = 70^\circ$ and $m\angle BCD = 170^\circ$ . What is the degree measure of $\angle BAD$ ?

$\mathrm{(A)}\ 75\qquad\mathrm{(B)}\ 80\qquad\mathrm{(C)}\ 85\qquad\mathrm{(D)}\ 90\qquad\mathrm{(E)}\ 95$

## Solution 1 (Cyclic Quadrilateral)
- Note: This solution requires the use of cyclic quadrilateral properties but could be a bit time-consuming during the contest.
To start off, draw a diagram like in solution two and label the points. Create lines $\overline{AC}$ and $\overline{BD}$ . We can call their intersection point $Y$ . Note that triangle $BCD$ is an isosceles triangle so angles $CDB$ and $CBD$ are each $5$ degrees. Since $AB$ equals $BC$ , angle $BAC$ equals $55$ degrees, thus making angle $AYB$ equal to $60$ degrees. We can also find out that angle $CYB$ equals $120$ degrees.
Extend $\overline{CD}$ and $\overline{AB}$ and let their intersection be $E$ . Since angle $BEC$ plus angle $CYB$ equals $180$ degrees, quadrilateral $YCEB$ is a cyclic quadrilateral.
Next, draw a line from point $Y$ to point $E$ . Since angle $YBC$ and angle $YEC$ point to the same arc, angle $YEC$ is equal to $5$ degrees. Since $EYD$ is an isosceles triangle (based on angle properties) and $YAE$ is also an isosceles triangle, we can find that $YAD$ is also an isosceles triangle. Thus, each of the other angles is $\frac{180-120}{2}=30$ degrees. Finally, we have angle $BAD$ equals $30+55=\boxed{85}$ degrees.
~Minor edits by BakedPotato66

## Solution 2
First, connect the diagonal $DB$ , then, draw line $DE$ such that it is congruent to $DC$ and is parallel to $AB$ . Because triangle $DCB$ is isosceles and angle $DCB$ is $170^\circ$ , the angles $CDB$ and $CBD$ are both $\frac{180-170}{2} = 5^\circ$ . Because angle $ABC$ is $70^\circ$ , we get angle $ABD$ is $65^\circ$ . Next, noticing parallel lines $AB$ and $DE$ and transversal $DB$ , we see that angle $BDE$ is also $65^\circ$ , and subtracting off angle $CDB$ gives that angle $EDC$ is $60^\circ$ .
Now, because we drew $ED = DC$ , triangle $DEC$ is equilateral. We can also conclude that $EC=DC=CB$ meaning that triangle $ECB$ is isosceles, and angles $CBE$ and $CEB$ are equal.
Finally, we can set up our equation. Denote angle $BAD$ as $x^\circ$ . Then, because $ABED$ is a parallelogram, the angle $DEB$ is also $x^\circ$ . Then, $CEB$ is $(x-60)^\circ$ . Again because $ABED$ is a parallelogram, angle $ABE$ is $(180-x)^\circ$ . Subtracting angle $ABC$ gives that angle $CBE$ equals $(110-x)^\circ$ . Because angle $CBE$ equals angle $CEB$ , we get \[x-60=110-x\] , solving into $x=\boxed{85^\circ}$ .
[asy] unitsize(1cm); defaultpen(.8); real a=4; pair A=(0,0), B=a*dir(0), C=B+a*dir(110), D=C+a*dir(120), E=D+a*dir(0); draw(A--B--C--D--cycle); draw(E--C); draw(B--D); draw(B--E); draw(D--E); label("$A$",A,SW); label("$B$",B,SE); label("$C$",C,SE); label("$D$",D,N); label("$E$",E,NE); label("$60^\circ$",C + .75*dir(360-65-115-55-30)); label("$65^\circ$",B + .75*dir(180-32.5)); label("$x^\circ$",A + .5*dir(42.5)); label("$5^\circ$",D + 2.5*dir(360-60-2.5)); label("$60^\circ$",D + .75*dir(360-30)); label("$60^\circ$",E + .5*dir(360-150)); label("$5^\circ$",B + 2.5*dir(180-65-2.5)); [/asy]
Side note: this solution was inspired by some basic angle chasing and finding some 60 degree angles, which made me want to create equilateral triangles.
~Someonenumber011

## Solution 3(Using Trig.)
[asy] unitsize(3 cm); pair A, B, C, D; A = (0,0); B = dir(85); C = B + dir(-25); D = C + dir(-35); draw(A--B--C--D--cycle); draw(A--C); draw(B--D); draw(((A + B)/2 + scale(0.02)*rotate(90)*(B - A))--((A + B)/2 + scale(0.02)*rotate(90)*(A - B))); draw(((B + C)/2 + scale(0.02)*rotate(90)*(C - B))--((B + C)/2 + scale(0.02)*rotate(90)*(B - C))); draw(((C + D)/2 + scale(0.02)*rotate(90)*(D - C))--((C + D)/2 + scale(0.02)*rotate(90)*(C - D))); dot("$A$", A, SW); dot("$B$", B, N); dot("$C$", C, NE); dot("$D$", D, SE); label("$I$", 6/7*C); [/asy]
Let the unknown $\angle BAD$ be $x$ .
First, we draw diagonal $BD$ and $AC$ . $I$ is the intersection of the two diagonals. The diagonals each form two isosceles triangles, $\triangle BCD$ and $\triangle ABC$ .
Using this, we find: $\angle DBC = \angle CDB = 5^\circ$ and $\angle BAC = \angle BCA = 55^\circ$ . Expanding on this, we can fill in a couple more angles. $\angle ABD = 70^\circ - 5^\circ = 65^\circ$ , $\angle ACD = 170^\circ - 55^\circ = 115^\circ$ , $\angle BIA = \angle CID = 180^\circ - (65^\circ + 55^\circ) = 60^\circ$ , $\angle BIC = \angle AID = 180^\circ - 60^\circ = 120^\circ$ .
We can rewrite $\angle CAD$ and $\angle BDA$ in terms of $x$ . $\angle CAD = x - 55^\circ$ and $\angle BDA = 180^\circ - (120^\circ + x - 55^\circ) = 115^\circ - x$ .
Let us relabel $AB = BC = CD = a$ and $AD = b$ .
By Rule of Sines on $\triangle ACD$ and $\triangle ABD$ respectively, $\frac{\sin(\angle CAD)}{a} = \frac{\sin(\angle ACD)}{b}$ , and $\frac{\sin(\angle ABD)}{b} = \frac{\sin(\angle BDA)}{a}$
In a more convenient form, $\frac{\sin(x-55^\circ)}{a} = \frac{\sin(115^\circ)}{b} \implies \frac{a}{b} = \frac{\sin(x-55^\circ)}{\sin(115^\circ)}$
and $\frac{\sin(65^\circ)}{b} = \frac{\sin(115^\circ-x)}{a} \implies \frac{a}{b} = \frac{\sin(115^\circ-x)}{\sin(65^\circ)}$
$\implies \frac{\sin(115^\circ-x)}{\sin(65^\circ)} = \frac{\sin(x-55^\circ)}{\sin(115^\circ)}$
Now, by identity $\sin(\theta) = \sin(180^\circ-\theta)$ , $\sin(65^\circ) = \sin(115^\circ)$
Therefore, $\sin(115^\circ-x) = \sin(x-55^\circ).$ This equation is only satisfied by option $\boxed{\text {(C) } 85^\circ}$
Note: I'm pretty bad at Asymptote, if anyone could edit this and fill in the angles into the diagram, that would be pretty cool.
~Raghu9372

## Solution 4 (Cheese)
Using a protractor ruler, draw an accurate diagram ( Example Diagram ). $\angle BAD$ looks slightly lessthan $90$ degrees. Therefore the answer is $\boxed{\textbf{(C) } 85}$ as $85$ is slightly less than $90$ .
~bobthegod78
~Reworded by South
added a single R to spell “ruler” correctly ~ethanhansummerfun

## Solution 5 (annoying amounts of algebra + trig identities)
place A at the origin of a coordinate system, with D on the x-axis let angle BAD be $\theta$ , and AB=BC=CD=1
The y value of from B-A is $\sin\theta$ . The y value from C-B is $\theta-(180^\circ-70^\circ)=\theta-110^\circ$ . The y value from D-C is $\theta-110^\circ-(180^\circ-170^\circ)=\theta-120^\circ$
The angles for the vectors from B to C and C to D are angle_original-(180-angle_polygon) are because the external angle of the polygon is 180-external angle, which is subtracted from the angle since it heads that amount off from the original direction.
since D-C+C-B+B-A=D-A=0 (since A, D are both on x-axis and have the same y value of 0), then: \[\sin\theta+\sin(\theta-110^\circ)+\sin(\theta-120^\circ)=0\]
from here we expand out the trig expressions using sin addition and isolate $\theta$
\[\sin\theta+\sin(\theta-110^\circ)+\sin(\theta-120^\circ)=0\] \[\sin\theta+\sin(\theta)\cos(110^\circ)-\cos(\theta)\sin(110^\circ) + \sin(\theta)\cos(120^\circ)-\cos(\theta)\sin(120^\circ)=0\]
\[1+\cos(110^\circ)-\cot(\theta)\sin(110^\circ)+\cos(120^\circ)-\cot(\theta)\sin(120^\circ)=0\] \[\cot(\theta)=\frac{1+\cos(110^\circ)+\cos(120^\circ)}{\sin(110^\circ)+\sin(120^\circ)}\]
At this point if you are a human calculator feel free to to solve, otherwise we want to try and evaluate the right hand side into some nice expression (ideally cot of an angle).
\[\cot(\theta)=\frac{1+\cos(120^\circ-10^\circ)+\cos(120^\circ)}{\sin(120^\circ-10^\circ)+\sin(120^\circ}\]
\[\cot(\theta)=\frac{1+\cos(120^\circ)\cos(10^\circ)+\sin(120^\circ)\sin(10^\circ)+\cos(120^\circ)} {\sin(120^\circ)\cos(10^\circ)-\cos(120^\circ)\sin(10^\circ)+\sin(120^\circ}\]
\[\cot(\theta)=\frac{1+\frac{-1}{2}\cos(10^\circ)+\frac{\sqrt{3}}{2}\sin(10^\circ)+\frac{-1}{2}} {\frac{\sqrt{3}}{2}\cos(10^\circ)-\frac{-1}{2}\sin(10^\circ)+\frac{\sqrt{3}}{2}}\]
\[\cot(\theta)=\frac{1-\cos(10^\circ)+\sqrt{3}\sin(10^\circ)} {\sqrt{3}\cos(10^\circ)+\sin(10^\circ)+\sqrt{3}}\]
since the expression still isn't simplified, notice that using the double angle identity on cosine can be used to cancel the 1, and $\sqrt{3}$
Let: $\cos(5^\circ)=a$ , $\sin(5^\circ)=b$
\[\cot(\theta)=\frac{1-(1-2b^2)+\sqrt{3}\cdot(2ab)} {\sqrt{3}(2a^2-1)+2ab+\sqrt{3}}\]
\[\cot(\theta)=\frac{2b^2+2ab\sqrt{3}} {2a^2\sqrt{3}+2ab}\]
\[\cot(\theta)=\frac{2b(b+a\sqrt{3})} {2a(a\sqrt{3}+b)}\]
\[\cot(\theta)=\frac{b}{a}\]
\[\cot(\theta)=\tan(5^\circ)\]
\[\cot(\theta)=\cot(85^\circ)\]
\[\theta=85^\circ\] ~sahan

## Solution 6 (guess and check)
Obtain: $\sin\theta+\sin(\theta-110^\circ)+\sin(\theta-120^\circ)=0$ from solution 5 We now guess $\theta=85^\circ$ and try to verify
\[\sin85^\circ+\sin-25^\circ+\sin-35^\circ=0\] \[\cos5^\circ=\sin25^\circ+\sin35^\circ\] \[\cos5^\circ=\sin(30^\circ-5^\circ)+\sin(30^\circ+5^\circ)\] \[\cos5^\circ=2\sin30^\circ\cos5^\circ\] \[\cos5^\circ=\cos5^\circ\]

## Solution 7 (alternate way to bash out algebra + trig identities)
Use equation from Solution 5: \[\sin\theta+\sin(\theta-110^\circ)+\sin(\theta-120^\circ)=0\] \[\sin\theta+\sin(\theta-115^\circ+5^\circ)+\sin(\theta-115^\circ-5^\circ)=0\] \[\sin\theta+2\sin(\theta-115^\circ)\cos(5^\circ)=0\] \[\sin\theta-2\sin(\theta+65^\circ)\cos(5^\circ)=0\] \[\sin\theta=2\sin(\theta+65^\circ)\cos(5^\circ)\]
now guess $\theta=85$ so that the cos(5) is dealt with (and then check it works)
If you refuse to guess work through the following algebra :D
Let: $\phi=\theta+65^\circ$
\[\sin(\phi-65^\circ)=2\sin\phi\cos(5^\circ)\] \[\sin\phi\cos(65^\circ)-\cos\phi\sin(65^\circ)=2\sin\phi\cos(5^\circ)\] \[\cos(65^\circ)-\cot(\phi)\sin(65^\circ)=2\cos(5^\circ)\] \[\cot(\phi)(\sin(60^\circ)\cos(5^\circ)+\cos(60^\circ)\sin(5^\circ))=(\cos(60^\circ)\cos(5^\circ)-\sin(60^\circ)\sin(5^\circ)) -2\cos(5^\circ)\] \[\cot(\phi)(\frac{\sqrt{3}}{2}\cos(5^\circ)+\frac{1}{2}\sin(5^\circ))=(\frac{1}{2}\cos(5^\circ)-\frac{\sqrt{3}}{2}\sin(5^\circ)) -2\cos(5^\circ)\] \[\cot(\phi)(\frac{\sqrt{3}}{2}\cos(5^\circ)+\frac{1}{2}\sin(5^\circ))=(\frac{-3}{2}\cos(5^\circ)-\frac{\sqrt{3}}{2}\sin(5^\circ))\] \[\cot(\phi)(\frac{\sqrt{3}}{2}\cos(5^\circ)+\frac{1}{2}\sin(5^\circ))=-\sqrt{3} (\frac{\sqrt{3}}{2}\cos(5^\circ)+\frac{1}{2}\sin(5^\circ))\] \[\cot(\phi)=-\sqrt3\]
\[\phi=150^\circ\]
\[\theta=150^\circ-65^\circ=85^\circ\]
\[\angle BAD = 85^\circ\]

## Video Solution by CanadaMath
https://youtu.be/gUyeqE-afDs?si=_UowLNW-UxT9stws&t=1188
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
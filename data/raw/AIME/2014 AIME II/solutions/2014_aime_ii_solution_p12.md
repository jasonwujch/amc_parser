# 2014 AIME II Problem 12

## Problem

Suppose that the angles of $\triangle ABC$ satisfy $\cos(3A)+\cos(3B)+\cos(3C)=1.$ Two sides of the triangle have lengths 10 and 13. There is a positive integer $m$ so that the maximum possible length for the remaining side of $\triangle ABC$ is $\sqrt{m}.$ Find $m.$

## Solution 1
Note that $\cos{3C}=-\cos{(3A+3B)}$ . Thus, our expression is of the form $\cos{3A}+\cos{3B}-\cos{(3A+3B)}=1$ . Let $\cos{3A}=x$ and $\cos{3B}=y$ .
Using the fact that $\cos(3A+3B)=\cos 3A\cos 3B-\sin 3A\sin 3B=xy-\sqrt{1-x^2}\sqrt{1-y^2}$ , we get $x+y-xy+\sqrt{1-x^2}\sqrt{1-y^2}=1$ , or $\sqrt{1-x^2}\sqrt{1-y^2}=xy-x-y+1=(x-1)(y-1)$ .
Squaring both sides, we get $(1-x^2)(1-y^2) = [(x-1)(y-1)]^2$ . Cancelling factors, $(1+x)(1+y) = (1-x)(1-y)$ .
- Notice here that we cancelled out one factor of (x-1) and (y-1), which implies that (x-1) and (y-1) were not 0. If indeed they were 0 though, we would have
$cos(3A)-1=0, cos(3A)=1$
For this we could say that A must be 120 degrees for this to work. This is one case. The B case follows in the same way, where B must be equal to 120 degrees. This doesn't change the overall solution though, as then the other angles are irrelevant (this is the largest angle, implying that this will have the longest side and so we would want to have the 120 degreee angle opposite of the unknown side).
Expanding, $1+x+y+xy=1-x-y+xy\rightarrow x+y=-x-y$ .
Simplification leads to $x+y=0$ .
Therefore, $\cos(3C)=1$ . So $\angle C$ could be $0^\circ$ or $120^\circ$ . We eliminate $0^\circ$ and use law of cosines to get our answer:
\[m=10^2+13^2-2\cdot 10\cdot 13\cos\angle C\] \[\rightarrow m=269-260\cos 120^\circ=269-260\left(\text{-}\frac{1}{2}\right)\] \[\rightarrow m=269+130=399\]
$\framebox{399}$
Note: We can get $x=-y$ from $(1+x)(1+y) = (1-x)(1-y)$ , and plugging in $\cos{3A}+\cos{3B}=0$ directly gives $\cos(3C)=1$ . Angle C being 120 degrees is also sufficient for $(1+x)(1+y) = (1-x)(1-y)$ , so we can skip the casework part. -HappyByron

## Solution 2
WLOG, let C be the largest angle in the triangle.
As above, we can see that $\cos3A+\cos3B-\cos(3A+3B)=1$
Expanding, we get
$\cos3A+\cos3B-\cos3A\cos3B+\sin3A\sin3B=1$
$\cos3A\cos3B-\cos3A-\cos3B+1=\sin3A\sin3B$
$(\cos3A-1)(\cos3B-1)=\sin3A\sin3B$
CASE 1: If $\sin 3A = 0$ or $\sin 3B = 0$ ,
This implies one or both of A or B are 60 or 120.
If one of A or B is 120, we have a contradiction, since C must be the largest angle.
Otherwise, if one of A or B is 60, WLOG, assume A = 60, we would have $\cos(3B) + \cos(3C) = 2$ , and thus, cos(3B) and cos(3C) both equal 1, implying $B = C = 120$ , a contradiction to the fact that the sum of the angles of a triangle must be 180 degrees.
CASE 2: If $\sin 3A \neq 0$ and $\sin 3B \neq 0$
$\frac{\cos3A-1}{\sin3A}\cdot\frac{\cos3B-1}{\sin3B}=1$
$\tan{\frac{3A}{2}}\tan{\frac{3B}{2}}=1$
Note that $\tan{x}=\frac{1}{\tan(90-x)}$ , or $\tan{x}\tan(90-x)=1$
Thus $\frac{3A}{2}+\frac{3B}{2}=90$ , or $A+B=60$ .
Now we know that $C=120$ , so we can just use the Law of Cosines to get $\boxed{399}$
-Alexlikemath

## Solution 3
\[\cos3A+\cos3B=1-\cos(3C)=1+\cos(3A+3B)\] \[2\cos\frac{3}{2}(A+B)\cos\frac{3}{2}(A-B)=2\cos^2\frac{3}{2}(A+B)\] If $\cos\frac{3}{2}(A+B) = 0$ , then $\frac{3}{2}(A+B)=90$ , $A+B=60$ , so $C=120$ ; otherwise, \[2\cos\frac{3}{2}(A-B)=2 \cos\frac{3}{2}(A+B)\] \[\sin\frac{3}{2}A\sin\frac{3}{2}B=0\] so either $\sin\frac{3}{2}A=0$ or $\sin\frac{3}{2}B=0$ , i.e., either $A=120$ or $B=120$ . In all cases, one of the angles must be 120, which opposes the longest side. Final result follows. $\boxed{399}$
-Mathdummy

## Solution 4(quick sketch solve)
Let $BC$ be the unknown side length. By Law of Cosines we have that $BC = \sqrt{269-260\cos{A}}$ . We notice that $\cos{A}$ should be negative to optimize $BC$ so $A$ is between $90$ and $180$ degrees. We also know that the value inside the square root is an integer $m$ , so $269-260\cos{A}$ should be an integer. We can then assume that $A$ is $120$ degrees so $\cos{A} = \frac{-1}{2}$ . We do this because $120$ degrees is a "common" value and it makes the value inside the square root an integer. Plugging this into $269-260\cos{A}$ for $m$ we get that it is $\boxed{399}$ .
-srisainandan6

## Video Solution
https://youtu.be/SLSsGYZ4Ix0?si=_f4Uct20WROmBa8E
~MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
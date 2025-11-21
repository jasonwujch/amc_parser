# 2013 AIME II Problem 5

## Problem

In equilateral $\triangle ABC$ let points $D$ and $E$ trisect $\overline{BC}$ . Then $\sin(\angle DAE)$ can be expressed in the form $\frac{a\sqrt{b}}{c}$ , where $a$ and $c$ are relatively prime positive integers, and $b$ is an integer that is not divisible by the square of any prime. Find $a+b+c$ .

## Solution 1
[asy] pair A = (1, sqrt(3)), B = (0, 0), C= (2, 0); pair M = (1, 0); pair D = (2/3, 0), E = (4/3, 0); draw(A--B--C--cycle); label("$A$", A, N); label("$B$", B, SW); label("$C$", C, SE); label("$D$", D, S); label("$M$", M, S); label("$E$", E, S); draw(A--D); draw(A--M); draw(A--E); [/asy]
Without loss of generality, assume the triangle sides have length 3. Then the trisected side is partitioned into segments of length 1, making your computation easier.
Let $M$ be the midpoint of $\overline{DE}$ . Then $\Delta MCA$ is a 30-60-90 triangle with $MC = \dfrac{3}{2}$ , $AC = 3$ and $AM = \dfrac{3\sqrt{3}}{2}$ . Since the triangle $\Delta AME$ is right, then we can find the length of $\overline{AE}$ by pythagorean theorem, $AE = \sqrt{7}$ . Therefore, since $\Delta AME$ is a right triangle, we can easily find $\sin(\angle EAM) = \dfrac{1}{2\sqrt{7}}$ and $\cos(\angle EAM) = \sqrt{1-\sin(\angle EAM)^2}=\dfrac{3\sqrt{3}}{2\sqrt{7}}$ . So we can use the double angle formula for sine, $\sin(\angle EAD) = 2\sin(\angle EAM)\cos(\angle EAM) = \dfrac{3\sqrt{3}}{14}$ . Therefore, $a + b + c = \boxed{020}$ .

## Solution 2
We find that, as before, $AE = \sqrt{7}$ , and also the area of $\Delta DAE$ is $\dfrac{1}{3}$ the area of $\Delta ABC$ . Thus, using the area formula, $\dfrac{1}{2} \cdot 7 \cdot \sin(\angle EAD) = \dfrac{3\sqrt{3}}{4}$ , and $\sin(\angle EAD) = \dfrac{3\sqrt{3}}{14}$ . Therefore, $a + b + c = \boxed{020}.$

## Solution 3
Let A be the origin of the complex plane, B be $1+i\sqrt{3}$ , and C be $2$ . Also, WLOG, let D have a greater imaginary part than E. Then, D is $\frac{4}{3}+\frac{2i\sqrt{3}}{3}$ and E is $\frac{5}{3}+\frac{i\sqrt{3}}{3}$ . Then, $\sin(\angle DAE) = Im\left(\dfrac{\frac{4}{3}+\frac{2i\sqrt{3}}{3}}{ \frac{5}{3}+\frac{i\sqrt{3}}{3}}\right) = Im\left(\frac{26+6i\sqrt{3}}{28}\right) = \frac{3\sqrt{3}}{14}$ . Therefore, $a + b + c = \boxed{020}$

## Solution 4
Without loss of generality, say that the side length of triangle ABC is 3. EC is 1 and by the law of cosines, $AE^2=1+3^2-2(1)(3)\cos(\angle DAE)$ or $AE=\sqrt7$ The same goes for AD. DE equals 1 because AD and AE trisect BC. By the law of cosines, $\cos(\angle DAE)=(1-7-7)/-2(\sqrt7)(\sqrt7)=13/14$ Since $\sin^2(\angle DAE)=1-cos^2(\angle DAE)$ Then $\sin^2(\angle DAE)= 1-\frac{169}{196}=\frac{27}{196}$ So $\sin(\angle DAE)=\frac{3\sqrt{3}}{14}$ . Therefore, $a + b + c = \boxed{020}$

## Solution 5 (Vectors)
Setting up a convinient coordinate system, we let $A$ be at point $(0, 0)$ , $B$ be at point $(3, 3\sqrt3)$ , and $C$ be at point $(6, 0)$ . Then $D$ and $E$ will be at points $(4, 2\sqrt3)$ and $(5, \sqrt3)$ . Then $\cos(\angle DAE) = \frac{\vec{AD}\cdot\vec{AE}}{\|\vec{AD}\| \|\vec{AE}\|} = \frac{4\cdot5 + 2\sqrt{3}\cdot\sqrt{3}}{28}=\frac{13}{14}$ . From here, we see that $\sin(\angle DAE) = \sqrt{1-\cos^2(\angle DAE)} = \frac{3\sqrt3}{14}\Longrightarrow\boxed{020}$

## Solution 6
We first drop the altitude from $A$ to $BC$ , and that evaluates to a length of $5$ . Now, we can find $AD$ by Pythag. We have $AD = \sqrt{7}$ . Now, we can set $\angle{DAE}$ to be $\theta$ , and now we we can solve for $\sin{\theta}$ . We will take advantage of the different ways to find the area of a triangle. We have the area of the triangle is $\dfrac{\dfrac{1}{2} \cdot \dfrac{3\sqrt3}{2}}{2} = \dfrac{3\sqrt3}{4}$ . We can also express it as $\dfrac{1}{2} \cdot 7 \cdot \sin{\theta}$ , and solving for $\sin{\theta}$ , we get \[\dfrac{3\sqrt3}{14} \Longrightarrow \boxed{020}\]
~jb2015007
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
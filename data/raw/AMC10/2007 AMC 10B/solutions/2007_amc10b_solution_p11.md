# 2007 AMC 10B Problem 11

## Problem

A circle passes through the three vertices of an isosceles triangle that has two sides of length $3$ and a base of length $2$ . What is the area of this circle?

$\textbf{(A) } 2\pi \qquad\textbf{(B) } \frac{5}{2}\pi \qquad\textbf{(C) } \frac{81}{32}\pi \qquad\textbf{(D) } 3\pi \qquad\textbf{(E) } \frac{7}{2}\pi$

## Solutions

## Solution 1
Let $\triangle ABC$ have vertex $A$ and center $O$ , with foot of altitude from $A$ intersecting $BC$ at $D$ .
Then by the Pythagorean Theorem (with radius $r$ and height $OD = h$ ) on $\triangle OBD$ and $\triangle ABD$ \begin{align*} h^2 + 1 & = r^2 \\ (h + r)^2 + 1 & = 9 \end{align*}
Substituting and solving gives $r = \frac {9}{4\sqrt {2}}$ . Then the area of the circle is $r^2 \pi = \left(\frac {9}{4\sqrt {2}}\right)^2 \pi = \boxed{\mathrm{(C) \ } \frac {81}{32} \pi}$ .

## Solution 2
By $A = \frac {1}{2}Bh = \frac {abc}{4R}$ (or we could use $s = 4$ and Heron's formula ), \[R = \frac {abc}{2Bh} = \frac {3 \cdot 3 \cdot 2}{2(2)(2\sqrt {2})} = \frac {9}{4\sqrt {2}}\] and the answer is $R^2 \pi = \boxed{\mathrm{(C) \ } \frac {81}{32} \pi}$
Alternatively, by the Extended Law of Sines , \[2R = \frac {AC}{\sin \angle ABC} = \frac {3}{\frac {2\sqrt {2}}{3}} \Longrightarrow R = \frac {9}{4\sqrt {2}}\] Answer follows as above.

## Solution 3
Extend segment $AD$ to $R$ on Circle $O$ .
By the Pythagorean Theorem \[AD^2 = 3^2 - 1^2\] \[AD = 2\sqrt{2}\]
$\triangle ADC$ is similar to $\triangle ACR$ , so \[\frac {2\sqrt{2}}{3} = \frac {3}{2r}\] which gives us \[2r = \frac {9}{2\sqrt{2}} = \frac {9\sqrt{2}}{4}\] therefore \[r = \frac {9\sqrt{2}}{8}\]
The area of the circle is therefore $\pi r^2 = \left(\frac {9\sqrt{2}}{8}\right)^2 \pi = \boxed{\mathrm{(C) \ } \frac {81}{32} \pi}$

## Solution 4
First, we extend $AD$ to intersect the circle at $E.$
By the Pythagorean Theorem , we know that \[1^2+AD^2=3^2\implies AD=2\sqrt{2}.\] We also know that, from the Power of a Point Theorem , \[AD\cdot DE=BD\cdot DC.\] We can substitute the values we know to get \[2\sqrt{2}\cdot DE=1\] We can simplify this to get that \[DE=\dfrac{2\sqrt{2}}{8}.\] We add $AD$ and $DE$ together to get the length of the diameter, and then we can find the area. \[AE=AD+DE=2\sqrt{2}+\dfrac{2\sqrt{2}}{8}=\dfrac{9\sqrt{2}}{4}.\] Therefore, the radius is $\dfrac{9\sqrt{2}}{8}$ , so the area is \[\left(\dfrac{9\sqrt{2}}{8}\right)^2\pi=\boxed{(\text{C})\dfrac{81}{32}\pi.}\]

## Solution 5
Another possible solution is to plot the circle and triangle on a graph with the circle having center $(0,0)$ . Let the radius of the circle = $r$ . Let the distance between the origin and the base of triangle = $a$ . \[1 + a^2 = r^2\] \[r + a = 2\sqrt{2}\] \[a = 2\sqrt{2} - r\] \[9 - 4r\sqrt{2} = 0\] \[r = \frac{9\sqrt{2}}{8}\] \[\pi r^2 = \boxed{(\text{C})\frac{81}{32}\pi}\]

## Solution 6
We can also use LOC to solve this problem. If O is the center of the circle, angle $OBC$ is double angle $BAC$ . From law of cosines, we have that $\cos(\angle BAC) = \frac{7}{9}$ . We now apply law of cosines on triangle $OBC$ to get that $4 = r^2+r^2-2r^2\cos(2 \angle BAC)$ but we know that $2 \cos (\angle BAC) = 2 \cdot (\frac{7}{9})^2 - 1 = \frac{17}{81}$ . Plugging this in and simplifying, we get $r = \frac{9}{8} \cdot \sqrt{2}$ and thus the area of the circle is equal to $\frac{81}{32} \pi$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
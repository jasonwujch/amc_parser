# 2023 AIME II Problem 3

## Problem

Let $\triangle ABC$ be an isosceles triangle with $\angle A = 90^\circ.$ There exists a point $P$ inside $\triangle ABC$ such that $\angle PAB = \angle PBC = \angle PCA$ and $AP = 10.$ Find the area of $\triangle ABC.$

### Diagram

[asy] /* Made by MRENTHUSIASM */ size(200); pair A, B, C, P; A = origin; B = (0,10*sqrt(5)); C = (10*sqrt(5),0); P = intersectionpoints(Circle(A,10),Circle(C,20))[0]; dot("$A$",A,1.5*SW,linewidth(4)); dot("$B$",B,1.5*NW,linewidth(4)); dot("$C$",C,1.5*SE,linewidth(4)); dot("$P$",P,1.5*NE,linewidth(4)); markscalefactor=0.125; draw(rightanglemark(B,A,C,10),red); draw(anglemark(P,A,B,25),red); draw(anglemark(P,B,C,25),red); draw(anglemark(P,C,A,25),red); add(pathticks(anglemark(P,A,B,25), n = 1, r = 0.1, s = 10, red)); add(pathticks(anglemark(P,B,C,25), n = 1, r = 0.1, s = 10, red)); add(pathticks(anglemark(P,C,A,25), n = 1, r = 0.1, s = 10, red)); draw(A--B--C--cycle^^P--A^^P--B^^P--C); label("$10$",midpoint(A--P),dir(-30),blue); [/asy] ~MRENTHUSIASM

## Solution 1
This solution refers to the Diagram section.
Let $\angle PAB = \angle PBC = \angle PCA = \theta,$ from which $\angle PAC = 90^\circ-\theta,$ and $\angle APC = 90^\circ.$
Moreover, we have $\angle PBA = \angle PCB = 45^\circ-\theta,$ as shown below: [asy] /* Made by MRENTHUSIASM */ size(250); pair A, B, C, P; A = origin; B = (0,10*sqrt(5)); C = (10*sqrt(5),0); P = intersectionpoints(Circle(A,10),Circle(C,20))[0]; dot("$A$",A,1.5*SW,linewidth(4)); dot("$B$",B,1.5*NW,linewidth(4)); dot("$C$",C,1.5*SE,linewidth(4)); dot("$P$",P,1.5*NE,linewidth(4)); markscalefactor=0.125; draw(rightanglemark(B,A,C,10),red); draw(rightanglemark(A,P,C,10),red); draw(anglemark(P,A,B,25),red); draw(anglemark(P,B,C,25),red); draw(anglemark(P,C,A,25),red); draw(anglemark(A,B,P,25),green); draw(anglemark(B,C,P,25),green); draw(anglemark(C,A,P,25),green); add(pathticks(anglemark(P,A,B,25), n = 1, r = 0.1, s = 10, red)); add(pathticks(anglemark(P,B,C,25), n = 1, r = 0.1, s = 10, red)); add(pathticks(anglemark(P,C,A,25), n = 1, r = 0.1, s = 10, red)); draw(A--B--C--cycle^^P--A^^P--B^^P--C); label("$10$",midpoint(A--P),dir(-30),blue); label("$\theta$",A,9.5*dir(76),red); label("$\theta$",C,9.5*dir(168),red); label("$\theta$",B,9*dir(305),red); label("$45^\circ-\theta$",B,6*dir(235),green); label("$45^\circ-\theta$",C,6*dir(85),green); label("$90^\circ-\theta$",A,2*dir(-40),green); [/asy] Note that $\triangle PAB \sim \triangle PBC$ by AA Similarity. The ratio of similitude is $\frac{PA}{PB} = \frac{PB}{PC} = \frac{AB}{BC},$ so $\frac{10}{PB} = \frac{1}{\sqrt2}$ and thus $PB=10\sqrt2.$ Similarly, we can figure out that $PC=20$ .
Finally, $AC=\sqrt{10^2+20^2}=10\sqrt{5}$ , so the area of $\triangle ABC$ is \[\frac12\cdot AB\cdot AC = \frac12\cdot (10\sqrt{5})^2 = \boxed{250}.\]
~s214425
~MRENTHUSIASM

## Solution 2
Since the triangle is a right isosceles triangle, $\angle B = \angle C = 45^\circ$ .
Let the common angle be $\theta$ . Note that $\angle PAC = 90^\circ-\theta$ , thus $\angle APC = 90^\circ$ . From there, we know that $AC = \frac{10}{\sin\theta}$ .
Note that $\angle ABP = 45^\circ-\theta$ , so from law of sines we have \[\frac{10}{\sin\theta \cdot \frac{\sqrt{2}}{2}}=\frac{10}{\sin(45^\circ-\theta)}.\] Dividing by $10$ and multiplying across yields \[\sqrt{2}\sin(45^\circ-\theta)=\sin\theta.\] From here use the sine subtraction formula, and solve for $\sin\theta$ : \begin{align*} \cos\theta-\sin\theta&=\sin\theta \\ 2\sin\theta&=\cos\theta \\ 4\sin^2\theta&=\cos^2\theta \\ 4\sin^2\theta&=1-\sin^2\theta \\ 5\sin^2\theta&=1 \\ \sin\theta&=\frac{1}{\sqrt{5}}. \end{align*} Substitute this to find that $AC=10\sqrt{5}$ , thus the area is $\frac{(10\sqrt{5})^2}{2}=\boxed{250}$ .
~SAHANWIJETUNGA

## Solution 3
Since the triangle is a right isosceles triangle, $\angle B = \angle C = 45^\circ$ .
Do some angle chasing yielding:
- $\angle APB = \angle BPC = 135^\circ$
- $\angle APC=90^\circ$
We have $AC=\frac{10}{\sin\theta}$ since $\triangle APC$ is a right triangle. Since $\triangle ABC$ is a $45^\circ$ - $45^\circ$ - $90^\circ$ triangle, $AB=\frac{10}{\sin\theta}$ , and $BC=\frac{10\sqrt{2}}{\sin\theta}$ .
Note that $\triangle APB \sim \triangle BPC$ by a factor of $\sqrt{2}$ . Thus, $BP = 10\sqrt{2}$ , and $PC = 20$ .
From Pythagorean theorem, $AC=10\sqrt{5}$ so the area of $\triangle ABC$ is $\frac{(10\sqrt{5})^2}{2}=\boxed{250}$ .
~SAHANWIJETUNGA

## Solution 4
Since the triangle is a right isosceles triangle, $\angle B = \angle C = 45^\circ$ .
Notice that in triangle $PBC$ , $\angle PBC + 45-\angle PCA = 45^\circ$ , so $\angle BPC = 135^\circ$ . Similar logic shows $\angle APC = 135^\circ$ .
Now, we see that $\triangle APB \sim \triangle BPC$ with ratio $1:\sqrt{2}$ (as $\triangle ABC$ is a $45^\circ$ - $45^\circ$ - $90^\circ$ triangle). Hence, $\overline{PB}=10\sqrt{2}$ . We use the Law of Cosines to find $AB$ . \begin{align*} AB^2&=BP^2+AP^2-2ab\cos(APB) \\ &=100+200-2(10)(10\sqrt{2}\cos(135^\circ)) \\ &=300+200\cdot\sqrt{2}\cdot\frac{1}{\sqrt{2}} \\ &=500. \end{align*} Since $\triangle ABC$ is a right triangle, the area is $\frac{AB^2}{2}=\frac{500}{2}=\boxed{250}$ .
~Kiran

## Solution 5
Denote the area of $X$ by $[X].$ As in previous solutions, we see that $\angle APC = 90 ^\circ, \triangle BPC \sim \triangle APB$ with ratio $k = \sqrt{2}\implies$ \[\frac {PC}{PB} = \frac {PB}{PA} = k \implies PC = k^2 \cdot AP = 20 \implies [APC] = \frac {AP \cdot PC}{2} = 100.\] \[[BPC] = k^2 [APB] = 2 [APB].\] \[AB = BC, \angle PCA = \angle PAB \implies \frac {[APC]}{[APB]} = \frac {PC}{PA} = 2 \implies\] \[[ABC] = [APB] + [APC] + [BPC] = [APC] \cdot (\frac {1}{2} + 1 + 2 \cdot \frac {1}{2}) = \frac {5}{2} \cdot [APC] = \boxed{250}.\] vladimir.shelomovskii@gmail.com, vvsss

## Solution 6
Denote $\angle PCA = \theta$ . Then, by trig Ceva's: \begin{align*} \frac{\sin^3(\theta)}{\sin(90-\theta) \cdot \left(\sin(45-\theta)\right)^2} &= 1 \\ \sin^3(\theta) &= \cos(\theta) \cdot \left(\sin(45) \cos(\theta) - \cos(45) \sin(\theta)\right)^2 \\ 2\sin^3(\theta) &= \cos(\theta) \cdot \left(\cos(\theta) - \sin(\theta)\right)^2 \\ 2\sin^2(\theta) &= \cot(\theta) \cdot \left(1 - 2\sin(\theta)\cos(\theta)\right) \\ 2\sin^2(\theta) &= \cot(\theta) - 2\cos^2(\theta) \\ \cot(\theta) &= 2 \\ \sin(\theta) &= \frac{\sqrt{5}}{5}. \end{align*} Note that $\angle APC$ is a right angle. Therefore: \begin{align*} \sin(\theta) &= \frac{AP}{AC} \\ AC &= \frac{10}{\frac{\sqrt{5}}{5}} \\ &= 10\sqrt{5} \\ |ABC| &= \frac{AC^2}{2} \\ &= \boxed{250}. \end{align*} ~ConcaveTriangle

## Solution 7
Notice that point $P$ is one of the two Brocard Points of $\triangle ABC$ . (The angle equalities given in the problem are equivalent to the definition of a Brocard point.) By the Brocard point formula, \begin{align*} \cot(\phi) = \cot(A)+\cot(B)+\cot(C) \end{align*} , where $\phi$ is equal to $\angle PAB$ .(This is also called the Brocard angle of triangle ABC). Because the triangle is an isosceles right triangle, the cotangents are easy to compute: \begin{align*}\cot(\phi) = 0 + 1 + 1 \\ \cot(\phi) = 2\end{align*} By definition, $\cot(\phi) = \frac{\cos(\phi)}{\sin(\phi)}$ . By the Pythagorean identity, $\cos(\phi)=\frac{2\sqrt{5}}{5}$ and $\sin(\phi) = \cos(\phi)=\frac{\sqrt{5}}{5}$ . Consider triangle $APB$ . By the problem condition, $\angle PBA = 45-\phi$ , so $\angle BPA = 135^{\circ}$ \begin{align*}\sin{45-\theta} = \sin{45}\cos{\phi}-\cos{45}\sin{\phi} = \frac{\sqrt{10}}{10}\end{align*} Now, we can use the Law of Sines. \begin{align*} \frac{AP}{\sin{45-\theta}}&=\frac{AB}{\sin{135}} \\ 10 \sqrt{10} &= \sqrt{2} AB \\ AB &= 10 \sqrt{5} \end{align*} Therefore, the answer is \[[ABC] = \frac{1}{2} (AB)^2 = \boxed{250}.\] ~ewei12

## Solution 8
Notice that $\angle APC = 90^{\circ}$ , $\angle BPA = 135^{\circ}$ , and $\angle CPB = 135^{\circ}$ (from Solution 4). Now let $a = 0$ and $p = 10i$ . Then by the angle restrictions $c = m + 10i$ and $b = -n + (n+10)i$ for some $m, n$ . Since $\angle BAC = 90^{\circ}$ , $ci = b$ , or $(m + 10i)i = -n + (n+10)i$ . Therefore $n = 10$ , $AB = \sqrt{10^2 + 20^2} = \sqrt{500}$ , and $[ABC] = \frac{1}{2} AB^2 = \boxed{250}$ .
~aliz

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=APSUN-9Z_AU

## Video Solution 2 by Piboy
https://www.youtube.com/watch?v=-WUhMmdXCxU&t=26s&ab_channel=Piboy

## Video Solution by The Power of Logic(#3 and #4)
https://youtu.be/dS9K1o4gCA0
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
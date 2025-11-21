# 2000 AIME II Problem 9

## Problem

Given that $z$ is a complex number such that $z+\frac 1z=2\cos 3^\circ$ , find the least integer that is greater than $z^{2000}+\frac 1{z^{2000}}$ .

## Solution
Using the quadratic equation on $z^2 - (2 \cos 3 )z + 1 = 0$ , we have $z = \frac{2\cos 3 \pm \sqrt{4\cos^2 3 - 4}}{2} = \cos 3 \pm i\sin 3 = \text{cis}\,3^{\circ}$ .
There are other ways we can come to this conclusion. Note that if $z$ is on the unit circle in the complex plane, then $z = e^{i\theta} = \cos \theta + i\sin \theta$ and $\frac 1z= e^{-i\theta} = \cos \theta - i\sin \theta$ . We have $z+\frac 1z = 2\cos \theta = 2\cos 3^\circ$ and $\theta = 3^\circ$ . Alternatively, we could let $z = a + bi$ and solve to get $z=\cos 3^\circ + i\sin 3^\circ$ .
Using De Moivre's Theorem we have $z^{2000} = \cos 6000^\circ + i\sin 6000^\circ$ , $6000 = 16(360) + 240$ , so $z^{2000} = \cos 240^\circ + i\sin 240^\circ$ .
We want $z^{2000}+\frac 1{z^{2000}} = 2\cos 240^\circ = -1$ .
Finally, the least integer greater than $-1$ is $\boxed{000}$ .

## Solution 2
Let $z=re^{i\theta}$ . Notice that we have $2\cos(3^{\circ})=e^{i\frac{\pi}{60}}+e^{-i\frac{\pi}{60}}=re^{i\theta}+\frac{1}{r}e^{-i\theta}.$
$r$ must be $1$ (or if you take the magnitude would not be the same). Therefore, $z=e^{i\frac{\pi}{\theta}}$ and plugging into the desired expression, we get $e^{i\frac{100\pi}{3}}+e^{-i\frac{100\pi}{3}}=2\cos{\frac{100\pi}{3}}=-1$ . Therefore, the least integer greater is $\boxed{000}.$
~solution by williamgolly

## Solution 3 Intuitive
For this solution, we assume that $z^{2000} + 1/z^{2000}$ and $z^{2048} + 1/z^{2048}$ has the same least integer greater than their solution.
We have $z + 1/z = 2\cos 3$ . Since $\cos 3<1$ , $2\cos 3<2$ . If we square the equation $z + 1/z = 2\cos 3$ , we get $z^2 + 2 + 1/(z^2) = 4\cos^2 3$ , or $z^2 + 1/(z^2) = 4\cos^2 3 - 2$ . $4\cos^2 3 - 2$ is is less than $2$ , since $4\cos^2 3$ is less than $4$ . If we square the equation again, we get $z^4 + 1/(z^4) = (4\cos^2 3 - 2)^2 -2$ .
Since $4\cos^2 3 - 2$ is less than 2, $(4\cos^2 3 - 2)^2$ is less than 4, and $(4\cos^2 3 - 2)^2 -2$ is less than 2. However $(4\cos^2 3 - 2)^2 -2$ is also less than $4\cos^2 3 - 2$ . we can see that every time we square the equation, the right-hand side gets smaller and into the negatives. Since the smallest integer that is allowed as an answer is 0, the smallest integer greater is $\boxed{000}.$
~ PaperMath ~megaboy6679

## Solution 4
First, let $z = a+bi$ where $a$ and $b$ are real numbers. We now have that \[a+bi+\frac{a-bi}{a^2+b^2} = 2 \cos{3^{\circ}}\] given the conditions of the problem. Equating imaginary coefficients, we have that \[b \left( 1 - \frac{1}{a^2+b^2}\right) = 0\] giving us that either $b=0$ or $|z| = 1$ . Let's consider the latter case for now.
We now know that $a^2+b^2=1$ , so when we equate real coefficients we have that $2a = 2 \cos{3^{\circ}}$ , therefore $a = \cos{3^{\circ}}$ . So, $b = \sin{3^{\circ}}$ and then we can write $z = \text{cis}(3)^{\circ}$ .
By De Moivre's Theorem, \[z^{2000} + \frac{1}{z^{2000}} = \text{cis} (6000)^{\circ} + \text{cis} (-6000)^{\circ}\] . The imaginary parts cancel, leaving us with $2 \cos{6000^{\circ}}$ , which is $240 \pmod{360}$ . Therefore, it is $-1$ , and our answer is $\boxed{000}$ .
Now, if $b=0$ then we have that $a+\frac{1}{a} = 2 \cos{3^{\circ}}$ . Therefore, $a$ is not violating our conditions set above.
1981 AHSME Q24 may be related.
These problems are copyrighted © by the Mathematical Association of America.
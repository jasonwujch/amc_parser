# 2003 AIME I Problem 12

## Problem

In convex quadrilateral $ABCD, \angle A \cong \angle C, AB = CD = 180,$ and $AD \neq BC.$ The perimeter of $ABCD$ is $640$ . Find $\lfloor 1000 \cos A \rfloor.$ (The notation $\lfloor x \rfloor$ means the greatest integer that is less than or equal to $x.$ )

## Solution

## Solution 1
By the Law of Cosines on $\triangle ABD$ at angle $A$ and on $\triangle BCD$ at angle $C$ (note $\angle C = \angle A$ ),
\[180^2 + AD^2 - 360 \cdot AD \cos A = 180^2 + BC^2 - 360 \cdot BC \cos A\] \[(AD^2 - BC^2) = 360(AD - BC) \cos A\] \[(AD - BC)(AD + BC) = 360(AD - BC) \cos A\] \[(AD + BC) = 360 \cos A\] We know that $AD + BC = 640 - 360 = 280$ . $\cos A = \dfrac{280}{360} = \dfrac{7}{9} = 0.777 \ldots$
$\lfloor 1000 \cos A \rfloor = \boxed{777}$ .

## Solution 2
Notice that $AB = CD$ , and $BD = DB$ , and $\angle{DAB} \cong \angle{BCD}$ , so we have side-side-angle matching on triangles $ABD$ and $CDB$ . Since the problem does not allow $\triangle{ABD} \cong \triangle{CDB}$ , we know that $\angle{ADB}$ is not a right angle, and there is a unique other triangle with the matching side-side-angle.
Overlay the triangles $\triangle BDA$ and $\triangle BDC$ on each other as in the diagram above (where the red labels correspond to $\triangle BDA$ and the blue labels correspond to $\triangle BDC$ ). Here we assume without loss of generality that $BC>AD$ . Furthermore, let $\theta$ be the angle $A$ referenced in the problem; we need to find $\lfloor 1000\cos\theta\rfloor$ .
Since the perimeter of $ABCD$ is $640$ , we have $AD+BC=640-360=280$ . Thus let $BC=a$ and $AD=280-a$ for some positive real number $a$ . But the sides that correspond to $\overline{BD}$ above are congruent, so we can drop a perpendicular from the topmost point to a point $E$ , where the base of the isosceles triangle is bisected. Notice that the base of the isosceles triangle has length $a-(280-a)=2a-280$ , so in the diagram above, $AE=280-a+\frac{1}{2}(2a-280)=280-a+a-140=140$ .
Looking above at the right triangle containing $\theta$ , we see that $\cos\theta=\frac{AE}{180}=\frac{140}{180}=\frac{7}{9}$ . Hence $\left\lfloor 1000\cdot\frac{7}{9}\right\rfloor=\boxed{777}$ is our answer.
~ eevee9406

## Solution 3
Start the same as solution 1. We get \[180^2+a^2-360a \cos A = 180^2+b^2-360b \cos A \Rightarrow a^2-360a \cos A = b^2-360b \cos A,\] where $a$ is the length of $BC$ and $b$ is the length of $AD$ . Let the common value of $a^2-360a \cos A$ and $b^2-360b \cos A$ be $c$ . Then, the quadratic in $x$ \[x^2-360 \cos A \cdot x - c = 0\] has solutions $a$ and $b$ . Therefore, by Vieta's, $a+b = 360 \cos A$ . However, we know that the perimeter of $ABCD$ is $640$ , so $a+b+180+180=640$ , so $a+b=280$ . Therefore, \[360 \cos A = 280 \Rightarrow \cos A = \frac{280}{360} \Rightarrow \cos A = \frac{7}{9} \Rightarrow \lfloor 1000 \cos A \rfloor = \boxed{777}.\]
These problems are copyrighted © by the Mathematical Association of America.
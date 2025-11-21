# 2022 AMC 10A Problem 15

## Problem

Quadrilateral $ABCD$ with side lengths $AB=7, BC=24, CD=20, DA=15$ is inscribed in a circle. The area interior to the circle but exterior to the quadrilateral can be written in the form $\frac{a\pi-b}{c},$ where $a,b,$ and $c$ are positive integers such that $a$ and $c$ have no common prime factor. What is $a+b+c?$

$\textbf{(A) } 260 \qquad \textbf{(B) } 855 \qquad \textbf{(C) } 1235 \qquad \textbf{(D) } 1565 \qquad \textbf{(E) } 1997$

### Diagram

[asy] /* Made by MRENTHUSIASM */ size(200); pair O, A, B, C, D; O = origin; A = (-25/2,0); C = (25/2,0); B = intersectionpoints(Circle(A,7),Circle(C,24))[0]; D = intersectionpoints(Circle(A,15),Circle(C,20))[1]; fill(Circle(O,25/2),yellow); fill(A--B--C--D--cycle,white); dot("$A$",A,1.5*W,linewidth(4)); dot("$B$",B,1.5*dir(B),linewidth(4)); dot("$C$",C,1.5*E,linewidth(4)); dot("$D$",D,1.5*dir(D),linewidth(4)); dot(O,linewidth(4)); draw(Circle(O,25/2)); draw(A--B--C--D--cycle); label("$7$",midpoint(A--B),rotate(90)*dir(midpoint(A--B)--A)); label("$24$",midpoint(B--C),rotate(-90)*dir(midpoint(B--C)--B)); label("$20$",midpoint(C--D),rotate(-90)*dir(midpoint(C--D)--C)); label("$15$",midpoint(D--A),rotate(90)*dir(midpoint(D--A)--D)); [/asy] ~MRENTHUSIASM

## Solution 1 (Inscribed Angle Theorem)
Opposite angles of every cyclic quadrilateral are supplementary, so \[\angle B + \angle D = 180^{\circ}.\] We claim that $AC=25.$ We can prove it by contradiction:
- If $AC<25,$ then $\angle B$ and $\angle D$ are both acute angles. This arrives at a contradiction.
- If $AC>25,$ then $\angle B$ and $\angle D$ are both obtuse angles. This arrives at a contradiction.
By the Inscribed Angle Theorem, we conclude that $\overline{AC}$ is the diameter of the circle. So, the radius of the circle is $r=\frac{AC}{2}=\frac{25}{2}.$
The area of the requested region is \[\pi r^2 - \frac12\cdot AB\cdot BC - \frac12\cdot AD\cdot DC = \frac{625\pi}{4}-\frac{168}{2}-\frac{300}{2}=\frac{625\pi-936}{4}.\] Therefore, the answer is $a+b+c=\boxed{\textbf{(D) } 1565}.$
~MRENTHUSIASM

## Solution 2 (Brahmagupta‘s Formula)
When we look at the side lengths of the quadrilateral we see $7$ and $24,$ which screams out $25$ because of Pythagorean triplets. As a result, we can draw a line through points $A$ and $C$ to make a diameter of $25.$ See Solution 1 for a rigorous proof.
This can also be shown using the Law of Cosines: Since $7^2+24^2-2\cdot7\cdot24\cdot\cos B=15^2+20^2-2\cdot15\cdot20\cdot\cos D$ and $\cos B + \cos D = 0,$ it follows that $\cos B = \cos D = 0.$
Since the diameter is $25,$ we can see the area of the circle is just $\frac{625\pi}{4}$ from the formula of the area of the circle with just a diameter.
Then we can use Brahmagupta Formula $\sqrt{(s - a)(s - b)(s - c)(s - d)}$ where $a,b,c,d$ are side lengths, and $s$ is semi-perimeter to find the area of the quadrilateral.
You can find the answer to this quickly by noting that $\sqrt{(33-7)(33-24)(33-20)(33-15)} = \sqrt{(26)(9)(13)(18)} = \sqrt{2^2 \cdot 3^4 \cdot 13^2} = 2 \cdot 9 \cdot 13 = 234$ . So now the area of the region we are trying to find is $\frac{625\pi}{4} - 234 = \frac{625\pi-936}{4}.$
Therefore, the answer is $a+b+c=\boxed{\textbf{(D) } 1565}.$
~Gdking ~Oinava ~ South

## Solution 3 (Circumradius's Formula)
We can guess that this quadrilateral is actually made of two right triangles: $\triangle CDA$ has a $3 \text{-} 4 \text{-} 5$ ratio in the side lengths, and $\triangle ABC$ is a $7 \text{-} 24 \text{-} 25$ triangle. (See Solution 1 for a proof.)
Next, we can choose one of these triangles and use the circumradius formula to find the radius. Let's choose the $15-20-25$ triangle. The area of the triangle is equal to the product of the side lengths divided by $4$ times the circumradius. Therefore, $150 = \frac{15\cdot20\cdot25}{4r}$ . Solving this simple algebraic equation gives us $r = \frac{25}{2}$ .
Plugging in the values, we have $\frac{25}{2}^2\cdot\pi - \left(\frac{15\cdot20}{2}+\frac{7\cdot24}{2}\right) = \frac{625\cdot\pi}{4} - 234$ . Rewriting this gives us $\frac{625\pi-936}{4}$ .
Therefore, adding these values gets us $\boxed{\textbf{(D) } 1565}.$
~ orenbad

## Solution 4 (Complete Bash Using Brahmagupta’s and Parameshvara’s Formulas)
To start, we can apply a couple formulas to find the circumradius and the area of the cyclic quadrilateral, and then just subtract the area of the quadrilateral from the area of the circle, and that is our final answer. This formula is really tedious with many calculations so don't do this in a contest. To find the circumradius we have: \[\text{Circumradius} = \frac{1}{4} \sqrt{\frac{(ab + cd)(ac + bd)(ad + bc)}{(s-a)(s-b)(s-c)(s-d)}}\] If we let $a = 7, b = 24, c = 20, \text{and}, d = 15$ , that means that the semi-perimeter is just \[\dfrac{7+24+20+15}{2} = 33\] . Note that $s$ stands for the semi-perimeter. The calculations will take very long so Im just going to skip to the answer of $\dfrac{25}{2}$ as our circumradius. This means that the area of the circle is $\dfrac{625}{4}\pi$ . Now applying Brahmagupta's formula to find the area of a cyclic quadrilateral which is just: \[\sqrt{(s-a)(s-b)(s-c)(s-d)}\] . Again we will use the same representations as these letters from before, so $a = 7, b = 24, c = 20, \text{and}, d = 15$ . Plugging in the numbers we have that the area is $234$ . To express our answer in the form that was asked at the top we have: \[\dfrac{625\pi-936}{4}\] , so our final answer is \[625+936+4 = \boxed{\textbf{(D) } 1565}.\]
-jb2015007

## Video Solution 1
https://youtu.be/ZHuInvG82PY
~Education, the Study of Everything

## Video Solution 2
https://youtu.be/Ov9AA7veKKk

## Video Solution by TheBeautyofMath (Simple Pythagorean Triples)
https://youtu.be/0kkc4-y8TkU?t=1632
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
# 2017 AMC 10B Problem 22

## Problem

The diameter $\overline{AB}$ of a circle of radius $2$ is extended to a point $D$ outside the circle so that $BD=3$ . Point $E$ is chosen so that $ED=5$ and line $ED$ is perpendicular to line $AD$ . Segment $\overline{AE}$ intersects the circle at a point $C$ between $A$ and $E$ . What is the area of $\triangle ABC$ ?

$\textbf{(A)}\ \frac{120}{37}\qquad\textbf{(B)}\ \frac{140}{39}\qquad\textbf{(C)}\ \frac{145}{39}\qquad\textbf{(D)}\ \frac{140}{37}\qquad\textbf{(E)}\ \frac{120}{31}$

## Solution 1
Notice that $ADE$ and $ABC$ are right triangles. Then $AE = \sqrt{7^2+5^2} = \sqrt{74}$ . $\sin{DAE} = \frac{5}{\sqrt{74}} = \sin{BAE} = \sin{BAC} = \frac{BC}{4}$ , so $BC = \frac{20}{\sqrt{74}}$ . We also find that $AC = \frac{28}{\sqrt{74}}$ (You can also use power of point ~MATHWIZARD2010), and thus the area of $ABC$ is $\frac{\frac{20}{\sqrt{74}}\cdot\frac{28}{\sqrt{74}}}{2} = \frac{\frac{560}{74}}{2} = \boxed{\textbf{(D) } \frac{140}{37}}$ .

## Solution 2 (Similar Triangles)
We note that $\triangle ACB \sim \triangle ADE$ by $AA$ similarity. Also, since the area of $\triangle ADE = \frac{7 \cdot 5}2 = \frac{35}2$ and $AE = \sqrt{74}$ , $\frac{[ABC]}{[ADE]} = \frac{[ABC]}{\frac{35}2} = \left(\frac{4}{\sqrt{74}}\right)^2$ , so the area of $\triangle ABC = \boxed{\textbf{(D) } \frac{140}{37}}$ .

## Solution 3
As stated before, note that $\triangle ACB$ is similar to $\triangle ADE$ . By similarity, we note that $\frac{\overline{AC}}{\overline{BC}}$ is equivalent to $\frac{7}{5}$ . We set $\overline{AC}$ to $7x$ and $\overline{BC}$ to $5x$ . By the Pythagorean Theorem, $(7x)^2+(5x)^2 = 4^2$ . Combining, $49x^2+25x^2=16$ . We can add and divide to get $x^2=\frac{8}{37}$ . We square root and rearrange to get $x=\frac{2\sqrt{74}}{37}$ . We know that the legs of the triangle are $7x$ and $5x$ . Multiplying $x$ by $7$ and $5$ eventually gives us $\frac {14\sqrt{74}}{37}$ and $\frac {10\sqrt{74}}{37}$ . We divide this by $2$ , since $\frac{1}{2}bh$ is the formula for a triangle. This gives us $\boxed{\textbf{(D) } \frac{140}{37}}$ .

## Solution 4
Let's call the center of the circle that segment $AB$ is the diameter of, $O$ . Note that $\triangle ODE$ is an isosceles right triangle. Solving for side $OE$ , using the Pythagorean theorem, we find it to be $5\sqrt{2}$ . Calling the point where segment $OE$ intersects circle $O$ , the point $I$ , segment $IE$ would be $5\sqrt{2}-2$ . Also, noting that $\triangle ADE$ is a right triangle, we solve for side $AE$ , using the Pythagorean Theorem, and get $\sqrt{74}$ . Using Power of Point on point $E$ , we can solve for $CE$ . We can subtract $CE$ from $AE$ to find $AC$ and then solve for $CB$ using Pythagorean theorem once more.
$(AE)(CE)$ = (Diameter of circle $O$ + $IE$ ) $(IE)$ $\rightarrow$ ${\sqrt{74}}(CE)$ = $(5\sqrt{2}+2)(5\sqrt{2}-2)$ $\Rightarrow$ $CE$ = $\frac{23\sqrt{74}}{37}$
$AC = AE - CE$ $\rightarrow$ $AC$ = ${\sqrt74}$ - $\frac{23\sqrt{74}}{37}$ $\Rightarrow$ $AC$ = $\frac{14\sqrt{74}}{37}$
Now to solve for $CB$ :
$AB^2$ - $AC^2$ = $CB^2$ $\rightarrow$ $4^2$ + $\frac{14\sqrt{74}}{37}^2$ = $CB^2$ $\Rightarrow$ $CB$ = $\frac{10\sqrt{74}}{37}$
Note that $\triangle ABC$ is a right triangle because the hypotenuse is the diameter of the circle. Solving for area using the bases $AC$ and $BC$ , we get the area of triangle $ABC$ to be $\boxed{\textbf{(D) } \frac{140}{37}}$ .

## Solution 5 (Coordinate Geo)
Drawing the picture, we realize that the equation for the line from A to E is $y=\frac{5x}{7}$ , and the equation for the circle is $(x-2)^2+y^2=4$ plugging in $\frac{5x}{7}$ for y we get $x(74x-196)=0$ so $x=\frac{98}{37}$ , that means $y = \frac{98}{37} \cdot \frac{5}{7} = \frac{70}{37}$
the height is $\frac{70}{37}$ and the base is $4$ , so the area is $\boxed{\textbf{(D) } \frac{140}{37}}$
-harsha12345

## Solution 6 (Coordinate bashing)
We draw out the diagram, and let the center of the circle be the origin. $A$ would then be $(0,-2)$ , and $B$ would be $(2,0)$ . We find that the equation of the line $AE$ is $\frac{5}{7}x + \frac{10}{7}$ . The equation of the circle is $x^2+y^2=4$ . We use substitution and bashing with the quadratic formula to get $x = \frac{24}{37}$ . From this, we get $y = \frac{70}{37}$ and get that the area is $\frac{70}{37}\cdot 4/2 = \boxed{\textbf{(D) } \frac{140}{37}}$ .
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
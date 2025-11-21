# 2014 AMC 10B Problem 22

## Problem

Eight semicircles line the inside of a square with side length 2 as shown. What is the radius of the circle tangent to all of these semicircles?

$\text{(A) } \dfrac{1+\sqrt2}4 \quad \text{(B) } \dfrac{\sqrt5-1}2 \quad \text{(C) } \dfrac{\sqrt3+1}4 \quad \text{(D) } \dfrac{2\sqrt3}5 \quad \text{(E) } \dfrac{\sqrt5}3$

[asy] scale(200); draw(scale(.5)*((-1,-1)--(1,-1)--(1,1)--(-1,1)--cycle)); path p = arc((.25,-.5),.25,0,180)--arc((-.25,-.5),.25,0,180); draw(p); p=rotate(90)*p; draw(p); p=rotate(90)*p; draw(p); p=rotate(90)*p; draw(p); draw(scale((sqrt(5)-1)/4)*unitcircle); [/asy]

## Solution
We connect the centers of the circle and one of the semicircles, then draw the perpendicular from the center of the middle circle to that side, as shown.
[asy] scale(200); draw(scale(.5)*((-1,-1)--(1,-1)--(1,1)--(-1,1)--cycle)); path p = arc((.25,-.5),.25,0,180)--arc((-.25,-.5),.25,0,180); draw(p); p=rotate(90)*p; draw(p); p=rotate(90)*p; draw(p); p=rotate(90)*p; draw(p); draw(scale((sqrt(5)-1)/4)*unitcircle); pair OO=(0,0); pair XX=(-.25,-.5); pair YY=(0,-.5); draw(YY--OO--XX--cycle,black+1bp); label("$\frac12$",.5*(XX+YY),S); label("$1$",.5*YY,E); [/asy]
We will start by creating an equation by the Pythagorean theorem: \[\sqrt{1^2 + \left(\frac12\right)^2} = \sqrt{\frac54} = \frac{\sqrt5}{2}.\]
Let's call $r$ as the radius of the circle that we want to find. We see that the hypotenuse of the bold right triangle is $\dfrac{1}{2}+r$ , and thus $r$ is $\boxed{\textbf{(B)} \frac{\sqrt{5}-1}{2}}$ .
-- LORD_ERTY09
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
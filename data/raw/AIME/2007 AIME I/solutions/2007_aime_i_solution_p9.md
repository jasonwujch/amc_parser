# 2007 AIME I Problem 9

## Problem

In right triangle $ABC$ with right angle $C$ , $CA = 30$ and $CB = 16$ . Its legs $CA$ and $CB$ are extended beyond $A$ and $B$ . Points $O_1$ and $O_2$ lie in the exterior of the triangle and are the centers of two circles with equal radii . The circle with center $O_1$ is tangent to the hypotenuse and to the extension of leg $CA$ , the circle with center $O_2$ is tangent to the hypotenuse and to the extension of leg $CB$ , and the circles are externally tangent to each other. The length of the radius either circle can be expressed as $p/q$ , where $p$ and $q$ are relatively prime positive integers . Find $p+q$ .

## Solutions

## Solution 1
Label the points as in the diagram above. If we draw $\overline{O_1A}$ and $\overline{O_2B}$ , we form two right triangles . As $\overline{AF}$ and $\overline{AD}$ are both tangents to the circle, we see that $\overline{O_1A}$ is an angle bisector . Thus, $\triangle AFO_1 \cong \triangle ADO_1$ . Call $x = AD = AF$ and $y = EB = BG$ . We know that $x + y + 2r = 34$ .
If we call $\angle CAB = \theta$ , then $\angle DAO_1 = \frac{180 - \theta}{2}$ . Apply the tangent half-angle formula ( $\tan \frac{\theta}{2} = \sqrt{\frac{1 - \cos \theta}{1 + \cos \theta}}$ ). We see that $\frac rx = \tan \frac{180 - \theta}{2} = \sqrt{\frac{1 - \cos (180 - \theta)}{1 + \cos (180 - \theta)}}$ $= \sqrt{\frac{1 + \cos \theta}{1 - \cos \theta}}$ . Also, $\cos \theta = \frac{30}{34} = \frac{15}{17}$ . Thus, $\frac rx = \sqrt{\frac{1 + \frac{15}{17}}{1 - \frac{15}{17}}}$ , and $x = \frac{r}{4}$ .
Similarly, we find that $y = r/\sqrt{\frac{1 + \frac{8}{17}}{1 - \frac{8}{17}}} = \frac{3r}{5}$ .
Therefore, $x + y + 2r = \frac{r}{4} + \frac{3r}{5} + 2r = \frac{57r}{20} = 34 \Longrightarrow r = \frac{680}{57}$ , and $p + q = 737$ .

## Solution 2
Use a similar solution to the aforementioned solution. Instead, call $\angle CAB = 2\theta$ , and then proceed by simplifying through identities. We see that $\frac rx = \tan \left(\frac{180 - 2\theta}{2}\right) = \tan (90 - \theta)$ . In terms of $r$ , we find that $x = \frac{r}{\cot \theta} = \frac{r\sin \theta}{\cos \theta}$ . Similarly, we find that $y = \frac{r \sin(45 - \theta)}{\cos (45 - \theta)}$ .
Substituting, we find that $r\left(\frac{\sin \theta}{\cos \theta} + \frac{\sin(45 - \theta)}{\cos (45 - \theta)} + 2\right) = 34$ . Under a common denominator, $r\left(\frac{\sin \theta \cos (45 - \theta) + \cos \theta \sin (45 - \theta)}{\cos \theta \cos (45 - \theta)} + 2\right) = 34$ . Trigonometric identities simplify this to $r\left(\frac{\sin\left((\theta) + (45 - \theta)\right)}{\frac 12 \left(\cos (\theta + 45 - \theta) + \cos (\theta - 45 + \theta) \right)} + 2\right) = 34$ . From here, it is possible to simplify:
Our answer is $34 \cdot \frac{20}{57} = \frac{680}{57}$ , and $p + q = 737$ .

## Solution 3
Let the point where CB's extension hits the circle be G, and the point where the hypotenuse hits that circle be E. Clearly $EB=GB$ . Let $EB=x$ . Draw the two perpendicular radii to G and E. Now we have a cyclic quadrilateral . Let the radius be length $r$ . We see that since the cosine of angle ABC is $\frac{15}{17}$ the cosine of angle EBG is $-\frac{15}{17}$ . Since the measure of the angle opposite to EBG is the complement of this one, its cosine is $\frac{15}{17}$ . Using the law of cosines, we see that $x^{2}+x^{2}+\frac{30x^{2}}{17}=r^{2}+r^{2}-\frac{30r^{2}}{17}$ This tells us that $r=4x$ .
Now look at the other end of the hypotenuse. Call the point where CA hits the circle F and the point where the hypotenuse hits the circle D. Draw the radii to F and D and we have cyclic quadrilaterals once more. Using the law of cosines again, we find that the length of our tangents is $2.4x$ . Note that if we connect the centers of the circles we have a rectangle with sidelengths 8x and 4x. So, $8x+2.4x+x=34$ . Solving we find that $4x=\frac{680}{57}$ so our answer is 737.

## Solution 4
By Pythagoras, $AB = 34$ . Let $I_{C}$ be the $C$ -excenter of triangle $ABC$ . Then the $C$ -exradius $r_{C}$ is given by $r_{C}= \frac{K}{s-c}= \frac{240}{40-34}= 40$ .
The circle with center $O_{1}$ is tangent to both $AB$ and $AC$ , which means that $O_{1}$ lies on the external angle bisector of $\angle BAC$ . Therefore, $O_{1}$ lies on $AI_{C}$ . Similarly, $O_{2}$ lies on $BI_{C}$ .
Let $r$ be the common radius of the circles with centers $O_{1}$ and $O_{2}$ . The distances from points $O_{1}$ and $O_{2}$ to $AB$ are both $r$ , so $O_{1}O_{2}$ is parallel to $AB$ , which means that triangles $I_{C}AB$ and $I_{C}O_{1}O_{2}$ are similar.
The distance from $I_{C}$ to $AB$ is $r_{C}= 40$ , so the distance from $I_{C}$ to $O_{1}O_{2}$ is $40-r$ . Therefore,
$\frac{40-r}{40}= \frac{O_{1}O_{2}}{AB}= \frac{2r}{34}\quad \Rightarrow \quad r = \frac{680}{57}$ .
Hence, the final answer is $680+57 = 737$ .

## Solution 5
Start with a scaled 16-30-34 triangle. Inscribe a circle. The height, $h,$ and radius, $r,$ are found via $A=\frac{1}{2}\times 16s\times 30s=\frac{1}{2}\times 34s\times h=\frac{1}{2}\times rp,$ where $p$ is the perimeter .
Cut the figure through the circle and perpendicular to the hypotenuse. Slide the two pieces in opposite directions along the hypotenuse until they are one diameter of the circle apart. Complete the two partial circles.
The linear dimensions of the new triangle are $\frac{46s}{34s}=\frac{23}{17}$ times the size of the original. The problem's 16-30-34 triangle sits above the circles. Equate heights and solve for $r=6s$ :
$r = 6s = \frac{680}{57}$
$\frac{240s}{17}\times\frac{23}{17} = \frac{240}{17}+12s$
$20s\times 23 = 20\times 17+s\times 17\times 17$
$s = \frac{340}{171}$
The answer is $737$ .

## Solution 6
Using homothety in the diagram above, as well as the auxiliary triangle, leads to the solution.

## Solution 7
A different approach is to plot the triangle on the Cartesian Plane with $C$ at $(0,0)$ , $A$ at $(0,30)$ , and $B$ at $(16,0)$ . We wish to find the coordinates of $O_1$ and $O_2$ in terms of the radius, which will be expressed as $r$ in the rest of this solution. When we know the coordinates, we will set the distance between the 2 points equal to $2r$ . All points $r$ units away from $\overline{AB}$ are on the line with slope $-\frac{15}{8}$ , and y-intercept $30+ \frac{17}{8} r$
$O_1$ will have x-coordinate $r$ and likewise $O_2$ will have y-coordinate $r$ plugging this into the equation for the line mentioned in the sentence above gives us:
$O_1 = \left(r,\frac14 r+30\right)$ and $O_2 = \left(\frac35 r+16,r\right)$
By the distance formula and the fact that the circles and tangent, we have: $\left(16-\frac25 r\right)^2 + \left(30-\frac34 r\right)^2 = (2r)^2$
which simplifies into the quadratic equation: $1311 r^2 + 23120 r - 462400 = 0$
And by the quadratic equation, the solutions are: $\frac{-23120 \pm 54400}{2622}$ The solution including the " $-$ " is extraneous so we have the radius equal to $\frac{31280}{2622}$
Which simplifies to $\frac{680}{57}$ . The sum of the numerator and the denominator is $\boxed{737}$

## Solution 8 (simple algebra)
It is known that $O_1O_2$ is parallel to AB. Thus, extending $O_1F$ and $GO_2$ to intersect at H yields similar triangles $O_1O_2H$ and BAC, so that $O_1O_2 = 2r$ , $O_1H = \frac{16r}{17}$ , and $HO_2 = \frac{30r}{17}$ . It should be noted that $O_2G = r$ . Also, FHGC is a rectangle, and so AF = $\frac{47r}{17} - 30$ and similarly for BG. Because tangents to a circle are equal, the hypotenuse can be expressed in terms of r: \[2r + \frac{47r}{17} - 30 + \frac{33r}{17} - 16 = 34\] Thus, r = $\frac{680}{57}$ , and the answer is $\boxed{737}.$
### Note
When drawing the diagram, it may seem that $H$ lies on circle $O_1$ , but it is actually not: $H$ lies inside of circle $O_1$ . We can see this from the similarity ratios: $\frac{O_1O_2}{BA}=\frac{HO_1}{CB}=\frac{HO_2}{CA}$ . Taking a look at the first equation ( $\tfrac{O_1O_2}{BA}=\tfrac{HO_1}{CB}$ ), $\frac{2r}{34}=\frac{HO_1}{16}$ which simplifies to $\frac r{17}=\frac{HO_1}{16}$ . Indeed, $HO_1$ does not equal $r$ , instead, $HO_1=\frac{16}{17}r$ .
~BakedPotato66

## Solution 9
Let the radius of the circle be $r$ . It can be seen that $\Delta FHO_{1}$ and $\Delta O_{2}GJ$ are similar to $\Delta ACB$ , and the length of the hypotenuses are $\frac{17}{8}r$ and $\frac {17}{15}r$ , respectively. Then, the entire length of $HJ$ is going to be $(\frac{17}{8}+\frac{17}{15}+2)r = \frac{631}{120}r$ . The length of the hypotenuse of $\Delta ACB$ is 34, so the length of the height to $AB$ is $\frac{16*30}{34} = \frac{240}{17}$ . Thus, the height to $\Delta HCJ$ is going to be $\frac{240}{17} + r$ . $\Delta HCJ$ is similar to $\Delta ACB$ so we have the following: $\frac{\frac{631}{120}r}{34} = \frac{\frac{240}{17} + r}{\frac{240}{17}}$ . Cross multiplying and simplifying, we get that $r = \frac{680}{57}$ so the answer is $\boxed{737}$ . ~Leonard_my_dude~

## Video Solution
2007 AIME I #9
MathProblemSolvingSkills.com
Exradius (Solution 4)
These problems are copyrighted © by the Mathematical Association of America.
# 2024 AMC 10A Problem 22

## Problem

Let $\mathcal K$ be the kite formed by joining two right triangles with legs $1$ and $\sqrt3$ along a common hypotenuse. Eight copies of $\mathcal K$ are used to form the polygon shown below. What is the area of triangle $\Delta ABC$ ?

$\textbf{(A) }2+3\sqrt3\qquad\textbf{(B) }\dfrac92\sqrt3\qquad\textbf{(C) }\dfrac{10+8\sqrt3}{3}\qquad\textbf{(D) }8\qquad\textbf{(E) }5\sqrt3$

## Solution 1
First, we should find the length of $AB$ . In order to do this, as we see in the diagram, it can be split into 4 equal sections. Since diagram $K$ shows us that it is made up of two ${30,60,90}$ triangles, then the triangle outlined in red must be a $30,60,90$ triangle, as ${30+30=60}$ , and the two lines are perpendicular (it is proveable, but during competition, it is best to assume this is true, as the diagram is drawn pretty well to scale). Also, since we know the length of the longest side of the red triangle is ${\sqrt3}$ , then the side we are looking for, which is outlined in blue, must be $\frac{3}{2}$ by the ${1,\sqrt3, 2}$ relationship of ${30,60,90}$ triangles. Therefore $AB$ , which is the base of the triangle we are looking, for must be $6.$
Now all we have to do is find the height. We can split the height into 2 sections, the green and the light green. The green section must be ${\sqrt3}$ , as $K$ shows us. Also, the light green section must be equal to ${\frac{\sqrt3}{2}}$ , as in the previous paragraph, the triangle outlined in red is $30,60,90$ . Then, the green section, which is the height, must be ${\sqrt3}+{\frac{\sqrt3}{2}}$ , which is just ${\frac{3\sqrt3}{2}}$ .
Then the area of the triangle must be ${\frac{1}{2}}\cdot {b} \cdot {h}$ , which is just $\boxed{ \textbf{(B) } \frac{9}{2} \sqrt3}.$
Simple Proof of the red triangle having $30^\circ$ , $60^\circ$ , and $90^\circ$ angles:
In the small kite illustrated in the problem, we can see that the two angles on the left side add up to $60^\circ$ (this is easily noticeable if you look hard enough.) So, the angle that the arrow is pointing to is $60^\circ$ . Since another angle in the red triangle is obviously $90^\circ$ , the portion of the angle that is in the red triangle and at point A is $180^\circ - 90^\circ - 60^\circ = 30^\circ$ . Therefore, the red triangle is a $30^\circ$ $60^\circ$ $90^\circ$ triangle.
~Solution by HappySharks ~Minor Edits by mathkiddus ~Simple Red Triangle $30^\circ$ $60^\circ$ $90^\circ$ Proof by ckevhl78

## Solution 2
Let $\mathcal K$ be quadrilateral $MNOP$ . Drawing line $MO$ splits the triangle into $\Delta MNO$ . Drawing the altitude from $N$ to point $Q$ on line $MO$ , we know $NQ$ is $\frac{\sqrt{3}}{2}$ , $MQ$ is $\frac{3}{2}$ , and $QO$ is $\frac{1}{2}$ .
Due to the many similarities present, we can find that $AB$ is $4(MQ)$ , and the height of $\Delta ABC$ is $NQ+MN$
$AB$ is $4(\frac{3}{2})=6$ and the height of $\Delta ABC$ is $\sqrt3+\frac{\sqrt{3}}{2}=\frac{3\sqrt{3}}{2}$ .
Solving for the area of $\Delta ABC$ gives $6\cdot\frac{3\sqrt{3}}{2}\cdot\frac{1}{2}$ which is $\boxed{\textbf{(B) }\dfrac92\sqrt3}$
~9897 (latex beginner here)
~i_am_suk_at_math(very minor latex edits)

## Solution 3
Let's start by looking at kite $\mathcal K$ . We can quickly deduce based off of the side lengths that the kite can be split into two $30-60-90$ triangles. Going back to the triangle $\triangle ABC$ , focus on side $AB$ . There are $4$ kites, they are all either reflected over the line $AB$ or a line perpendicular to $AB$ , meaning the length of $AB$ can be split up into 4 equal parts.
Pick out the bottom-left kite, and we can observe that the kite and the triangle formed by the intersection of the kite and $\Delta ABC$ share a $60$ degree angle. (this was deduced from the $30-60-90$ triangles in the kite) The line AB and the right side of the kite are perpendicular, forming a $90^{\circ}$ angle. Because that is also a $30-60-90$ triangle with a hypotenuse of $\sqrt3$ , so we find the length of AB to be $4*3/2$ , which is $6$ .
Then, we can drop an altitude from $C$ to $AB$ . We know that will be equivalent to the sum of the longer side of the kite and the shorter side of the triangle formed by the intersection of the kite and $\Delta ABC$ . (Look at the line formed on the left of $C$ that drops down to $AB$ if you are confused) We already have those values from the $30-60-90$ triangles, so we can just plug it into the triangle area formula, $bh/2$ . We get \[6\cdot\dfrac{\sqrt3+\frac{\sqrt3}{2}}{2}\rightarrow3\cdot(\sqrt3+\dfrac{\sqrt3}{2})\rightarrow3\cdot\dfrac{\sqrt3}{2}\rightarrow\boxed{\textbf{(B) }\dfrac92\sqrt3}\]
~YTH
~WIP (Header)
~Tacos_are_yummy_1 ( $\LaTeX$ & Formatting)

## Solution 4
~mathboy282

## Solution 5
Let the point of intersection of $AB$ and the kite with $A$ as vertex be $D$ .
Let the left kite with $C$ as a vertex touch the kite with $A$ as vertex at point $E$ .
$\triangle ADE$ is a $30-60-90$ so $AD = \frac{3}{2}$ and $DE = \frac{\sqrt3}{2}$ .
So, $AB = 4\cdot AD = 6$ and $CD=CE+DE= \frac{3\sqrt3}{2}$ , and the area is $\frac12\cdot AB \cdot CD = \boxed{ \textbf{(B) } \frac{9}{2} \sqrt3}.$
~Mintylemon66

## Solution 6(trig bash)
\[\textbf{Step 1:}\] As stated in the solutions above we can easily find that $AB$ is split into $4$ equal parts, so we have $AB=4(AE)$ We can calculate $AE,$ by using $AA$ similarity to find $\triangle{ADE}$ is a $30-60-90$ triangle, therefore we have $AD=\sqrt{3},DE=\frac{\sqrt{3}}{2},$ and finally $AE=\frac{3}{2},$ therefore $AB=4(AE)=4(\frac{3}{2})=6.$ Similarly we have $CF$ is congruent to $FG,$ therefore $CF=FG=1.$ Next we have $AD$ is congruent to $DF$ telling us $AF=AD+DF=2(AD)=2\sqrt{3}.$ Noticing $\triangle{CFA}$ is right, we apply Pythagorean theorem to $\triangle{CFA}$ to find \[AC^2=CF^2+AF^2\] \[AC^2=(1)^2+(2\sqrt{3})^2=13\] \[AC=\sqrt{13}.\] \[\textbf{Step 2:}\] Next we would like to calculate CJ, As said before $CF=FG=1$ so $CG=2.$ We know the inscribed angle between CG and GJ is $60\cdot2=120,$ and finally we know $GJ=1.$ So we apply LoC on triangle CGJ in order to find CJ. \[CJ^2=CG^2+GJ^2-2\cdot{CG}\cdot{GJ}\cdot\cos{120^{\circ}}.\] \[CJ^2=2^2+1^2-2\cdot2\cdot1\cdot\cos{120^{\circ}}.\] \[CJ^2=5-2\cdot2\cdot\frac{-1}{2}=7.\] \[CJ=\sqrt{7}.\] \[\textbf{Step 3:}\] Now since we have all side lengths of $\triangle{CAJ}$ we can find $\cos{\angle{CAJ}}.$ Applying LoC again on $\triangle{CAJ}$ we have, \[CJ^2=CA^2+AJ^2-2\cdot{CA}\cdot{AJ}\cdot\cos{\angle{CAJ}}.\] \[{\sqrt{7}}^2={\sqrt{13}}^2+{3}^2-2\cdot3\cdot{\sqrt{13}}\cdot\cos{\angle{CAJ}}.\] \[7=22-6{\sqrt{13}}\cdot\cos{\angle{CAJ}}.\] \[\frac{-15}{-6{\sqrt{13}}}=\frac{5\sqrt{13}}{26}=\cos{\angle{CAJ}}.\] \[\textbf{Step 4:}\] We can solve for the area using the sin area formula which is $\frac{1}{2}\cdot{AC}\cdot{AB}\sin{\angle{CAJ}}.$ To find $\sin{\angle{CAJ}}$ we use the well known fact $\sin^2{x}+\cos^2{x}=1.$ So we find, \[\sin^2{\angle{CAJ}}+\cos^2{\angle{CAJ}}=1.\] \[\sin^2{\angle{CAJ}}+(\frac{5\sqrt{13}}{26})^2=1.\] \[\sin^2{\angle{CAJ}}+\frac{25}{52}=1.\] \[\sin^2{\angle{CAJ}}=\frac{27}{52}.\] \[\sin{\angle{CAJ}}=\frac{3\sqrt{39}}{26}.\] Finally to wrap up we can find the area of $\triangle{ABC}$ using the sin area formula, \[[ABC]=\frac{1}{2}\cdot{AC}\cdot{AB}\cdot\sin{\angle{CAJ}}.\] \[[ABC]=\frac{1}{2}\cdot\sqrt{13}\cdot{6}\cdot\frac{3\sqrt{39}}{26}=\frac{9\sqrt{3}}{2}.\] Therefore our answer is $\boxed{\textbf{(B) } \frac{9}{2} \sqrt3.}$
~ mathkiddus

## Solution 7(coordinate bash)
Assume we set A as $(0, 0)$ . The line AB can be split into 4 equal sections, easily noticed in the picture. Not that the first equal section, starting at A. When we follow the line AB, we see that it's a right angle, noticing its a 30, 60, 90 triangle. Because the hypothenuse of that triangle is $\sqrt{3}$ . Using the 30, 60, 90 ratio, we see that one of those equal sections is 3/2. Making the coordinate of B, $(6, 0)$ .
Now, we must find the coordinate of C. Note that when we drop C down to the perpindicular of AB, there is a $x$ component to C, and a $y$ component to C. To find the X component, we see that it's one equal section found before as 3/2, and another section equal to 1, given in the question, making it $x$ = 5/2. The Y component can be seen as another two sections. The two green sections marked in solution 1. One is $\sqrt{3}/2$ due to the same 30 60 90 triangle we found in the first part of the solution. And the other part is $\sqrt{3}$ , given in the question. Making $y$ = $\frac{3}{2} \sqrt3$ . So we see that C = ( $5/2$ , $\frac{3}{2} \sqrt3$ )
Using shoelace theorem, we get to get $\boxed{ \textbf{(B) } \frac{9}{2} \sqrt3}.$
sorry for no diagrams D:
-marcus
Alternate way to calculate area: Notice once you get the y-coordinate of C, you can realize it's just the height of the triangle. So the area would be $\frac{1}{2}$ times base times height where the base is ${6}$ and the height is $\frac{3}{2}$ $\sqrt{3}$ . ~ilikemath247365
### Sidenote
The figure made of kites was in fact, an einstein tile (also known as the Hat). The einstein tile was discovered in November of 2022 by a retired printing systems engineer in England. It comes from the German word for one stone, and has been proven to infinitely tile a plane aperiodically, quite a unique property - it took decades for mathematicians to find a periodical tilings of smaller and smaller numbers, with Penrose discovering a method using only 2 tilings in 1974. ~LeonQS

## Solution 8
When looking at the figure, we can see that the corner is shaped irregularly. This can make a regular hexagon with side length 2. Then, you would find the height of the triangle using the hexagon, which would get you \(\frac{1}{2} \times 6 \times \frac{3\sqrt{3}}{2}\), which is $\boxed{ \textbf{(B) } \frac{9}{2} \sqrt3}.$
~Mathman645

## Solution 9
The triangle with side lengths $1$ , $\sqrt3$ , and $2$ will be referenced as "half kite" in this solution
First, notice how the altitude is composed of three half kites.
After finding the altitude of a half kite, which is $\frac{\sqrt3}{2}$ , we can figure out that the altitude of triangle ABC is $\frac{3\sqrt3}{2}$
Now we take a look at the base. Notice how we can create two half kites, each with base $2$ . Adding that to the two $1$ unit segments and the base will have length 6.
Using the area formula for a triangle, we get $6\cdot\frac{3\sqrt{3}}{2}\cdot\frac{1}{2}$ which is $\boxed{\textbf{(B) }\dfrac92\sqrt3}$
~SpectralScholar

## Video Solution by grogg007 (Under 3 Minutes ⏩)
https://www.youtube.com/watch?v=hNUJSdrn1V0

## Video Solution by Power Solve
https://www.youtube.com/watch?v=bxC_UENbmNk

## Video Solution by Pi Academy (Fast and Easy⚡️🚀)
https://youtu.be/hcpej1uRYu4?si=-DekbEWkAg_c6nsg

## Video Solution by Innovative Minds
https://www.youtube.com/watch?v=bhC58BB3kJA
~i_am_suk_at_math_2

## Video Solution by SpreadTheMathLove
https://youtu.be/UqFK6iLzlEw?si=pWR8qSn_Byj-H2Zq

## Video Solution by Just Math⚡
https://www.youtube.com/watch?v=OjdLNjiO5Qw

## Video solution by TheNeuralMathAcademy
https://www.youtube.com/watch?v=4b_YLnyegtw&t=4859s
### See Also
- AMC 10
- AMC 10 Problems and Solutions
- Mathematics competitions
- Mathematics competition resources
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
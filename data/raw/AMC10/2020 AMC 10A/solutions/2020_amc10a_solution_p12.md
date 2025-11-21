# 2020 AMC 10A Problem 12

## Problem

Triangle $AMC$ is isosceles with $AM = AC$ . Medians $\overline{MV}$ and $\overline{CU}$ are perpendicular to each other, and $MV=CU=12$ . What is the area of $\triangle AMC?$

[asy] draw((-4,0)--(4,0)--(0,12)--cycle); draw((-2,6)--(4,0)); draw((2,6)--(-4,0)); draw((-2,6)--(2,6)); label("M", (-4,0), W); label("C", (4,0), E); label("A", (0, 12), N); label("V", (2, 6), NE); label("U", (-2, 6), NW); label("P", (0, 3.6), S); [/asy]

$\textbf{(A) } 48 \qquad \textbf{(B) } 72 \qquad \textbf{(C) } 96 \qquad \textbf{(D) } 144 \qquad \textbf{(E) } 192$

## Solution 1
Since quadrilateral $UVCM$ has perpendicular diagonals, its area can be found as half of the product of the length of the diagonals. Also note that $\triangle AUV$ has $\frac 14$ the area of triangle $AMC$ by similarity, so $[UVCM]=\frac 34\cdot [AMC].$ Thus, \[\frac 12 \cdot 12\cdot 12=\frac 34 \cdot [AMC]\] \[72=\frac 34\cdot [AMC]\] \[[AMC]=96\rightarrow \boxed{\textbf{(C)}}.\]
Note: We know that since $AU$ is the median $AU$ divided by $AM$ is $1/2$ . Since triangle $AUV$ is similar to triangle $AMC$ , and by a factor of $1/2$ , then every sidelength of $AMC$ must also be scaled by a factor of $1/2$ to get $AUV$ . The base and height are all scaled by $1/2$ , so then the ratio is $1/2 \cdot 1/2$ .
~<B+ converted "Note" into proper LaTeX as it was in plain text previously when it was required to convert into LaTeX by writer of the "Note"

## Solution 2 (Trapezoid)
[asy] draw((-4,0)--(4,0)--(0,12)--cycle); draw((-2,6)--(4,0)); draw((2,6)--(-4,0)); draw((-2,6)--(2,6)); label("M", (-4,0), W); label("C", (4,0), E); label("A", (0, 12), N); label("V", (2, 6), NE); label("U", (-2, 6), NW); label("P", (0, 3.6), S); [/asy]
We know that $\triangle AUV \sim \triangle AMC$ , and since the ratios of its sides are $\frac{1}{2}$ , the ratio of of their areas is $\left(\frac{1}{2}\right)^2=\frac{1}{4}$ .
If $\triangle AUV$ is $\frac{1}{4}$ the area of $\triangle AMC$ , then trapezoid $MUVC$ is $\frac{3}{4}$ the area of $\triangle AMC$ .
Let's call the intersection of $\overline{UC}$ and $\overline{MV}$ $P$ . Let $\overline{UP}=x$ . Then $\overline{PC}=12-x$ . Since $\overline{UC} \perp \overline{MV}$ , $\overline{UP}$ and $\overline{CP}$ are heights of triangles $\triangle MUV$ and $\triangle MCV$ , respectively. Both of these triangles have base $12$ .
Area of $\triangle MUV = \frac{x\cdot12}{2}=6x$
Area of $\triangle MCV = \frac{(12-x)\cdot12}{2}=72-6x$
Adding these two gives us the area of trapezoid $MUVC$ , which is $6x+(72-6x)=72$ .
This is $\frac{3}{4}$ of the triangle, so the area of the triangle is $\frac{4}{3}\cdot{72}=\boxed{\textbf{(C) } 96}$ ~quacker88, diagram by programjames1

## Solution 3 (Medians)
Draw median $\overline{AB}$ . [asy] draw((-4,0)--(4,0)--(0,12)--cycle); draw((-2,6)--(4,0)); draw((2,6)--(-4,0)); draw((0,12)--(0,0)); label("M", (-4,0), W); label("C", (4,0), E); label("A", (0, 12), N); label("V", (2, 6), NE); label("U", (-2, 6), NW); label("P", (0.5, 4), E); label("B", (0, 0), S); [/asy]
Since we know that all medians of a triangle intersect at the centroid, we know that $\overline{AB}$ passes through point $P$ . We also know that medians of a triangle divide each other into segments of ratio $2:1$ . Knowing this, we can see that $\overline{PC}:\overline{UP}=2:1$ , and since the two segments sum to $12$ , $\overline{PC}$ and $\overline{UP}$ are $8$ and $4$ , respectively.
Finally knowing that the medians divide the triangle into $6$ sections of equal area, finding the area of $\triangle PUM$ is enough. $\overline{PC} = \overline{MP} = 8$ .
The area of $\triangle PUM = \frac{4\cdot8}{2}=16$ . Multiplying this by $6$ gives us $6\cdot16=\boxed{\textbf{(C) }96}$
~quacker88

## Solution 4 (Triangles)
[asy] draw((-4,0)--(4,0)--(0,12)--cycle); draw((-2,6)--(4,0)); draw((2,6)--(-4,0)); draw((-2,6)--(2,6)); label("M", (-4,0), W); label("C", (4,0), E); label("A", (0, 12), N); label("V", (2, 6), NE); label("U", (-2, 6), NW); label("P", (0, 3.6), S); [/asy] We know that $AU = UM$ , $AV = VC$ , so $UV = \frac{1}{2} MC$ .
As $\angle UPM = \angle VPC = 90$ , we can see that $\triangle UPM \cong \triangle VPC$ and $\triangle UVP \sim \triangle MPC$ with a side ratio of $1 : 2$ .
So $UP = VP = 4$ , $MP = PC = 8$ .
With that, we can see that $[\triangle UPM] = 16$ , and the area of trapezoid $MUVC$ is 72.
As said in solution 1, $[\triangle AMC] = 72 / \frac{3}{4} = \boxed{\textbf{(C) } 96}$ .
-QuadraticFunctions, solution 1 by ???

## Solution 5 (Only Pythagorean Theorem)
[asy] draw((-4,0)--(4,0)--(0,12)--cycle); draw((-2,6)--(4,0)); draw((2,6)--(-4,0)); draw((0,12)--(0,0)); label("M", (-4,0), W); label("C", (4,0), E); label("A", (0, 12), N); label("V", (2, 6), NE); label("U", (-2, 6), NW); label("P", (0.5, 4), E); label("B", (0, 0), S); [/asy]
Let $AB$ be the height. Since medians divide each other into a $2:1$ ratio, and the medians have length 12, we have $PC=MP=8$ and $UP=VP=4$ . From right triangle $\triangle{MUP}$ , \[MU^2=MP^2+UP^2=8^2+4^2=80,\] so $MU=\sqrt{80}=4\sqrt{5}$ . Since $CU$ is a median, $AM=8\sqrt{5}$ . From right triangle $\triangle{MPC}$ , \[MC^2=MP^2+PC^2=8^2+8^2=128,\] which implies $MC=\sqrt{128}=8\sqrt{2}$ . By symmetry $MB=\dfrac{8\sqrt{2}}{2}=4\sqrt{2}$ .
Applying the Pythagorean Theorem to right triangle $\triangle{MAB}$ gives $AB^2=AM^2-MB^2=8\sqrt{5}^2-4\sqrt{2}^2=288$ , so $AB=\sqrt{288}=12\sqrt{2}$ . Then the area of $\triangle{AMC}$ is \[\dfrac{AB \cdot MC}{2}=\dfrac{8\sqrt{2} \cdot 12\sqrt{2}}{2}=\dfrac{96 \cdot 2}{2}=\boxed{\textbf{(C) }96}\]

## Solution 6 (Drawing)
By similarity, the area of $AUV$ is equal to $\frac{1}{4}$ .
The area of $UVCM$ is equal to 72.
Assuming the total area of the triangle is S, the equation will be : $\frac{3}{4}$ S = 72.
S = $\boxed{\textbf{(C) }96}$

## Solution 7(fastest)
Given a triangle with perpendicular medians with lengths $x$ and $y$ , the area will be $\frac{2xy}{3}=\boxed{\textbf{(C) }96}$ .

## Solution 8
Connect the line segment $UV$ and it's easy to see quadrilateral $UVMC$ has an area of the product of its diagonals divided by $2$ which is $72$ . Now, solving for triangle $AUV$ could be an option, but the drawing shows the area of $AUV$ will be less than the quadrilateral meaning the the area of $AMC$ is less than $72*2$ but greater than $72$ , leaving only one possible answer choice, $\boxed{\textbf{(C) } 96}$ .
-Rohan S.

## Solution 9
[asy] draw((-4,0)--(4,0)--(0,12)--cycle); draw((-2,6)--(4,0)); draw((2,6)--(-4,0)); draw((0,12)--(0,0)); label("M", (-4,0), W); label("C", (4,0), E); label("A", (0, 12), N); label("V", (2, 6), NE); label("U", (-2, 6), NW); label("P", (0.5, 4), E); label("B", (0, 0), S); [/asy]
Connect $AP$ , and let $B$ be the point where $AP$ intersects $MC$ . $MB=CB$ because all medians of a triangle intersect at one point, which in this case is $P$ . $MP:PV=2:1$ because the point at which all medians intersect divides the medians into segments of ratio $2:1$ , so $MP=8$ and similarly $CP=8$ . We apply the Pythagorean Theorem to triangle $MPC$ and get $MC=\sqrt{128}=8\sqrt{2}$ . The area of triangle $MPC$ is $\dfrac{MP\cdot CP}{2}=32$ , and that must equal to $\dfrac{MC\cdot BP}{2}$ , so $BP=\dfrac{8}{\sqrt{2}}=4\cdot\sqrt{2}$ . $BP=\dfrac{1}{3}BA$ , so $BA=12\sqrt{2}$ . The area of triangle $AMC$ is equal to $\dfrac{MC\cdot BA}{2}=\dfrac{8 \cdot \sqrt{2} \cdot 12 \cdot \sqrt{2}}{2}=\boxed{\textbf{(C)}\ 96}$ .
-SmileKat32

## Solution 10 (High IQ)
$[\square MUVC] = 72$ . Let intersection of line $AP$ and base $MC$ be $B$ \[[AUV]=[MUB]=[UVB]=[BVC] \implies \left[\frac{\triangle AMC}{4}\right] = \left[\frac{\square MUVC}{3}\right] \implies [AMC] = \boxed{\textbf{(C)}\ 96}\]
~herobrine-india

## Solution 11 (Kite)
[asy] draw((-4,0)--(4,0)--(0,12)--cycle); draw((-2,6)--(4,0)); draw((2,6)--(-4,0)); draw((-2,6)--(2,6)); label("M", (-4,0), W); label("C", (4,0), E); label("A", (0, 12), N); label("V", (2, 6), NE); label("U", (-2, 6), NW); label("P", (0, 3.6), S); [/asy]
Since $\overline{MV}$ and $\overline{CU}$ intersect at a right angle, this means $MUVC$ is a kite. Hence, the area of this kite is $\frac{12 \cdot 12}{2} = 72$ .
Also, notice that $\triangle AUV \sim \triangle AMC$ by AAA Similarity. Since the ratios of its sides is $\frac{1}{2}$ , the ratios of the area is $\left(\frac{1}{2}\right)^2=\frac{1}{4}$ . Therefore,
\[[AMC] = [MUVC] + \frac{1}{4} \cdot [AMC]\]
Simplifying gives us $\frac{3}{4} \cdot [AMC] = 72$ , so $[AMC] = 72 \cdot \frac{4}{3} = \boxed{\textbf{(C)}\ 96}$
~MrThinker

## Solution 12 (Educated guessing)
Horizontally translate line $\overline{UC}$ until point $U$ is at point $V$ , with $C$ subsequently at $C'$ , and then connect up $C'$ and $C$ to create $\triangle MVC'$ , which is a right triangle.
[asy] draw((-4,0)--(4,0)--(0,12)--cycle); draw((-2,6)--(4,0)); draw((2,6)--(-4,0)); draw((-2,6)--(2,6)); draw((2,6)--(8,0)); draw((4,0)--(8,0)); label("M", (-4,0), W); label("C", (4,0), S); label("A", (0, 12), N); label("V", (2, 6), NE); label("U", (-2, 6), NW); label("P", (0, 3.6), S); label("C'", (8,0), E); [/asy]
Notice that $\triangle MVC'$ = $12 \cdot 12 \cdot \frac{1}{2} = 72$ , and $\triangle MVC'$ = $\triangle MVC + \triangle MUV$ (since the latter has the same base and height as the sub-triangle $\triangle CVC'$ inside $\triangle MVC'$ ).
From this, we can deduce that $\textbf{(B)}$ cannot be true, since an incomplete part of $\triangle AMC$ is equal to it. We can also deduce that $\textbf{(D)}$ also cannot be true, since the unknown triangle $\triangle AUV = \triangle MUV$ , and $\triangle MUV = \triangle CVC' < \triangle MVC'$ . Therefore, the answer must be between $72$ and $144$ , leaving $\boxed{\textbf{(C)}\ 96}$ as the only possible correct answer.
~DifrractSliver

## Video Solution 1
Education, The Study of Everything
https://youtu.be/0TslJ3aDXac

## Video Solution by TheBeautyofMath
https://youtu.be/ZGwAasE32Y4
~IceMatrix

## Video Solution 3
https://youtu.be/7ZvKOYuwSnE
~savannahsolver

## Video Solution 4 by OmegaLearn
https://youtu.be/4_x1sgcQCp4?t=2067
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
# 2021 AIME I Problem 2

## Problem

In the diagram below, $ABCD$ is a rectangle with side lengths $AB=3$ and $BC=11$ , and $AECF$ is a rectangle with side lengths $AF=7$ and $FC=9,$ as shown. The area of the shaded region common to the interiors of both rectangles is $\frac mn$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ . [asy] pair A, B, C, D, E, F; A=(0,3); B=(0,0); C=(11,0); D=(11,3); E=foot(C, A, (9/4,0)); F=foot(A, C, (35/4,3)); draw(A--B--C--D--cycle); draw(A--E--C--F--cycle); filldraw(A--(9/4,0)--C--(35/4,3)--cycle,gray*0.5+0.5*lightgray); dot(A^^B^^C^^D^^E^^F); label("$A$", A, W); label("$B$", B, W); label("$C$", C, (1,0)); label("$D$", D, (1,0)); label("$F$", F, N); label("$E$", E, S); [/asy]

## Solution 1 (Similar Triangles)
Let $G$ be the intersection of $AD$ and $FC$ . From vertical angles, we know that $\angle FGA= \angle DGC$ . Also, because we are given that $ABCD$ and $AFCE$ are rectangles, we know that $\angle AFG= \angle CDG=90 ^{\circ}$ . Therefore, by AA similarity, we know that $\triangle AFG\sim\triangle CDG$ .
Let $AG=x$ . Then, we have $DG=11-x$ . By similar triangles, we know that $FG=\frac{7}{3}(11-x)$ and $CG=\frac{3}{7}x$ . We have $\frac{7}{3}(11-x)+\frac{3}{7}x=FC=9$ .
Solving for $x$ , we have $x=\frac{35}{4}$ . The area of the shaded region is just $3\cdot \frac{35}{4}=\frac{105}{4}$ .
Thus, the answer is $105+4=\framebox{109}$ .
~yuanyuanC

## Solution 2 (Similar Triangles)
Again, let the intersection of $AE$ and $BC$ be $G$ . By AA similarity, $\triangle AFG \sim \triangle CDG$ with a $\frac{7}{3}$ ratio. Define $x$ as $\frac{[CDG]}{9}$ . Because of similar triangles, $[AFG] = 49x$ . Using $ABCD$ , the area of the parallelogram is $33-18x$ . Using $AECF$ , the area of the parallelogram is $63-98x$ . These equations are equal, so we can solve for $x$ and obtain $x = \frac{3}{8}$ . Thus, $18x = \frac{27}{4}$ , so the area of the parallelogram is $33 - \frac{27}{4} = \frac{105}{4}$ .
Finally, the answer is $105+4=\boxed{109}$ .
~mathboy100

## Solution 3 (Pythagorean Theorem)
Let the intersection of $AE$ and $BC$ be $G$ , and let $BG=x$ , so $CG=11-x$ .
By the Pythagorean theorem, ${AG}^2={AB}^2+{BG}^2$ , so $AG=\sqrt{x^2+9}$ , and thus $EG=9-\sqrt{x^2+9}$ .
By the Pythagorean theorem again, ${CG}^2={EG}^2+{CE}^2$ : \[11-x=\sqrt{7^2+(9-\sqrt{x^2+9})^2}.\]
Solving, we get $x=\frac{9}{4}$ , so the area of the parallelogram is $3\cdot\left(11-\frac{9}{4}\right)=\frac{105}{4}$ , and $105+4=\framebox{109}$ .
~JulianaL25

## Solution 4 (Pythagorean Theorem)
Let $P = AD \cap FC$ , and $K = AE \cap BC$ . Also let $AP = x$ .
$CK$ also has to be $x$ by parallelogram properties. Then $PD$ and $BK$ must be $11-x$ because the sum of the segments has to be $11$ .
We can easily solve for $PC$ by the Pythagorean Theorem: \begin{align*} DC^2 + PD^2 &= PC^2\\ 9 + (11-x)^2 &= PC^2 \end{align*} It follows shortly that $PC = \sqrt{x^2-22x+30}$ .
Also, $FC = 9$ , and $FP + PC = 9$ . We can then say that $PC = \sqrt{x^2-22x+30}$ , so $FP = 9 - \sqrt{x^2-22x+30}$ .
Now we can apply the Pythagorean Theorem to $\triangle AFP$ . \begin{align*} AF^2 + FP^2 = AP^2\\ 49 + \left(9 - \sqrt{x^2-22x+30}\right)^2 = x^2 \end{align*}
This simplifies (not-as-shortly) to $x = \dfrac{35}{4}$ . Now we have to solve for the area of $APCK$ . We know that the height is $3$ because the height of the parallelogram is the same as the height of the smaller rectangle.
From the area of a parallelogram (we know that the base is $\dfrac{35}{4}$ and the height is $3$ ), it is clear that the area is $\dfrac{105}{4}$ , giving an answer of $\boxed{109}$ .
~ishanvannadil2008 (Solution Sketch)
~Tuatara (Rephrasing and $\LaTeX$ )

## Solution 5 (Coordinate Geometry)
Suppose $B=(0,0).$ It follows that $A=(0,3),C=(11,0),$ and $D=(11,3).$
Since $AECF$ is a rectangle, we have $AE=FC=9$ and $EC=AF=7.$ The equation of the circle with center $A$ and radius $\overline{AE}$ is $x^2+(y-3)^2=81,$ and the equation of the circle with center $C$ and radius $\overline{CE}$ is $(x-11)^2+y^2=49.$
We now have a system of two equations with two variables. Expanding and rearranging respectively give \begin{align*} x^2+y^2-6y&=72, &(1) \\ x^2+y^2-22x&=-72. &(2) \end{align*} Subtracting $(2)$ from $(1),$ we obtain $22x-6y=144.$ Simplifying and rearranging produce \[x=\frac{3y+72}{11}. \hspace{34.5mm} (*)\] Substituting $(*)$ into $(1)$ gives \[\left(\frac{3y+72}{11}\right)^2+y^2-6y=72,\] which is a quadratic of $y.$ We clear fractions by multiplying both sides by $11^2=121,$ then solve by factoring: \begin{align*} \left(3y+72\right)^2+121y^2-726y&=8712 \\ \left(9y^2+432y+5184\right)+121y^2-726y&=8712 \\ 130y^2-294y-3528&=0 \\ 2(5y+21)(13y-84)&=0 \\ y&=-\frac{21}{5},\frac{84}{13}. \end{align*} Since $E$ is in Quadrant IV, we have $E=\left(\frac{3\left(-\frac{21}{5}\right)+72}{11},-\frac{21}{5}\right)=\left(\frac{27}{5},-\frac{21}{5}\right).$ It follows that the equation of $\overleftrightarrow{AE}$ is $y=-\frac{4}{3}x+3.$
Let $G$ be the intersection of $\overline{AD}$ and $\overline{FC},$ and $H$ be the intersection of $\overline{AE}$ and $\overline{BC}.$ Since $H$ is the $x$ -intercept of $\overleftrightarrow{AE},$ we get $H=\left(\frac94,0\right).$
By symmetry, quadrilateral $AGCH$ is a parallelogram. Its area is $HC\cdot AB=\left(11-\frac94\right)\cdot3=\frac{105}{4},$ from which the requested sum is $105+4=\boxed{109}.$
~MRENTHUSIASM

## Solution 6 (Trigonometry)
Let the intersection of $AE$ and $BC$ be $G$ . It is useful to find $\tan(\angle DAE)$ , because $\tan(\angle DAE)=\frac{3}{BG}$ and $\frac{3}{\tan(\angle DAE)}=BG$ . From there, subtracting the areas of the two triangles from the larger rectangle, we get Area = $33-3BG=33-\frac{9}{\tan(\angle DAE)}$ .
let $\angle CAD = \alpha$ . Let $\angle CAE = \beta$ . Note, $\alpha+\beta=\angle DAE$ .
$\alpha=\tan^{-1}\left(\frac{3}{11}\right)$
$\beta=\tan^{-1}\left(\frac{7}{9}\right)$
$\tan(\angle DAE) = \tan\left(\tan^{-1}\left(\frac{3}{11}\right)+\tan^{-1}\left(\frac{7}{9}\right)\right) = \frac{\frac{3}{11}+\frac{7}{9}}{1-\frac{3}{11}\cdot\frac{7}{9}} = \frac{\frac{104}{99}}{\frac{78}{99}} = \frac{4}{3}$
$\mathrm{Area}=33-\frac{9}{\frac{4}{3}} = 33-\frac{27}{4 } = \frac{105}{4}$ . The answer is $105+4=\boxed{109}$ .
~twotothetenthis1024

## Video Solution by Punxsutawney Phil
https://youtube.com/watch?v=H17E9n2nIyY&t=289s

## Video Solution
https://youtu.be/M3DsERqhiDk?t=275

## Video Solution by Steven Chen (in Chinese)
https://youtu.be/eaS5gRLSqgY

## Video Solution
https://www.youtube.com/watch?v=BinfKrc5bWo

## Video Solution by Power of Logic
https://youtu.be/WS6X1MQ37jg
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
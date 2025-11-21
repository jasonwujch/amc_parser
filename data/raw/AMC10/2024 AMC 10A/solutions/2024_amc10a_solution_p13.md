# 2024 AMC 10A Problem 13

## Problem

Two transformations are said to commute if applying the first followed by the second gives the same result as applying the second followed by the first. Consider these four transformations of the coordinate plane:

- a translation $2$ units to the right,

- a $90^{\circ}$ -rotation counterclockwise about the origin,

- a reflection across the $x$ -axis, and

- a dilation centered at the origin with scale factor $2.$

Of the $6$ pairs of distinct transformations from this list, how many commute?

$\textbf{(A)}~1\qquad\textbf{(B)}~2\qquad\textbf{(C)}~3\qquad\textbf{(D)}~4\qquad\textbf{(E)}~5$

## Solution 1 (Generalized)
Label the given transformations $T_1, T_2, T_3,$ and $T_4,$ respectively. The rules of transformations are:
- $T_1: \ (x,y)\to(x+2,y)$
- $T_2: \ (x,y)\to(-y,x)$
- $T_3: \ (x,y)\to(x,-y)$
- $T_4: \ (x,y)\to(2x,2y)$
Note that:
- Applying $T_1$ and then $T_2$ gives $(x,y)\to(x+2,y)\to(-y,x+2).$ Applying and then gives Therefore, and do not commute. One counterexample is the preimage
- Applying $T_1$ and then $T_3$ gives $(x,y)\to(x+2,y)\to(x+2,-y).$ Applying and then gives Therefore, and commute. They form a glide reflection.
- Applying $T_1$ and then $T_4$ gives $(x,y)\to(x+2,y)\to(2x+4,2y).$ Applying and then gives Therefore, and do not commute. One counterexample is the preimage
- Applying $T_2$ and then $T_3$ gives $(x,y)\to(-y,x)\to(-y,-x).$ Applying and then gives Therefore, and do not commute. One counterexample is the preimage
- Applying $T_2$ and then $T_4$ gives $(x,y)\to(-y,x)\to(-2y,2x).$ Applying and then gives Therefore, and commute.
- Applying $T_3$ and then $T_4$ gives $(x,y)\to(x,-y)\to(2x,-2y).$ Applying and then gives Therefore, and commute.
Applying $T_2$ and then $T_1$ gives $(x,y)\to(-y,x)\to(-y+2,x).$
Therefore, $T_1$ and $T_2$ do not commute. One counterexample is the preimage $(0,0).$
Applying $T_3$ and then $T_1$ gives $(x,y)\to(x,-y)\to(x+2,-y).$
Therefore, $T_1$ and $T_3$ commute. They form a glide reflection .
Applying $T_4$ and then $T_1$ gives $(x,y)\to(2x,2y)\to(2x+2,2y).$
Therefore, $T_1$ and $T_4$ do not commute. One counterexample is the preimage $(0,0).$
Applying $T_3$ and then $T_2$ gives $(x,y)\to(x,-y)\to(y,x).$
Therefore, $T_2$ and $T_3$ do not commute. One counterexample is the preimage $(1,0).$
Applying $T_4$ and then $T_2$ gives $(x,y)\to(2x,2y)\to(-2y,2x).$
Therefore, $T_2$ and $T_4$ commute.
Applying $T_4$ and then $T_3$ gives $(x,y)\to(2x,2y)\to(2x,-2y).$
Therefore, $T_3$ and $T_4$ commute.
Together, $\boxed{\textbf{(C)}~3}$ pairs of transformations commute: $T_1$ and $T_3, T_2$ and $T_4,$ and $T_3$ and $T_4.$
Remark
To show that two transformations do not commute, we only need one counterexample.
~MRENTHUSIASM

## Solution 2 (Specific)
Label the transformations as follows:
• a translation $2$ units to the right $(W)$
• a $90^{\circ}$ -rotation counterclockwise about the origin $(X)$
• a reflection across the $x$ -axis $(Y)$
• a dilation centered at the origin with scale factor $2$ $(Z)$
Now, examine each possible pair of transformations with the point $(1,0)$ :
$1.$ $W$ and $X$ . $W\rightarrow X$ ends with the point $(0,3)$ . Going $X\rightarrow W$ ends in the point $(1,2)$ , so this pair does not work
$2.$ $W$ and $Y$ . $W\rightarrow Y$ gives the point $(3,0)$ , and going $Y\rightarrow W$ ends in the same point. This pair is valid.
$3.$ $W$ and $Z$ . $W\rightarrow Z$ ends in the point $(6,0)$ , while going the other way gives $(4,0)$ . This pair isn't commute.
$4.$ $X$ and $Y$ . $X\rightarrow Y$ . gives the point $(0,-1)$ , while the other way gives $(0,1)$ . Not a valid pair
$5.$ $X$ and $Z$ . $X\rightarrow Z$ ends in the point $(0,2)$ , and $Z\rightarrow X$ also ends in $(0,2)$ . This pair works.
$6.$ $Y$ and $Z$ . $Y\rightarrow Z$ gives the point $(2,0)$ , and going the other way also ends in $(2,0)$ . This pair is valid.
Therefore, the answer is $\boxed{\textbf{(C) }3}$ .
Note: It is easier to just visualize this problem instead of actually calculating points on paper.
~Tacos_are_yummy_1

## Solution 3 (Specific)
Label the transformations as follows:
• a translation $2$ units to the right $(A)$
• a $90^{\circ}$ -rotation counterclockwise about the origin $(B)$
• a reflection across the $x$ -axis $(C)$
• a dilation centered at the origin with scale factor $2$ $(D)$
Now, we count each transformation individually. It is not hard to see that $AC, BD,$ and $CD$ are commutative (an easy way to test commutativity for some cases would be to have the original point on the $x$ -axis).
In total, $\boxed{\textbf{(C) }3}$ transformation pairs commute.
~xHypotenuse

## Solution 4 (Quick With Reasoning)
Alright so realize that obviously rotation and dilation are commute, if you ever looked at the polar plane. Also, reflecting around the x-axis means that moving to the right two units and dilating are commute. You can easily see this by taking an arbitrary point and applying the transformations. The rest don’t work since you can easily test out using random points on the plane, which means the answer is $\boxed{\textbf{(C) }3}$ .
~EaZ_Shadow

## Video Solution (Organized)
https://youtu.be/l3VrUsZkv8I

## Video Solution by Pi Academy
https://youtu.be/ABkKz0gS1MU?si=ZQBgDMRaJmMPSSMM

## Video Solution 1 by Power Solve
https://youtu.be/QVDbm5sDxxU

## Video Solution 2 by SpreadTheMathLove
https://youtu.be/K_oPg09cLFU?si=-b1pubCvxj1aXrIg

## Video Solution by Dr. David
https://youtu.be/JBnMIK4D8tA

## Video solution by TheNeuralMathAcademy
https://www.youtube.com/watch?v=4b_YLnyegtw&t=2055s
### See Also
- AMC 10
- AMC 10 Problems and Solutions
- Mathematics competitions
- Mathematics competition resources
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
# 2025 AMC 8 Problem 24

## Problem

In trapezoid $ABCD$ , angles $B$ and $C$ measure $60^\circ$ and $AB = DC$ . The side lengths are all positive integers, and the perimeter of $ABCD$ is 30 units. How many non-congruent trapezoids satisfy all of these conditions?

[asy] // Asymptote by aoum import olympiad; size(7cm); pair A,B,C,D; A = (-1,2); B = (-2,0); C = (2,0); D = (1,2); draw(A--B--C--D--cycle); label("$A$", A, NW); label("$B$", B, SW); label("$C$", C, SE); label("$D$", D, NE); draw(anglemark(B,A,D,t=6)); draw(anglemark(A,D,C,t=6)); label(scale(0.8)*"$60^\circ$", B, NE + 0.5E); label(scale(0.8)*"$60^\circ$", C, NW + 0.5W); add(pathticks(A--B)); add(pathticks(D--C)); [/asy]

$\textbf{(A)}\ 0 \qquad \textbf{(B)}\ 1 \qquad \textbf{(C)}\ 2 \qquad \textbf{(D)}\ 3 \qquad \textbf{(E)}\ 4$

## Solution 1
Let $a$ be the length of the shorter base, and let $b$ be the length of the longer one. Note that these two parameters, along with the angle measures and the fact that the trapezoid is isosceles, uniquely determine a trapezoid. We drop perpendiculars down from the endpoints of the top base. Then the length from the foot of this perpendicular to either vertex will be half the difference between the lengths of the two bases, or $\frac{b-a}{2}$ . Now, since we have a 30-60-90 triangle and this side length corresponds to the "30" part, the length of the hypotenuse (one of the legs) is $2 \cdot \frac{b-a}{2} = b-a$ . Then the perimeter of the trapezoid is $2(b-a)+a+b=3b-a=30$ . The only other stipulation for this trapezoid to be valid is that $b>a$ (which was our assumption). We can now easily count the valid pairs $(a,b)$ , yielding $(3,11),(6,12),(9,13),(12,14)$ . It is clear that proceeding further would cause $a \geq b$ , so we have $\boxed{\textbf{(E)}~4}$ valid trapezoids. ~cxsmi

## Solution 2
Let $x$ be the length of $AB$ and $DC$ , and let $b$ be the length of the shorter base. Because $\angle B$ and $\angle C = 60^{\circ}$ , the length of the longer base is $b + \frac{x}{2} + \frac{x}{2} = b + x$ . Therefore, the perimeter is $3x + 2b = 30$ . The number of positive integer pairs $(x, b)$ is $(2,12), (4,9), (6,6), (8,3)$ , meaning the answer is $\boxed{\textbf{(E)}~4}$ .
~alwaysgonnagiveyouup
way where you don't have to test pairs:
We can rearrange $3x + 2b = 30$ to $\frac{30-3x}{2} = b$ . We want $\frac{30-3x}{2}$ to be a positive integer so b is a positive integer. 30 is a multiple of 3 and $-3x$ is just subtracting multiples of 3's from 30 so every number on the numerator of $\frac{30-3x}{2}$ is a multiple of 3 under 30 ( $x$ is also a positive integer so it can't be larger than 30 or not be a multiple of 3). For $30-3x$ to be divisible by 2 it must be even, so we are finding even multiples of 3 under 30 which are 24, 18, 12, and 6. Each number will give us a valid $x$ and a valid $b$ pair giving us 4 solutions.
~happymaths

## Solution 3
Let $x$ be the length of the legs of the trapezoid. Draw the angle bisectors of the 120 degree angles. Now you have 2 equilateral triangles, and another figure in between them. Let $x+a$ be the length of the shorter base of the trapezoid, and let $2x+a$ be the length of the longer base. Since the perimeter of the trapezoid is 30, $5x+2a = 30$ . Since $x>$ 0, and $a$ can be negative as long as $x+a>0$ , you get 4 solutions for $(x,a)$ , namely $(2,10), (4,5), (6,0), (8,-5)$ . Any solution with $x\ge10$ would lead to $x+a\le0$ . Hence, the answer is $\boxed{\textbf{(E)}~4}$
~adi2011

## Solution 4
Drop altitudes from angle $A$ and angle $D$ . Then, two $30-60-90$ triangles and a rectangle are created. Let the hypotenuse of both of the triangles equal $x$ and let side $AD$ equal $y$ . Then, the distance from $B$ and $C$ to the feet of the altitudes that are closest to them is $\frac{x}{2}$ , and the distance between the feet of the two altitudes would be $y$ . The rest is similar to Solution 2 ~Soupboy0

## Solution 5 (SIMILAR TO SOLUTION 4)
We give lengths to the base of the $30-60-90$ triangles on both sides as the trapezoid as variable $x$ . We give lengths of Line $AB$ and the other side as variable $y$ . When we add them, we have $6x+2y=30$ from the sides. If we lext $x=5$ , the other sides won't work so it has to be integers less than $5$ which is $4$ which is the answer. - Spacepandamath13

## Solution 6
Since the trapezoid perimeter is $30$ , we can name the top, congruent side lengths, and bottom variables. The top length is $A$ , the congruent side length is $C$ , and the bottom should be $B$ . (Since the top side is $A$ , and its parallel to the bottom, then the bottom side length should be $A + 2B,$ $B$ being one of the two lengths.) The perimeter of the trapezoid is $2A + 2B + 2C = 30,$ which can be divided by $2$ to become $A + B + C = 15$ Now, since the $B$ is the base of a 30-60-90 right triangle, and its angle opposite to the side is $30$ degrees. Therefore, $B$ is exactly half of side $C$ . We can test out cases of $B$ . If $B = 1$ , then $C = 2$ , $A + 1 + 2 = 15$ which would give $A$ the value of $12$ . Keep repeating this process until $A$ is no longer a positive integer. Therefore, there are $\boxed{\textbf{(E)}~4}$ possible configurations of the trapezoid. ~Imhappy62789

## Solution 7
Explanations and Reasoning to Similar Solutions
Note that trapezoid $ABCD$ is isosceles with $B$ and $C$ being the bottom 2 vertices. The shape can be dissected into 3 shapes with 2 congruent right triangles separated by a rectangle. This is done by dropping an altitude, a perpendicular point on the base from each of the 2 top vertices, named $E$ and $F$ , respectively below $A$ and $D$ . The property that angles $\angle$ $B$ and $\angle$ $C$ measure $60^\circ$ is significant here, forming $30-60-90$ triangles ( $\triangle$ $ABE$ and $\triangle$ $DCF$ ). Now the assumed larger $^a$ side $BC$ is separated into 3 sections by the 3 shapes. Or $BC = BE + EF + CF$ . $^b$ Recall that $\triangle$ $ABE$ and $\triangle$ $DCF$ are $30-60-90$ triangles, the side length ratios are $1:\sqrt3:2$ . Naming the length of the shorter side of the right triangles as $a$ , and the length of side $AD$ as $b$ , then the trapezoid's side lengths can be expressed in only 2 variables. Now knowing $AD = b$ , $DC = 2a$ $^c$ , $BC = a + b + a = 2a + b$ , and $AC = 2a$ , the perimeter is $b + 2a + 2a + b + 2a = 2b + 6a = 30$ . Simplifying, $3a + b = 15$ , only 4 pairs of values satisfy this condition, namely $(1,12)$ , $(2,9)$ , $(3,6)$ , $(4,3)$ .
Thus there $\boxed{\textbf{(E)}~4}$ possible non-congruent trapezoids.
$^a$ The question asks for non-congruent trapezoids, and rotation preserves congruence so the assumption is always true WLOG.
$^b$ The shortest side of $\triangle$ ABE, the length of AD (shape ADFE is a rectangle so FE = AD), and the shortest side of $\triangle$ DCF.
$^c$ $AB = DC = 2a$ , $AB$ and $DC$ are the hypotenuse of triangles $\triangle$ ABE and $\triangle$ DCF. ~moracle

## Solution 8
Let $a = AD$ and $s = AB = DC$ . Draw a segment from $A$ to $\overline{BC}$ parallel to $\overline{DC}$ , meeting $\overline{BC}$ at point $P$ , forming parallelogram $ADCP$ . It follows that $AP = DC = s$ and $PC = AD = a$ . Isosceles $\triangle ABP$ has base angles measuring $60^\circ$ , so it is equilateral and $BP = s$ .
[asy] size(8cm); draw((-6, 0)--(6, 0)--(3, 3sqrt(3))--(-3, 3sqrt(3))--cycle); draw((0, 0)--(-3, 3sqrt(3))--cycle); label("$P$", (0, 0), S); label("$B$", (-6, 0), SW); label("$C$", (6, 0), SE); label("$A$", (-3, 3sqrt(3)), NW); label("$D$", (3, 3sqrt(3)), NE); label("$a$", (0, 3sqrt(3)), N); label("$a$", (3, 0), S); label("$s$", (-3, 0), S); label("$s$", (-4.5, 3sqrt(3)/2), W); label("$s$", (-1.5, 3sqrt(3)/2), E); label("$s$", (4.5, 3sqrt(3)/2), E); label("$60^{\circ}$", (-5.75, 0), NE); label("$60^{\circ}$", (-0.25, 0), NW); label("$60^{\circ}$", (5.75, 0), NW); [/asy]
Then the perimeter of $ABCD$ is $L = 2a + 3s = 30$ . To satisfy this equation with positive integer values, the number $a$ must be divisible by $3$ because $2a = 3(10 - s)$ . The only possible values for $a$ are $3, 6, 9,$ and $12$ , each value corresponding to a different trapezoid. Greater multiples of $3$ will not lead to a positive integer value for $s$ . Therefore there are $\boxed{4}$ different trapezoids that satisfy the conditions.
The table below lists the side lengths $a$ , $s$ , and $a + s$ for these $4$ trapezoids, along with their perimeters.
\begin{array}{c|c|c|c} a & s & a + s & L = 2a + 3s \\ \hline 3 & 8 & 11 & 2 \cdot 3 + 3 \cdot 8 = 30 \\ 6 & 6 & 12 & 2 \cdot 6 + 3 \cdot 6 = 30 \\ 9 & 4 & 13 & 2 \cdot 9 + 3 \cdot 4 = 30 \\ 12 & 2 & 14 & 2 \cdot 12 + 3 \cdot 2 = 30 \\ \end{array}
~ alwaysgonnagiveyouup

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=jTTcscvcQmI

## Video Solution 2
~hsnacademy

## Video Solution 4 by Thinking Feet
https://youtu.be/PKMpTS6b988

## Video Solution 5 by Dr. David
https://youtu.be/BbaifFoDeCk
### See Also
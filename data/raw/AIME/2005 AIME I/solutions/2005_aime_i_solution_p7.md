# 2005 AIME I Problem 7

## Problem

In quadrilateral $ABCD,\ BC=8,\ CD=12,\ AD=10,$ and $m\angle A= m\angle B = 60^\circ.$ Given that $AB = p + \sqrt{q},$ where $p$ and $q$ are positive integers , find $p+q.$

1 Problem

- 1 Problem

- 2 Solution 2.1 Solution 1 2.2 Solution 2 2.3 Solution 3 2.4 Solution 4 2.5 Solution 5 (EASY EASY VERY TREMENDOUSLY EASY)

- 3 See also

- 2.1 Solution 1

- 2.2 Solution 2

- 2.3 Solution 3

- 2.4 Solution 4

- 2.5 Solution 5 (EASY EASY VERY TREMENDOUSLY EASY)

## Solution

## Solution 1
[asy]draw((0,0)--(20.87,0)--(15.87,8.66)--(5,8.66)--cycle); draw((5,8.66)--(5,0)); draw((15.87,8.66)--(15.87,0)); draw((5,8.66)--(16.87,6.928)); label("$A$",(0,0),SW); label("$B$",(20.87,0),SE); label("$E$",(15.87,8.66),NE); label("$D$",(5,8.66),NW); label("$P$",(5,0),S); label("$Q$",(15.87,0),S); label("$C$",(16.87,7),E); label("$12$",(10.935,7.794),S); label("$10$",(2.5,4.5),W); label("$10$",(18.37,4.5),E); [/asy]
Draw line segment $DE$ such that line $DE$ is concurrent with line $BC$ . Then, $ABED$ is an isosceles trapezoid so $AD=BE=10$ , and $BC=8$ and $EC=2$ . We are given that $DC=12$ . Since $\angle CED = 120^{\circ}$ , using Law of Cosines on $\bigtriangleup CED$ gives \[12^2=DE^2+4-2(2)(DE)(\cos 120^{\circ})\] which gives \[144-4=DE^2+2DE\] . Adding $1$ to both sides gives $141=(DE+1)^2$ , so $DE=\sqrt{141}-1$ . $\bigtriangleup DAP$ and $\bigtriangleup EBQ$ are both $30-60-90$ , so $AP=5$ and $BQ=5$ . $PQ=DE$ , and therefore $AB=AP+PQ+BQ=5+\sqrt{141}-1+5=9+\sqrt{141} \rightarrow (p,q)=(9,141) \rightarrow \boxed{150}$ .

## Solution 2
Draw the perpendiculars from $C$ and $D$ to $AB$ , labeling the intersection points as $E$ and $F$ . This forms 2 $30-60-90$ right triangles , so $AE = 5$ and $BF = 4$ . Also, if we draw the horizontal line extending from $C$ to a point $G$ on the line $DE$ , we find another right triangle $\triangle DGC$ . $DG = DE - CF = 5\sqrt{3} - 4\sqrt{3} = \sqrt{3}$ . The Pythagorean Theorem yields that $GC^2 = 12^2 - \sqrt{3}^2 = 141$ , so $EF = GC = \sqrt{141}$ . Therefore, $AB = 5 + 4 + \sqrt{141} = 9 + \sqrt{141}$ , and $p + q = \boxed{150}$ .

## Solution 3
Extend $AD$ and $BC$ to an intersection at point $E$ . We get an equilateral triangle $ABE$ . We denote the length of a side of $\triangle ABE$ as $s$ and solve for it using the Law of Cosines : \[12^2 = (s - 10)^2 + (s - 8)^2 - 2(s - 10)(s - 8)\cos{60}\] \[144 = 2s^2 - 36s + 164 - (s^2 - 18s + 80)\] This simplifies to $s^2 - 18s - 60=0$ ; the quadratic formula yields the (discard the negative result) same result of $9 + \sqrt{141}$ .

## Solution 4
Extend $BC$ and $AD$ to meet at point $E$ , forming an equilateral triangle $\triangle ABE$ . Draw a line from $C$ parallel to $AB$ so that it intersects $AD$ at point $F$ . Then, apply Stewart's Theorem on $\triangle CFE$ . Let $CE=x$ . \[2x(x-2) + 12^2x = 2x^2 + x^2(x-2)\] \[x^3 - 2x^2 - 140x = 0\] By the quadratic formula (discarding the negative result), $x = 1 + \sqrt{141}$ , giving $AB = 9 + \sqrt{141}$ for a final answer of $p+q=150$ .

## Solution 5 (EASY EASY VERY TREMENDOUSLY EASY)
Draw a line from point $C$ to a new point $E$ on $AD$ parallel to $AB$ . Draw a line from point $E$ to a new point $F$ on $AB$ parallel to $CD$ . This creates parallelogram $CEFB$ .
$\angle CEF = 60^{\circ}$ and triangle $AEF$ is an equilateral triangle with side length 8. Thus, $AF = 8$ .
$ED = 10 - 8 = 2$ . By the Law of Cosines, $CD^2 = ED^2 + EC^2 - 2 \cdot {ED} \cdot {EC} \cdot \cos{\angle DEC}$ . Thus, $144 = 4 + c^2 - 2c$ and $c = 1 + \sqrt{141}$ . $EC = FB$ .
$AB = AF + FB = 8 + 1 + \sqrt{141} = 9 + \sqrt{141}$ so the answer is $p+q=150$ .
-unhappyfarmer
These problems are copyrighted © by the Mathematical Association of America.
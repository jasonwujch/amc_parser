# 2023 AIME II Problem 9

## Problem

Circles $\omega_1$ and $\omega_2$ intersect at two points $P$ and $Q,$ and their common tangent line closer to $P$ intersects $\omega_1$ and $\omega_2$ at points $A$ and $B,$ respectively. The line parallel to $AB$ that passes through $P$ intersects $\omega_1$ and $\omega_2$ for the second time at points $X$ and $Y,$ respectively. Suppose $PX=10,$ $PY=14,$ and $PQ=5.$ Then the area of trapezoid $XABY$ is $m\sqrt{n},$ where $m$ and $n$ are positive integers and $n$ is not divisible by the square of any prime. Find $m+n.$

## Video Solution & More by MegaMath
https://www.youtube.com/watch?v=x-5VYR1Dfw4

## Solution 1
Denote by $O_1$ and $O_2$ the centers of $\omega_1$ and $\omega_2$ , respectively. Let $XY$ and $AO_1$ intersect at point $C$ . Let $XY$ and $BO_2$ intersect at point $D$ .
Because $AB$ is tangent to circle $\omega_1$ , $O_1 A \perp AB$ . Because $XY \parallel AB$ , $O_1 A \perp XY$ . Because $X$ and $P$ are on $\omega_1$ , $O_1A$ is the perpendicular bisector of $XP$ . Thus, $PC = \frac{PX}{2} = 5$ .
Analogously, we can show that $PD = \frac{PY}{2} = 7$ .
Thus, $CD = CP + PD = 12$ . Because $O_1 A \perp CD$ , $O_1 A \perp AB$ , $O_2 B \perp CD$ , $O_2 B \perp AB$ , $ABDC$ is a rectangle. Hence, $AB = CD = 12$ .
Let $QP$ and $AB$ meet at point $M$ . Thus, $M$ is the midpoint of $AB$ . Thus, $AM = \frac{AB}{2} = 6$ . This is the case because $PQ$ is the radical axis of the two circles, and the powers with respect to each circle must be equal.
In $\omega_1$ , for the tangent $MA$ and the secant $MPQ$ , following from the power of a point, we have $MA^2 = MP \cdot MQ$ . By solving this equation, we get $MP = 4$ .
We notice that $AMPC$ is a right trapezoid. Hence, \begin{align*} AC & = \sqrt{MP^2 - \left( AM - CP \right)^2} \\ & = \sqrt{15} . \end{align*}
Therefore, \begin{align*} [XABY] & = \frac{1}{2} \left( AB + XY \right) AC \\ & = \frac{1}{2} \left( 12 + 24 \right) \sqrt{15} \\ & = 18 \sqrt{15}. \end{align*}
Therefore, the answer is $18 + 15 = \boxed{\textbf{(033)}}$ .
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 2
Notice that line $\overline{PQ}$ is the radical axis of circles $\omega_1$ and $\omega_2$ . By the radical axis theorem, we know that the tangents of any point on line $\overline{PQ}$ to circles $\omega_1$ and $\omega_2$ are equal. Therefore, line $\overline{PQ}$ must pass through the midpoint of $\overline{AB}$ , call this point M. In addition, we know that $AM=MB=6$ by circle properties and midpoint definition.
Then, by Power of Point,
\begin{align*} AM^2&=MP*MQ \\ 36&=MP(MP+5) \\ MP&=4 \\ \end{align*}
Call the intersection point of line $\overline{A\omega_1}$ and $\overline{XY}$ be C, and the intersection point of line $\overline{B\omega_2}$ and $\overline{XY}$ be D. $ABCD$ is a rectangle with segment $MP=4$ drawn through it so that $AM=MB=6$ , $CP=5$ , and $PD=7$ . Dropping the altitude from $M$ to $\overline{XY}$ , we get that the height of trapezoid $XABY$ is $\sqrt{15}$ . Therefore the area of trapezoid $XABY$ is
\begin{align*} \frac{1}{2}\cdot(12+24)\cdot(\sqrt{15})=18\sqrt{15} \end{align*}
Giving us an answer of $\boxed{033}$ .
~ Danielzh

## Solution 3
Refer to Solution 1.
We let $AC=BD=x$ and the extension of $AC$ to the circle $\neq A$ as $E.$ By Power of a Point on point $C$ of circle $w_1$ we find \[x\cdot{CE}=5\cdot5.\] \[CE=\frac{25}{x}.\] We have diameter $AE = AC+CE=x+\frac{25}{x}.$ Therefore the radius of $w_1$ is $\frac{x+\frac{25}{x}}{2}=\frac{25+x^2}{2x} = O_1A = O_1P.$
Similarly repeating this procedure on $w_2$ we find the radius of $w_2$ is $\frac{49+x^2}{2x} = O_2P = O_2B.$
Next we solve for $O_1O_2$ in two ways. Let the perpendicular from $O_1$ to $BO_2$ intersect at $K$ we have $O_1K =AB = 12.$ We also have \[O_2K = BO_2 - AO_1 =\frac{49+x^2}{2x}- \frac{25+x^2}{2x}=\frac{12}{x}.\] Therefore since $\triangle{O_1KO_2}$ is right, we have $(O_1O_2)^2 = (O_1K)^2+(O_2K)^2 = 12^2 + \frac{12}{x}^2 =144 + \frac{144}{x^2}.$
For our second way, we let the midpoint of $PQ$ be $M.$ Note that $PM$ forms the right triangles $PO_1M$ and $PO_2M$ both of which share an leg of $PM$ or $\frac{5}{2}.$ Using Pythag we can solve for $O_1O_2.$
\[O_1O_2 = O_1M+O_2M = \sqrt{(O_1P)^2 - (PM)^2}+\sqrt{(O_2P)^2 - (PM)^2}\] \[\sqrt{144 + \frac{144}{x^2}} = \sqrt{(\frac{25+x^2}{2x})^2 - (\frac{5}{2})^2}+\sqrt{(\frac{49+x^2}{2x})^2 - (\frac{5}{2})^2}\] \[\sqrt{144 + \frac{144}{x^2}} = \sqrt{\frac{(25+x^2)^2}{4x^2} - \frac{25}{4}}+\sqrt{\frac{(49+x^2)^2}{4x^2} - \frac{25}{4}}\] We let $x^2 = a$ to slightly simplify the equation, \[\sqrt{144 + \frac{144}{a}} = \sqrt{\frac{(25+a)^2}{4a} - \frac{25}{4}}+\sqrt{\frac{(49+a)^2}{4a} - \frac{25}{4}}\] \[12\sqrt{1+\frac{1}{a}} = \sqrt{\frac{a^2 + 25a + 625}{4a}} + \sqrt{\frac{a^2 +73a + 2401}{4a}}.\] \[24\sqrt{1+\frac{1}{a}} = \sqrt{\frac{a^2 + 25a + 625}{a}} + \sqrt{\frac{a^2 +73a + 2401}{a}}.\] \[24\sqrt{a+1} = \sqrt{a^2 + 25a + 625} + \sqrt{a^2 +73a + 2401}.\] \[\sqrt{a^2 + 25a + 625}=24\sqrt{a+1}-\sqrt{a^2 +73a + 2401}.\] \[a^2 + 25a + 625=576a+576+a^2+73a+2401-48\sqrt{(a+1)(a^2 +73a + 2401)}.\] \[48\sqrt{(a+1)(a^2 +73a + 2401)}=624a+2352.\] \[\sqrt{(a+1)(a^2 +73a + 2401)}=13a+49.\] \[a^3 + 74 a^2 + 2474 a + 2401=169 a^2 + 1274 a + 2401.\] \[a^3 -95a^2 + 1200a = 0\] \[a(a-15)(a-80)=0\] Thus the solutions are $a=0,15,80.$ Checking bounds $a=15$ is the only valid solution, which means $x=\sqrt{15}.$ Finally to find the area of $XABY,$ we have the bases $XY=24$ and $AB=12$ and the height $x=\sqrt{15}$ therefore \[[XABY]=\frac{1}{2}\cdot(12+24)\cdot\sqrt{15}=18\sqrt{15}.\] Giving us an answer of $18+15 = \boxed{033}.$
~ mathkiddus

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=RUv6qNY_agI
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
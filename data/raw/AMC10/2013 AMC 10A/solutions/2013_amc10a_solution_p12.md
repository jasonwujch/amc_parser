# 2013 AMC 10A Problem 12

## Problem

In $\triangle ABC$ , $AB=AC=28$ and $BC=20$ . Points $D,E,$ and $F$ are on sides $\overline{AB}$ , $\overline{BC}$ , and $\overline{AC}$ , respectively, such that $\overline{DE}$ and $\overline{EF}$ are parallel to $\overline{AC}$ and $\overline{AB}$ , respectively. What is the perimeter of parallelogram $ADEF$ ?

[asy] size(180); pen dps = linewidth(0.7) + fontsize(10); defaultpen(dps); real r=5/7; pair A=(10,sqrt(28^2-100)),B=origin,C=(20,0),D=(A.x*r,A.y*r); pair bottom=(C.x+(D.x-A.x),C.y+(D.y-A.y)); pair E=extension(D,bottom,B,C); pair top=(E.x+D.x,E.y+D.y); pair F=extension(E,top,A,C); draw(A--B--C--cycle^^D--E--F); dot(A^^B^^C^^D^^E^^F); label("$A$",A,NW); label("$B$",B,SW); label("$C$",C,SE); label("$D$",D,W); label("$E$",E,S); label("$F$",F,dir(0)); [/asy]

$\textbf{(A) }48\qquad \textbf{(B) }52\qquad \textbf{(C) }56\qquad \textbf{(D) }60\qquad \textbf{(E) }72\qquad$

## Solution 1
Note that because $\overline{DE}$ and $\overline{EF}$ are parallel to the sides of $\triangle ABC$ , the internal triangles $\triangle BDE$ and $\triangle EFC$ are similar to $\triangle ABC$ , and are therefore also isosceles triangles.
It follows that $BD = DE$ . Thus, $AD + DE = AD + DB = AB = 28$ .
The opposite sides of parallelograms are equal (you can prove this fact simply by drawing the diagonal of the parallelogram and proving that the two resulting triangles are congruent by SSS), so the perimeter is $2 \times (AD + DE) = 56\implies \boxed{\textbf{(C)}}$ .

## Solution 2
We will be using logic to solve this problem :-)!
The ratio \( AB/BC = DB/BE \) is just \( 28/20 = DB/BE \) which implies, through cross multiplication, that \( 28BE = 20DB \). Similarly, the ratio \( AB/BC = FE/EC \) is just \( 28/20 = FE/EC \), and thus, also implies that \( 28EC = 20FE \).
For Reference, we shall also put \( DB/BE = FE/EC \), or \( DB \cdot EC = FE \cdot BE \).
Analyzing \( 28BE=20DB \), we find out that the number of ordered pairs \( (BE,DB) \) that work are \( (5, 7) \), \( (10, 14) \) and \( (15, 21) \).
The most logical choice for BE is \( BE = 15 \), \( DB = 21 \).
Because \( BE + EC = 20 \), We know that \( EC = 5 \), and thus, by using the same logic, \( FE = 7 \).
The perimeter of parallelogram \( ADEF \) is none other than \( 2(21) + 2(7) = 42 + 14 = \) $\boxed{56 \Rightarrow \textbf{(C)}}$
~Pinotation

## Solution 3
Similar to Solution 1, we find that the internal triangles $\triangle BDE$ and $\triangle EFC$ are similar to $\triangle ABC$ , and are therefore also isosceles triangles and similar to each other. We know that the perimeter of $ADEF$ can be found by $2(l + w)$ , and $DE$ will be the length and the width will be $EF$ . These can be found by looking at the long sides of $\triangle DBE$ and $\triangle FEC$ respectively. We then find the ratio of long sides to the short side of $\triangle ABC$ to be $7/5$ by $28/20$ , which applies to the other triangles since they are similar. We set up an expression, calling $BE$ as $x$ and $EC$ as $20 - x$ , and substitute it into the perimeter equation knowing our long sides from the ratio:
$2(7x/5 + 7/5(20-x))$
$2(7x/5 + 28 - 7x/5)$
$2(28)$
$56\implies \boxed{\textbf{(C)}}$
~neeyakkid23

## Solution 4
The problem implies that where you choose $D$ , $E$ , and $F$ are irrelevant. This means that to make it easier, choose it such that $D$ , $E$ , and $F$ are the midpoints of $\overline{AB}$ , $\overline{BC}$ , and $\overline{AC}$ respectively. $28 \div 2 = 14$ , $14 \times 4 = 56$ , so $\boxed{\textbf{(C)}}$ .
~yhbettysun

## Solution 5
Drawing the diagram with a ruler and compass (and scaling back by x4), we can draw approximate parallel lines. This yields about 14, but we need to multiply by 4 to get 56, or $\boxed{(C)}$ .

## Video Solution
https://youtu.be/8ki_yMyE6no
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
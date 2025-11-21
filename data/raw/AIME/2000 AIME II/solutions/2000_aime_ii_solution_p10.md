# 2000 AIME II Problem 10

## Problem

A circle is inscribed in quadrilateral $ABCD$ , tangent to $\overline{AB}$ at $P$ and to $\overline{CD}$ at $Q$ . Given that $AP=19$ , $PB=26$ , $CQ=37$ , and $QD=23$ , find the square of the radius of the circle.

## Solution 1
Call the center of the circle $O$ . By drawing the lines from $O$ tangent to the sides and from $O$ to the vertices of the quadrilateral, four pairs of congruent right triangles are formed.
Thus, $\angle{AOP}+\angle{POB}+\angle{COQ}+\angle{QOD}=180$ , or $(\arctan(\tfrac{19}{r})+\arctan(\tfrac{26}{r}))+(\arctan(\tfrac{37}{r})+\arctan(\tfrac{23}{r}))=180$ .
Take the $\tan$ of both sides and use the identity for $\tan(A+B)$ to get \[\tan(\arctan(\tfrac{19}{r})+\arctan(\tfrac{26}{r}))+\tan(\arctan(\tfrac{37}{r})+\arctan(\tfrac{23}{r}))=n\cdot0=0.\]
Use the identity for $\tan(A+B)$ again to get \[\frac{\tfrac{45}{r}}{1-19\cdot\tfrac{26}{r^2}}+\frac{\tfrac{60}{r}}{1-37\cdot\tfrac{23}{r^2}}=0.\]
Solving gives $r^2=\boxed{647}$ .
Note: the equation may seem nasty at first, but once you cancel the $r$ s and other factors, you are just left with $r^2$ . That gives us $647$ quite easily.

## Solution 2
Just use the area formula for tangential quadrilaterals. The numbers are really big. A terrible problem to work on ( $a, b, c,$ and $d$ are the tangent lengths, not the side lengths). \[A = \sqrt{(a+b+c+d)(abc+bcd+cda+dab)} = 105\sqrt{647}\] $r^2=\frac{A^2}{(a+b+c+d)^2} = \boxed{647}$ .

## Solution 3 (Smart algebra to make 2 less annoying)
Using the formulas established in solution 2, one notices: \[r^2=\frac{A^2}{(a+b+c+d)^2}\] \[r^2=\frac{(a+b+c+d)(abc+bcd+cda+abd) }{(a+b+c+d)^2}\] \[r^2=\frac{abc+bcd+acd+abd}{a+b+c+d}\] \[r^2=\boxed{647}\]
which is nowhere near as hard of a calculation. In fact, this is basically the same exact calculation done at the end of solution 1, just with less opportunity to cancel coefficients beforehand.
These problems are copyrighted © by the Mathematical Association of America.
# 2001 AIME I Problem 4

## Problem

In triangle $ABC$ , angles $A$ and $B$ measure $60$ degrees and $45$ degrees, respectively. The bisector of angle $A$ intersects $\overline{BC}$ at $T$ , and $AT=24$ . The area of triangle $ABC$ can be written in the form $a+b\sqrt{c}$ , where $a$ , $b$ , and $c$ are positive integers, and $c$ is not divisible by the square of any prime. Find $a+b+c$ .

## Solution
After chasing angles, $\angle ATC=75^{\circ}$ and $\angle TCA=75^{\circ}$ , meaning $\triangle TAC$ is an isosceles triangle and $AC=24$ .
Using law of sines on $\triangle ABC$ , we can create the following equation:
$\frac{24}{\sin(\angle ABC)}$ $=$ $\frac{BC}{\sin(\angle BAC)}$
$\angle ABC=45^{\circ}$ and $\angle BAC=60^{\circ}$ , so $BC = 12\sqrt{6}$ .
We can then use the Law of Sines area formula $\frac{1}{2} \cdot BC \cdot AC \cdot \sin(\angle BCA)$ to find the area of the triangle.
$\sin(75)$ can be found through the sin addition formula.
$\sin(75)$ $=$ $\frac{\sqrt{6} + \sqrt{2}}{4}$
Therefore, the area of the triangle is $\frac{\sqrt{6} + \sqrt{2}}{4}$ $\cdot$ $24$ $\cdot$ $12\sqrt{6}$ $\cdot$ $\frac{1}{2}$
$72\sqrt{3} + 216$
$72 + 3 + 216 =$ $\boxed{291}$

## Solution 2 (no trig)
First, draw a good diagram.
We realize that $\angle C = 75^\circ$ , and $\angle CAT = 30^\circ$ . Therefore, $\angle CTA = 75^\circ$ as well, making $\triangle CAT$ an isosceles triangle. $AT$ and $AC$ are congruent, so $AC=24$ . We now drop an altitude from $C$ , and call the foot this altitude point $D$ .
By 30-60-90 triangles, $AD=12$ and $CD=12\sqrt{3}$ .
We also notice that $\triangle CDB$ is an isosceles right triangle. $CD$ is congruent to $BD$ , which makes $BD=12\sqrt{3}$ . The base $AB$ is $12+12\sqrt{3}$ , and the altitude $CD=12\sqrt{3}$ . We can easily find that the area of triangle $ABC$ is $216+72\sqrt{3}$ , so $a+b+c=\boxed{291}$ .
-youyanli

## Solution 3(Speedy and Simple)
After drawing line $AT$ , we see that we have two triangles: $\triangle ABT,$ with $45$ , $30$ , and $105$ degrees, and $\triangle ATC$ , with $30$ , $75$ , $75$ degrees. If we can sum these two triangles' areas, we have our answer.
Let's take care of $\triangle ATC$ first. We see that $\triangle ATC$ is a isosceles triangle, with $AT = AC = 24$ . Because the area of a triangle is $\frac{1}{2}ab\sin C$ , we have $\frac{1}{2}\cdot 24^2\cdot\frac{1}{2}$ , which is equal to $144.$
Now, on to $\triangle ABT$ . Draw the altitude from angle $\angle T$ to $AB$ , and call the point of intersection $D$ . This splits $\triangle ABT$ into $2$ triangles, one with $30-60-90$ ( $\triangle ADT$ ), and another with $45-45-90$ ( $\triangle BDT$ ). Now, because we know that $AT$ is $24$ , we have by special right triangle ratios. The area of $\triangle ADT$ is $\frac{12\sqrt{3}\cdot 12}{2}$ , and the area of $\triangle BDT$ is $\frac{12\cdot 12}{2}$ , which adds to $72\sqrt{3} + 72$ .
Adding this to $\triangle ATC$ we get a total sum of $216 + 72\sqrt{3}.$ Thus, $a + b + c$ would be $216 + 72 + 3 = \boxed{291}.$
~MathCosine

## Solution 4 (very fast)
Recall the triangle area via sine formula $\frac{ab\sin{C}}{2}$ . We notice that they have given almost all we need to use this, since $AC=24$ by properties of isosceles triangles and $\angle A$ itself equals $60$ . So, we are trying to find $AB$ . This is very trivial, as when we drop an altitude from $T$ to $AB$ (let the intersecting point be $U$ ), $AU=12\sqrt{3}$ and $BU=12$ by $30-60-90$ and $45-45-90$ triangles respectively. Therefore, the answer is just \[\frac{(12+12\sqrt{3})(24)\sin{60}}{2}\] \[=(12+12\sqrt{3})(6)(\sqrt{3})\] \[=72\sqrt{3}+72\times 3\] \[=216 + 72\sqrt{3}\] \[\Longrightarrow 216+72+3=\boxed{291}.\]
~martianrunner

## Video Solution by OmegaLearn
https://youtu.be/BIyhEjVp0iM?t=526
~ pi_is_3.14
These problems are copyrighted © by the Mathematical Association of America.
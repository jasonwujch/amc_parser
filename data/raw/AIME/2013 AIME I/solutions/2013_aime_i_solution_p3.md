# 2013 AIME I Problem 3

## Problem

Let $ABCD$ be a square, and let $E$ and $F$ be points on $\overline{AB}$ and $\overline{BC},$ respectively. The line through $E$ parallel to $\overline{BC}$ and the line through $F$ parallel to $\overline{AB}$ divide $ABCD$ into two squares and two nonsquare rectangles. The sum of the areas of the two squares is $\frac{9}{10}$ of the area of square $ABCD.$ Find $\frac{AE}{EB} + \frac{EB}{AE}.$

## Solution
It's important to note that $\dfrac{AE}{EB} + \dfrac{EB}{AE}$ is equivalent to $\dfrac{AE^2 + EB^2}{(AE)(EB)}$
We define $a$ as the length of the side of larger inner square, which is also $EB$ , $b$ as the length of the side of the smaller inner square which is also $AE$ , and $s$ as the side length of $ABCD$ . Since we are given that the sum of the areas of the two squares is $\frac{9}{10}$ of the the area of ABCD, we can represent that as $a^2 + b^2 = \frac{9s^2}{10}$ . The sum of the two nonsquare rectangles can then be represented as $2ab = \frac{s^2}{10}$ .
Looking back at what we need to find, we can represent $\dfrac{AE^2 + EB^2}{(AE)(EB)}$ as $\dfrac{a^2 + b^2}{ab}$ . We have the numerator, and dividing $\frac{s^2}{10}$ by two gives us the denominator $\frac{s^2}{20}$ . Dividing $\dfrac{\frac{9s^2}{10}}{\frac{s^2}{20}}$ gives us an answer of $\boxed{018}$ .

## Solution 2
Let the side of the square be $1$ . Therefore the area of the square is also $1$ . We label $AE$ as $a$ and $EB$ as $b$ . Notice that what we need to find is equivalent to: $\frac{a^2+b^2}{ab}$ . Since the sum of the two squares ( $a^2+b^2$ ) is $\frac{9}{10}$ (as stated in the problem) the area of the whole square, it is clear that the sum of the two rectangles is $1-\frac{9}{10} \implies \frac{1}{10}$ . Since these two rectangles are congruent, they each have area: $\frac{1}{20}$ . Also note that the area of this is $ab$ . Plugging this into our equation we get:
$\frac{\frac{9}{10}}{\frac{1}{20}} \implies \boxed{018}$

## Solution 3
Let $AE$ be $x$ , and $EB$ be $1$ . Then we are looking for the value $x+\frac{1}{x}$ . The areas of the smaller squares add up to $9/10$ of the area of the large square, $(x+1)^2$ . Cross multiplying and simplifying we get $x^2-18x+1=0$ . Rearranging, we get $x+\frac{1}{x}=\boxed{018}$

## Solution 4 (Vieta's)
As before, $\dfrac{AE}{EB} + \dfrac{EB}{AE}$ is equivalent to $\dfrac{AE^2 + EB^2}{(AE)(EB)}$ . Let $x$ represent the value of $AE=CF$ . Since $EB=FB=1-x,$ the area of the two rectangles is $2x(1-x)=-2x^2+2x=\frac1{10}$ . Adding $2x^2-2x$ to both sides and dividing by $2$ gives $x^2-x+\frac1{20}=0.$ Note that the two possible values of $x$ in the quadratic both sum to $1,$ like how $AE$ and $EB$ does. Therefore, $EB$ must be the other root of the quadratic that $AE$ isn't. Applying Vietas and manipulating the numerator, we get $\frac{x_1^2+x_2^2}{x_1x_2}=\frac{(x_1+x_2)^2-2x_1x_2}{\frac{1}{20}}=\frac{1^2-\frac1{10}}{\frac1{20}}=\frac{\frac9{10}}{\frac{1}{20}}=\boxed{018}$ .

## Solution 5 (Fast)
Let $AE = x$ and $BE = y$ . From this, we get $AB = x + y$ . The problem is asking for $\frac{x}{y} + \frac{y}{x}$ , which can be rearranged to give $\frac{x^2 + y^2}{xy}$ . The problem tells us that $x^2 + y^2 = \frac{9(x+y)^2}{10}$ . We simplify to get $x^2 + y^2 = 18xy$ . Finally, we divide both sides by $xy$ to get $\frac{x^2 + y^2}{xy} = \boxed{018}$ . - Spacesam

## Solution 5 (A faster Vieta's)
After we get the polynomial $x^2 - 18x + 1,$ we want to find $x + \frac 1 {x}.$ Since the product of the roots of the polynomial is 1, the roots of the polynomial are simply $x, \frac 1 {x}.$ Hence $x + \frac 1 {x}$ is just $18$ by Vieta's formula, or $\boxed{018}$

## Solution 6
We have the equation $x^2 + y^2$ = $\frac {9}{10} \cdot (x+y)^2$ . We get $x^2 + y^2 = 18xy$ . We rearrange to get $x^2 + y^2 - 18xy = 0$ . Since the problem only asks us for a ratio, we assume $x$ = $1$ . We have $y^2 - 18y + 1$ = $0$ . Solving the quadratic yields $9 + 4 \sqrt 5$ and $9 - 4 \sqrt 5$ . It doesn't really matter which one it is, since both of them are positive. We will use $9 + 4 \sqrt 5$ .
We have $9 + 4 \sqrt 5 + \frac {1}{9+4 \sqrt 5}$ . Rationalizing the denominator gives us $9 + 4 \sqrt 5 + \frac {9 - 4 \sqrt 5}{81-80} = (9 + 4 \sqrt 5) + (9 - 4 \sqrt 5) = 18$ . Our answer is $\boxed {018}$
~Arcticturn

## Solution 7
Set side length of square to be $10$ , $AE = x$ and $EB = y$ . From this, we get $y+x=10$ , and since the area of the square will be 100, the area of the two rectangles will be $2xy = 10$ . We can substitute and say that $2xy = x+y$ , and subtract $y$ from both sides, and then divide by $y$ , getting the equation $\frac {x}{y} = 2x-1$ , and doing the same thing with $x$ to get $\frac {y}{x} = 2y-1$ . Adding these equations, we get the desired sum to be $2(x+y) - 2$ , or $20-2$ which is equal to $\boxed {018}$ .
~ E___

## Solution 8 (Quadratic Equation)
You can call the side length of the square 1. Call length AE x and solve the quadratic equation x^2+1-2x+x^2=9/10 with the quadratic formula.

## Video Solution by OmegaLearn
https://youtu.be/FWmrHV1dWPM?t=39
~ pi_is_3.14

## Video Solution
https://www.youtube.com/watch?v=kz3ZX4PT-_0 ~Shreyas S
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
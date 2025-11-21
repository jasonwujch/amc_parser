# 2014 AIME I Problem 14

## Problem

Let $m$ be the largest real solution to the equation

$\frac{3}{x-3}+\frac{5}{x-5}+\frac{17}{x-17}+\frac{19}{x-19}=x^2-11x-4$

There are positive integers $a$ , $b$ , and $c$ such that $m=a+\sqrt{b+\sqrt{c}}$ . Find $a+b+c$ .

## Solution 1
The first step is to notice that the 4 on the right hand side can simplify the terms on the left hand side. If we distribute 1 to $\frac{3}{x-3}$ , then the fraction becomes of the form $\frac{x}{x - 3}$ . A similar cancellation happens with the other four terms. If we assume $x = 0$ is not the highest solution (which is true given the answer format) we can cancel the common factor of $x$ from both sides of the equation.
$\frac{1}{x - 3} + \frac{1}{x - 5} + \frac{1}{x - 17} + \frac{1}{x - 19} = x - 11$
Then, if we make the substitution $y = x - 11$ , we can further simplify.
$\frac{1}{y + 8} + \frac{1}{y + 6} + \frac{1}{y - 6} + \frac{1}{y - 8} =y$
If we group and combine the terms of the form $y - n$ and $y + n$ , we get this equation:
$\frac{2y}{y^2 - 64} + \frac{2y}{y^2 - 36} = y$
Then, we can cancel out a $y$ from both sides, knowing that $x = 11$ is not a possible solution given the answer format. After we do that, we can make the final substitution $z = y^2$ .
$\frac{2}{z - 64} + \frac{2}{z - 36} = 1$
$2z - 128 + 2z - 72 = (z - 64)(z - 36)$
$4z - 200 = z^2 - 100z + 64(36)$
$z^2 - 104z + 2504 = 0$
Using the quadratic formula, we get that the largest solution for $z$ is $z = 52 + 10\sqrt{2}$ . Then, repeatedly substituting backwards, we find that the largest value of $x$ is $11 + \sqrt{52 + \sqrt{200}}$ . The answer is thus $11 + 52 + 200 = \boxed{263}$
Note: When $x$ is barely larger than $19$ , then $\frac{19}{x-19}$ is very large, so the left side of the equation approaches infinity as $x$ approaches $19$ from the side greater than $19$ . However, we also know as $x$ gets very large, the fractions get smaller as the left side approaches $0$ . Since the quadratic on the right side is increasing and positive when $x=19$ , the equation will be true at a certain $x>19.$ So, we don't have to assume there is an answer $x>0.$

## Solution 2
Proceed as with Solution 1 until we get the following.
$\frac{2y}{y^2 - 64} + \frac{2y}{y^2 - 36} = y \implies$
$\frac{1}{y^2 - 64} + \frac{1}{y^2 - 36} = \frac{1}{2}.$
Here, we may also use a slightly different substitution, $z = y^2 - 50.$ This gives:
$\frac{1}{z - 14} + \frac{1}{z + 14} = \frac{1}{2} \implies$
$\frac{2z}{z^2 - 196} = \frac{1}{2} \implies$
$z^2 - 4z - 196 = 0.$
We now have a simpler quadratic, eliminating tedious and potentially error-prone calculations. Following through, we get $z = 2 + \sqrt{200} \implies y = \sqrt{52 + \sqrt{200}}$ as desired.

## Video Solution by Punxsutawney Phil
https://youtu.be/pNsmv333SE0

## Video Solution by Mathematical Dexterity (Pure magic!)
https://www.youtube.com/watch?v=7b7IPOYZbrk

## Video Solution: Math Bear presents... A Fun Algebra Equation Problem
https://www.youtube.com/watch?v=1hdYnbm4Tvo
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
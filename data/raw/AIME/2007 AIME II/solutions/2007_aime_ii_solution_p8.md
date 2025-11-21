# 2007 AIME II Problem 8

## Problem

A rectangular piece of paper measures 4 units by 5 units. Several lines are drawn parallel to the edges of the paper. A rectangle determined by the intersections of some of these lines is called basic if

Given that the total length of all lines drawn is exactly 2007 units, let $N$ be the maximum possible number of basic rectangles determined. Find the remainder when $N$ is divided by 1000.

1 Problem

- 1 Problem

- 2 Solution 2.1 Solution 1 2.2 Solution 2

- 3 Video Solution

- 4 See also

- 2.1 Solution 1

- 2.2 Solution 2

## Solution

## Solution 1
Denote the number of horizontal lines drawn as $x$ , and the number of vertical lines drawn as $y$ . The number of basic rectangles is $(x - 1)(y - 1)$ . $5x + 4y = 2007 \Longrightarrow y = \frac{2007 - 5x}{4}$ . Substituting, we find that $(x - 1)\left(-\frac 54x + \frac{2003}4\right)$ .
FOIL this to get a quadratic, $-\frac 54x^2 + 502x - \frac{2003}4$ . Use $\frac{-b}{2a}$ to find the maximum possible value of the quadratic: $x = \frac{-502}{-2 \cdot \frac 54} = \frac{1004}5 \approx 201$ . However, this gives a non-integral answer for $y$ . The closest two values that work are $(199,253)$ and $(203,248)$ .
We see that $252 \cdot 198 = 49896 > 202 \cdot 247 = 49894$ . The solution is $\boxed{896}$ .

## Solution 2
We realize that drawing $x$ vertical lines and $y$ horizontal lines, the number of basic rectangles we have is $(x-1)(y-1)$ . The easiest possible case to see is $223$ vertical and $223$ horizontal lines, as $(4+5)223 = 2007$ . Now, for every 4 vertical lines you take away, you can add 5 horizontal lines, so you basically have the equation $(222-4x)(222+5x)$ maximize.
Expanded, this gives $-20x^{2}+222x+222^{2}$ . From $-\frac{b}{2a}$ you get that the vertex is at $x=\frac{111}{20}$ . This is not an integer though, so you see that when $x=5$ , you have $-20*25+222*5+222^{2}$ and that when x=6, you have $-20*36+222*6+222^{2}$ . $222 > 20*11$ , so the maximum integral value for x occurs when $x=6$ . Now you just evaluate $-20*36+222*6+222^{2}\mod 1000$ which is ${896}$ .

## Video Solution
2007 AIME II #8
MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
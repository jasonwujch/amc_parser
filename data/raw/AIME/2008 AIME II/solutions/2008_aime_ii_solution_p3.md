# 2008 AIME II Problem 3

## Problem

A block of cheese in the shape of a rectangular solid measures $10$ cm by $13$ cm by $14$ cm. Ten slices are cut from the cheese. Each slice has a width of $1$ cm and is cut parallel to one face of the cheese. The individual slices are not necessarily parallel to each other. What is the maximum possible volume in cubic cm of the remaining block of cheese after ten slices have been cut off?

## Solution
Let the lengths of the three sides of the rectangular solid after the cutting be $a,b,c$ , so that the desired volume is $abc$ . Note that each cut reduces one of the dimensions by one, so that after ten cuts, $a+b+c = 10 + 13 + 14 - 10 = 27$ . By AM-GM , $\frac{a+b+c}{3} = 9 \ge \sqrt[3]{abc} \Longrightarrow abc \le \boxed{729}$ . Equality is achieved when $a=b=c=9$ , which is possible if we make one slice perpendicular to the $10$ cm edge, four slices perpendicular to the $13$ cm edge, and five slices perpendicular to the $14$ cm edge.

## Solution 2
A more intuitive way to solve it is by seeing that to keep the volume of the rectangular cheese the greatest, we must slice the cheese off to decrease the greatest length of the cheese (this is easy to check). Here are the ten slices:
${10, 13, 14} \rightarrow {10, 13, 13} \rightarrow {10, 12, 13} \rightarrow {10, 12, 12} \rightarrow {10, 11, 12} \rightarrow {10, 11, 11} \rightarrow {10, 10, 11} \rightarrow {10, 10, 10} \rightarrow {9, 10, 10} \rightarrow {9, 9, 10} \rightarrow {9, 9, 9}.$
So the greatest possible volume is thus $9 \times 9 \times 9 = \boxed{729}$
These problems are copyrighted © by the Mathematical Association of America.
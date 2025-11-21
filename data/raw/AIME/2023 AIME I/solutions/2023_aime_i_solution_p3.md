# 2023 AIME I Problem 3

## Problem

A plane contains $40$ lines, no $2$ of which are parallel. Suppose that there are $3$ points where exactly $3$ lines intersect, $4$ points where exactly $4$ lines intersect, $5$ points where exactly $5$ lines intersect, $6$ points where exactly $6$ lines intersect, and no points where more than $6$ lines intersect. Find the number of points where exactly $2$ lines intersect.

## Solution
In this solution, let -line points be the points where exactly $n$ lines intersect. We wish to find the number of $2$ -line points.
There are $\binom{40}{2}=780$ pairs of lines. Among them:
- The $3$ -line points account for $3\cdot\binom32=9$ pairs of lines.
- The $4$ -line points account for $4\cdot\binom42=24$ pairs of lines.
- The $5$ -line points account for $5\cdot\binom52=50$ pairs of lines.
- The $6$ -line points account for $6\cdot\binom62=90$ pairs of lines.
It follows that the $2$ -line points account for $780-9-24-50-90=\boxed{607}$ pairs of lines, where each pair intersect at a single point.
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)
~MRENTHUSIASM
Six Seven :)

## Video Solution by TheBeautyofMath
https://youtu.be/3fC11X0LwV8
~IceMatrix
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
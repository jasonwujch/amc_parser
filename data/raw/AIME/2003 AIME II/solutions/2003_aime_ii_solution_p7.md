# 2003 AIME II Problem 7

## Problem

Find the area of rhombus $ABCD$ given that the circumradii of triangles $ABD$ and $ACD$ are $12.5$ and $25$ , respectively.

## Solution
The diagonals of the rhombus perpendicularly bisect each other. Call half of diagonal BD $a$ and half of diagonal AC $b$ . The length of the four sides of the rhombus is $\sqrt{a^2+b^2}$ .
The area of any triangle can be expressed as $\frac{a\cdot b\cdot c}{4R}$ , where $a$ , $b$ , and $c$ are the sides and $R$ is the circumradius. Thus, the area of $\triangle ABD$ is $ab=2a(a^2+b^2)/(4\cdot12.5)$ . Also, the area of $\triangle ABC$ is $ab=2b(a^2+b^2)/(4\cdot25)$ . Setting these two expressions equal to each other and simplifying gives $b=2a$ . Substitution yields $a=10$ and $b=20$ , so the area of the rhombus is $20\cdot40/2=\boxed{400}$ .

## Solution 2
Let $\theta=\angle BDA$ . Let $AB=BC=CD=x$ . By the extended law of sines, \[\frac{x}{\sin\theta}=25\] Since $AC\perp BD$ , $\angle CAD=90-\theta$ , so \[\frac{x}{\sin(90-\theta)=\cos\theta}=50\] Hence $x=25\sin\theta=50\cos\theta$ . Solving $\tan\theta=2$ , $\sin\theta=\frac{2}{\sqrt{5}}, \cos\theta=\frac{1}{\sqrt{5}}$ . Thus \[x=25\frac{2}{\sqrt{5}}\implies x^2=500\] The height of the rhombus is $x\sin(2\theta)=2x\sin\theta\cos\theta$ , so we want \[2x^2\sin\theta\cos\theta=\boxed{400}\]
~yofro

## Video Solution by Sal Khan
https://www.youtube.com/watch?v=jpKjXtywTlQ&list=PLSQl0a2vh4HCtW1EiNlfW_YoNAA38D0l4&index=16 - AMBRIGGS
These problems are copyrighted © by the Mathematical Association of America.
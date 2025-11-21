# 2015 AMC 8 Problem 19

## Problem

A triangle with vertices as $A=(1,3)$ , $B=(5,1)$ , and $C=(4,4)$ is plotted on a $6\times5$ grid. What fraction of the grid is covered by the triangle?

$\textbf{(A) }\frac{1}{6} \qquad \textbf{(B) }\frac{1}{5} \qquad \textbf{(C) }\frac{1}{4} \qquad \textbf{(D) }\frac{1}{3} \qquad \textbf{(E) }\frac{1}{2}$

[asy] draw((1,0)--(1,5),linewidth(.5)); draw((2,0)--(2,5),linewidth(.5)); draw((3,0)--(3,5),linewidth(.5)); draw((4,0)--(4,5),linewidth(.5)); draw((5,0)--(5,5),linewidth(.5)); draw((6,0)--(6,5),linewidth(.5)); draw((0,1)--(6,1),linewidth(.5)); draw((0,2)--(6,2),linewidth(.5)); draw((0,3)--(6,3),linewidth(.5)); draw((0,4)--(6,4),linewidth(.5)); draw((0,5)--(6,5),linewidth(.5)); draw((0,0)--(0,6),EndArrow); draw((0,0)--(7,0),EndArrow); draw((1,3)--(4,4)--(5,1)--cycle); label("$y$",(0,6),W); label("$x$",(7,0),S); label("$A$",(1,3),dir(210)); label("$B$",(5,1),SE); label("$C$",(4,4),dir(100)); [/asy]

## Solutions

## Solution 1
The area of $\triangle ABC$ is equal to half the product of its base and height. By the Pythagorean Theorem, we find its height is $\sqrt{1^2+2^2}=\sqrt{5}$ , and its base is $\sqrt{2^2+4^2}=\sqrt{20}$ . We multiply these and divide by $2$ to find the area of the triangle is $\frac{\sqrt{5 \cdot 20}}2=\frac{\sqrt{100}}2=\frac{10}2=5$ . Since the grid has an area of $30$ , the fraction of the grid covered by the triangle is $\frac 5{30}=\boxed{\textbf{(A) }\frac{1}{6}}$ .

## Solution 2
Note angle $\angle ACB$ is right; thus, the area is $\sqrt{1^2+3^2} \times \sqrt{1^2+3^2}\times \dfrac{1}{2}=10 \times \dfrac{1}{2}=5$ ; thus, the fraction of the total is $\dfrac{5}{30}=\boxed{\textbf{(A)}~\dfrac{1}{6}}$ .

## Solution 3
By the Shoelace Theorem , the area of $\triangle ABC=|\dfrac{1}{2}(15+4+4-1-20-12)|=|\dfrac{1}{2}(-10)|=5$ .
This means the fraction of the total area is $\dfrac{5}{30}=\boxed{\textbf{(A)}~\dfrac{1}{6}}$ .

## Solution 4
The smallest rectangle that follows the grid lines and completely encloses $\triangle ABC$ has an area of $12$ , where $\triangle ABC$ splits the rectangle into four triangles. The area of $\triangle ABC$ is therefore $12 - (\frac{4 \cdot 2}{2}+\frac{3 \cdot 1}{2}+\frac{3 \cdot 1}{2}) = 12 - (4 + \frac{3}{2} + \frac{3}{2}) = 12 - 7 = 5$ . That means that $\triangle ABC$ takes up $\frac{5}{30} = \boxed{\textbf{(A)}~\frac{1}{6}}$ of the grid.

## Solution 5 (Very much recommended to learn this)
Using Pick's Theorem , the area of the triangle is $4 + \dfrac{4}{2} - 1=5$ . Therefore, the triangle takes up $\dfrac{5}{30}=\boxed{\textbf{(A)}~\frac{1}{6}}$ of the grid.

## Solution 6 (Heron's Formula, Not Recommended)
We can find the lengths of the sides by using the Pythagorean Theorem . Then, we apply Heron's Formula to find the area. \[\sqrt{\left(\frac{\sqrt{10}+\sqrt{10}+2\sqrt{5}}{2}\right)\left(\frac{\sqrt{10}+\sqrt{10}+2\sqrt{5}}{2}-\sqrt{10}\right)\left(\frac{\sqrt{10}+\sqrt{10}+2\sqrt{5}}{2}-\sqrt{10}\right)\left(\frac{\sqrt{10}+\sqrt{10}+2\sqrt{5}}{2}-2\sqrt{5}\right)}.\] This simplifies to \[\sqrt{\left(\sqrt{10}+\sqrt{5}\right)\left(\sqrt{10}+\sqrt{5}-\sqrt{10}\right)\left(\sqrt{10}+\sqrt{5}-\sqrt{10}\right)\left(\sqrt{10}+\sqrt{5}-2\sqrt{5}\right)}.\] Again, we simplify to get \[\sqrt{\left(\sqrt{10}+\sqrt{5}\right)\left(\sqrt{5}\right)\left(\sqrt{5}\right)\left(\sqrt{10}-\sqrt{5}\right)}.\] The middle two terms inside the square root multiply to $5$ , and the first and last terms inside the square root multiply to $\sqrt{10}^2-\sqrt{5}^2=10-5=5.$ This means that the area of the triangle is \[\sqrt{5\cdot 5}=5.\] The area of the grid is $6\cdot 5=30.$ Thus, the answer is $\frac{5}{30}=\boxed{\textbf{(A) }\frac{1}{6}}$ .

## Solution 7 (Simple Deduction)
First, count the number of shapes inside the main triangle (you should count 10). Then, upon closer inspection, most of the shapes that are not a single unit on the triangle can be created by connecting another shape. The only exceptions are one shape that is a single unit and one that would need 2 shapes connected to it to make a single unit. On average, you need to connect 2 shapes to make a unit. Knowing this, if there are 10 shapes and you require 2 shapes to make a unit, 10 divided by 2 equals 5, which is the area.5 is 1/6 of 30(the total of the graph) and so the final answer is $\frac{5}{30}=\boxed{\textbf{(A) }\frac{1}{6}}$ . -Themathnerd3.14

## Video Solution (HOW TO THINK CRITICALLY!!!)
https://youtu.be/ZOEG-KfBA2E
~Education, the Study of Everything

## Video Solution
https://youtu.be/EyDGtLc6xGE
~savannahsolver

## Video Solution by OmegaLearn
https://youtu.be/j3QSD5eDpzU?t=507
### See Also
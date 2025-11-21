# 2018 AMC 8 Problem 20

## Problem

In $\triangle ABC,$ a point $E$ is on $\overline{AB}$ with $AE=1$ and $EB=2.$ Point $D$ is on $\overline{AC}$ so that $\overline{DE} \parallel \overline{BC}$ and point $F$ is on $\overline{BC}$ so that $\overline{EF} \parallel \overline{AC}.$ What is the ratio of the area of $CDEF$ to the area of $\triangle ABC?$

[asy] size(7cm); pair A,B,C,DD,EE,FF; A = (0,0); B = (3,0); C = (0.5,2.5); EE = (1,0); DD = intersectionpoint(A--C,EE--EE+(C-B)); FF = intersectionpoint(B--C,EE--EE+(C-A)); draw(A--B--C--A--DD--EE--FF,black+1bp); label("$A$",A,S); label("$B$",B,S); label("$C$",C,N); label("$D$",DD,W); label("$E$",EE,S); label("$F$",FF,NE); label("$1$",(A+EE)/2,S); label("$2$",(EE+B)/2,S); [/asy]

$\textbf{(A) } \frac{4}{9} \qquad \textbf{(B) } \frac{1}{2} \qquad \textbf{(C) } \frac{5}{9} \qquad \textbf{(D) } \frac{3}{5} \qquad \textbf{(E) } \frac{2}{3}$

## Solution 1
By similar triangles, we have $[ADE] = \frac{1}{9}[ABC]$ . Similarly, we see that [mathjax][BEF] = \dfrac{4}{9}[ABC][/mathjax]. Using this information, we get \[[ACFE] = \frac{5}{9}[ABC].\] Then, since $[ADE] = \frac{1}{9}[ABC]$ , it follows that the [mathjax][CDEF] = \dfrac{4}{9}[ABC][/mathjax]. Thus, the answer would be $\boxed{\textbf{(A) } \frac{4}{9}}$ .
Sidenote: [mathjax][ABC][/mathjax] denotes the area of triangle [mathjax]ABC[/mathjax]. Similarly, [mathjax][ABCD][/mathjax] denotes the area of figure [mathjax]ABCD[/mathjax].

## Solution 2
Let $a = DE$ and $b =$ the height of $\triangle ABC$ . We can extend $\triangle ABC$ to form a parallelogram, which would equal $3a \cdot 3b$ . The smaller parallelogram is $a$ times $2b$ . The smaller parallelogram is $\frac{2}{9}$ of the larger parallelogram, so the answer would be $\frac{2}{9} \cdot 2$ , since the triangle is $\frac{1}{2}$ of the parallelogram, so the answer is $\boxed{\textbf{(A) } \frac{4}{9}}$ .
By babyzombievillager with credits to many others who helped with the solution :D

## Solution 3
$\triangle{ADE} \sim \triangle{ABC} \sim \triangle{EFB}$ . We can substitute $\overline{DA}$ as $\frac{1}{3}x$ and $\overline{CD}$ as $\frac{2}{3}x$ , where $x$ is $\overline{AC}$ . Side $\overline{CB}$ having, distance $y$ , has $2$ parts also. And, $\overline{CF}$ and $\overline{FB}$ are $\frac{1}{3}y$ and $\frac{2}{3}y$ respectfully. You can consider the height of $\triangle{ADE}$ and $\triangle{EFB}$ as $z$ and $2z$ respectfully. The area of $\triangle{ADE}$ is $\frac{1\cdot z}{2}=0.5z$ because the area formula for a triangle is $\frac{1}{2}bh$ or $\frac{bh}{2}$ . The area of $\triangle{EFB}$ will be $\frac{2\cdot 2z}{2}=2z$ . So, the area of $\triangle{ABC}$ will be $\frac{3\cdot (2z+z)}{2}=\frac{3\cdot 3z}{2}=\frac{9z}{2}=4.5z$ . The area of parallelogram $CDEF$ will be $4.5z-(0.5z+2z)=4.5z-2.5z=2z$ . Parallelogram $CDEF$ to $\triangle{ABC}= \frac{2z}{4.5z}=\frac{2}{4.5}=\frac{4}{9}$ . The answer is $\boxed{\textbf{(A) } \frac{4}{9}}$ .

## Video Solution (CREATIVE ANALYSIS!!!)
https://youtu.be/ayUmpmgFi3E
~Education, the Study of Everything

## Video Solution (Meta-Solving Technique)
https://youtu.be/GmUWIXXf_uk?t=1541
~ pi_is_3.14

## Video Solution 2
https://youtu.be/V_-yIhs_Bps
~savannahsolver

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=TpsuRedYOiM&t=250s
### See Also
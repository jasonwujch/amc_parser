# 2006 AMC 10B Problem 19

## Problem

A circle of radius $2$

[asy] defaultpen(linewidth(0.8)); pair O=origin, A=(1,0), C=(0,1), B=(1,1), D=(1, sqrt(3)), E=(sqrt(3), 1), point=B; fill(Arc(O, 2, 0, 90)--O--cycle, mediumgray); clip(B--Arc(O, 2, 30, 60)--cycle); draw(Circle(origin, 2)); draw((-2,0)--(2,0)^^(0,-2)--(0,2)); draw(A--D^^C--E); label("$A$", A, dir(point--A)); label("$C$", C, dir(point--C)); label("$O$", O, dir(point--O)); label("$D$", D, dir(point--D)); label("$E$", E, dir(point--E)); label("$B$", B, SW); [/asy]

$\mathrm{(A) \ } \frac{\pi}{3}+1-\sqrt{3}\qquad \mathrm{(B) \ } \frac{\pi}{2}(2-\sqrt{3}) \qquad \mathrm{(C) \ } \pi(2-\sqrt{3})\qquad \mathrm{(D) \ } \frac{\pi}{6}+\frac{\sqrt{3}+1}{2}\qquad \mathrm{(E) \ } \frac{\pi}{3}-1+\sqrt{3}$

## Solution 1
The shaded area is equivalent to the area of sector $DOE$ minus the area of triangle $DOE$ plus the area of triangle $DBE$ .
Using the Pythagorean Theorem , $(DA)^2=(CE)^2=2^2-1^2=3$ so $DA=CE=\sqrt{3}$ .
Clearly, $DOA$ and $EOC$ are $30-60-90$ triangles with $\angle EOC = \angle DOA = 60^\circ$ . Since $OABC$ is a square, $\angle COA = 90^\circ$ .
$\angle DOE$ can be found by doing some subtraction of angles.
$\angle COA - \angle DOA = \angle DOC = \angle EOA$
$90^\circ - 60^\circ = \angle EOA = 30^\circ$
$\angle DOA - \angle EOA = \angle DOE$
$60^\circ - 30^\circ = \angle DOE = 30^\circ$
So, the area of sector $DOE$ is $\frac{30}{360} \cdot \pi \cdot 2^2 = \frac{\pi}{3}$ .
The area of triangle $DOE$ is $\frac{1}{2}\cdot 2 \cdot 2 \cdot \sin 30^\circ = 1$ .
Since $AB=CB=1$ , $DB=EB=(\sqrt{3}-1)$ . So, the area of triangle $DBE$ is $\frac{1}{2} \cdot (\sqrt{3}-1)^2 = 2-\sqrt{3}$ . Therefore, the shaded area is $(\frac{\pi}{3}) - (1) + (2-\sqrt{3}) = \boxed{\textbf{(A) }\frac{\pi}{3} + 1 - \sqrt{3}}$
OR
$\triangle{ODA}$ has the same height as $\triangle{OBD}$ which is $1.$
We already know that $BD = \sqrt{3} - 1.$
Therefore the area of $\triangle{OBD}$ is $(\sqrt{3}-1) \cdot 1 \cdot \frac{1}{2} = \frac{\sqrt{3}-1}{2}.$
Since $\triangle{OBD} = \triangle{OBE} = \frac{\sqrt{3}-1}{2}.$
Therefore the sum of the areas is $2 \cdot \frac{\sqrt{3}-1}{2} = \sqrt{3}-1.$
Then the area of the shaded area becomes $\frac{\pi}{3} - (\sqrt{3} - 1) = \boxed{\textbf{(A) }\frac{\pi}{3} +1 - \sqrt{3}}.$
~mathboy282

## Solution 2
From the Pythagorean Theorem, we can see that $DA$ is $\sqrt{3}$ . Then, $DB = DA - BA = \sqrt{3} - 1$ . The area of the shaded element is the area of sector $DOE$ minus the areas of triangle $DBO$ and triangle $EBO$ combined. Below is an image to help.
[asy] defaultpen(linewidth(0.8)); pair O=origin, A=(1,0), C=(0,1), B=(1,1), D=(1, sqrt(3)), E=(sqrt(3), 1), point=B; fill(Arc(O, 2, 0, 90)--O--cycle, mediumgray); clip(B--Arc(O, 2, 30, 60)--cycle); draw(Circle(origin, 2)); draw((-2,0)--(2,0)^^(0,-2)--(0,2)); draw(A--D^^C--E^^D--O^^E--O^^B--O); label("$A$", A, dir(point--A)); label("$C$", C, dir(point--C)); label("$O$", O, dir(point--O)); label("$D$", D, dir(point--D)); label("$E$", E, dir(point--E)); label("$B$", (1.33,1.04), SW); [/asy]
Using the Base Altitude formula, where $DB$ and $BE$ are the bases and $OA$ and $CO$ are the altitudes, respectively, $[DBO] = [EBO] = \frac{\sqrt{3}-1}{2}$ . The area of sector $DOE$ is $\frac{1}{12}$ of circle $O$ . The area of circle $O$ is $4\pi$ , and therefore we have the area of sector $DBE$ to be $\boxed{\textbf{(A) }\frac{\pi}{3} + 1 - \sqrt{3}}$ .

## Solution 3 (Using Answer Choices)
Like the first solutions, you find that the area of sector $DOE$ is $\frac{\pi}{3}$ . We also know that the triangles will not be in terms of ${\pi}$ . Looking at the answers, choices $\text{(A)}$ and $\text{(E)}$ both contain $\frac{\pi}{3}$ . However, based on the diagram, we observe that the answer must be less than $\frac {\pi}{3}$ . Only $\boxed{\textbf{(A) }\frac{\pi}{3} + 1 - \sqrt{3}}$ consists of a value less than $\frac{\pi}{3}$ .

## Solution 4
We calculate the shaded area by subtracting the unshaded area in the quarter circle from a quarter circle, which consists of two $30 ^{\circ}$ sectors and two 30-60-90 triangles minus a square. The area of the shaded region is $\frac {\pi \times 2^2}{4} - 2 ( \frac {\pi \times 2^2}{12} + \frac {\sqrt 3}{2} - 1 ) = \boxed{\textbf{(A) }\frac{\pi}{3} + 1 - \sqrt{3}}$
~thatmathsguy

## Video Solution
https://youtu.be/BmIXToyrZzY?list=PLoZ0gn0j87fcm-YyWXXnIdAcT5NLq9W2i&t=1801
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
# 2019 AMC 10B Problem 8

## Problem

The figure below shows a square and four equilateral triangles, with each triangle having a side lying on a side of the square, such that each triangle has side length $2$ and the third vertices of the triangles meet at the center of the square. The region inside the square but outside the triangles is shaded. What is the area of the shaded region?

[asy] pen white = gray(1); pen gray = gray(0.5); draw((0,0)--(2sqrt(3),0)--(2sqrt(3),2sqrt(3))--(0,2sqrt(3))--cycle); fill((0,0)--(2sqrt(3),0)--(2sqrt(3),2sqrt(3))--(0,2sqrt(3))--cycle, gray); draw((sqrt(3)-1,0)--(sqrt(3),sqrt(3))--(sqrt(3)+1,0)--cycle); fill((sqrt(3)-1,0)--(sqrt(3),sqrt(3))--(sqrt(3)+1,0)--cycle, white); draw((sqrt(3)-1,2sqrt(3))--(sqrt(3),sqrt(3))--(sqrt(3)+1,2sqrt(3))--cycle); fill((sqrt(3)-1,2sqrt(3))--(sqrt(3),sqrt(3))--(sqrt(3)+1,2sqrt(3))--cycle, white); draw((0,sqrt(3)-1)--(sqrt(3),sqrt(3))--(0,sqrt(3)+1)--cycle); fill((0,sqrt(3)-1)--(sqrt(3),sqrt(3))--(0,sqrt(3)+1)--cycle, white); draw((2sqrt(3),sqrt(3)-1)--(sqrt(3),sqrt(3))--(2sqrt(3),sqrt(3)+1)--cycle); fill((2sqrt(3),sqrt(3)-1)--(sqrt(3),sqrt(3))--(2sqrt(3),sqrt(3)+1)--cycle, white); [/asy]

$\textbf{(A) } 4 \qquad \textbf{(B) } 12 - 4\sqrt{3} \qquad \textbf{(C) } 3\sqrt{3}\qquad \textbf{(D) } 4\sqrt{3} \qquad \textbf{(E) } 16 - 4\sqrt{3}$

## Solution 1
We notice that the square can be split into $4$ congruent smaller squares, with the altitude of the equilateral triangle being the side of this smaller square. Note that area of shaded part in a quarter square is the total area of quarter square minus a white triangle (which has already been split in half).
When we split an equilateral triangle in half, we get two $30^{\circ}-60^{\circ}-90^{\circ}$ triangles. Therefore, the altitude, which is also the side length of one of the smaller squares, is $\sqrt{3}$ . We can then compute the area of the two triangles as $2 \cdot \frac{1 \cdot \sqrt{3}}{2} = \sqrt{3}$ .
The area of the each small squares is the square of the side length, i.e. $\left(\sqrt{3}\right)^2 = 3$ . Therefore, the area of the shaded region in each of the four squares is $3 - \sqrt{3}$ .
Since there are $4$ of these squares, we multiply this by $4$ to get $4\left(3 - \sqrt{3}\right) = \boxed{\textbf{(B) } 12 - 4\sqrt{3}}$ as our answer.

## Solution 2
We can see that the side length of the square is $2\sqrt{3}$ by considering the altitude of the equilateral triangle as in Solution 1. Using the Pythagorean Theorem, the diagonal of the square is thus $\sqrt{12+12}=\sqrt{24}=2\sqrt{6}$ . Because of this, the height of one of the four shaded kites is $\sqrt{6}$ . Now, we just need to find the length of that kite. By the Pythagorean Theorem again, this length is $\frac{2\sqrt{3} - 2}{2} \times \sqrt{2} = \sqrt{3} - 1 = \sqrt{6} - \sqrt{2}$ . Now using $\text{area} = \frac{1}{2} \cdot \text{length} \cdot \text{width}$ , the area of one of the four kites is $2 \sqrt{6} \times \left(\sqrt{6}-\sqrt{2}\right) = 12 - 2\sqrt{12} = \boxed{\textbf{(B) } 12 - 4\sqrt{3}}$ .

## Solution 3
Based on the previous solutions, we know that the side length of the square is $2\sqrt{3}$ . That means that the area of the square is $2\sqrt{3} \times 2\sqrt{3} = 12$
We also know that the area of one of the triangles is $\sqrt{3} \times 2 \div 2 = \sqrt{3}$ . That means that all four triangles have a total area of $\sqrt{3} \times 4 = 4\sqrt{3}$
So the answer is $12 - 4\sqrt{3} = \boxed{\textbf{(B) } 12 - 4\sqrt{3}}$ .

## Solution 4 (usage of answer choices)
From the previous solutions, we know that the side length of the square is $2\sqrt{3}$ , which means that the area of the square is $(2\sqrt{3})^2 = 12$ . Since the side lengths of the equilateral triangles are integers and not expressions containing an integer and a radical, we know that the combined areas of the triangles will be in the form $x\sqrt{3}$ . Therefore, the only solution that would work is $\boxed{\textbf{(B) }12 - 4\sqrt{3}}$ because it is the only solution with a $12$ subtracted by a multiple of the square root of $3$ .
-RuiyangWu

## Solution 5 (diagonals)
Draw the two diagonals of the square. Notice that this splits the shaded region into 8 triangles of equal area. The triangles are equilateral and have length $2$ , so their height is $\sqrt{3}$ . Adding the two heights of the triangles together, we get the square's side length of $2\sqrt{3}$ . Then we know that the length of the base of the shaded triangles is $\frac{2\sqrt{3}-2}{2}=\sqrt{3}-1$ and the height of the shaded triangle is the height of the equilateral triangle, $\sqrt{3}$ , so the area is $8\cdot\left(\frac{\left(\sqrt{3}-1\right)\sqrt{3}}{2}\right)=4\left(\sqrt{3}-1\right)\sqrt{3}=12-4\sqrt{3}$ or $\boxed{\textbf{(B) }12 - 4\sqrt{3}}$ .

## Video Solution
https://youtu.be/r7j1zniWUG4
~Education, the Study of Everything

## Video Solution
https://youtu.be/7xf_g3YQk00
~IceMatrix
https://youtu.be/KMLKF0S66Vg
~savannahsolver

## Video Solution
https://youtu.be/4_x1sgcQCp4?t=1390
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
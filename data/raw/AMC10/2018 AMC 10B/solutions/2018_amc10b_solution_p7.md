# 2018 AMC 10B Problem 7

## Problem

In the figure below, $N$ congruent semicircles lie on the diameter of a large semicircle, with their diameters covering the diameter of the large semicircle with no overlap. Let $A$ be the combined area of the small semicircles and $B$ be the area of the region inside the large semicircle but outside the semicircles. The ratio $A:B$ is $1:18$ . What is $N$ ?

[asy] draw((0,0)--(18,0)); draw(arc((9,0),9,0,180)); filldraw(arc((1,0),1,0,180)--cycle,gray(0.8)); filldraw(arc((3,0),1,0,180)--cycle,gray(0.8)); filldraw(arc((5,0),1,0,180)--cycle,gray(0.8)); filldraw(arc((7,0),1,0,180)--cycle,gray(0.8)); label("...",(9,0.5)); filldraw(arc((11,0),1,0,180)--cycle,gray(0.8)); filldraw(arc((13,0),1,0,180)--cycle,gray(0.8)); filldraw(arc((15,0),1,0,180)--cycle,gray(0.8)); filldraw(arc((17,0),1,0,180)--cycle,gray(0.8)); [/asy]

$\textbf{(A) } 16 \qquad \textbf{(B) } 17 \qquad \textbf{(C) } 18 \qquad \textbf{(D) } 19 \qquad \textbf{(E) } 36$

## Solution 1 (Work using Answer Choices)
Use the answer choices and calculate them. The one that works is $\bold{\boxed{\text{(D)19}}}$ .
~Flame_Thrower

## Solution 2 (More Algebraic Approach)
Let the number of semicircles be $n$ and let the radius of each semicircle be $r$ . To find the total area of all of the small semicircles, we have $n \cdot \frac{\pi \cdot r^2}{2}$ .
Next, we have to find the area of the larger semicircle. The radius of the large semicircle can be deduced to be $n \cdot r$ . So, the area of the larger semicircle is $\frac{\pi \cdot n^2 \cdot r^2}{2}$ .
Now that we have found the area of both A and B, we can find the ratio. $\frac{A}{B}=\frac{1}{18}$ , so part-to-whole ratio is $1:19$ . When we divide the area of the small semicircles combined by the area of the larger semicircles, we get $\frac{1}{n}$ . This is equal to $\frac{1}{19}$ . By setting them equal, we find that $n = 19$ . This is our answer, which corresponds to choice $\bold{\boxed{\text{(D)19}}}$ .
Solution by: Archimedes15
Note: using WLOG you could have just set $r$ as $1$ in the beginning.

## Solution 3 (Fakesolve)
Each small semicircle is $\frac{1}{N^2}$ of the large semicircle. Since $N$ small semicircles make $\frac{1}{19}$ of the large one, $\frac{N}{N^2} = \frac1{19}$ . Solving this, we get $\boxed{19}$ .
... Don't think this one works

## Video Solution
https://youtu.be/4KT0AtJZQzU
~savannahsolver

## Video Solution (HOW TO THINK CREATIVELY!!!)
https://youtu.be/qdyL6-Vmrrk
~Education, the Study of Everything

## Video Solution
https://youtu.be/NsQbhYfGh1Q?t=1120
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
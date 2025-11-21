# 2007 AIME II Problem 11

## Problem

Two long cylindrical tubes of the same length but different diameters lie parallel to each other on a flat surface . The larger tube has radius $72$ and rolls along the surface toward the smaller tube, which has radius $24$ . It rolls over the smaller tube and continues rolling along the flat surface until it comes to rest on the same point of its circumference as it started, having made one complete revolution. If the smaller tube never moves, and the rolling occurs with no slipping, the larger tube ends up a distance $x$ from where it starts. The distance $x$ can be expressed in the form $a\pi+b\sqrt{c},$ where $a,$ $b,$ and $c$ are integers and $c$ is not divisible by the square of any prime . Find $a+b+c.$

## Solution
If it weren’t for the small tube, the larger tube would travel $144\pi$ . Consider the distance from which the larger tube first contacts the smaller tube, until when it completely loses contact with the smaller tube.
Drawing the radii as shown in the diagram, notice that the hypotenuse of the right triangle in the diagram has a length of $72 + 24 = 96$ . The horizontal line divides the radius of the larger circle into $72 - 24 = 48$ on the top half, which indicates that the right triangle has leg of 48 and hypotenuse of 96, a $30-60-90 \triangle$ .
Find the length of the purple arc in the diagram (the distance the tube rolled, but not the horizontal distance). The sixty degree central angle indicates to take $\frac{60}{360} = \frac 16$ of the circumference of the larger circle (twice), while the $180 - 2(30) = 120^{\circ}$ central angle in the smaller circle indicates to take $\frac{120}{360} = \frac 13$ of the circumference. This adds up to $2 \cdot \frac 16 144\pi + \frac 13 48\pi = 64\pi$ .
The actual horizontal distance it takes can be found by using the $30-60-90 \triangle$ s. The missing leg is equal in length to $48\sqrt{3}$ . Thus, the total horizontal distance covered is $96\sqrt{3}$ .
Thus, we get $144\pi - 64\pi + 96\sqrt{3} = 80\pi + 96\sqrt{3}$ , and our answer is $\boxed{179}$ .

## Video Solution
2007 AIME II #11
MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
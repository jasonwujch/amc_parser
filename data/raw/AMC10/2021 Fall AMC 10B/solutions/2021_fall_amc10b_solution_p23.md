# 2021 Fall AMC 10B Problem 23

## Problem

Each of the $5{ }$ sides and the $5{ }$ diagonals of a regular pentagon are randomly and independently colored red or blue with equal probability. What is the probability that there will be a triangle whose vertices are among the vertices of the pentagon such that all of its sides have the same color?

$(\textbf{A})\: \frac23\qquad(\textbf{B}) \: \frac{105}{128}\qquad(\textbf{C}) \: \frac{125}{128}\qquad(\textbf{D}) \: \frac{253}{256}\qquad(\textbf{E}) \: 1$

## Solution 1
Instead of finding the probability of a same-colored triangle appearing, let us find the probability that one does not appear. After drawing the regular pentagon out, note the topmost vertex; it has 4 sides/diagonals emanating outward from it. We do casework on the color distribution of these sides/diagonals.
$\textbf{Case 1}$ : all 4 are colored one color. In that case, all of the remaining sides must be of the other color to not have a triangle where all three sides are of the same color. We can correspondingly fill out each color based on this constraint, but in this case you will always end up with a triangle where all three sides have the same color by inspection.
$\textbf{Case 2}$ : 3 are one color and one is the other. Following the steps from the previous case, you can try filling out the colors, but will always arrive at a contradiction so this case does not work either.
$\textbf{Case 3}$ : 2 are one color and 2 are of the other color. Using the same logic as previously, we can color the pentagon 2 different ways by inspection to satisfy the requirements. There are ${4\choose2}$ ways to color the original sides/diagonals and 2 ways after that to color the remaining ones for a total of $6\cdot 2 = 12$ ways to color the pentagon so that no such triangle has the same color for all of its sides.
These are all the cases, and there are a total of $2^{10}$ ways to color the pentagon. Therefore the answer is $1-\frac{12}{1024} = 1-\frac{3}{256} = \frac{253}{256} = \boxed{D}$
~KingRavi

## Solution 2 (Ramsey's Theorem)
This problem is related to a special case of Ramsey's Theorem , R(3, 3) = 6 . Suppose we color every edge of a $6$ vertex complete graph $(K_6)$ with $2$ colors, there must exist a $3$ vertex complete graph $(K_3)$ with all it's edges in the same color. That is, $K_6$ with edges in $2$ colors contains a monochromatic $K_3$ . For $K_5$ with edges in $2$ colors, a monochromatic $K_3$ does not always exist.
This is a problem about the probability of a monochromatic $K_3$ exist in a $5$ vertex complete graph $K_5$ with edges in $2$ colors.
Choose a vertex, it has $4$ edges.
$\textbf{Case 1}$ : When $3$ or more edges are the same color, there must exist a monochromatic $K_3$ . Suppose the color is red, as shown below.
There is only $1$ way to color all the edges in the same color. There is $\binom{4}{3} = 4$ ways to color $3$ edges in the same color. There are $2$ colors. The probability of $3$ or more edges the same color is $\frac{(1 + 4) \cdot 2}{2^4} = \frac{5}{8}$ . So the probability of containing a monochromatic $K_3$ is $\frac{5}{8}$ .
$\textbf{Case 2}$ : When $2$ edges are the same color, graphs that does not contain a monochromatic $K_3$ can exist. The following diagram shows steps to obtain graphs that does not contain a monochromatic $K_3$ .
There are $\binom{4}{2} = 6$ ways to choose $2$ edges with the same color. For the other $4$ vertices there are $\binom{4}{2} = 6$ edges among them, there are $2^6 = 64$ ways to color the edges. There are only $2$ cases without a monochromatic $K_3$ .
So the probability without monochromatic $K_3$ is $\frac{2}{64} = \frac{1}{32}$ .
The probability with monochromatic $K_3$ is $1 - \frac{1}{32} = \frac{31}{32}$ .
From case 1 and case 2, the probability with monochromatic $K_3$ is $\frac{5}{8} + \left( 1 - \frac{5}{8} \right) \cdot \frac{31}{32} = \boxed{(\textbf{D}) \frac{253}{256}}$
~ isabelchen

## Solution 3 (Elementary Casework)
We can break this problem down into cases based on the distribution of the two colors throughout the $5$ sides(not diagonals) of the pentagon. This idea comes from the fact that if you play around with the sides for a while and their colors, you will see that the interior diagonals actually depend largely on the colors of the five exterior sides. The total number of combinations is $2^{10} = 1024$ . We will be counting the number of arrangements in which there are no triangles with all $3$ sides the same color, and we can subtract from the total(complementary counting).
- Exterior sides are the five sides of the regular pentagon
- Interior Diagonals are the five diagonals inside the pentagon made by the connection of two non-adjacent vertices
Case $1$ : The five exterior sides are all blue or all red.
There are $2$ options for the color given in the title of this case, and for each color, only one option is given for the exterior(All $5$ sides the same color; either Red or Blue). Once you color the five sides a single color, it is simple to notice that all the $5$ interior diagonals must be in the other color which the sides are not. To make it more clear, if all of the $5$ exterior sides are blue, all of the $5$ interior diagonals must be red, and if all of the $5$ exterior sides are red, all of the $5$ interior diagonals must be blue. This gives us a total of $2$ (Choices of Colors) $\cdot 1$ (Configuration for particular color existing on all 5 exterior edges) $= 2$ ways.
Case $2$ : Four of the five exterior sides are in one color, while the remaining one exterior side is in the other color.
There are $2$ ways to choose which color occupies four exterior sides and which color occupies the remaining one. Either we can have four red and one blue, or four blue and one red, which are the $2$ ways mentioned above. When we calculated the total number of combinations, we took into account that each segment could either be red or blue which gives $2$ choices for each of $10$ segments yielding $2^{10}$ . What you must understand is that when we calculated this total, we did not account for any rotations or reflections or any other symmetry. For the same reason, we must not account for any symmetry such as rotations or reflections when calculating the number of arrangements where there is not a triangle consisting of three sides of the same color. There are $5$ ways to arrange the one blue and four reds or one red and four blues on the $5$ exterior sides(draw it out to see), and once you start playing with our condition, that no triangle may have all three sides in the same color, you will see that this case actually yields zero solutions as there comes a triangle in the middle consisting of all three sides of the same color. Hence this case yields $0$ ways.
Case $3$ : Three of the five exterior sides in one color and the remaining two in another color.
There are two sub-cases, one in which the two exterior sides which are colored differently from the other three are adjacent, and the other case in which they are separated by one other exterior side.
Subcase $1$ : The case in which the two exterior sides colored differently from the other three are adjacent.
If you draw the five exterior sides with two colored in one color and the other three colored in a different color, you will see, that there are absolutely no ways to color the interior diagonals such that no triangle with all three sides the same color exists. This subcase yields $0$ ways.
Subcase $2$ : The case in which the two exterior sides colored differently from the other three are separated by another exterior side. There are $5$ arrangements for the exterior (draw and see for yourself) and the colors can be swapped with each other and since each of the exterior configurations force a particular interior configuration, this yields $2 \cdot 5=10$ ways.
In total, there are $10+2=12$ ways, such that no triangle has all three sides in the same color. This yields $1024-12=1012$ ways such that there is a triangle such that it has all three sides in the same color. Thus, the probability is: $\frac{1012}{2^{10}} = \boxed{(\textbf{D}) \frac{253}{256}}$ ~Shiva Kannan

## Video Solution 1
https://www.youtube.com/watch?v=Iaz1dT_XBHU
~Interstigation

## Video Solution 2
https://youtu.be/RqKYqCaZBlo
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
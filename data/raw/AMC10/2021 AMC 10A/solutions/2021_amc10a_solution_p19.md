# 2021 AMC 10A Problem 19

## Problem

The area of the region bounded by the graph of \[x^2+y^2 = 3|x-y| + 3|x+y|\] is $m+n\pi$ , where $m$ and $n$ are integers. What is $m + n$ ?

$\textbf{(A)} ~18\qquad\textbf{(B)} ~27\qquad\textbf{(C)} ~36\qquad\textbf{(D)} ~45\qquad\textbf{(E)} ~54$

## Solution 1
In order to attack this problem, we can use casework on the sign of $|x-y|$ and $|x+y|$ .
Case 1: $|x-y|=x-y, |x+y|=x+y$
Substituting and simplifying, we have $x^2-6x+y^2=0$ , i.e. $(x-3)^2+y^2=3^2$ , which gives us a circle of radius $3$ centered at $(3,0)$ .
Case 2: $|x-y|=y-x, |x+y|=x+y$
Substituting and simplifying again, we have $x^2+y^2-6y=0$ , i.e. $x^2+(y-3)^2=3^2$ . This gives us a circle of radius $3$ centered at $(0,3)$ .
Case 3: $|x-y|=x-y, |x+y|=-x-y$
Doing the same process as before, we have $x^2+y^2+6y=0$ , i.e. $x^2+(y+3)^2=3^2$ . This gives us a circle of radius $3$ centered at $(0,-3)$ .
Case 4: $|x-y|=y-x, |x+y|=-x-y$
One last time: we have $x^2+y^2+6x=0$ , i.e. $(x+3)^2+y^2=3^2$ . This gives us a circle of radius $3$ centered at $(-3,0)$ .
After combining all the cases and drawing them on the Cartesian Plane, this is what the diagram looks like:
[asy] size(10cm); Label f; f.p=fontsize(7); xaxis(-8,8,Ticks(f, 1.0)); yaxis(-8,8,Ticks(f, 1.0)); draw(arc((-3,0),3,90,270) -- cycle, gray); draw(arc((0,3),3,0,180) -- cycle, gray); draw(arc((3,0),3,-90,90) -- cycle, gray); draw(arc((0,-3),3,-180,0) -- cycle, gray); draw((-3,3)--(3,3)--(3,-3)--(-3,-3)--cycle, grey); [/asy] Now, the area of the shaded region is just a square with side length $6$ with four semicircles of radius $3$ . The area is $6\cdot6+4\cdot \frac{9\pi}{2} = 36+18\pi$ . The answer is $36+18$ which is $\boxed{\textbf{(E) }54}$
~Bryguy

## Solution 2
A somewhat faster variant of solution 1 is to use a bit of symmetry in order to show that the remaining three cases are identical to Case 1 in the above solution, up to rotations by $90^{\circ}$ about the origin. This allows us to quickly sketch the region after solving Case 1.
Upon simplifying Case 1, we obtain $(x-3)^2 + y^2 = 3^2$ which is a circle of radius 3 centered at $(3,0)$ . We remark that only the points on the semicircle where $x \ge 3$ work here, since Case 1 assumes $x-y \ge 0$ and $x+y \ge 0$ . Next, we observe that an ordered pair is a solution to the given equation if and only if any of its $90^{\circ}$ rotations about the origin is a solution. This follows as the value of $x^2+y^2-3(|x-y|+|x+y|)$ is invariant to $90^{\circ}$ rotations, since $x^2+y^2$ simply represents the square of the distance to the origin (which is unchanged upon rotation), and $|x-y|+|x+y|$ is the sum of the distances to the lines $y=x$ and $y=-x$ , multiplied by $\sqrt{2}$ (also unchanged upon $90^{\circ}$ rotation).
By the above observation, we can quickly sketch the remainder of the region, and the area is $\boxed{\textbf{(E) }54}$ as above.
~scrabbler94

## Solution 3 (Guessing)
Assume $y$ = $0$ . We get that $x$ = $6$ . That means that this figure must contain the points $(0,6), (6,0), (0, -6), (-6, 0)$ . Now, assume that $x$ = $y$ . We get that $x$ = $3 \sqrt 3$ . We get the points $(3,3), (3,-3), (-3, 3), (-3, -3)$ .
Since this contains $x^2 + y^2$ , assume that there are circles. Therefore, we can guess that there is a center square with area $6 \cdot 6$ = $36$ and $4$ semicircles with radius $3$ . We get $4$ semicircles with area $4.5 \pi$ , and therefore the answer is $36+18$ = $\boxed {(E)54}$
~Arcticturn
### Remark
This problem asks for the area of the union of these four circles :
### Rotation by 45 degrees
with the help of rotation https://www.wolframalpha.com/input/?i=rotate+45+degrees , we can simplify the equation to $a^2 + b^2 = 3\sqrt2|a| + 3\sqrt2|b|$ . Then follow the previous question https://artofproblemsolving.com/wiki/index.php/2016_AMC_10B_Problems/Problem_21
~aliciawu

## Video Solution by OmegaLearn (Using Absolute Value Properties to Graph)
https://youtu.be/EHHpB6GIGPc
~ pi_is_3.14

## Video Solution by The Power Of Logic (Graphing)
https://youtu.be/-pa72wBA85Y

## Video Solution by TheBeautyofMath
https://youtu.be/U6obY_kio0g
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
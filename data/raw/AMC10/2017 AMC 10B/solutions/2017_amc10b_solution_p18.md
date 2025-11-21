# 2017 AMC 10B Problem 18

## Problem

In the figure below, $3$ of the $6$ disks are to be painted blue, $2$ are to be painted red, and $1$ is to be painted green. Two paintings that can be obtained from one another by a rotation or a reflection of the entire figure are considered the same. How many different paintings are possible?

[asy] size(110); pair A, B, C, D, E, F; A = (0,0); B = (1,0); C = (2,0); D = rotate(60, A)*B; E = B + D; F = rotate(60, A)*C; draw(Circle(A, 0.5)); draw(Circle(B, 0.5)); draw(Circle(C, 0.5)); draw(Circle(D, 0.5)); draw(Circle(E, 0.5)); draw(Circle(F, 0.5)); [/asy]

$\textbf{(A)}\ 6\qquad\textbf{(B)}\ 8\qquad\textbf{(C)}\ 9\qquad\textbf{(D)}\ 12\qquad\textbf{(E)}\ 15$

## Solution 1
First we figure out the number of ways to put the $3$ blue disks. Denote the spots to put the disks as $1-6$ from left to right, top to bottom. The cases to put the blue disks are $(1,2,3),(1,2,4),(1,2,5),(1,2,6),(2,3,5),(1,4,6)$ . For each of those cases we can easily figure out the number of ways for each case, so the total amount is $2+2+3+3+1+1 = \boxed{\textbf{(D) } 12}$ .

## Solution 2 (Fast and Easy)
Notice how you can arrange the colors like a circle with three blues two reds and one green.
We want to find the compliments of all the other cases that are invalid/ same rotation or reflections.
We use the Circular Gap Theorem to solve this problem.
\[C_n(A) = \frac{n}{k} \binom{n-k-1}{k-1}\] We have three cases, there are 3 blues that are not next to each other, 2 reds that are not next to each other, or one green that isn't next to itself. Our \( k \) value is \( k \in \{1,2,3\} \).
Case 1: \( k \in \{3\} \)
We substitute \( n = 6 \) total values to orient and \( k = 3 \). We get \( C_n(A) = \frac{6}{3} \binom{6-3-1}{3-1} = 2 \cdot \binom{2}{2} = 2 \).
Case 2: \( k \in \{2\} \)
We substitute \( n = 6 \) and \( k = 2 \) to get \( C_n(A) = \frac{6}{2} \binom{6-2-1}{2-1} = 3 \cdot \binom{3}{1} = 9 \).
Case 3: \( k \in \{1\} \)
This is quite obvious, we don't need to use the formula. There is only \( 1 \) case that works here as we have \( 1 \) color and we choose \( 1 \) of them, giving us \( 1 \) case.
The total number of cases is \( 2+9+1 = 12 \).
Therefore our answer is $\boxed{\textbf{(D) } 12}$ .
Notice how we didn't need to use Burnside's Lemma .
~Pinotation

## Solution 3 (similar to solution 5 but simpler)
Denote the $6$ discs as in the first solution. Ignoring reflections or rotations, there are $\binom{6}{3} \cdot \binom{3}{2} = 60$ colorings. Now we need to count the number of fixed points under possible transformations:
1. The identity transformation. Since this doesn't change anything, there are $60$ fixed points.
2. Reflect on a line of symmetry. There are $3$ lines of reflections. Take the line of reflection going through the centers of circles $1$ and $5$ . Then, the colors of circles $2$ and $3$ must be the same, and the colors of circles $4$ and $6$ must be the same. This gives us $4$ fixed points per line of reflection.
3. Rotate by $120^\circ$ counterclockwise or clockwise with respect to the center of the diagram. Take the clockwise case for example. There will be a fixed point in this case if the colors of circles $1$ , $4$ , and $6$ will be the same. Similarly, the colors of circles $2$ , $3$ , and $5$ will be the same. This is impossible, so this case gives us $0$ fixed points per rotation.
By Burnside's Lemma , the total number of colorings is $(1 \cdot 60+3 \cdot 4+2 \cdot 0)/(1+3+2) = \boxed{\textbf{(D) } 12}$ .

## Solution 4
Note that the green disk has two possibilities; in a corner or on the side. WLOG, we can arrange these as
[asy] filldraw(circle((0,0),1),green); draw(circle((2,0),1)); draw(circle((4,0),1)); draw(circle((1,sqrt(3)),1)); draw(circle((3,sqrt(3)),1)); draw(circle((2,2sqrt(3)),1)); draw(circle((8,0),1)); filldraw(circle((10,0),1),green); draw(circle((12,0),1)); draw(circle((9,sqrt(3)),1)); draw(circle((11,sqrt(3)),1)); draw(circle((10,2sqrt(3)),1)); [/asy]
Take the first case. Now, we must pick two of the five remaining circles to fill in the red. There are $\dbinom{5}{2}=10$ of these. However, due to reflection we must divide this by two. But, in two of these cases, the reflection is itself, so we must subtract these out before dividing by 2, and add them back afterwards, giving $\frac{10-2}{2}+2=6$ arrangements in this case.
Now, look at the second case. We again must pick two of the five remaining circles, and like in the first case, two of the reflections give the same arrangement. Thus, there are also $6$ arrangements in this case.
In total, we have $6+6=\boxed{\text{\bf(D) }12}$ .
~tdeng

## Solution 5 (Burnside's Lemma)
We note that the group $G$ acting on the possible colorings is $D_3 = \{e, r, r^2, s, sr, sr^2\}$ , where $r$ is a $120^\circ$ rotation and $s$ is a reflection. In particular, the possible actions are the identity, the $120^\circ$ and $240^\circ$ rotations, and the three reflections.
We will calculate the number of colorings that are fixed under each action. Every coloring is fixed under the identity, so we count $\dfrac{6!}{3!2!1!} = 60$ fixed colorings. Note that no colorings are fixed under the rotations, since then the outer three and inner three circle must be the same color, which is impossible in our situation.
Finally, consider the reflection with a line of symmetry going through the top circle. Every fixed coloring is determined by the color of the top circle (either green or blue), and the color of the middle circles (either blue or red). Hence, there are $2\cdot 2 = 4$ colorings fixed under this reflection action. The other two actions are symmetric, so they also have $4$ fixed colorings. Hence, by Burnside's lemma, the number of unique colorings up to reflections and rotations is \[\dfrac{1}{|D_3|} (1\cdot 60 + 2\cdot 0 + 3\cdot 4) = \dfrac{1}{6}\cdot 72 = \boxed{\textbf{(D) } 12}.\]

## Solution 6
Call the ball in the top row A, the two balls in the 2nd row from left to right B and C, and the bottom rows balls from left to right D, E, and F. The total amount of paintings is $6 \cdot \dbinom{5}{2} \cdot \dbinom{3}{3} = 60$ . If we divided this number by $3$ (for rotations) and $2$ (for reflections), we would not get the right answer, because the paintings that do not change when reflected are over-subtracted. So lets find the number of over subtracted paintings. To be symmetric, ball B and C must be the same color, D and F must be the same color, and A and E can be any color because they are on the line of symmetry. Pair B,C and D,F must be blue and red or red and blue, which is $2$ possibilities. Then, Ball A has $2$ possibilities, and Ball E has $1$ possibility (the one remaining color). That means, the number of paintings that when they are reflected do not change is $2 \cdot 2 = 4.$ The total amount of these paintings, after accounting for rotations, is $4 \cdot 3 = 12.$ Then there are $60 - 12 = 48$ paintings that when reflected, change. $48/(2 \cdot 3) = 8.$ (We divided by $2 \cdot 3$ since we are accounting for rotations and reflections.) Then, adding back the $4$ paintings we subtracted off because they didn't change when reflected, we get $4 + 8 = 12.$ □ (to look professional)
~heheman

## Solution 7
Notice that the green ball can be placed in 6 different positions. If the ball is placed on the top position, bottom-left position, or bottom-right position, it can be rotated to make the green ball on the top position. Meanwhile, if the green ball is placed on the middle-left, middle-right, or bottom-middle position, it can be rotated to move the green ball to the bottom-middle position. To avoid overcounting due to rotations, we can divide this problem into two cases: the green ball is at the top position, or the green ball is at the bottom-middle position.
Consider the first case. If the green ball is placed in the top position, the other five balls can be placed in $\tbinom{5}{2}$ ways. (We choose 2 of the 5 positions to be occupied by the red ball.) In the following positions,
the position is identical under reflection over a vertical line. All other 8 positions have a reflection that is different. Thus, we can count only half of these 8 positions (because otherwise we would be over counting), but we can count both of the two special cases (since they don't make a different image when reflected. Thus, this case has $\frac{8}{2}+2=6$ cases.
In the second case, the green ball is placed in the bottom-middle position. Similarly, the other five balls can be placed in $\tbinom{5}{2}$ ways. In the special cases,
the position is identical under reflection over a vertical line. Proceeding just like the first case, there are $\frac{8}{2}+2=6$ cases.
In total, there are $6+6=\boxed{\textbf{(D) }12}$ different paintings.
~sid2012 [1]

## Video Solution by TheBeautyofMath
https://youtu.be/T7eNQISBzsc?si=vXE9H26SkMeedPmf
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
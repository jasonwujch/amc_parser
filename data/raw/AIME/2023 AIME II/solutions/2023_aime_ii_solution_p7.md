# 2023 AIME II Problem 7

## Problem

Each vertex of a regular dodecagon ( $12$ -gon) is to be colored either red or blue, and thus there are $2^{12}$ possible colorings. Find the number of these colorings with the property that no four vertices colored the same color are the four vertices of a rectangle.

## Solution 1
Note that the condition is equivalent to stating that there are no 2 pairs of oppositely spaced vertices with the same color.
Case 1: There are no pairs. This yields $2$ options for each vertices 1-6, and the remaining vertices 7-12 are set, yielding $2^6=64$ cases.
Case 2: There is one pair. Again start with 2 options for each vertex in 1-6, but now multiply by 6 since there are 6 possibilities for which pair can have the same color assigned instead of the opposite. Thus, the cases are: $2^6*6=384$
case 3: There are two pairs, but oppositely colored. Start with $2^6$ for assigning 1-6, then multiply by 6C2=15 for assigning which have repeated colors. Divide by 2 due to half the cases having the same colored opposites. $2^6*15/2=480$
It is apparent that no other cases exist, as more pairs would force there to be 2 pairs of same colored oppositely spaced vertices with the same color. Thus, the answer is: $64+384+480=\boxed{928}$
~SAHANWIJETUNGA

## Solution 2
First, we identify the geometric condition for the sentence ``four vertices colored the same color are the four vertices of a rectangle . Consider any four vertices on the dodecagon, $A$ , $B$ , $C$ , $D$ . Denote by $O$ the center of the dodecagon. Because $OA = OB = OC$ , $\angle OAB = \angle OBA$ and $\angle OBC = \angle OCB$ .
Thus, \begin{align*} \angle ABC & = \angle OBA + \angle OBC \\ & = \frac{\angle OBA + \angle OAB}{2} + \frac{\angle OBC + \angle OCB}{2} \\ & = \frac{180^\circ - \angle AOB}{2} + \frac{180^\circ - \angle COB}{2} \\ & = 180^\circ - \frac{\angle AOB + \angle COB}{2} \\ & = 180^\circ - \frac{\angle AOC}{2} . \end{align*}
Hence, $\angle ABC = 90^\circ$ if and only if $\angle AOC = 180^\circ$ . Similarly, $\angle ADC = 90^\circ$ if and only if $\angle AOC = 180^\circ$ , and $\angle BCD = 90^\circ$ (or $\angle DAB = 90^\circ$ ) if and only if $\angle BOD = 180^\circ$ .
Therefore, $ABCD$ is a rectangle if and only if two diagonals both pass through $O$ .
Now, we categorize 12 vertices into 6 groups. Each group contains 2 diagonal vertices. Next, we compute the number of coloring configurations such that the above same-color rectangles do not exist.
Case 1: Two vertices in each group has distinct colors.
For each group, we only need to determine which vertex is red. The other one must be blue. Therefore, the number of configurations in this case is $2^6$ .
Case 2: There is one group who vertices have the same color. All other groups are with vertices that have distinct colors.
We construct such an instance in the following steps.
Step 1: We determine which group has two vertices that have the same color.
The number of ways is 6.
Step 2: For the selected group, we choose a color for its two vertices.
The number of ways is 2.
Step 3: For each unselected group, we determine which vertex is red.
The number of ways is $2^5$ .
Following from the rule of product, the total number of configurations in this case is $6 \cdot 2 \cdot 2^5 = 6 \cdot 2^6$ .
Case 3: One group has two red vertices, one group has two blue vertices, and each of the other four groups has vertices with distinct colors.
We construct such an instance in the following steps.
Step 1: We determine which group has two vertices that have both red color.
The number of ways is 6.
Step 2: We determine which group has two vertices that have both blue color.
The number of ways is 5.
Step 3: For each unselected group, we determine which vertex is red.
The number of ways is $2^4$ .
Following from the rule of product, the total number of configurations in this case is $6 \cdot 5 \cdot 2^4 = 30 \cdot 2^4$ .
Putting all cases together, the total number of feasible configurations is \[ 2^6 + 6 \cdot 2^6 + 30 \cdot 2^4 = \boxed{\textbf{(928) }}. \]
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 3 (Similar to Solution 1, just reworded a bit)
Note that a rectangle is formed if and only if it's diagonals pass through the center of the dodecagon and the diagonal's endpoints are the same color.
Consider the $6$ diagonals that pass through the center. A rectangle is formed if the endpoints of some pair of them are all the same color. We can now perform casework on the diagonals:
Case $1:$ The endpoints of all the diagonals are all different (e.g. for all diagonals, the endpoints are red and blue in some order).
The amount of ways to do this is $2^6=64,$ since there are $2$ ways to order which vertice is red and which is blue for each diagonal.
Case $2:$ There exists one diagonal such that the endpoints are the same color.
There are $6$ ways to choose this diagonal, $2$ ways to choose which color it is, and $2^5$ ways to color the rest of the diagonals. Therefore, the total for this case is $6 \cdot 2 \cdot 2^5 = 384.$
Case $3:$ There exists two diagonals such that the endpoints are the same color, but they are different colors
Then, there are $6 \cdot 5=30$ ways to choose these two diagonals, and $2^4=16$ ways to color the rest, so the total for this case is $30 \cdot 16 = 480.$
Summing all of the cases, we have $64+384+480=\boxed{928}.$
~happypi31415

## Solution 4 ≈ Solution 1
\[\text{First, we notice that a rectangle is made from two pairs of vertices 1/2 turn away from each other.}\]
\[\textit{Note: The image is }\frac{\textit{280}}{\textit{841}}\approx\frac{\textit{1}}{\textit{3}}\textit{ size.}\]
\[\text{For there to be no rectangles, there can be at most one same-colored pair for each color and the rest need to have one red and blue.}\]
\[\textit{\underline{Case 1: \textbf{No pairs}}}\]
\[\text{Each pair has two ways to color: One red or the other red. Thus, there are }2^6=\boxed{64}\text{ ways in this case.}\]
\[\textit{\underline{Case 2: \textbf{One red pair}}}\]
\[\text{The red pair has }\binom{6}{1}\text{ positions. All the rest still have two ways. Therefore, there are }\binom{6}{1}\cdot 2^5=\frac{6}{1}\dot 2^5=6\cdot 32=\boxed{192} \text{ ways in this case.}\]
\[\textit{\underline{Case 3: \textbf{One blue pair}}}\]
\[\text{This is the same as the one red pair case so there are still }\binom{6}{1}\cdot 2^5=6\cdot 2^5=6\cdot 32=\boxed{192}\text{ ways.}\]
\[\textit{\underline{Case 4: \textbf{One pair of each color}}}\]
\[\text{The red pair has }\binom{6}{1}\text{ positions. The blue pair has }\binom{5}{1}\text{ positions. All the rest still have two ways. Therefore, there are }\binom{6}{1}\cdot\binom{5}{1}\cdot 2^4=\frac{6\cdot 5=30}{1\cdot 1=1}\cdot 2^4=30\cdot 16=\boxed{480}\text{ ways in this case.}\]
\[\textit{\underline{\textbf{Solution}}}\]
\[\text{In total, there are }64+192+192+480=\boxed{928}\text{ways.}\]
~~By:afly

## Video Solution by The Power of Logic
https://youtu.be/sTOqj9OAc4o
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
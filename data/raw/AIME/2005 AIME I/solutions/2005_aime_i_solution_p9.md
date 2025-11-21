# 2005 AIME I Problem 9

## Problem

Twenty seven unit cubes are painted orange on a set of four faces so that two non-painted faces share an edge . The 27 cubes are randomly arranged to form a $3\times 3 \times 3$ cube. Given the probability of the entire surface area of the larger cube is orange is $\frac{p^a}{q^br^c},$ where $p,q,$ and $r$ are distinct primes and $a,b,$ and $c$ are positive integers , find $a+b+c+p+q+r.$

1 Problem

- 1 Problem

- 2 Solution 2.1 Solution 2

- 3 See also

- 2.1 Solution 2

## Solution
We can consider the orientation of each of the individual cubes independently. The unit cube at the center of our large cube has no exterior faces, so all of its orientations work.
For the six unit cubes and the centers of the faces of the large cube, we need that they show an orange face. This happens in $\frac{4}{6} = \frac{2}{3}$ of all orientations, so from these cubes we gain a factor of $\left(\frac{2}{3}\right)^6$ .
The twelve unit cubes along the edges of the large cube have two faces showing, and these two faces are joined along an edge. Thus, we need to know the number of such pairs that are both painted orange. We have a pair for each edge, and 7 edges border one of the unpainted faces while only 5 border two painted faces. Thus, the probability that two orange faces show for one of these cubes is $\frac{5}{12}$ , so from all of these cubes we gain a factor of $\left(\frac{5}{12}\right)^{12} = \frac{5^{12}}{2^{24}3^{12}}$ .
Finally, we need to orient the eight corner cubes. Each such cube has 3 faces showing, and these three faces share a common vertex. Thus, we need to know the number of vertices for which all three adjacent faces are painted orange. There are six vertices which are a vertex of one of the unpainted faces and two vertices which have our desired property, so each corner cube contributes a probability of $\frac{2}{8} = \frac{1}{4}$ and all the corner cubes together contribute a probability of $\left(\frac{1}{4}\right)^8 = \frac{1}{2^{16}}$
Since these probabilities are independent, the overall probability is just their product, $\frac{2^6}{3^6} \cdot \frac{5^{12}}{2^{24}3^{12}} \cdot \frac{1}{2^{16}} = \frac{5^{12}}{2^{34}\cdot 3^{18}}$ and so the answer is $2 + 3 + 5 + 12 + 34 + 18 = \boxed{074}$ .

## Solution 2
Rather than worry about the actual painted faces, consider the position of the shared edge of the non-colored faces. The six centers of the faces can be calculated in the same manner as last time, getting $\left(\frac{2}{3}\right)^6$ .
The twelve edge cubes show two faces. We want the shared edge of the non-colored faces to not be one of the edges that are exposed on the outside. There are 7 such edges that can be seen when viewed from the outside, so the probability they cannot be seen are $\left(\frac{5}{12}\right)^{12}$ .
The eight corner cubes each have 9 visible edges from the outside, so the probability that the edge of the non-colored faces is not one of those is $\left(\frac{3}{12}\right)^8 = \left(\frac{1}{4}\right)^8$ . Multiplying the probabilities together, we get the same exact solution.
As a side note, notice that the placement of the two unpainted faces is in fact of vital importance: if they were on opposite faces, the answer would be 0 because any placement of such a cube in the corner of the large cube would show one unpainted face.
These problems are copyrighted © by the Mathematical Association of America.
# 2001 AIME I Problem 15

## Problem

The numbers $1, 2, 3, 4, 5, 6, 7,$ and $8$ are randomly written on the faces of a regular octahedron so that each face contains a different number. The probability that no two consecutive numbers, where $8$ and $1$ are considered to be consecutive, are written on faces that share an edge is $m/n,$ where $m$ and $n$ are relatively prime positive integers. Find $m + n.$

## Official Solution (MAA)
It is helpful to consider the cube $ABCDEFGH$ , where the vertices of the cube represent the faces of the octahedron, and the edges of the cube represent adjacent octahedral faces. Each assignment of the numbers $1,2,3,4,5,6,7$ , and $8$ to the faces of the octahedron corresponds to a permutation of $ABCDEFGH$ , and thus to an octagonal circuit of these vertices. The cube has 16 diagonal segments that join nonadjacent vertices. In effect, the problem asks one to count octagonal circuits that can be formed by eight of these diagonals. Six of the diagonals are edges of tetrahedron $ACFH$ , six are edges of tetrahedron $DBEG$ , and four are $\textit{long}$ , joining a vertex of one tetrahedron to the diagonally opposite point from the other. Notice that each vertex belongs to exactly one long diagonal.
It follows that an octagon cannot have two successive long diagonals. Also notice that an octagonal path can jump from one tetrahedron to the other only along one of the long diagonals. It follows that an octagon must contain either 2 long diagonals separated by 3 tetrahedron edges or 4 long diagonals alternating with tetrahedron edges.
To form an octagon that contains four long diagonals, choose two opposite edges from tetrahedron $ACFH$ and two opposite edges from tetrahedron $DBEG$ . For each of the three ways to choose a pair of opposite edges from tetrahedron $ACFH$ , there are two possible ways to choose a pair of opposite edges from tetrahedron $DBEG$ . There are 6 distinct octagons of this type and $8\cdot 2$ ways to describe each of them, making 96 permutations.
To form an octagon that contains exactly two of the long diagonals, choose a three-edge path along tetrahedron $ACFH$ , which can be done in $4! = 24$ ways. Then choose a three-edge path along tetrahedron $DBEG$ which, because it must start and finish at specified vertices, can be done in only 2 ways. Since this counting method treats each path as different from its reverse, there are $8\cdot 24\cdot 2=384$ permutations of this type.
In all, there are $96 +384 = 480$ permutations that correspond to octagonal circuits formed exclusively from cube diagonals. The probability of randomly choosing such a permutation is $\tfrac{480}{8!}=\tfrac{1}{84}$ , and $m+n=\boxed{085}$ .

## Solution 1
Choose one face of the octahedron randomly and label it with $1$ . There are three faces adjacent to this one, which we will call A-faces. There are three faces adjacent to two of the A-faces, which we will call B-faces, and one face adjacent to the three B-faces, which we will call the C-face.
Clearly, the labels for the A-faces must come from the set $\{3,4,5,6,7\}$ , since these faces are all adjacent to $1$ . There are thus $5 \cdot 4 \cdot 3 = 60$ ways to assign the labels for the A-faces.
The labels for the B-faces and C-face are the two remaining numbers from the above set, plus $2$ and $8$ . The number on the C-face must not be consecutive to any of the numbers on the B-faces.
From here it is easiest to brute force the $10$ possibilities for the $4$ numbers on the B and C faces:
- 2348 (2678): 8(2) is the only one not adjacent to any of the others, so it goes on the C-face. 4(6) has only one B-face it can go to, while 2 and 3 (7 and 8) can be assigned randomly to the last two. 2 possibilities here.
- 2358 (2578): 5 cannot go on any of the B-faces, so it must be on the C-face. 3 and 8 (2 and 7) have only one allowable B-face, so just 1 possibility here.
- 2368 (2478): 6(4) cannot go on any of the B-faces, so it must be on the C-face. 3 and 8 (2 and 7) have only one allowable B-face, so 1 possibility here.
- 2458 (2568): All of the numbers have only one B-face they could go to. 2 and 4 (6 and 8) can go on the same, so one must go to the C-face. Only 2(8) is not consecutive with any of the others, so it goes on the C-face. 1 possibility.
- 2378: None of the numbers can go on the C-face because they will be consecutive with one of the B-face numbers. So this possibility is impossible.
- 2468: Both 4 and 6 cannot go on any B-face. They cannot both go on the C-face, so this possibility is impossible.
There is a total of $10$ possibilities. There are $3!=6$ permutations (rotations/reflections) of each, so $60$ acceptable ways to fill in the rest of the octahedron given the $1$ . There are $7!=5040$ ways to randomly fill in the rest of the octahedron. So the probability is $\frac {60}{5040} = \frac {1}{84}$ . The answer is $\boxed{085}$ .

## Solution 2
Consider the cube formed from the face centers of the regular octahedron. Color the vertices in a checker board fashion. We seek the number of circuits traversing the cube entirely composed of diagonals. Notice for any vertex, it can be linked to at most one different-colored vertex, i.e. its opposite vertex. Thus, there are only two possible types of circuits ( $B$ for black and $W$ for white).
Type I: $BB-WWWW-BB$ . There are $4!$ ways to arrange the black vertices and consequently two of the white vertices and $2!$ ways to arrange the other two white vertices. Since the template has a period of $8$ , there are $4!\cdot 2!\cdot 8 = 384$ circuits of type I.
Type II: $B-WW-BB-WW-B$ . There are $4!$ ways to arrange the black vertices and consequently the white vertices. Since the template has a period of $4$ , there are $4! \cdot 4 = 96$ circuits of type II.
Thus, there are $384+96=480$ circuits satisfying the given condition, out of the $8!$ possible circuits. Therefore, the desired probability is $\frac{480}{8!} = \frac{1}{84}$ . The answer is $\boxed{085}$ .

## Solution 3
As in the previous solution, consider the cube formed by taking each face of the octahedron as a vertex. Let one fixed vertex be A. Then each configuration (letting each vertex have a number value from 1-8) of A and the three vertices adjacent to A uniquely determine a configuration that satisfies the conditions, i.e. no two vertices have consecutive numbers. Thus, the number of desired configurations is equivalent to the number of ways of choosing the values of A and its three adjacent vertices.
The value of A can be chosen in 8 ways, and the 3 vertices adjacent to A can be chosen in $5\cdot4\cdot3=60$ ways, since they aren't adjacent to each other, but they can't, after all, be consecutive values to A. For example, if A=1, then the next vertex can't be 1,2 or 8, so there are 5 choices. However, the next vertex also adjacent to A can be chosen in 4 ways; it can't be equal to 1,2,8, or the value of the previously chosen vertex. With the same reasoning, the last such vertex has 3 possible choices.
The total number of ways to choose the values of the vertices of the cube independently is 8!, so our probability is thus $\frac{8\cdot60}{8!}=\frac{8\cdot5\cdot4\cdot3}{8!}=\frac{1}{84}$ , from which the answer is $\boxed{085}$ .
, the average is one per choice of 3 to border the 1, ex 5,6,7 border 2 solutions, 3,5,7 border 0 solution

## Solution 4
[asy] import three; draw((0,0,0)--(0,0,1)--(0,1,1)--(1,1,1)--(1,0,1)--(1,0,0)--(1,1,0)--(0,1,0)--(0,0,0)); draw((1,1,0)--(1,1,1)); draw((0,1,0)--(0,1,1)); draw((0,0,0)--(1,0,0)); draw((0,0,1)--(1,0,1)); for(int i = 0; i < 2; ++i) { for(int j = 0; j < 2; ++j) { for(int k = 0; k < 2; ++k) { dot((i,j,k)); } } } // dot((0,0,1),blue); // dot((0,1,0),green); // dot((1,0,0),red); draw((0,0,0)--(1,1,0)); draw((0,1,0)--(1,0,0)); draw((0,0,1)--(1,1,1)); draw((0,1,1)--(1,0,1)); [/asy]
The probability is equivalent to counting the number of Hamiltonian cycles in this 3D graph over $7!.$ This is because each Hamiltonian cycle corresponds to eight unique ways to label the faces. Label the vertices $AR,BR,CR,DR,AX,BX,CX,DX$ where vertices $ab$ and $cd$ are connected if $a=c$ or $b=d.$
Case 1: Four of the vertical edges are used. $6\cdot 2=12.$
Case 2: Two of the vertical edges are used. $4\cdot 3 \cdot 2\cdot 2=48.$
So, the probability is $\frac{60}{5040}=\frac{1}{84}.$ Therefore, our answer is $\boxed{085}$

## Solution 5
As with some of the previous solutions, consider the cube formed by connecting the centroids of the faces on the octahedron. We choose a random vertex(hence fixing the diagram), giving us $7!$ ways as our denominator. WLOG, we color this start vertex red, and we color all $3$ vertices adjacent to it blue. We repeat this for the other vertices.
Note that there is a 1-1 correspondence between the number of valid face numberings with rotational symmetry and the number of ways to move a particle to every vertex of the cube and returning to the start vertex with only diagonal moves. We can move along either short diagonals and long diagonals.
Next, note that we can only move from the red vertices to the blue vertices and back with long diagonals(since short diagonals keep us on the color we are currently on). Thus, it is easy to check that the only possible sequences of long and short diagonals are cyclic permutations of $SSSLSSSL$ and $SLSLSLSL$ .
Case 1: $SSSLSSSL$ . There are $4$ cyclic permutations, and we can traverse the entirety of the red tetrahedron in $4$ steps in $3!$ ways. Then, after the move to the blue tetrahedron from one of the non-starting red vertices, we realize that our first step cannot be to the blue vertex opposite the starting red vertex. Hence, there are $2$ possibilities for our first step. However, once we make our first move, the path is fixed. This leaves us with $4! \cdot 2$ ways.
Case 2: $SLSLSLSL$ There are $2$ cyclic permutations in this case. After we choose one of the $3$ red vertices to go to from the starting vertex and move to the blue tetrahedron, we are once again left with $2$ choices to move to by similar logic to the first case. However, after we move back to the red tetrahedron, our choices are fixed. This leaves us with $2 \cdot 3 \cdot 2$ ways.
Finally, summing and dividing by $7!$ gives us $\frac{60}{7!} = \frac{1}{84} \rightarrow \boxed{085}$ , as desired. - Spacesam

## Video Solution
https://youtu.be/tbfZaGQvBRE?si=lR0pGEZUPpqPMNrs
~MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
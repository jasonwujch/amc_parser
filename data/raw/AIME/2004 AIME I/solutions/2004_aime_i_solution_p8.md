# 2004 AIME I Problem 8

## Problem

Define a regular $n$ -pointed star to be the union of $n$ line segments $P_1P_2, P_2P_3,\ldots, P_nP_1$ such that

- the points $P_1, P_2,\ldots, P_n$ are coplanar and no three of them are collinear,

- each of the $n$ line segments intersects at least one of the other line segments at a point other than an endpoint,

- all of the angles at $P_1, P_2,\ldots, P_n$ are congruent,

- all of the $n$ line segments $P_1P_2, P_2P_3,\ldots, P_nP_1$ are congruent, and

- the path $P_1P_2, P_2P_3,\ldots, P_nP_1$ turns counterclockwise at an angle of less than 180 degrees at each vertex.

There are no regular 3-pointed, 4-pointed, or 6-pointed stars. All regular 5-pointed stars are similar, but there are two non-similar regular 7-pointed stars. How many non-similar regular 1000-pointed stars are there?

## Solution 1
We use the Principle of Inclusion-Exclusion (PIE).
If we join the adjacent vertices of the regular $n$ -star, we get a regular $n$ -gon. We number the vertices of this $n$ -gon in a counterclockwise direction: $0, 1, 2, 3, \ldots, n-1.$
A regular $n$ -star will be formed if we choose a vertex number $m$ , where $0 \le m \le n-1$ , and then form the line segments by joining the following pairs of vertex numbers: $(0 \mod{n}, m \mod{n}),$ $(m \mod{n}, 2m \mod{n}),$ $(2m \mod{n}, 3m \mod{n}),$ $\cdots,$ $((n-2)m \mod{n}, (n-1)m \mod{n}),$ $((n-1)m \mod{n}, 0 \mod{n}).$
If $\gcd(m,n) > 1$ , then the star degenerates into a regular $\frac{n}{\gcd(m,n)}$ -gon or a (2-vertex) line segment if $\frac{n}{\gcd(m,n)}= 2$ . Therefore, we need to find all $m$ such that $\gcd(m,n) = 1$ .
Note that $n = 1000 = 2^{3}5^{3}.$
Let $S = \{1,2,3,\ldots, 1000\}$ , and $A_{i}= \{i \in S \mid i\, \textrm{ divides }\,1000\}$ . The number of $m$ 's that are not relatively prime to $1000$ is: $\mid A_{2}\cup A_{5}\mid = \mid A_{2}\mid+\mid A_{5}\mid-\mid A_{2}\cap A_{5}\mid$ $= \left\lfloor \frac{1000}{2}\right\rfloor+\left\lfloor \frac{1000}{5}\right\rfloor-\left\lfloor \frac{1000}{2 \cdot 5}\right\rfloor$ $= 500+200-100 = 600.$
Vertex numbers $1$ and $n-1=999$ must be excluded as values for $m$ since otherwise a regular n-gon, instead of an n-star, is formed.
The cases of a 1st line segment of (0, m) and (0, n-m) give the same star. Therefore we should halve the count to get non-similar stars.
Therefore, the number of non-similar 1000 pointed stars is $\frac{1000-600-2}{2}= \boxed{199}.$
Note that in general, the number of $n$ -pointed stars is given by $\frac{\phi(n)}{2} - 1$ (dividing by $2$ to remove the reflectional symmetry, subtracting $1$ to get rid of the $1$ -step case), where $\phi(n)$ is the Euler's totient function . It is well-known that $\phi(n) = n\left(1-\frac{1}{p_1}\right)\left(1-\frac{1}{p_2}\right)\cdots \left(1-\frac{1}{p_n}\right)$ , where $p_1,\,p_2,\ldots,\,p_n$ are the distinct prime factors of $n$ . Thus $\phi(1000) = 1000\left(1 - \frac 12\right)\left(1 - \frac 15\right) = 400$ , and the answer is $\frac{400}{2} - 1 = 199$ .

## Solution 2
Continue as before by cyclically constructing a star by taking every $k$ -th point. We can think of this construction as the orbit of a point by a rotation $R^k\in D_{1000}$ . Then, we want $|R^k|=1000$ , meaning that $k\in (\mathbb Z/1000\mathbb Z)^\times$ . Then, $k$ is coprime to $1000$ , meaning $k$ may take on $\phi(1000)=400$ possible values. For any $R^k$ , the dihedral symmetry $TR^k$ defines the figure-preserving bijection $R^k\mapsto R^{-k}$ , meaning half of our possible values of $k$ are similar. Finally, the condition that each edge must intersect another rules out $k=1$ , giving a total of $\frac{400}2-1=\boxed{199}$ pointed stars.
~pineconee
These problems are copyrighted © by the Mathematical Association of America.
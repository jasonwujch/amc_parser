# 2021 AIME I Problem 12

## Problem

Let $A_1A_2A_3\ldots A_{12}$ be a dodecagon ( $12$ -gon). Three frogs initially sit at $A_4,A_8,$ and $A_{12}$ . At the end of each minute, simultaneously, each of the three frogs jumps to one of the two vertices adjacent to its current position, chosen randomly and independently with both choices being equally likely. All three frogs stop jumping as soon as two frogs arrive at the same vertex at the same time. The expected number of minutes until the frogs stop jumping is $\frac mn$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

## Solution 1
Define the distance between two frogs as the number of sides between them that do not contain the third frog.
Let $E(a,b,c)$ denote the expected number of minutes until the frogs stop jumping, such that the distances between the frogs are $a,b,$ and $c$ (in either clockwise or counterclockwise order). Without the loss of generality, assume that $a\leq b\leq c.$
We wish to find $E(4,4,4).$ Note that:
1. At any moment before the frogs stop jumping, the only possibilities for $(a,b,c)$ are $(4,4,4),(2,4,6),$ and $(2,2,8).$
1. $E(a,b,c)$ does not depend on the actual positions of the frogs, but depends on the distances between the frogs.
1. At the end of each minute, each frog has $2$ outcomes. So, there are $2^3=8$ outcomes in total.
We have the following system of equations: \begin{align*} E(4,4,4)&=1+\frac{2}{8}E(4,4,4)+\frac{6}{8}E(2,4,6), \\ E(2,4,6)&=1+\frac{4}{8}E(2,4,6)+\frac{1}{8}E(4,4,4)+\frac{1}{8}E(2,2,8), \\ E(2,2,8)&=1+\frac{2}{8}E(2,2,8)+\frac{2}{8}E(2,4,6). \end{align*} Rearranging and simplifying each equation, we get \begin{align*} E(4,4,4)&=\frac{4}{3}+E(2,4,6), &(1) \\ E(2,4,6)&=2+\frac{1}{4}E(4,4,4)+\frac{1}{4}E(2,2,8), &\hspace{12.75mm}(2) \\ E(2,2,8)&=\frac{4}{3}+\frac{1}{3}E(2,4,6). &(3) \end{align*} Substituting $(1)$ and $(3)$ into $(2),$ we obtain \[E(2,4,6)=2+\frac{1}{4}\left[\frac{4}{3}+E(2,4,6)\right]+\frac{1}{4}\left[\frac{4}{3}+\frac{1}{3}E(2,4,6)\right],\] from which $E(2,4,6)=4.$ Substituting this into $(1)$ gives $E(4,4,4)=\frac{16}{3}.$
Therefore, the answer is $16+3=\boxed{019}.$
~Ross Gao ~MRENTHUSIASM

## Solution 2 (Markov Chain)
We can solve the problem by removing $1$ frog, and calculate the expected time for the remaining $2$ frogs. In the original problem, when the movement stops, $2$ of the $3$ frogs meet. Because the $3$ frogs cannot meet at one vertex, the probability that those two specific frogs meet is $\tfrac13$ . If the expected time for the two frog problem is $E'$ , then the expected time for the original problem is $\tfrac 13 E'$ .
The distance between the two frogs can only be $0$ , $2$ , $4$ , $6$ . We use the distances as the states to draw the following Markov Chain . This Markov Chain is much simpler than that of Solution 1 Supplement in the Remark section.
\begin{align*} E(2) &= 1 + \frac12 \cdot E(2) + \frac14 \cdot E(4)\\ E(4) &= 1 + \frac14 \cdot E(2) + \frac12 \cdot E(4) + \frac14 \cdot E(6)\\ E(6) &= 1 + \frac12 \cdot E(4) + \frac12 \cdot E(6) \end{align*}
By solving the above system of equations, $E(4) = 16$ . The answer for the original problem is $\frac{16}{3}$ , $16 + 3 = \boxed{\textbf{019}}$
~ isabelchen
### Remark (Markov Chain)

## Solution 1 Supplement
Solution 1 can be represented by the following Markov Chain :
- From state $(4, 4, 4)$ to state $(4, 4, 4)$ : the $3$ frogs must jump in the same direction, $2 \cdot \frac18 = \frac14$ .
- From state $(4, 4, 4)$ to state $(2, 4, 6)$ : $2$ frogs must jump in the same direction, and the other must jump in the opposite direction, $\binom32 \cdot 2 \cdot \frac18 = \frac34$ .
- From state $(2, 4, 6)$ to state $(4, 4, 4)$ : the $2$ frogs with a distance of $4$ in between must jump in the same direction so that they will be further away from the other frog, and the other frog must jump in the opposite direction as those $2$ frogs, $\frac18$ .
- From state $(2, 4, 6)$ to state $(2, 4, 6)$ : the $3$ frogs can all jump in the same direction; or the $2$ frogs with a distance of $2$ in between jumps away from each other and the other frog jumps closer to the closest frog; or the $2$ frogs with a distance of $6$ in between jump closer to each other and away from the third frog, the third frog jumps closer to the closest frog; $(2 + 1 + 1) \cdot \frac18 = \frac12$ .
- From state $(2, 4, 6)$ to state $(2, 2, 8)$ : the $2$ frogs with a distance of $2$ in between must jump closer to the other frog and the other frog must jump close to those $2$ frogs, $\frac18$ .
- From state $(2, 2, 8)$ to state $(2, 4, 6)$ : $2$ frogs that have no frogs in between must both jump in the same direction away from the other frog, the other frog must also jump away from those $2$ frogs, $2 \cdot \frac18 = \frac14$ .
- From state $(2, 2, 8)$ to state $(2, 2, 8)$ : the $3$ frogs must all jump in the same direction, $2 \cdot \frac18 = \frac14$ .
- From state $(2, 2, 8)$ to state $(0, x, y)$ : frogs with a distance of $2$ must jump closer to each other, the other frog can jump in any direction, $\frac12 \cdot \frac12 \cdot 2 = \frac12$ .
- From state $(2, 4, 6)$ to state $(0, x, y)$ : the frogs with a distance of $2$ must jump closer to each other, the other frog can jump in any direction, $\frac12 \cdot \frac12 = \frac14$ .
Because $a + b + c = 12$ , we can use $(a, b)$ to represent the states which is simpler than using $(a, b, c)$ in Solution 1.
### Summary
The two above Markov Chains are Absorbing Markov Chain . The state of $2$ frogs meeting is the absorbing state. This problem asks for the Expected Number of Steps before being absorbed in the absorbing state.
Let $p_{ij} = P(X_{n+1} = j | X_n = i)$ , the probability that state $i$ transits to state $j$ on the next step.
Let $e_i$ be the expected number of steps before being absorbed in the absorbing state when starting from transient state $i$ .
$e_i = \sum_{j} [p_{ij} \cdot ( 1 + e_{j})] = \sum_{j} (p_{ij} + p_{ij} \cdot e_{j}) = \sum_{j} p_{ij} + \sum_{j} (p_{ij} \cdot e_{j}) = 1 + \sum_{j} (p_{ij} \cdot e_{j})$
$e_i$ is $1$ plus the sum of the products of $p_{ij}$ and $s_j$ of all the next state $j$ , $\sum_{j} p_{ij} = 1$ .
2014 AMC 12B Problem 22 and 2017 AMC 12A Problem 22 are similar problem with simpler states, both problems can be solved by Absorbing Markov Chain.
~ isabelchen

## Video Solution
https://www.youtube.com/watch?v=nt4xwt5Ldtc
~Math Problem Solving Skills
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
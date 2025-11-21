# 2014 AMC 10B Problem 24

## Problem

The numbers $1, 2, 3, 4, 5$ are to be arranged in a circle. An arrangement is $\textit{bad}$ if it is not true that for every $n$ from $1$ to $15$ one can find a subset of the numbers that appear consecutively on the circle that sum to $n$ . Arrangements that differ only by a rotation or a reflection are considered the same. How many different bad arrangements are there?

$\textbf {(A) } 1 \qquad \textbf {(B) } 2 \qquad \textbf {(C) } 3 \qquad \textbf {(D) } 4 \qquad \textbf {(E) } 5$ .

## Solution 1
We see that there are $5!$ total ways to arrange the numbers. However, we can always rotate these numbers so that, for example, the number $1$ is always at the top of the circle. Thus, there are only $4!$ ways under rotation. Every case has exactly $1$ reflection, so that gives us only $4!/2$ , or $12$ cases, which is not difficult to list out. We systematically list out all $12$ cases.
Now, we must examine if they satisfy the conditions. We can see that by choosing one number at a time, we can always obtain subsets with sums $1, 2, 3, 4,$ and $5$ . By choosing the full circle, we can obtain $15$ . By choosing everything except for $1, 2, 3, 4,$ and $5$ , we can obtain subsets with sums of $10, 11, 12, 13,$ and $14$ .
This means that we now only need to check for $6, 7, 8,$ and $9$ . However, once we have found a set summing to $6$ , we can choose all remaining numbers and obtain a set summing to $15-6=9$ , and similarly for $7$ and $8$ . Thus, we only need to check each case for whether or not we can obtain $6$ or $7$ .
We can make $6$ by having $4, 2$ , or $3, 2, 1$ , or $5, 1$ . We can start with the group of three. To separate $3, 2, 1$ from each other, they must be grouped two together and one separate, like this.
[asy] draw(circle((0, 0), 5)); pair O, A, B, C, D, E; O=origin; A=(0, 5); B=rotate(72)*A; C=rotate(144)*A; D=rotate(216)*A; E=rotate(288)*A; label("$x$", A, N); label("$y$", C, SW); label("$z$", D, SE); [/asy]
Now, we note that $x$ is next to both blank spots, so we can't have a number from one of the pairs. So since we can't have $1$ , because it is part of the $5, 1$ pair, and we can't have $2$ there, because it's part of the $4, 2$ pair, we must have $3$ inserted into the $x$ spot. We can insert $1$ and $2$ in $y$ and $z$ interchangeably, since reflections are considered the same.
[asy] draw(circle((0, 0), 5)); pair O, A, B, C, D, E; O=origin; A=(0, 5); B=rotate(72)*A; C=rotate(144)*A; D=rotate(216)*A; E=rotate(288)*A; label("$3$", A, N); label("$2$", C, SW); label("$1$", D, SE); [/asy]
We have $4$ and $5$ left to insert. We can't place the $4$ next to the $2$ or the $5$ next to the $1$ , so we must place $4$ next to the $1$ and $5$ next to the $2$ .
[asy] draw(circle((0, 0), 5)); pair O, A, B, C, D, E; O=origin; A=(0, 5); B=rotate(72)*A; C=rotate(144)*A; D=rotate(216)*A; E=rotate(288)*A; label("$3$", A, N); label("$5$", B, NW); label("$2$", C, SW); label("$1$", D, SE); label("$4$", E, NE); [/asy]
This is the only solution to make $6$ "bad."
Next we move on to $7$ , which can be made by $3, 4$ , or $5, 2$ , or $4, 2, 1$ . We do this the same way as before. We start with the three group. Since we can't have $4$ or $2$ in the top slot, we must have one there, and $4$ and $2$ are next to each other on the bottom. When we have $3$ and $5$ left to insert, we place them such that we don't have the two pairs adjacent.
[asy] draw(circle((0, 0), 5)); pair O, A, B, C, D, E; O=origin; A=(0, 5); B=rotate(72)*A; C=rotate(144)*A; D=rotate(216)*A; E=rotate(288)*A; label("$1$", A, N); label("$3$", B, NW); label("$2$", C, SW); label("$4$", D, SE); label("$5$", E, NE); [/asy]
This is the only solution to make $7$ "bad."
We've covered all needed cases, and the two examples we found are distinct, therefore the answer is $\boxed{\textbf {(B) }2}$ .

## Solution 2 (Complex Compliments)
We can use a clever approach for this problem by finding out how many non-adjacency's exist and subtracting it by the total configurations.
The formula \( C_n(A) = \frac{n}{k} \binom{n-k-1}{k-1} \) represents the Circular Gap Theorem, a crucial formula for finding out how many compliment cases exist where we want \( k \) values to not be adjacent from \( n \) total values.
Considering reflections and rotations are practically the same, we see that we have \( (n-1)!/2 \), \( n=5 \) ways = \( 4!/2 = 24/2 = 12 \) total configurations.
Now, we do some casework. Notice that we have \( n=5 \) values. Our \( k \in \{1,2,3,4,5\} \). We see that the values \( k \in \{3, 4, 5\} \) don't work as they make \( \binom{n-k-1}{k-1} \) invalid (3 gives \( 5-3-1 \choose 3-1 \) = \( 1 \choose 2 \) which doesn't exist, 4 gives \( 0 \choose 3 \) which doesn't exist, and 5 gives \( -1 \choose 4 \) which obviously doesn't exist).
We solve for \( k \in \{1,2\} \). When \( k \in 1 \), we get \( C_n(A) = \frac{5}{1} \binom{5-1-1}{1-1} = 5(1) = 5 \) cases and when \( k \in 2 \), we get \( C_n(A) = \frac{5}{2} \binom{5-2-1}{2-1} = \frac{5}{2}(2) = 5 \). The total cases that lead to a good sum is \( 5+5=10 \).
The answer isn't 10 however, because the theorem finds the compliments of the values, so the number of compliments is 10. We need to find the bad cases, which is \( 12 - 10 \) or $\textbf{(B)} \text{ }2$
~Pinotation
### Circular Gap Theorem Simplification
It is also helpful to note \( C_n(A) = \frac{n}{k} \binom{n-k-1}{k-1} \) = \( \binom{n}{2k} \).
~Pinotation

## Solution 3
Note that any ordering satisfies the following numbers:
$1$ through $5:$ choose the number
$10$ through $14:$ choose all numbers excluding a specific one (such as $1, 2, 3, 4$ in some order for $10$ )
$15:$ choose all the numbers.
Now, the pairs $7, 8$ and $6, 9$ are the same cases, since if a sequence satisfies a number, we can choose all the remaining numbers to make the other number. ( $1, 2, 3$ for $6$ , then $4, 5$ for $9$ .)
Thus, we have two cases, whether a sequence doesn't make $6$ or whether a sequence doesn't make $7.$
$6$ can be made by $(1,2,3), (1, 5), (2, 4).$ We can put $1, 2, 3$ around the circle. $4$ and $5$ now need to go in $2$ of the $3$ spots in between $1, 2, 3.$ Also keeping in mind the other two ways to make $6,$ $4$ has to go in the spot opposite of $2$ and $5$ has to go in the spot opposite of $1.$ Thus the only ordering that works is $1, 4, 3, 5, 2$ (ignore rotations and reflections).
Similarly, for the case with $7,$ the only ordering that works is $1, 5, 4, 2, 3$ with gives the answer of $\mathbf{(B) }2.$

## Solution 4 (Minimal Casework)
Note that $\{1,2,3,4,5,10,11,12,13,14,15\}$ will always be there. Thus, we need to prevent either the $(6,9)$ or the $(7,8)$ pair. We consider the neighbors of 5.
Case 1: No 7s. Then we have $1-5-4$ , and the neighbor of 4 cannot be 3 so the full config must be $3-1-5-4-2$ .
Case 2: No 6s. Then we have $2-5-3$ , and the neighbor of 2 cannot be 4, so the full config must be $1-2-5-3-4$ .
Both of these are bad, and they're the only bads, so the answer is $\textbf{(B)} \text{ }2$ .

## Solution 5 (Maximal Casework)
Like all previous solutions, we only need to find an arrangement where a sum of $6$ or $7$ isn't achievable. Reflections and rotations are considered the same, so there are actually only $\frac{5!}{5} \cdot \frac{1}{2} = 12$ distinct arrangements. We can simply draw all $12$ arrangements and cross out the ones that aren't bad, leaving us with $\boxed{2}$ bad arrangements.

## Video Solution by icematrix
https://youtu.be/45TQEV8OjRk
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
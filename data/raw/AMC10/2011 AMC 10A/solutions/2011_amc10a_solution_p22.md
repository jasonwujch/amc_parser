# 2011 AMC 10A Problem 22

## Problem

Each vertex of convex pentagon $ABCDE$ is to be assigned a color. There are $6$ colors to choose from, and the ends of each diagonal must have different colors. How many different colorings are possible?

$\textbf{(A)}\ 2520\qquad\textbf{(B)}\ 2880\qquad\textbf{(C)}\ 3120\qquad\textbf{(D)}\ 3250\qquad\textbf{(E)}\ 3750$

## Solution 1
Let vertex $A$ be any vertex, then vertex $B$ be one of the diagonal vertices to $A$ , $C$ be one of the diagonal vertices to $B$ , and so on. We consider cases for this problem.
In the case that $C$ has the same color as $A$ , $D$ has a different color from $A$ and so $E$ has a different color from $A$ and $D$ . In this case, $A$ has $6$ choices, $B$ has $5$ choices (any color but the color of $A$ ), $C$ has $1$ choice, $D$ has $5$ choices, and $E$ has $4$ choices, resulting in a possible of $6 \cdot 5 \cdot 1 \cdot 5 \cdot 4 = 600$ combinations.
In the case that $C$ has a different color from $A$ and $D$ has a different color from $A$ , $A$ has $6$ choices, $B$ has $5$ choices, $C$ has $4$ choices (since $A$ and $B$ necessarily have different colors), $D$ has $4$ choices, and $E$ has $4$ choices, resulting in a possible of $6 \cdot 5 \cdot 4 \cdot 4 \cdot 4 = 1920$ combinations.
In the case that $C$ has a different color from $A$ and $D$ has the same color as $A$ , $A$ has $6$ choices, $B$ has $5$ choices, $C$ has $4$ choices, $D$ has $1$ choice, and $E$ has $5$ choices, resulting in a possible of $6 \cdot 5 \cdot 4 \cdot 1 \cdot 5 = 600$ combinations.
Adding all those combinations up, we get $600+1920+600=\boxed{3120 \ \mathbf{(C)}}$ .

## Solution 2
First, notice that there can be $3$ cases. One with all vertices painted different colors, one with one pair of adjacent vertices painted the same color and the final one with two pairs of adjacent vertices painted two different colors.
Case $1$ : There are $6!$ ways of assigning each vertex a different color. $6! = 720$
Case $2$ : There are $\frac {6!}{2!} * 5$ ways. After picking four colors, we can rotate our pentagon in $5$ ways to get different outcomes. $\frac {6!}{2} * 5 = 1800$
Case $3$ : There are $\frac {\frac {6!}{3!} * 10}{2!}$ ways of arranging the final case. We can pick $3$ colors for our pentagon. There are $5$ spots for the first pair of colors. Then, there are $2$ possible ways we can put the final pair in the last $3$ spaces. But because the two pairs are indistinguishable, we divide by $2!$ . $\frac {\frac {6!}{3!} * 10}{2!} = 600$
Adding all the possibilities up, we get $720+1800+600=\boxed{3120 \ \mathbf{(C)}}$
~ZericHang

## Solution 3
There are $6$ ways to assign a color to $A$ . WLOG, give vertex $A$ a color; we can multiply by $6$ at the end. Since vertices $A$ and $C$ cannot have the same color, there are $5$ ways to assign colors to vertex $C$ . Using this same logic, there are $5$ ways to assign a color to vertices $E$ , $B$ , and $D$ , giving a total of $5^4=625$ ways. However, vertex $D$ cannot be the same color as vertex $A$ . To use complementary counting, we need to find the amount of ways for $D$ and $A$ to have the same color. Notice that this is equivalent to the amount of ways to arrange colors among the vertices of a square. Using the same logic as above, there are $5^3=125$ ways, except we must subtract the number of ways for a triangle. Each time, there is $1$ less vertex, so $5$ times less ways to color. This process stops when there are only $2$ vertices left; in this case there are simply $5$ ways to color this figure. So in conclusion, there are $6(5^4-(5^3-(5^2-(5))))=6(5^4-5^3+5^2-5)=\boxed{3120 \ \mathbf{(C)}}$ ways.

## Solution 4
This problem is a direct application of the chromatic polynomial of a graph, represented by $P_k(G)$ , which returns a polynomial representing the number of ways to color a graph $G$ with $k$ colors such that no two adjacent vertices share the same color. In other words, it gives us a polynomial in terms of $k$ where we can plug in $k=6$ to get our answer.
Well, if we want to find $P_k$ for a graph $G$ , we should probably first draw the graph, right? We can first draw five vertices (without any edges) in the shape of a pentagon. After connecting the diagonals, we get a star. We attempt to shift the vertices around to simplify the graph, which we quickly realize is isomorphic (can be turned into) the five-cycle, or the pentagon.
Finding $P_k$ on a graph with a cycle of length at most 3 is straightforward -- we first pick a vertex v. It has 0 colored (visited) neighbors, so we can color it in k ways. We then move on to the vertices adjacent to v, etc, and at the end we multiply all these together. For example, the chromatic polynomial of a triangle is $k(k-1)(k-2)$ . However, cycles with length > 3 introduce ambiguity, and thus the above technique fails. Thus, we need to use the recursive formula $P_k(G) = P_k(G-e)-P_k(G*e)$ , where $G-e$ represents removing e and $G*e$ represents contracting e, or collapsing the two endpoints of e into one. When we hit a graph where the longest cycle has length 3, we can use the first technique to quickly find $P_k$ .
After about four iterations of the algorithm, we get that the chromatic polynomial is $k(k-1)^4 - k(k-1)^3 + k(k-1)(k-2)$ . Plugging in 6 gives us $\boxed{3120 \ \mathbf{(C)}}$ .
~Helloworld1

## Solution 5 (constructive counting)
In pentagon $ABCDE$ , fix any vertex $A$ . Now draw diagonal $AC$ . There are six choices for vertex $A$ and $5$ choices for vertex $C$
Now draw diagonal $CE$ . Since $E$ cannot be the same color as vertex $C$ , we have $5$ choices for $E$ . Again, we have five choices for vertex $D$ (draw diagonal $AD$ ).
Thus there are $6 \cdot 5$ choices for vertices $A$ and $C$ and $5 \cdot 5$ combinations for $D$ and $E$ .
To determine the final count, we consider two cases for the final $25$ combinations of $D$ and $E$ , which uniquely determines $B$ . Then, we multiply by $30$ since the choices of $A$ and $C$ are independent from these two cases.
Case $1$ : $D$ and $E$ are the same color. There are $4$ possible pairs (This is because $D$ and $E$ are not chosen from the same 5 colors. $D$ cannot be $A$ as they are on a diagonal, but $E$ can be. ~ primegn. In other words, $D$ cannot be $A$ because they are diagonal, and $E$ cannot be $C$ for the same reason ( $C$ cannot be $A$ because they are diagonal), therefore $D$ and $E$ cannot be $A$ and $C$ so there are 4 possible pairs left ~Puer_137), and thus we have $5$ choices for $B$ . There are $20$ cases here.
Case $2$ : $D$ and $E$ are different. There are $25-4 = 21$ possible combinations and we have $4$ choices for $B$ (not the color of $D$ nor $E$ ). In this cas,e we have $21 \cdot 4 = 84$ cases.
Our final count is $30(84+20) = \boxed{3120}$ , which is answer $\boxed{\textbf{(C)}}$ .
~FIREDRAGONMATH16

## Solution 6 (Casework)
WLOG, draw $ABCDE$ such that point $A$ is at the top, and write the letters in counterclockwise order. WLOG, fill in $A$ first. There are $6$ ways to do so. From here we proceed with casework on the color of $B$ :
- Case 1: $B$ is the same color as $A$
- Case 2: $B$ and $A$ are different colors
- Case 2.1: $C$ and $B$ are the same color
- Case 2.2: $C$ and $B$ are different colors
Summing up the cases, $600+600+1920=3120 \Longrightarrow \boxed{\textbf{(C) } 3120}$ .
~JH. L

## Solution 7
Notice that a minimum of, $3$ and a maximum of $5$ colours can be used.
- Case $1$ : $5$ colours used.
This is straight forward and there are $6P5 = 720$ ways.
- Case $2$ : $4$ colours used.
If $x$ and $y$ have same colours, they have to be adjacent. Let $x$ be directly right of $y$ . $4$ consecutive points from $x$ clockwise have different colours. They can be coloured in $6P4=360$ ways. And $x$ can be chosen in $5$ ways, bringing the total to $360 \times 5=1800$ .
- Case $3$ : $3$ colours used.
Note that $3$ points can't have the same colour as at least $1$ of the lines joining them will be a diagonal. Then the arrangement is $2-2-1$ . The point with distinct colour can be chosen in $5$ ways and can be coloured in $6$ ways. The next two points clockwise can be coloured in $5$ ways and the next two in $4$ ways. The total is $5 \times 6 \times 5 \times 4=600$ .
Finally, adding all cases, the answer is $600+1800+720=3120 \Longrightarrow \boxed{\textbf{(C) } 3120}$ .
~IamBATMAN1313

## Solution 8
Name the pentagon $ADBEC$ . Then $A,B;$ $B,C;$ $C,D;$ $D,E$ and $E,A$ have to be of different colours.
$A$ can be coloured in $6$ ways, $B$ in $5$ ways (Without the one used for $A$ ), $C$ in $5$ ways (Without the one used for $B$ ), $D$ in $5$ ways (Without the one used for $C$ ).
Now we find the expected value of how many ways can $E$ be coloured.
If $A$ and $C$ are of the same colour, $A$ and $D$ are always different. This happens $\frac{1}{5}$ times and leaves $4$ options for $E$ .
If $A$ and $C$ are of different colours $\left(\frac{4}{5} \ \text{of the time} \right)$ then there is a $\frac{1}{5}$ chance that $A$ and $D$ are of same colour and $\frac{4}{5}$ chance that they are different. The first one leaves $5$ ways to colour $E$ and the second one leaves $4$ .
Calculating all these, we find the expected value for the number of ways $E$ can be coloured is $\frac{1}{5} \times 4 + \frac{4}{5} \left( \frac{1}{5} \times 5 + \frac{4}{5} \times 4 \right) = 4.16$
Therefore total number or ways $= 6 \times 5 \times 5 \times 5 \times 4.16 = \boxed{\textbf{(C) } 3120}$ .
~IamBATMAN1313

## Solution 9 (Elimination of answers)
First, we know that there are $6$ ways to assign a color to vertex $A$ . Then, there are $6$ ways to assign a color to vertex $B$ , because it doesn't depend on vertex $A$ . There are also $5$ ways to assign a color to vertex $C$ , because it can't be the same color as vertex $A$ . Notice that both vertices $E$ and $D$ have 5 or 4 choices, depending on whether $A$ , $B$ , and $C$ are the same color. This means that the we know that the amount of choices must be bigger than $6 \times 6 \times 5 \times 4 \times 4 = 2880$ , which eliminates options $A$ and $B$ .
Then, notice that the amount of choices must be smaller than $6 \times 6 \times 5 \times 4.5 \times 4.5 = 3645$ , because the expected amount of choices $E$ and $D$ have are less than 4.5. (There is a greater probability that $A$ , $B$ , and $B$ , $C$ are both different). This eliminates option $E$ , which leaves us with options $C$ and $D$ .
We know that the amount of choices must be a multiple of $6$ , so $D$ is eliminated, leaving us with option $\boxed{\textbf{(C) } 3120}$
~Jonathanzhou18

## Video Solution
https://youtu.be/FThly7dRBIE
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
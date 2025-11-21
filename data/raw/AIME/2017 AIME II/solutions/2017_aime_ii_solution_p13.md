# 2017 AIME II Problem 13

## Problem

For each integer $n\geq3$ , let $f(n)$ be the number of $3$ -element subsets of the vertices of the regular $n$ -gon that are the vertices of an isosceles triangle (including equilateral triangles). Find the sum of all values of $n$ such that $f(n+1)=f(n)+78$ .

## Solution 1
Considering $n \pmod{6}$ , we have the following formulas:
$n\equiv 0$ : $\frac{n(n-4)}{2} + \frac{n}{3}$
$n\equiv 2, 4$ : $\frac{n(n-2)}{2}$
$n\equiv 3$ : $\frac{n(n-3)}{2} + \frac{n}{3}$
$n\equiv 1, 5$ : $\frac{n(n-1)}{2}$
To derive these formulas, we note the following: Any isosceles triangle formed by the vertices of our regular $n$ -sided polygon $P$ has its sides from the set of edges and diagonals of $P$ . Notably, as two sides of an isosceles triangle must be equal, it is important to use the property that same-lengthed edges and diagonals come in groups of $n$ , unless $n$ is even when one set of diagonals (those which bisect the polygon) comes in a group of $\frac{n}{2}$ . Three properties hold true of $f(n)$ :
When $n$ is odd there are $\frac{n(n-1)}{2}$ satisfactory subsets (This can be chosen with $n$ choices for the not-base vertex, and $\frac{n-1}{2}$ for the pair of equal sides as we have $n-1$ edges to choose from, and we must divide by 2 for over-count).*
- Another explanation: For any diagonal or side of the polygon chosen as the base of the isosceles triangle, there is exactly 1 isosceles triangle that can be formed. So, the total number of satisfactory subsets is $\dbinom{n}{2}=\dfrac{n(n-1)}{2}.$
When $n$ is even there are $\frac{n(n-2)}{2}$ satisfactory subsets (This can be chosen with $n$ choices for the not-base vertex, and $\frac{n-2}{2}$ for the pair of equal sides as we have $n-1$ edges to choose from, one of them which is not satisfactory (the bisecting edge), and we must divide by 2 for over-count).
When $n$ is a multiple of three we additionally over-count equilateral triangles, of which there are $\frac{n}{3}$ . As we count them three times, we are two times over, so we subtract $\frac{2n}{3}$ .
Considering the six possibilities $n \equiv 0,1,2,3,4,5 \pmod{6}$ and solving, we find that the only valid solutions are $n = 36, 52, 157$ , from which the answer is $36 + 52 + 157 = \boxed{245}$ .

## Solution 2 (elaborates on the possible cases)
In the case that $n\equiv 0\pmod 3$ , there are $\frac{n}{3}$ equilateral triangles. We will now count the number of non-equilateral isosceles triangles in this case.
Select a vertex $P$ of a regular $n$ -gon. We will count the number of isosceles triangles with their vertex at $P$ . (In other words, we are counting the number of isosceles triangles $\triangle APB$ with $A, B, P$ among the vertices of the $n$ -gon, and $AP=BP$ .)
If the side $AP$ spans $k$ sides of the $n$ -gon (where $k<\frac{n}{2}$ ), the side $BP$ must span $k$ sides of the $n$ -gon, and, thus, the side $AB$ must span $n-2k$ sides of the $n$ -gon. As $\triangle ABP$ has three distinct vertices, the side $AB$ must span at least one side, so $n-2k \ge 1$ . Combining this inequality with the fact that $1\le k<\frac{n}{2}$ and $k\not = \frac{n}{3}$ (as $\triangle ABP$ cannot be equilateral), we find that there are $\lceil\frac{n}{2}\rceil-2$ possible $k$ .
As each of the $n$ vertices can be the vertex of a given triangle $\triangle ABP$ , there are $\left(\lceil \frac{n}{2} \rceil -2 \right)\cdot n$ non-equilateral isosceles triangles.
Adding in the $\frac{n}{3}$ equilateral triangles, we find that for $n\equiv 0\pmod 3$ : $f(n) = \frac{n}{3}+\left(\lceil \frac{n}{2} \rceil -2\right)\cdot n$ .
On the other hand, if $n\equiv 1, 2\pmod 3$ , there are no equilateral triangles, and we may follow the logic of the paragraph above to find that $f(n)=\left(\lceil \frac{n}{2} \rceil -1\right)\cdot n$ .
We may now rewrite the given equation, based on the remainder $n$ leaves when divided by 3.
Case 1: $n\equiv 0\pmod 3$ The equation $f(n+1)=f(n)+78$ for this case is $\left(\lceil \frac{n+1}{2} \rceil -1\right)\cdot (n+1)=\frac{n}{3}+\left(\lceil \frac{n}{2} \rceil -2\right)\cdot n+78$ .
In this case, $n$ is of the form $6k$ or $6k+3$ , for some integer $k$ .
Subcase 1: $n=6k$ Plugging into the equation above yields $k=6\rightarrow n=36$ .
Subcase 2: $n=6k+3$ Plugging into the equation above yields $7k=75$ , which has no integer solutions.
Case 2: $n\equiv 1\pmod 3$ The equation $f(n+1)=f(n)+78$ for this case is $\left(\lceil \frac{n+1}{2} \rceil -1\right)\cdot (n+1)=\left(\lceil \frac{n}{2} \rceil -1\right)\cdot n+78$ .
In this case, $n$ is of the form $6k+1$ or $6k+4$ , for some integer $k$ .
Subcase 1: $n=6k+1$ In this case, the equation above yields $k=8\rightarrow n=52$ .
Subcase 2: $n=6k+4$ In this case, the equation above yields $k=26\rightarrow n=157$ .
Case 3: $n\equiv 2\pmod 3$ The equation $f(n+1)=f(n)+78$ for this case is $\frac{n+1}{3}+\left(\lceil \frac{n+1}{2} \rceil -2\right)\cdot (n+1)=\left(\lceil \frac{n}{2} \rceil -1\right)\cdot n+78$ .
In this case, $n$ is of the form $6k+2$ or $6k+5$ , for some integer $k$ .
Subcase 1: $n=6k+2$ The equation above reduces to $5k=77$ , which has no integer solutions.
Subcase 2: $n=6k+5$ The equation above reduces to $k=-80$ , which does not yield a positive integer solution for $n$ .
In summary, the possible $n$ are $36, 52, 157$ , which add to $\boxed{245}$ .

## Solution 3
We first notice that when a polygon has $s$ sides where $s\not\equiv 0\pmod{3}$ , there cannot exist any three vertices that form an equilateral triangle. Also, the parity of $s$ and $s+1$ also matters, since they influence how many isosceles triangles including equilateral triangles exist in the polygon. We can model an equation $2x+y=s$ , where the lines that are congruent connect the vertices that are $x$ vertices apart and the other line has vertices that are $y$ vertices apart. If $s$ is even, there are $\frac{s-2}{2}$ solutions for $(x,y)$ which would create a unique type of isosceles triangle. We subtract two since $y$ cannot be zero. If $s$ is odd, there are $\frac{s-1}{2}$ solutions for $(x,y)$ . Next, we do casework on the congruence of $s\pmod{3}$ and the parody of $s$ using the information above:
Case 1:
$s\not\equiv 0\pmod{3}$ , $s+1\not\equiv 0\pmod{3}$
$s$ is even, $s+1$ is odd
There are $\frac{s-2}{2}$ unique types of isosceles triangles in the polygon with $s$ sides. Each isosceles triangle has a unique point which connects the two congruent sides. Therefore, for each type of isosceles triangle, there exists $s$ of those triangles since the unique point can be any of the $s$ vertices. There are $\frac{s}{2}$ types of isosceles triangles in the polygon with $s+1$ sides and $s+1$ unique points for each type of triangle. Therefore, $\frac{s}{2}\cdot{(s+1)}-\frac{s-2}{2}\cdot{(s)}=78$ . Solving, we get $s=52$ .
Case 2:
$s\not\equiv 0\pmod{3}$ , $s+1\not\equiv 0\pmod{3}$
$s$ is odd, $s+1$ is even
Using similar logic, there are $\frac{s-1}{2}\cdot{(s)}$ possible isosceles triangles in the $s$ sided polygon. There are $\frac{s-1}{2}\cdot{(s+1)}$ possible isosceles triangles in the $s+1$ sided polygon. The difference should be $78$ , so $\frac{s-1}{2}\cdot{(s+1)}-\frac{s-1}{2}\cdot{(s)}=78$ . Solving gives $s=157$ .
For both of these cases, we don't have to worry about equilateral triangles since in both cases $s,s+1\nmid3$ .
Case 3:
$s\not\equiv 0\pmod{3}$ , $s+1\equiv 0\pmod{3}$
$s$ is even, $s+1$ is odd
There are $\frac{s-2}{2}\cdot{(s)}$ possible isosceles triangles in the $s$ sided polygon. The $s+1$ case is a bit more complicated, as we have to consider equilateral triangles as well. In this case, there is one solution where $x=y$ , which would produce an equilateral triangle. Therefore, we subtract that case to calculate only isosceles triangles with 2 congruent sides. Only isosceles triangles with exactly 2 congruent sides have a unique point, while there exist only $\frac{s+1}{3}$ distinct equilateral triangles in a polygon with $s+1$ sides, the rest are equivalent and symmetrical. Therefore, there are $(\frac{s}{2}-1)\cdot{(s+1)}+\frac{s+1}{3}$ isosceles triangles with at least 2 congruent sides in a polygon with $s+1$ sides. Putting it together, $\frac{s}{2}-1\cdot{(s+1)}+(\frac{s+1}{3})-\frac{s-2}{2}\cdot{(s)}=78$ . Solving yields $5s=772$ which is impossible since $s$ has to be an integer. Therefore, this case is not valid.
Case 4:
$s\not\equiv 0\pmod{3}$ , $s+1\equiv 0\pmod{3}$
$s$ is odd, $s+1$ is even
There are $\frac{s-1}{2}\cdot{(s)}$ isosceles triangles in the $s$ sided polygon. Using the idea above, there are $(\frac{s-1}{2}-1)\cdot{(s+1)}$ isosceles triangles with 2 congruent sides in an $s+1$ sided polygon. There are $\frac{s+1}{3}$ equilateral triangles. Therefore, $(\frac{s-1}{2}-1)\cdot{(s+1)}+(\frac{s+1}{3})-\frac{s-1}{2}\cdot{(s)}=78$ . Looking at the left hand side, it is clear that $s$ has to be negative, which is not valid. Therefore, this case is not valid.
Case 5:
$s\equiv 0\pmod{3}$ , $s+1\not\equiv 0\pmod{3}$
$s$ is even, $s+1$ is odd
There are a total of $(\frac{s-2}{2}-1)\cdot{(s)}+(\frac{s}{3})$ isosceles triangles in a polygon with $s$ sides. There are a total of $\frac{s}{2}\cdot{(s+1)}$ isosceles triangles in a polygon with $s+1$ sides. Therefore, $\frac{s}{2}\cdot{(s+1)}-(\frac{s-2}{2}-1)\cdot{(s)}-(\frac{s}{3})=78$ . Simplifying, we get $s=36$ .
Case 6:
$s\equiv 0\pmod{3}$ , $s+1\not\equiv 0\pmod{3}$
$s$ is odd, $s+1$ is even
There are a total of $(\frac{s-1}{2}-1)\cdot{(s)}+(\frac{s}{3})$ isosceles triangles in the polygon with $s$ sides. There are $\frac{s-1}{2}\cdot{(s+1)}$ isosceles triangles in the polygon with $s+1$ sides. Therefore, $\frac{s-1}{2}\cdot{(s+1)}-(\frac{s-1}{2}-1)\cdot{(s)}-(\frac{s}{3})=78$ . Simplifying, we get $7s=471$ , which means $s$ is not an integer. Thus, this case is invalid.
Adding all the valid cases, we obtain $52+157+36=\boxed{245}$
~ Magnetoninja

## Video Solution
https://youtu.be/fFgakiw66WY
~MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
# 2001 AIME I Problem 10

## Problem

Let $S$ be the set of points whose coordinates $x,$ $y,$ and $z$ are integers that satisfy $0\le x\le2,$ $0\le y\le3,$ and $0\le z\le4.$ Two distinct points are randomly chosen from $S.$ The probability that the midpoint of the segment they determine also belongs to $S$ is $m/n,$ where $m$ and $n$ are relatively prime positive integers. Find $m + n.$

## Solutions

## Solution 1
The distance between the $x$ , $y$ , and $z$ coordinates must be even so that the midpoint can have integer coordinates. Therefore,
- For $x$ , we have the possibilities $(0,0)$ , $(1,1)$ , $(2,2)$ , $(0,2)$ , and $(2,0)$ , $5$ possibilities.
- For $y$ , we have the possibilities $(0,0)$ , $(1,1)$ , $(2,2)$ , $(3,3)$ , $(0,2)$ , $(2,0)$ , $(1,3)$ , and $(3,1)$ , $8$ possibilities.
- For $z$ , we have the possibilities $(0,0)$ , $(1,1)$ , $(2,2)$ , $(3,3)$ , $(4,4)$ , $(0,2)$ , $(0,4)$ , $(2,0)$ , $(4,0)$ , $(2,4)$ , $(4,2)$ , $(1,3)$ , and $(3,1)$ , $13$ possibilities.
However, we have $3\cdot 4\cdot 5 = 60$ cases where we have simply taken the same point twice, so we subtract those. Therefore, our answer is $\frac {5\cdot 8\cdot 13 - 60}{60\cdot 59} = \frac {23}{177}\Longrightarrow m+n = \boxed{200}$ .

## Solution 2
There are $(2 + 1)(3 + 1)(4 + 1) = 60$ points in total. We group the points by parity of each individual coordinate -- that is, if $x$ is even or odd, $y$ is even or odd, and $z$ is even or odd. Note that to have something that works, the two points must have this same type of classification (otherwise, if one doesn't match, the resulting sum for the coordinates will be odd at that particular spot).
There are $12$ EEEs (the first position denotes the parity of $x,$ the second $y,$ and the third $z.$ ), $8$ EEOs, $12$ EOEs, $6$ OEEs, $8$ EOOs, $4$ OEOs, $6$ OOEs, and $4$ OOOs. Doing a sanity check, $12 + 8 + 12 + 6 + 8 + 4 + 6 + 4 = 60,$ which is the total number of points.
Now, we can see that there are $12 \cdot 11$ ways to choose two EEEs (respective to order), $8 \cdot 7$ ways to choose two EEOs, and so on. Therefore, we get \[12\cdot11 + 8\cdot7 + 12\cdot11 + 6\cdot5 + 8\cdot7 + 4\cdot3 + 6\cdot5 + 4\cdot3 = 460\] ways to choose two points where order matters. There are $60 \cdot 59$ total ways to do this, so we get a final answer of \[\dfrac{460}{60 \cdot 59} = \dfrac{23}{3 \cdot 59} = \dfrac{23}{177},\] for our answer of $23 + 177 = \boxed{200}.$
Solution by Ilikeapos

## Solution 3
Similarly to Solution 2, we note that there are $60$ points and that the parities of the two points' coordinates must be the same in order for the midpoint to be in $S$ .
Ignore the distinct points condition. The probability that the midpoint is in $S$ is then \[\left(\left(\frac 23\right)^2+\left(\frac 13\right)^2\right)\left(\left(\frac 24\right)^2+\left(\frac 24\right)^2\right)\left(\left(\frac 35\right)^2+\left(\frac 25\right)^2\right)=\frac{13}{90}.\]
Note that $\frac{13}{90}=\frac{520}{3600}$ . Since there are $3600$ total ways to choose $2$ points from $S$ , there must be $520$ pairs of points that have their midpoint in $S$ . Of these pairs, $60$ of them contain identical points (not distinct).
Subtracting these cases, our answer is $\frac{520-60}{3600-60}=\frac{23}{177}\implies\boxed{200}$ .

## Solution 4
There are $(2 + 1)(3 + 1)(4 + 1) = 60$ points in total. Note that in order for the midpoint of the line segment to be a lattice point, the lengths on the x, y, and z axis must be even numbers. We will define all segments by denoting the amount they extend in each dimension: $(x, y, z)$ . For example, the longest diagonal possible will be $(2,3,4)$ , the space diagonal of the box. Thus, any line segment must have dimensions that are even. For $x$ the segment may have a value of $0$ for $x$ , (in which case the segment would be two dimensional) or a value of $2$ . The same applies for $y$ , because although it is three units long the longest even integer is two. For $z$ the value may be $0$ , $2$ , or $4$ . Notice that if a value is zero, then the segment will pertain to only two dimensions. If two values are zero then the line segment becomes one dimensional.
Then the total number of possibilities will be $2 \cdot 2 \cdot 3$ .
Listing them out appears as follows:
$2,2,4$
$2,2,2$
$2,2,0$
$2,0,4$
$2,0,2$
$2,0,0$
$0,2,4$
$0,2,2$
$0,2,0$
$0,0,4$
$0,0,2$
$0,0,0$ * this value is a single point
Now, picture every line segment to be the space diagonal of a box. Allow this box to define the space the segment occupies. The question now transforms into "how many ways can we arrange this smaller box in the two by three by four?".
Notice that the amount an edge can shift inside the larger box is the length of an edge of the larger box (2, 3, or 4) minus the edge of the smaller box (also known as the edge), plus one. For example, (0, 2, 2) would be $3 \cdot 2 \cdot 3$ . Repeat this process.
$2,2,4$ 2
$2,2,2$ 6
$2,2,0$ 10
$2,0,4$ 4
$2,0,2$ 12
$2,0,0$ 20
$0,2,4$ 6
$0,2,2$ 18
$0,2,0$ 30
$0,0,4$ 12
$0,0,2$ 36
$0,0,0$ 60 * this won't be included, but notice that sixty the number of lattice points
Finally, we remember that there are four distinct space diagonals in a box, so we should multiply every value by four, right? Unfortunately we forgot to consider that some values have only one or two dimensions. They should be multiplied by one or two, respectively. This is because segments with two dimensions are the diagonals of a rectangle and thus have two orientations. Then any value on our list without any zeroes will be multiplied by four, and any value on our list with only one zero will be multiplied by two, and finally any value on our list with two zeroes will be multiplied by one:
$2,2,4$ 2 8
$2,2,2$ 6 24
$2,2,0$ 10 20
$2,0,4$ 4 8
$2,0,2$ 12 24
$2,0,0$ 20 20
$0,2,4$ 6 12
$0,2,2$ 18 36
$0,2,0$ 30 30
$0,0,4$ 12 12
$0,0,2$ 36 36
$0,0,0$ 60 * it's nice to point out that this value will be multiplied by zero
add every value on the rightmost side of each term and we will receive $230$ . Multiply by two because each segment can be flipped, to receive $460$ . There are $60 \cdot 59$ ways to choose two distinct points, so we get \[\dfrac{460}{60 \cdot 59} = \dfrac{23}{3 \cdot 59} = \dfrac{23}{177},\] for our answer of $23 + 177 = \boxed{200}$ .
Solution by jackshi2006
These problems are copyrighted © by the Mathematical Association of America.
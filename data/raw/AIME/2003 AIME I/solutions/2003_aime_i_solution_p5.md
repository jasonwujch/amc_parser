# 2003 AIME I Problem 5

## Problem

Consider the set of points that are inside or within one unit of a rectangular parallelepiped (box) that measures $3$ by $4$ by $5$ units. Given that the volume of this set is $\frac{m + n\pi}{p},$ where $m, n,$ and $p$ are positive integers , and $n$ and $p$ are relatively prime , find $m + n + p.$

## Solution
The set can be broken into several parts: the big $3\times 4 \times 5$ parallelepiped, $6$ external parallelepipeds that each share a face with the large parallelepiped and have a height of $1$ , the $1/8$ spheres (one centered at each vertex of the large parallelepiped), and the $1/4$ cylinders connecting each adjacent pair of spheres.
- The volume of the parallelepiped is $3 \times 4 \times 5 = 60$ cubic units.
- The volume of the external parallelepipeds is $2(3 \times 4 \times 1)+2(3 \times 5 \times 1 )+2(4 \times 5 \times 1)=94$ .
- There are $8$ of the $1/8$ spheres, each of radius $1$ . Together, their volume is $\frac{4}{3}\pi$ .
- There are $12$ of the $1/4$ cylinders, so $3$ complete cylinders can be formed. Their volumes are $3\pi$ , $4\pi$ , and $5\pi$ , adding up to $12\pi$ .
The combined volume of these parts is $60+94+\frac{4}{3}\pi+12\pi = \frac{462+40\pi}{3}$ . Thus, the answer is $m+n+p = 462+40+3 = \boxed{505}$ .
These problems are copyrighted © by the Mathematical Association of America.
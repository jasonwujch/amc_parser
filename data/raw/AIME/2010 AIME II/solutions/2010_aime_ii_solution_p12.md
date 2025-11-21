# 2010 AIME II Problem 12

## Problem

Two noncongruent integer-sided isosceles triangles have the same perimeter and the same area. The ratio of the lengths of the bases of the two triangles is $8: 7$ . Find the minimum possible value of their common perimeter.

## Solution 1
Let $s$ be the semiperimeter of the two triangles. Also, let the base of the longer triangle be $16x$ and the base of the shorter triangle be $14x$ for some arbitrary factor $x$ . Then, the dimensions of the two triangles must be $s-8x,s-8x,16x$ and $s-7x,s-7x,14x$ . By Heron's Formula, we have
\[\sqrt{s(8x)(8x)(s-16x)}=\sqrt{s(7x)(7x)(s-14x)}\] \[8\sqrt{s-16x}=7\sqrt{s-14x}\] \[64s-1024x=49s-686x\] \[15s=338x\]
Since $15$ and $338$ are coprime, to minimize, we must have $s=338$ and $x=15$ . However, we want the minimum perimeter. This means that we must multiply our minimum semiperimeter by $2$ , which gives us a final answer of $\boxed{676}$ .

## Solution 2
Let the first triangle have sides $16n,a,a$ , so the second has sides $14n,a+n,a+n$ . The height of the first triangle is $\frac{7}{8}$ the height of the second triangle. Therefore, we have \[a^2-64n^2=\frac{49}{64}((a+n)^2-49n^2).\] Multiplying this, we get \[64a^2-4096n^2=49a^2+98an-2352n^2,\] which simplifies to \[15a^2-98an-1744n^2=0.\] Solving this for $a$ , we get $a=n\cdot\frac{218}{15}$ , so $n=15$ and $a=218$ and the perimeter is $15\cdot16+218+218=\boxed{676}$ .
~john0512
### Notes
The triangles in question have sides $\boxed{240,218,218}$ and $\boxed{210,233,233}$ . ~eevee9406
We use $16x$ and $14x$ instead of $8x$ and $7x$ to ensure that the triangle has integral side lengths. Plugging $8x$ and $7x$ directly into Heron's gives $s=338$ , but for this to be true, the second triangle would have side lengths of $\frac{223}{2}$ , which is impossible.
~jd9
Video Solution: https://www.youtube.com/watch?v=IUxOyPH8b4o
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
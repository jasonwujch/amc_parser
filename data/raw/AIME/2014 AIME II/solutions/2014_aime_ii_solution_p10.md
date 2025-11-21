# 2014 AIME II Problem 10

## Problem

Let $z$ be a complex number with $|z|=2014$ . Let $P$ be the polygon in the complex plane whose vertices are $z$ and every $w$ such that $\frac{1}{z+w}=\frac{1}{z}+\frac{1}{w}$ . Then the area enclosed by $P$ can be written in the form $n\sqrt{3}$ , where $n$ is an integer. Find the remainder when $n$ is divided by $1000$ .

## Solution 1 (long but non-bashy)
Note that the given equality reduces to
\[\frac{1}{w+z} = \frac{w+z}{wz}\] \[wz = {(w+z)}^2\] \[w^2 + wz + z^2 = 0\] \[\frac{w^3 - z^3}{w-z} = 0\] \[w^3 = z^3, w \neq z\]
Now, let $w = r_w e^{i \theta_w}$ and likewise for $z$ . Consider circle $O$ with the origin as the center and radius 2014 on the complex plane. It is clear that $z$ must be one of the points on this circle, as $|z| = 2014$ .
By DeMoivre's Theorem, the complex modulus of $w$ is cubed when $w$ is cubed. Thus $w$ must lie on $O$ , since its the cube of its modulus, and thus its modulus, must be equal to $z$ 's modulus.
Again, by DeMoivre's Theorem, $\theta_w$ is tripled when $w$ is cubed and likewise for $z$ . For $w$ , $z$ , and the origin to lie on the same line, $3 \theta_w$ must be some multiple of 360 degrees apart from $3 \theta_z$ , so $\theta_w$ must differ from $\theta_z$ by some multiple of 120 degrees.
Now, without loss of generality, assume that $z$ is on the real axis. (The circle can be rotated to put $z$ in any other location.) Then there are precisely two possible distinct locations for $w$ ; one is obtained by going 120 degrees clockwise from $z$ about the circle and the other by moving the same amount counter-clockwise. Moving along the circle with any other multiple of 120 degrees in any direction will result in these three points.
Let the two possible locations for $w$ be $W_1$ and $W_2$ and the location of $z$ be point $Z$ . Note that by symmetry, $W_1W_2Z$ is equilateral, say, with side length $x$ . We know that the circumradius of this equilateral triangle is $2014$ , so using the formula $\frac{abc}{4R} = [ABC]$ and that the area of an equilateral triangle with side length $s$ is $\frac{s^2\sqrt{3}}{4}$ , so we have
\[\frac{x^3}{4R} = \frac{x^2\sqrt{3}}{4}\] \[x = R \sqrt{3}\] \[\frac{x^2\sqrt{3}}{4} = \frac{3R^2 \sqrt{3}}{4}\]
Since we're concerned with the non-radical part of this expression and $R = 2014$ ,
\[\frac{3R^2}{4} \equiv 3 \cdot 1007^2 \equiv 3 \cdot 7^2 \equiv \boxed{147} \pmod{1000}\]
and we are done. $\blacksquare$

## Solution 2 (short)
Assume $z = 2014$ . Then \[\frac{1}{2014 + w} = \frac{1}{2014} + \frac{1}{w}\]
\[2014w = w(2014 + w) + 2014(2014 + w)\]
\[2014w = 2014w + w^2 + 2014^2 + 2014w\]
\[0 = w^2 + 2014w + 2014^2\]
\[w = \frac{-2014 \pm \sqrt{2014^2 - 4(2014^2)}}{2} = -1007 \pm 1007\sqrt{3}i\]
Thus $P$ is an isosceles triangle with area $\frac{1}{2}(2014 - (-1007))(2\cdot 1007\sqrt{3}) = 3021\cdot 1007\sqrt{3}$ and $n \equiv 7\cdot 21\equiv \boxed{147} \pmod{1000}.$

## Solution 3 (Roots of Unity)
Notice that \[\frac1{w+z} = \frac{w+z}{wz} \implies 0 = w^2 + wz + z^2 = \frac{w^3-z^3}{w-z}.\] Hence, $w=ze^{2\pi i/3},ze^{4\pi i/3}$ , and $P$ is an equilateral triangle with circumradius $2014$ . Then, \[[P]=\frac{3}{2}\cdot 2014^2\cdot\sin\frac{\pi}3=3\cdot 1007^2\sqrt3,\] and the answer is $3\cdot 1007^2\equiv 3\cdot 7^2\equiv\boxed{147}\pmod{1000}$ .

## Solution 4 (Slick)
I find that generally, the trick to these kinds of AIME problems is to interpret the problem geometrically, and that is just what I did here. Looking at the initial equation, this seems like a difficult task, but rearranging yields a nicer equation: \[\frac1{z+w}=\frac1z+\frac1w\] \[\frac w{z+w}=\frac wz+1\] \[\frac w{z+w}=\frac{w+z}z\] \[\frac{w-0}{w-(-z)}=\frac{(-z)-w}{(-z)-0}\] We can interpret the difference of two complex numbers as a vector from one to the other, and we can interpret the quotient as a vector with an angle equal to the angle between the two vectors. Therefore, after labeling the complex numbers with $W$ ( $w$ ), $V$ ( $-z$ ), and $O$ ( $0$ ), we can interpret the above equation to mean that the $\angle OWV=\angle OVW$ , and hence triangle $OWV$ is isosceles, so length $OW$ = $OV$ . Rearranging the equation \[\frac{w-0}{w-(-z)}=\frac{(-z)-w}{(-z)-0},\] we find that \[(w-0)((-z)-0)=-(w-(-z))^2.\] Taking the magnitude of both sides and using the fact that $OW=OV\implies |w-0|=|(-z)-0|$ , we find that \[|w-0|^2=|w-(-z)|^2,\] so length $OW=VW$ and triangle $OWV$ is equilateral. There are only two possible $W$ 's for which $OWV$ is equilateral, lying on either side of $OV$ . After drawing these points on the circle of radius 2014 centered at the origin, it is easy to see that $z$ and the two $w$ 's form an equilateral triangle (this can be verified by simple angle chasing). Drawing a perpendicular bisector of one of the sides and using 30-60-90 triangles shows that the side length of this triangle is $2014\sqrt3$ and hence its area is $\frac{\sqrt3(2014\sqrt3)^2}4=\boxed{147}\sqrt3+1000k\sqrt3,$ for some integer $k$ .
~SymbolicPermutation
### Notes
This problem is killed by polar coordinates (complex numbers) . Solve using cosine-i-sine.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
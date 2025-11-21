# 2000 AIME II Problem 12

## Problem

The points $A$ , $B$ and $C$ lie on the surface of a sphere with center $O$ and radius $20$ . It is given that $AB=13$ , $BC=14$ , $CA=15$ , and that the distance from $O$ to $\triangle ABC$ is $\frac{m\sqrt{n}}k$ , where $m$ , $n$ , and $k$ are positive integers, $m$ and $k$ are relatively prime, and $n$ is not divisible by the square of any prime. Find $m+n+k$ .

## Solution 1
Let $D$ be the foot of the perpendicular from $O$ to the plane of $ABC$ . By the Pythagorean Theorem on triangles $\triangle OAD$ , $\triangle OBD$ and $\triangle OCD$ we get:
\[DA^2=DB^2=DC^2=20^2-OD^2\]
It follows that $DA=DB=DC$ , so $D$ is the circumcenter of $\triangle ABC$ .
By Heron's Formula the area of $\triangle ABC$ is (alternatively, a $13-14-15$ triangle may be split into $9-12-15$ and $5-12-13$ right triangles ):
\[K = \sqrt{s(s-a)(s-b)(s-c)} = \sqrt{21(21-15)(21-14)(21-13)} = 84\]
From $R = \frac{abc}{4K}$ , we know that the circumradius of $\triangle ABC$ is:
\[R = \frac{abc}{4K} = \frac{(13)(14)(15)}{4(84)} = \frac{65}{8}\]
Thus by the Pythagorean Theorem again,
\[OD = \sqrt{20^2-R^2} = \sqrt{20^2-\frac{65^2}{8^2}} = \frac{15\sqrt{95}}{8}.\]
So the final answer is $15+95+8=\boxed{118}$ .

## Solution 2 (Vectors)
We know the radii to $A$ , $B$ , and $C$ form a triangular pyramid $OABC$ . We know the lengths of the edges $OA = OB = OC = 20$ . First we can break up $ABC$ into its two component right triangles $5-12-13$ and $9-12-15$ . Let the $y$ axis be perpendicular to the base and $x$ axis run along $BC$ , and $z$ occupy the other dimension, with the origin as $C$ . We look at vectors $OA$ and $OC$ . Since $OAC$ is isoceles we know the vertex is equidistant from $A$ and $C$ , hence it is $7$ units along the $x$ axis. Hence for vector $OC$ , in form $<x,y,z>$ it is $<7, h, l>$ where $h$ is the height (answer) and $l$ is the component of the vertex along the $z$ axis. Now on vector $OA$ , since $A$ is $9$ along $x$ , and it is $12$ along $z$ axis, it is $<-2, h, 12- l>$ . We know both vector magnitudes are $20$ . Solving for $h$ yields $\frac{15\sqrt{95} }{8}$ , so Answer = $\boxed{118}$ .
Note: $OA$ is actually $\left< 2, -h, 12-l \right>$ . ~fermat_sLastAMC

## Solution 3
The distance from $O$ to $ABC$ forms a right triangle with the circumradius of the triangle and the radius of the sphere.
The hypotenuse has length $20$ , since it is the radius of the sphere.
The circumradius of a $13$ , $14$ , $15$ triangle is $\frac{65}{8}$ , so the distance from $O$ to $ABC$ is given by $\sqrt{20^2-(\frac{65}{8})^2} = \frac{15\sqrt{95}}{8}$ , and $15+95+8 = \boxed{118}$ .
-skibbysiggy
These problems are copyrighted © by the Mathematical Association of America. this is highly trivial for an AIME #12
this is highly trivial for an AIME #12
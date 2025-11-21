# 2011 AIME I Problem 14

## Problem

Let $A_1 A_2 A_3 A_4 A_5 A_6 A_7 A_8$ be a regular octagon. Let $M_1$ , $M_3$ , $M_5$ , and $M_7$ be the midpoints of sides $\overline{A_1 A_2}$ , $\overline{A_3 A_4}$ , $\overline{A_5 A_6}$ , and $\overline{A_7 A_8}$ , respectively. For $i = 1, 3, 5, 7$ , ray $R_i$ is constructed from $M_i$ towards the interior of the octagon such that $R_1 \perp R_3$ , $R_3 \perp R_5$ , $R_5 \perp R_7$ , and $R_7 \perp R_1$ . Pairs of rays $R_1$ and $R_3$ , $R_3$ and $R_5$ , $R_5$ and $R_7$ , and $R_7$ and $R_1$ meet at $B_1$ , $B_3$ , $B_5$ , $B_7$ respectively. If $B_1 B_3 = A_1 A_2$ , then $\cos 2 \angle A_3 M_3 B_1$ can be written in the form $m - \sqrt{n}$ , where $m$ and $n$ are positive integers. Find $m + n$ .

### Diagram

[asy] size(250); pair A,B,C,D,E,F,G,H,M,N,O,O2,P,W,X,Y,Z; A=(-76.537,184.776); B=(76.537,184.776); C=(184.776,76.537); D=(184.776,-76.537); E=(76.537,-184.776); F=(-76.537,-184.776); G=(-184.776,-76.537); H=(-184.776,76.537); M=(A+B)/2; N=(C+D)/2; O=(E+F)/2; O2=(A+E)/2; P=(G+H)/2; W=(100,-41.421); X=(-41.421,-100); Y=(-100,41.421); Z=(41.421,100); draw(A--B--C--D--E--F--G--H--A); label("$A_1$",A,dir(112.5)); label("$A_2$",B,dir(67.5)); label("$\textcolor{blue}{A_3}$",C,dir(22.5)); label("$A_4$",D,dir(337.5)); label("$A_5$",E,dir(292.5)); label("$A_6$",F,dir(247.5)); label("$A_7$",G,dir(202.5)); label("$A_8$",H,dir(152.5)); label("$M_1$",M,dir(90)); label("$\textcolor{blue}{M_3}$",N,dir(0)); label("$M_5$",O,dir(270)); label("$M_7$",P,dir(180)); label("$O$",O2,dir(152.5)); draw(M--W,red); draw(N--X,red); draw(O--Y,red); draw(P--Z,red); draw(O2--(W+X)/2,red); draw(O2--N,red); label("$\textcolor{blue}{B_1}$",W,dir(292.5)); label("$B_2$",(W+X)/2,dir(292.5)); label("$B_3$",X,dir(202.5)); label("$B_5$",Y,dir(112.5)); label("$B_7$",Z,dir(22.5)); [/asy] All distances are to scale.

## Solution 1
We use coordinates. Let the octagon have side length $2$ and center $(0, 0)$ . Then all of its vertices have the form $(\pm 1, \pm\left(1+\sqrt{2}\right))$ or $(\pm\left(1+\sqrt{2}\right), \pm 1)$ .
By symmetry, $B_{1}B_{3}B_{5}B_{7}$ is a square. Thus lines $\overleftrightarrow{B_{1}B_{3}}$ and $\overleftrightarrow{B_{5}B_{7}}$ are parallel, and its side length is the distance between these two lines. However, this is given to be the side length of the octagon, or $2$ .
Suppose the common slope of the lines is $m$ and let $m=\tan\theta$ . Then, we want to find \[\cos 2\left(90-\theta\right)=2\cos^{2}\left(90-\theta\right)-1=2\sin^{2}\theta-1.\]
It can easily be seen that the equations of the lines are \begin{align*} B_{1}B_{3}: y-mx+m\left(1+\sqrt{2}\right)=0 \\ B_{5}B_{7}: y-mx-m\left(1+\sqrt{2}\right)=0.\end{align*} By the distance between parallel lines formula , a corollary of the point to line distance formula , the distance between these two lines is \[\frac{|c_{2}-c_{1}|}{\sqrt{a^{2}+b^{2}}}=\frac{2m\left(1+\sqrt{2}\right)}{\sqrt{m^{2}+1}}.\] Since we want this to equal $2$ , we have \begin{align*}\frac{2m\left(1+\sqrt{2}\right)}{\sqrt{m^{2}+1}}&=2 \\ 4m^{2}\left(3+2\sqrt{2}\right)&=4m^{2}+4 \\ \left(12+8\sqrt{2}\right)m^{2}&=4m^{2}+4 \\ \left(8+8\sqrt{2}\right)m^{2}&=4 \\ m^{2}&=\frac{4}{8+8\sqrt{2}} \\ \Rightarrow m^{2}=\tan^{2}\theta=\frac{\sin^{2}\theta}{\cos^{2}\theta}&=\frac{1}{2+2\sqrt{2}}.\end{align*} Since $\sin^{2}\theta+\cos^{2}\theta=1,$ we have $\sin^{2}\theta=\frac{1}{3+2\sqrt{2}}$ . Thus \[2\sin^{2}\theta-1=\frac{2}{3+2\sqrt{2}}-1=\frac{-1-2\sqrt{2}}{3+2\sqrt{2}}=\frac{\left(-1-2\sqrt{2}\right)\left(3-2\sqrt{2}\right)}{\left(3+2\sqrt{2}\right)\left(3-2\sqrt{2}\right)}=\frac{5-4\sqrt{2}}{1}=5-\sqrt{32}.\] The answer is $\boxed{037}$ .

## Solution 2
Let $\theta=\angle M_1 M_3 B_1$ . Thus we have that $\cos 2 \angle A_3 M_3 B_1=\cos \left(2\theta + \frac{\pi}{2} \right)=-\sin2\theta$ .
Since $A_1 A_2 A_3 A_4 A_5 A_6 A_7 A_8$ is a regular octagon and $B_1 B_3 = A_1 A_2$ , let $k=A_1 A_2 = A_2 A_3 = B_1 B_3$ .
Extend $\overline{A_1 A_2}$ and $\overline{A_3 A_4}$ until they intersect. Denote their intersection as $I_1$ . Through similar triangles & the $45-45-90$ triangles formed, we find that $M_1 M_3=\frac{k}{2}(2+\sqrt2)$ .
We also have that $\triangle M_7 B_7 M_1 =\triangle M_1 B_1 M_3$ through ASA congruence ( $\angle B_7 M_7 M_1 =\angle B_1 M_1 M_3$ , $M_7 M_1 = M_1 M_3$ , $\angle B_7 M_1 M_7 =\angle B_1 M_3 M_1$ ). Therefore, we may let $n=M_1 B_7 = M_3 B_1$ .
Thus, we have that $\sin\theta=\frac{n-k}{\frac{k}{2}(2+\sqrt2)}$ and that $\cos\theta=\frac{n}{\frac{k}{2}(2+\sqrt2)}$ . Therefore $\cos\theta-\sin\theta=\frac{k}{\frac{k}{2}(2+\sqrt2)}=\frac{2}{2+\sqrt2}=2-\sqrt2$ .
Squaring gives that $\sin^2\theta - 2\sin\theta\cos\theta + \cos^2\theta = 6-4\sqrt2$ and consequently that $-2\sin\theta\cos\theta = 5-4\sqrt2 = -\sin2\theta$ through the identities $\sin^2\theta + \cos^2\theta = 1$ and $\sin2\theta = 2\sin\theta\cos\theta$ .
Thus we have that $\cos 2 \angle A_3 M_3 B_1=5-4\sqrt2=5-\sqrt{32}$ . Therefore $m+n=5+32=\boxed{037}$ .

## Solution 3
Let $A_1A_2 = 2$ . Then $B_1$ and $B_3$ are the projections of $M_1$ and $M_5$ onto the line $B_1B_3$ , so $2=B_1B_3=-M_1M_5\cos x$ , where $x = \angle A_3M_3B_1$ . Then since $M_1M_5 = 2+2\sqrt{2}, \cos x = \dfrac{-2}{2+2\sqrt{2}}= 1-\sqrt{2}$ , $\cos 2x = 2\cos^2 x -1 = 5 - 4\sqrt{2} = 5-\sqrt{32}$ , and $m+n=\boxed{037}$ .

## Solution 4
Notice that $R_3$ and $R_7$ are parallel ( $B_1B_3B_5B_7$ is a square by symmetry and since the rays are perpendicular) and $B_1B_3=B_3B_5=s=$ the distance between the parallel rays. If the regular hexagon as a side length of $s$ , then $M_3M_7$ has a length of $s+s\sqrt{2}$ . Let $X$ be on $R_3$ such that $M_7X$ is perpendicular to $M_3X$ , and $\phi=\angle M_7M_3X$ . The distance between $R_3$ and $R_7$ is $s=M_7X$ , so $\sin\phi=\frac{s}{s+s\sqrt{2}}=\frac{1}{1+\sqrt{2}}$ .
Since we are considering a regular hexagon, $M_3$ is directly opposite to $M_7$ and $\angle A_3M_3B_1=90 ^\circ +\phi$ . All that's left is to calculate $\cos 2\angle A_3M_3B_1=\cos^2(90^\circ+\phi)-\sin^2(90^\circ+\phi)=\sin^2\phi-\cos^2\phi$ . By drawing a right triangle or using the Pythagorean identity, $\cos^2\phi=\frac{2+2\sqrt2}{3+2\sqrt2}$ and $\cos 2\angle A_3M_3B_1=\frac{-1-2\sqrt2}{3+2\sqrt2}=5-4\sqrt2=5-\sqrt{32}$ , so $m+n=\boxed{037}$ .

## Solution 5
Assume that $A_1A_2=1.$ Denote the center $O$ , and the midpoint of $B_1$ and $B_3$ as $B_2$ . Then we have that \[\cos\angle A_3M_3B_1=\cos(\angle A_3M_3O+\angle OM_3B_1)=-\sin(\angle OM_3B_1)=-\frac{OB_2}{OM_3}=-\frac{1/2}{1/2+\sqrt2/2}=-\frac{1}{\sqrt2+1}=1-\sqrt2.\] Thus, by the cosine double-angle theorem, \[\cos2\angle A_3M_3B_1=2(1-\sqrt2)^2-1=5-\sqrt{32},\] so $m+n=\boxed{037}$ .

## Video Solution
2011 AIME I #14
MathProblemSolvingSkills.com
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
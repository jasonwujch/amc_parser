# 2017 AIME II Problem 15

## Problem

Tetrahedron $ABCD$ has $AD=BC=28$ , $AC=BD=44$ , and $AB=CD=52$ . For any point $X$ in space, suppose $f(X)=AX+BX+CX+DX$ . The least possible value of $f(X)$ can be expressed as $m\sqrt{n}$ , where $m$ and $n$ are positive integers, and $n$ is not divisible by the square of any prime. Find $m+n$ .

## Official Solution (MAA)
Let $M$ and $N$ be midpoints of $\overline{AB}$ and $\overline{CD}$ . The given conditions imply that $\triangle ABD\cong\triangle BAC$ and $\triangle CDA\cong\triangle DCB$ , and therefore $MC=MD$ and $NA=NB$ . It follows that $M$ and $N$ both lie on the common perpendicular bisector of $\overline{AB}$ and $\overline{CD}$ , and thus line $MN$ is that common perpendicular bisector. Points $B$ and $C$ are symmetric to $A$ and $D$ with respect to line $MN$ . If $X$ is a point in space and $X'$ is the point symmetric to $X$ with respect to line $MN$ , then $BX=AX'$ and $CX=DX'$ , so $f(X) = AX+AX'+DX+DX'$ .
Let $Q$ be the intersection of $\overline{XX'}$ and $\overline{MN}$ . Then $AX+AX'\geq 2AQ$ , from which it follows that $f(X) \geq 2(AQ+DQ) = f(Q)$ . It remains to minimize $f(Q)$ as $Q$ moves along $\overline{MN}$ .
Allow $D$ to rotate about $\overline{MN}$ to point $D'$ in the plane $AMN$ on the side of $\overline{MN}$ opposite $A$ . Because $\angle DNM$ is a right angle, $D'N=DN$ . It then follows that $f(Q) = 2(AQ+D'Q)\geq 2AD'$ , and equality occurs when $Q$ is the intersection of $\overline{AD'}$ and $\overline{MN}$ . Thus $\min f(Q) = 2AD'$ . Because $\overline{MD}$ is the median of $\triangle ADB$ , the Length of Median Formula shows that $4MD^2 = 2AD^2 + 2BD^2 - AB^2 = 2\cdot 28^2 + 2 \cdot 44^2 - 52^2$ and $MD^2 = 684$ . By the Pythagorean Theorem $MN^2 = MD^2 - ND^2 = 8$ .
Because $\angle AMN$ and $\angle D'NM$ are right angles, \[(AD')^2 = (AM+D'N)^2 + MN^2 = (2AM)^2 + MN^2 = 52^2 + 8 = 4\cdot 678.\] It follows that $\min f(Q) = 2AD' = 4\sqrt{678}$ . The requested sum is $4+678=\boxed{682}$ .

## Solution 2
Set $a=BC=28$ , $b=CA=44$ , $c=AB=52$ . Let $O$ be the point which minimizes $f(X)$ .
$\boxed{\textrm{Claim 1: } O \textrm{ is the gravity center } \ \tfrac {1}{4}(\vec A + \vec B + \vec C + \vec D)}$
$\textrm{Proof:}$ Let $M$ and $N$ denote the midpoints of $AB$ and $CD$ . From $\triangle ABD \cong \triangle BAC$ and $\triangle CDA \cong \triangle DCB$ , we have $MC=MD$ , $NA=NB$ an hence $MN$ is a perpendicular bisector of both segments $AB$ and $CD$ . Then if $X$ is any point inside tetrahedron $ABCD$ , its orthogonal projection onto line $MN$ will have smaller $f$ -value; hence we conclude that $O$ must lie on $MN$ . Similarly, $O$ must lie on the line joining the midpoints of $AC$ and $BD$ . $\square$
$\boxed{\textrm{Claim 2: The gravity center } O \textrm{ coincides with the circumcenter.} \phantom{\vec A}}$
$\textrm{Proof:}$ Let $G_D$ be the centroid of triangle $ABC$ ; then $DO = \tfrac 34 DG_D$ (by vectors). If we define $G_A$ , $G_B$ , $G_C$ similarly, we get $AO = \tfrac 34 AG_A$ and so on. But from symmetry we have $AG_A = BG_B = CG_C = DG_D$ , hence $AO = BO = CO = DO$ . $\square$
Now we use the fact that an isosceles tetrahedron has circumradius $R = \sqrt{\tfrac18(a^2+b^2+c^2)}$ .
Here $R = \sqrt{678}$ so $f(O) = 4R = 4\sqrt{678}$ . Therefore, the answer is $4 + 678 = \boxed{682}$ .

## Solution 3
Isosceles tetrahedron $ABCD$ or Disphenoid can be inscribed in a parallelepiped $AB'CD'C'DA'B,$ whose facial diagonals are the pares of equal edges of the tetrahedron $(AC = B'D',$ where $B'D' = BD).$ This parallelepiped is right-angled, therefore it is circumscribed and has equal diagonals. The center O of the circumscribed sphere (coincide with the centroid) has equal distance from each vertex. Tetrachedrons $ABCD$ and $A'B'C'D'$ are congruent, so point of symmetry O is point of minimum $f(X). f(O)= 4R$ , where $R$ is the circumradius of parallelepiped. \[8R^2 = 2 CC'^2 = 2CD'^2 + 2D'B^2 + 2BC'^2,\] \[2 CC'^2 = (CD'^2 + BC'^2) + (BC'^2 + BD'^2) + (CD'^2 + BD'^2) = AC^2 + AB^2+BC^2,\] \[R = OC =\sqrt{\frac {AB^2 + AC^2 + AD^2}{8}}, f(O)= 4R = 4\sqrt {678}.\]
vladimir.shelomovskii@gmail.com, vvsss (Reconstruction)
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
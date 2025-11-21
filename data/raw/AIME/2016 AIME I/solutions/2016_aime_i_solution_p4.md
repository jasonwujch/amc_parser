# 2016 AIME I Problem 4

## Problem

A right prism with height $h$ has bases that are regular hexagons with sides of length $12$ . A vertex $A$ of the prism and its three adjacent vertices are the vertices of a triangular pyramid. The dihedral angle (the angle between the two planes) formed by the face of the pyramid that lies in a base of the prism and the face of the pyramid that does not contain $A$ measures $60$ degrees. Find $h^2$ .

### Diagram

[asy] import bsp; typedef path3[] shape; shape operator *(transform3 T, shape p){ shape os; for(path3 g:p) os.push(T*g); return os; } path3 path(triple[] T){ path3 P; for(triple i:T) P=P--i; return P; } void addshapes(face[] F, shape[] shp, pen drawpen=currentpen, pen fillpen=white) { for(int i=0; i < shp.length; ++i) for(int j=0; j < shp[i].length; ++j) { path3 g=shp[i][j]; picture pic=F.push(g); if(fillpen != nullpen) filldraw(pic,project(g),fillpen, drawpen); else draw(pic,project(g),drawpen); // filldraw(pic,g,currentlight.intensity(F[F.length-1].point)*fillpen, drawpen); } } shape cylinder(real R=1, real H=1, int n=6){ shape Cyl; triple[] CTop; triple[] CBot; for(int i=0; i <= n; ++i) CBot.push((R*cos(2pi*i/n), R*sin(2pi*i/n),0)); CTop = CBot+(0,0,H); for(int i=0; i < n; ++i) Cyl.push(CBot[i]--CBot[i+1]--CTop[i+1]--CTop[i]--cycle); path3 P=path(CBot)--cycle; Cyl.push(P); Cyl.push(shift(H*Z)*P); return Cyl; } size(10cm,0); currentprojection=orthographic(1,1,1); shape cyl1 = cylinder(R=1, H=2); shape[] group={cyl1}; face[] hidden, visible; addshapes(hidden, group, drawpen=linewidth(bp)); addshapes(visible, group, drawpen=dotted, fillpen=nullpen); add(hidden); add(visible); //shipout(format="pdf"); [/asy]

~gundraja

## Solution 1
Let $B$ and $C$ be the vertices adjacent to $A$ on the same base as $A$ , and let $D$ be the last vertex of the triangular pyramid. Then $\angle CAB = 120^\circ$ . Let $X$ be the foot of the altitude from $A$ to $\overline{BC}$ . Then since $\triangle ABX$ is a $30-60-90$ triangle, $AX = 6$ . Since the dihedral angle between $\triangle ABC$ and $\triangle BCD$ is $60^\circ$ , $\triangle AXD$ is a $30-60-90$ triangle and $AD = 6\sqrt{3} = h$ . Thus $h^2 = \boxed{108}$ .
~gundraja

## Solution 2
Let $B$ and $C$ be the vertices adjacent to $A$ on the same base as $A$ , and let $D$ be the last vertex of the triangular pyramid. Notice that we can already find some lengths. We have $AB=AC=12$ (given) and $BC=BD=\sqrt{144+h^2}$ by the Pythagorean Theorem. Let $M$ be the midpoint of $BC$ . Then, we have $AM=6$ ( $30-60-90$ ) triangles and $DM=\sqrt{36+h^2}$ by the Pythagorean Theorem. Applying the Law of Cosines, since $\angle AMD=60^{\circ}$ , we get \[h^2=36+h^2+36-\frac12 \cdot 12 \sqrt{36+h^2} \implies h^2=\boxed{108},\] as desired.
-A1001
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
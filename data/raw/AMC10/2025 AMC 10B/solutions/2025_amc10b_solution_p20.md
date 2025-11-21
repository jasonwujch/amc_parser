# 2025 AMC 10B Problem 20

## Problem

Four congruent semicircles are inscribed in a square of side length $1$ so that their diameters are on the sides of the square, one endpoint of each diameter is at a vertex of the square, and adjacent semicircles are tangent to each other. A small circle centered at the center of the square is tangent to each of the four semicircles, as shown below. [asy] import geometry; size(6cm); real r = (sqrt(3)-1)/2, R = (sqrt(2) - 1)*(sqrt(3)-1)/2; draw((0,0) -- (1,0) -- (1, 1) -- (0,1) -- cycle); draw(arc((r, 0), r, 0, 180)); draw(arc((1, r), r, 90, 270)); draw(arc((1 - r, 1), r, 180, 360)); draw(arc((0, 1 - r), r, 270, 450)); draw(circle((1/2,1/2),R)); [/asy] The diameter of the small circle can be written as $(\sqrt a+b)(\sqrt c+d)$ , where $a$ , $b$ , $c$ , and $d$ are integers. What is $a+b+c+d$ ?

$\textbf{(A) } 3 \qquad \textbf{(B) } 5 \qquad \textbf{(C) } 8 \qquad \textbf{(D) } 9 \qquad \textbf{(E) } 11$

## Solution
Let the radius of the large semicircles be $r$ , and let the diameter of the inner be $D$ . Draw lines as follows:
[asy] import geometry; size(6cm); real r = (sqrt(3)-1)/2, R = (sqrt(2) - 1)*(sqrt(3)-1)/2; draw((0,0) -- (1,0) -- (1, 1) -- (0,1) -- cycle); draw(arc((r, 0), r, 0, 180)); draw(arc((1, r), r, 90, 270)); draw(arc((1 - r, 1), r, 180, 360)); draw(arc((0, 1 - r), r, 270, 450)); draw(circle((1/2,1/2),R)); draw((0.36602540378,0)--(0, 0.63397459622),dashed); label(“$r$”,(0,0.45),W); label(“$1-2r$”,(0,0.15),W); label(“$r$”,(0.15,0),S); label(“$r$”,(0.1,0.45),NE); label(“$r$”,(0.275,0.15),NE); label(“$r$”,(0.4,0.15),E); label(“$r$”,(0.6,0.85),E); label(“$D$”,(0.485,0.5),E); draw((0.36602540378,0)--(0.63397459622,1),dashed); label(“$r$”,(0.45,1),N); label(“$1-2r$”,(0.15,1),N); [/asy] By the Pythagorean Theorem, $r^2+(1-r)^2=(2r)^2$ , so $2r^2+2r-1=0$ . Hence $r=\frac{\sqrt{3}-1}{2}$ (we take the positive solution).
Now apply the Pythagorean Theorem on the quadrilateral’s altitude down to get $(1-2r)^2+1=(2r+D)^2$ . Solving yields $2r+D=\sqrt{8-4\sqrt{3}}=\sqrt{6}-\sqrt{2}$ . Then $D=\sqrt{6}-\sqrt{2}-\sqrt{3}+1=(\sqrt{3}-1)(\sqrt{2}-1)$ . Hence the answer is $3-1+2-1=\boxed{\textbf{(A) } 3}$ .
~ eevee9406

## Solution 2
We have the diagram:
[asy] import geometry; size(6cm); real r = (sqrt(3)-1)/2, R = (sqrt(2) - 1)*(sqrt(3)-1)/2; draw((0,0) -- (1,0) -- (1, 1) -- (0,1) -- cycle); draw(arc((r, 0), r, 0, 180)); draw(arc((1, r), r, 90, 270)); draw(arc((1 - r, 1), r, 180, 360)); draw(arc((0, 1 - r), r, 270, 450)); draw(circle((1/2,1/2),R)); draw((0.36602540378,0)--(0, 0.63397459622),dashed); draw((0.63397459622,1)--(0, 0.63397459622),dashed); draw((0.63397459622,1)--(1, 0.36602540378),dashed); draw((0.36602540378,0)--(1, 0.36602540378),dashed); label(“$x$”,(0.15,0),S); label(“$x$”,(0.1,0.45),SW); label(“$x$”,(0.275,0.15),SW); label(“$x$”,(0.22,0.64)); label(“$r$”,(0.45,0.55)); draw((0.5,0.5)--(0, 0.63397459622),dashed); draw((0.36602540378,0)--(0.5,0.5),dashed); draw((0.18301270189,0.31698729811)--(0.5,0.5),dashed); label("$J$",(0.20301270189,0.29698729811),SW); label(“$O$”,(0.485,0.5),E); label("$A$",(0,1),NW); label("$B$",(1,1),NE); label("$D$",(0,0),SW); label("$C$",(1,0),SE); label("$G$",(0.36602540378,0),S); label("$H$",(0, 0.63397459622),W); label("$E$",(0.63397459622,1),N); label("$F$",(1, 0.36602540378),E); label(“$\sqrt3 x$”,(0,0.3),W); [/asy]
We label the vertices of the square $A$ , $B$ , $C$ , and $D$ , the centers of the semicircle $E$ , $F$ , $G$ , and $H$ , and the center of the small circle $O$ . Lets call the radius of the big semicircle $x$ and the radius of the small circle $r$ .
Looking at $\triangle HDG$ , we can see it is a right triangle as $ABCD$ is a square, and we can also observe that since $DG$ is $x$ and the hypotenuse $GH$ is exactly twice at $2x$ , $\triangle HDG$ is a $30-60-90^\circ$ triangle. That means $HD$ is equal to $\sqrt3 x$ .
Upon inspection, we can also see that $AH$ is equal to $x$ , and since $ABCD$ is a unit square with all sides equal to $1$ , we can set the equation $HD+AH=1$ , \[x+\sqrt3 x = 1\] , so solving for $x$ , we get that \[x=\frac{\sqrt{3}-1}{2}\]
Then, if we compose an auxiliary line from $O$ perpendicular to $HG$ at $J$ , we can observe that $\triangle HOJ$ is an isosceles right triangle. That means $x+r=\sqrt2 x$ ( $1-1-\sqrt2$ relations), which means \[r=(\sqrt2 -1)x\]
We're asked to find the diameter of the small circle, so we can multiply the equation by $2$ to get \[2r=2(\sqrt2 -1)x\]
Plugging x in, the $2$ multiplied and the $2$ in the denominator cancel out, and we get \[2r=2(\sqrt2 -1)(\frac{\sqrt{3}-1}{2})\] \[2r=(\sqrt2 -1)(\sqrt3 -1)\]
$a$ , $b$ , $c$ , and $d$ are $2$ , $-1$ , $3$ respectively, and $-1$ , so $2+(-1)+3+(-1)$ gets us $\boxed{\textbf{(A) } 3}$
-Neo

## Solution 3
Let the centers of the four circles on $AB$ , $BC$ , $CD$ , and $AD$ be $E$ , $F$ , $G$ , and $H$ , respectively. Let $r_1$ be equal to the radius of one of the semicircles and $r_2$ be the radius of the inner circle. From the diagram from solution 2, we can easily recognize that $\triangle DHG$ is a $30-60-90$ triangle. We now form an equation $r_1 + r_1\sqrt{3} = 1$ . Solving for $r_1$ we will get $\frac{\sqrt{3}-1}{2}$ as the radius. We now need to recognize that $EFGH$ is a square. We can also see that $HF = 2r_1+2r_2$ . Because $EFGH$ is a square, and $HG = 2r_1$ , we can figure out that $HF = 2r_1\sqrt{2}$ . The final step is to plug in $r_1$ and solve for $2r_2$ (not $r_2$ as the question asks for the diameter).
$2(\frac{\sqrt{3}-1}{2})\sqrt{2} = 2(\frac{\sqrt{3}-1}{2}) + 2r_2$
$(\sqrt{3}-1)\sqrt{2} = \sqrt{3}-1 + 2r_2$
$(\sqrt{3}-1)(\sqrt{2}-1) = 2r_2$
Thus, the answer is $3 - 1 + 2 - 1 = \boxed{\textbf{(A) } 3}$
~ROGER8432V3

## Video Solution 1 by SpreadTheMathLove
https://www.youtube.com/watch?v=dLSWVrrKsgs

## Video Solution 2 by OmegaLearn.org
https://youtu.be/ttjGbBlkBfI

## Video Solution 3 (Fast and Easy)
https://www.youtube.com/watch?v=e6Yyk8C_TQc
~ Pi Academy
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
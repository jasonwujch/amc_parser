# 2020 AMC 8 Problem 9

## Problem

Akash's birthday cake is in the form of a $4 \times 4 \times 4$ inch cube. The cake has icing on the top and the four side faces, and no icing on the bottom. Suppose the cake is cut into $64$ smaller cubes, each measuring $1 \times 1 \times 1$ inch, as shown below. How many of the small pieces will have icing on exactly two sides?

[asy] /* Created by SirCalcsALot and sonone Code modfied from https://artofproblemsolving.com/community/c3114h2152994_the_old__aops_logo_with_asymptote */ import three; currentprojection=orthographic(1.75,7,2); //++++ edit colors, names are self-explainatory ++++ //pen top=rgb(27/255, 135/255, 212/255); //pen right=rgb(254/255,245/255,182/255); //pen left=rgb(153/255,200/255,99/255); pen top = rgb(170/255, 170/255, 170/255); pen left = rgb(81/255, 81/255, 81/255); pen right = rgb(165/255, 165/255, 165/255); pen edges=black; int max_side = 4; //+++++++++++++++++++++++++++++++++++++++ path3 leftface=(1,0,0)--(1,1,0)--(1,1,1)--(1,0,1)--cycle; path3 rightface=(0,1,0)--(1,1,0)--(1,1,1)--(0,1,1)--cycle; path3 topface=(0,0,1)--(1,0,1)--(1,1,1)--(0,1,1)--cycle; for(int i=0; i<max_side; ++i){ for(int j=0; j<max_side; ++j){ draw(shift(i,j,-1)*surface(topface),top); draw(shift(i,j,-1)*topface,edges); draw(shift(i,-1,j)*surface(rightface),right); draw(shift(i,-1,j)*rightface,edges); draw(shift(-1,j,i)*surface(leftface),left); draw(shift(-1,j,i)*leftface,edges); } } picture CUBE; draw(CUBE,surface(leftface),left,nolight); draw(CUBE,surface(rightface),right,nolight); draw(CUBE,surface(topface),top,nolight); draw(CUBE,topface,edges); draw(CUBE,leftface,edges); draw(CUBE,rightface,edges); // begin made by SirCalcsALot int[][] heights = {{4,4,4,4},{4,4,4,4},{4,4,4,4},{4,4,4,4}}; for (int i = 0; i < max_side; ++i) { for (int j = 0; j < max_side; ++j) { for (int k = 0; k < min(heights[i][j], max_side); ++k) { add(shift(i,j,k)*CUBE); } } } [/asy] $\textbf{(A) }12 \qquad \textbf{(B) }16 \qquad \textbf{(C) }18 \qquad \textbf{(D) }20 \qquad \textbf{(E) }24$

## Solution 1
Notice that, for a small cube which does not form part of the bottom face, it will have exactly $2$ faces with icing on them only if it is one of the $2$ center cubes of an edge of the larger cube. There are $12-4 = 8$ such edges (as we exclude the $4$ edges of the bottom face), so this case yields $2 \cdot 8 = 16$ small cubes. As for the bottom face, we can see that only the $4$ corner cubes have exactly $2$ faces with icing, so the total is $16+4 = \boxed{\textbf{(D) }20}$ .

## Solution 2
The following diagram shows $12$ of the small cubes having exactly $2$ faces with icing on them; that is all of them except for those on the hidden face directly opposite the front face.
But the hidden face is an exact copy of the front face, so the answer is $12+8=\boxed{\textbf{(D) }20}$ .

## Solution 3
It is observable that only the middle-edged pieces of each face will have the icing exactly on two sides. There are 4 such pieces on each face. Considering 5 faces of the cube (since the bottom is not iced), we can state that the number of such pieces of dimensions 1x1x1 will be 5x4=20. Therefore, our answer is 20.
~Edits by WrenMath

## Solution 4 (For Rubik's Cubers)
On a $4$ x $4$ Rubik's cube, there are exactly $24$ 'edge' pieces, $8$ 'corners', and $24$ 'center' pieces. Edge pieces have $2$ frosted faces (the ones on the bottom only have one, corners have $3$ frosted faces, and centers have $1$ . So since we have $24$ edges pieces, we subtract the $8$ 'edge' pieces on the bottom (they only have one frosted face), and then we add the $4$ bottom 'corner' pieces (they also have frosted faces). we get $24-8+4=\boxed{\textbf{(D) }20}$ .
-Solution by MismatchedCubing and Andrew_Lu
~Edits by WrenMath

## Video Solution by NiuniuMaths (Easy to understand!)
https://www.youtube.com/watch?v=8hgK6rESdek&t=9s
~NiuniuMaths

## Video Solution by Math-X (First understand the problem!!!)
https://youtu.be/UnVo6jZ3Wnk?si=9Se2Yd0UrYpxjhk3&t=1038
~Math-X

## Video Solution (CREATIVE THINKING!!!)
https://youtu.be/_diexvyeje4
~Education, the Study of Everything

## Video Solution by North America Math Contest Go-Go Go
https://www.youtube.com/watch?v=6LbBcFUmBr0
~North America Math Contest Go Go Go

## Video Solution by WhyMath
https://youtu.be/WyvmQUfxTfo
~savannahsolver

## Video Solution
https://youtu.be/61c1MR9tne8

## Video Solution by Interstigation
https://youtu.be/YnwkBZTv5Fw?t=355
~Interstigation

## Video Solution by STEMbreezy
https://youtu.be/U27z1hwMXKY?list=PLFcinOE4FNL0TkI-_yKVEYyA_QCS9mBNS&t=268
~STEMbreezy
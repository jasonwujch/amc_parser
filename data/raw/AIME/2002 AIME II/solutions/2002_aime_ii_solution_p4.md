# 2002 AIME II Problem 4

## Problem

Patio blocks that are hexagons $1$ unit on a side are used to outline a garden by placing the blocks edge to edge with $n$ on each side. The diagram indicates the path of blocks around the garden when $n=5$ .

If $n=202$ , then the area of the garden enclosed by the path, not including the path itself, is $m\left(\sqrt3/2\right)$ square units, where $m$ is a positive integer. Find the remainder when $m$ is divided by $1000$ .

## Solution 1
When $n>1$ , the path of blocks has $6(n-1)$ blocks total in it. When $n=1$ , there is just one lonely block. Thus, the area of the garden enclosed by the path when $n=202$ is
\[(1+6+12+18+\cdots +1200)A=(1+6(1+2+3...+200))A\] ,
where $A$ is the area of one block. Then, because $n(n+1)/2$ is equal to the sum of the first $n$ integers:
\[(1+6(1+2+3...+200))=(1+6((200)(201)/2))A=120601A\] .
Since $A=\dfrac{3\sqrt{3}}{2}$ , the area of the garden is
\[120601\cdot \dfrac{3\sqrt{3}}{2}=\dfrac{361803\sqrt{3}}{2}\] .
$m=361803$ , $\dfrac{m}{1000}=361$ Remainder $\boxed{803}$ .

## Solution 2
Note that this is just the definition for a centered hexagonal number, and the formula for $(n-1)^{th}$ term is $3n(n+1)+1$ . Applying this for $200$ as we want the inner area gives $120601$ . Then continue as above.
These problems are copyrighted © by the Mathematical Association of America.
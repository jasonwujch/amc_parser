# 2016 AIME II Problem 4

## Problem

An $a \times b \times c$ rectangular box is built from $a \cdot b \cdot c$ unit cubes. Each unit cube is colored red, green, or yellow. Each of the $a$ layers of size $1 \times b \times c$ parallel to the $(b \times c)$ faces of the box contains exactly $9$ red cubes, exactly $12$ green cubes, and some yellow cubes. Each of the $b$ layers of size $a \times 1 \times c$ parallel to the $(a \times c)$ faces of the box contains exactly $20$ green cubes, exactly $25$ yellow cubes, and some red cubes. Find the smallest possible volume of the box.

## Solution
By counting the number of green cubes $2$ different ways, we have $12a=20b$ , or $a=\dfrac{5}{3} b$ . Notice that there are only $3$ possible colors for unit cubes, so for each of the $1 \times b \times c$ layers, there are $bc-21$ yellow cubes, and similarly there are $ac-45$ red cubes in each of the $1 \times a \times c$ layers. Therefore, we have $a(bc-21)=25b$ and $b(ac-45)=9a$ . We check a few small values of $a,b$ and solve for $c$ , checking $(a,b)=(5,3)$ gives $c=12$ with a volume of $180$ , $(a,b)=(10,6)$ gives $c=6$ with a volume of $360$ , and $(a,b)=(15,9)$ gives $c=4$ , with a volume of $540$ . Any higher $(a,b)$ will $ab>180$ , so therefore, the minimum volume is $\boxed{180}$ .

## Solution 2
The total number of green cubes is given by $12a=20b\Longrightarrow a=\frac{5}{3}b$ .
Let $r$ be the number of red cubes on each one of the $b$ layers then the total number of red cubes is $9a=br$ . Substitute $a=\frac{5}{3}b$ gives $r=15$ .
Repeating the procedure on the number of yellow cubes $y$ on each of the $a$ layers gives $y=15$ .
Therefore $bc=9+12+15=36$ and $ac=15+20+25=60$ . Multiplying yields $abc^2=2160$ .
Since $abc^2$ is fixed, $abc$ is minimized when $c$ is maximized, which occurs when $a$ , $b$ are minimized (since each of $ac$ , $bc$ is fixed). Thus $(a,b,c)=(3,5,12)\Longrightarrow abc=\boxed{180}$
~ Nafer
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
# 2019 AMC 10B Problem 4

## Problem

All lines with equation $ax+by=c$ such that $a,b,c$ form an arithmetic progression pass through a common point. What are the coordinates of that point?

$\textbf{(A) } (-1,2) \qquad\textbf{(B) } (0,1) \qquad\textbf{(C) } (1,-2) \qquad\textbf{(D) } (1,0) \qquad\textbf{(E) } (1,2)$

## Solution 1
If all lines satisfy the condition, then we can just plug in values for $a$ , $b$ , and $c$ that form an arithmetic progression. Let's use $a=1$ , $b=2$ , $c=3$ , and $a=1$ , $b=3$ , $c=5$ . Then the two lines we get are: \[x+2y=3\] \[x+3y=5\] Use elimination to deduce \[y = 2\] and plug this into one of the previous line equations. We get \[x+4 = 3 \Rightarrow x=-1\] Thus the common point is $\boxed{\textbf{(A) } (-1,2)}$ .
~IronicNinja

## Solution 2
We know that $a$ , $b$ , and $c$ form an arithmetic progression, so if the common difference is $d$ , we can say $a,b,c = a, a+d, a+2d.$ Now we have $ax+ (a+d)y = a+2d$ , and expanding gives $ax + ay + dy = a + 2d.$ Factoring gives $a(x+y-1)+d(y-2) = 0$ . Since this must always be true (regardless of the values of $a$ and $d$ ), we must have $x+y-1 = 0$ and $y-2 = 0$ , so $x,y = -1, 2,$ and the common point is $\boxed{\textbf{(A) } (-1,2)}$ .

## Solution 3
We use process of elimination. $\textbf{B}$ doesn't necessarily work because $b = c$ isn't always true. $\textbf{C, D, E}$ also doesn't necessarily work because the x-value is $1$ , but the y-value is an integer. So by process of elimination, $\boxed{\textbf{(A) } (-1, 2)}$ is our answer. ~Baolan

## Solution 4
We know that in $ax + by = c$ , $a$ , $b$ , and $c$ are in an arithmetic progression. We can simplify any arithmetic progression to be $0$ , $1$ , $2$ , and $-1$ , $0$ , $1$ .
For example, the progression $2$ , $4$ , $6$ can be rewritten as $0$ , $2$ , $4$ by going back by one value. We can then divide all 3 numbers by 2 which gives us $0$ , $1$ , $2$ .
Now, we substitute $a$ , $b$ , and $c$ with $0$ , $1$ , $2$ , and $-1$ , $0$ , $1$ respectively. This gives us
$y = 2$ and $-x = 1$ which can be written as $x = -1$ . The only point of intersection is $(-1,2)$ . So, our answer is
$\boxed{\textbf{(A) } (-1, 2)}$ . ~Starshooter11

## Solution 5 (Solution 1 but faster and easier)
Since the problem doesn't specify any further conditions other than an arithmetic sequence (i.e., that the numbers have to be increasing, or positive or something like that) we choose the sequences $(0, 1, 2)$ and $(1, 0, -1)$ which correspond to the equations $0x+y=2$ and $1x+0y=-1$ . These just simplify to $x=-1$ and $y=2$ , so the coordinate is $(-1, 2)$ .
~JH. L

## Video Solution
https://youtu.be/9QZlOagfFMs
~Education, the Study of Everything

## Video Solution
https://youtu.be/kB_dR5H7Pzw
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
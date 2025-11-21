# 2001 AIME II Problem 8

## Problem

A certain function $f$ has the properties that $f(3x) = 3f(x)$ for all positive real values of $x$ , and that $f(x) = 1-|x-2|$ for $1\le x \le 3$ . Find the smallest $x$ for which $f(x) = f(2001)$ .

## Solution 1
Iterating the condition $f(3x) = 3f(x)$ , we find that $f(x) = 3^kf\left(\frac{x}{3^k}\right)$ for positive integers $k$ . We know the definition of $f(x)$ from $1 \le x \le 3$ , so we would like to express $f(2001) = 3^kf\left(\frac{2001}{3^k}\right),\ 1 \le \frac{2001}{3^k} \le 3 \Longrightarrow k = 6$ . Indeed,
\[f(2001) = 729\left[1 - \left| \frac{2001}{729} - 2\right|\right] = 186.\]
We now need the smallest $x$ such that $f(x) = 3^kf\left(\frac{x}{3^k}\right) = 186$ . The range of $f(x),\ 1 \le x \le 3$ , is $0 \le f(x) \le 1$ . So when $1 \le \frac{x}{3^k} \le 3$ , we have $0 \le f\left(\frac{x}{3^k}\right) = \frac{186}{3^k} \le 1$ . Multiplying by $3^k$ : $0 \le 186 \le 3^k$ , so the smallest value of $k$ is $k = 5$ . Then,
\[186 = {3^5}f\left(\frac{x}{3^5}\right).\]
Because we forced $1 \le \frac{x}{3^5} \le 3$ , so
\[186 = {3^5}f\left(\frac{x}{3^5}\right) = 243\left[1 - \left| \frac{x}{243} - 2\right|\right] \Longrightarrow x = \pm 57 + 2 \cdot 243.\]
We want the smaller value of $x = \boxed{429}$ .
An alternative approach is to consider the graph of $f(x)$ , which iterates every power of $3$ , and resembles the section from $1 \le x \le 3$ dilated by a factor of $3$ at each iteration.

## Solution 2 (Graphing)
First, we start by graphing the function when $1\leq{x}\leq3$ , which consists of the lines $y=x-1$ and $y=3-x$ that intersect at $(2,1)$ . Similarly, using $f(3x)=3f(x)$ , we get a dilation of our initial figure by a factor of 3 for the next interval and so on. Observe that the intersection of two lines always has coordinates $(2y,y)$ where $y=3^a$ for some $a$ . First, we compute $f(2001)$ . The nearest intersection point is $(1458,729)$ when $a=7$ . Therefore, we can safely assume that $f(2001)$ is somewhere on the line with a slope of $-1$ that intersects at that nearest point. Using the fact that the slope of the line is $-1$ , we compute $f(2001)=729-543=186$ . However, we want the minimum value such that $f(x)=186$ and we see that there is another intersection point on the left which has a $y>186$ , namely $(486,243)$ . Therefore, we want the point that lies on the line with slope $1$ that intersects this point. Once again, since the slope of the line is $1$ , we get $x=486-57=\boxed{429}$ .
~ Magnetoninja

## Solution 3 (Complete Bash but FAST)
We evaluate the first few terms of f(x) to try to find a pattern.
F(1)=0 F(2)=1 F(3)=0 F(4)=1 F(5) = 3(F( $\frac{5}{3}$ )) = 2
That doesn‘t seem to be getting us anywhere. We notice what we did with f(5) will probably work with f(2001).
$F(2001) = 3f(667)=9f(\frac{667}{3}) = 27f(\frac{667}{9}) = 81f(\frac{667}{27})=243f(\frac{667}{81})=729f(\frac{667}{243})$
From here, we can evaluate f(2001) = $186$ when we plug in $\frac{667}{243}$ into $1 - |x - 2|$ . So all we need to find is the least number, let‘s call it, say y such that f(y)=186.
Repeating the same process we did before with f(2001),
$186 = F(y)= 3f(\frac{y}{3}) = 9f(\frac{y}{9}) = 27f(\frac{y}{27})=81f(\frac{y}{81}) = 243f(\frac{y}{243})$
Notice that we stopped at $243f(\frac{y}{243})$ because $\frac{186}{243}$ is inside the range of $1-|x-2|$ , which is [0,1]. Now, f(y/243) = 186/243. Setting $186/243 = 1-|x-2|$ , we get 2 solutions for x: $\frac{543}{243}$ and $\frac{429}{243}$ .
Now, the problem asks for the smallest solution, so we obviously choose 429/243 as the solution for 243f(y/243) because it is smaller.
We found that $\frac{y}{243}=\frac{429}{243}$ , and solving this equation gives our answer $\boxed{429}$
~MathCosine

## Video Solution
https://www.youtube.com/watch?v=j3hj2yNga0w
by Coach Jay
These problems are copyrighted © by the Mathematical Association of America.
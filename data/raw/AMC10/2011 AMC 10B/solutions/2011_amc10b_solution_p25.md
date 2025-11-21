# 2011 AMC 10B Problem 25

## Problem

Let $T_1$ be a triangle with side lengths $2011, 2012,$ and $2013$ . For $n \ge 1$ , if $T_n = \triangle ABC$ and $D, E,$ and $F$ are the points of tangency of the incircle of $\triangle ABC$ to the sides $AB, BC$ , and $AC,$ respectively, then $T_{n+1}$ is a triangle with side lengths $AD, BE,$ and $CF,$ if it exists. What is the perimeter of the last triangle in the sequence $( T_n )$ ?

$\textbf{(A)}\ \frac{1509}{8} \qquad\textbf{(B)}\ \frac{1509}{32} \qquad\textbf{(C)}\ \frac{1509}{64} \qquad\textbf{(D)}\ \frac{1509}{128} \qquad\textbf{(E)}\ \frac{1509}{256}$

## Solution 1
By constructing the bisectors of each angle and the perpendicular radii of the incircle the triangle consists of 3 kites.
Hence $AD=AF$ and $BD=BE$ and $CE=CF$ . Let $AD = x, BD = y$ and $CE = z$ gives three equations:
$x+y = a-1$
$x+z = a$
$y+z = a+1$
(where $a = 2012$ for the first triangle.)
Solving gives:
$x= \frac{a}{2} -1$
$y = \frac{a}{2}$
$z = \frac{a}{2}+1$
Subbing in gives that $T_2$ has sides of $1005, 1006, 1007$ .
$T_3$ can easily be derived from this as the sides still differ by 1 hence the above solutions still work (now with $a=1006$ ). All additional triangles will differ by one as the solutions above differ by one so this process can be repeated indefinitely until the side lengths no longer form a triangle.
Subbing in gives $T_3$ with sides $502, 503, 504$ .
$T_4$ has sides $\frac{501}{2}, \frac{503}{2}, \frac{505}{2}$ .
$T_5$ has sides $\frac{499}{4}, \frac{503}{4}, \frac{507}{4}$ .
$T_6$ has sides $\frac{495}{8}, \frac{503}{8}, \frac{511}{8}$ .
$T_7$ has sides $\frac{487}{16}, \frac{503}{16}, \frac{519}{16}$ .
$T_8$ has sides $\frac{471}{32}, \frac{503}{32}, \frac{535}{32}$ .
$T_9$ has sides $\frac{439}{64}, \frac{503}{64}, \frac{567}{64}$ .
$T_{10}$ has sides $\frac{375}{128}, \frac{503}{128}, \frac{631}{128}$ .
$T_{11}$ would have sides $\frac{247}{256}, \frac{503}{256}, \frac{759}{256}$ but these lengths do not make a triangle as \[\frac{247}{256} + \frac{503}{256} < \frac{759}{256}\]
Likewise, you could create an equation instead of listing all the triangles to $T_{11}$ . The sides of a triangle $T_{k}$ would be \[\frac{503}{2^{k-3}} - 1, \frac{503}{2^{k-3}}, \frac{503}{2^{k-3}} + 1\] We then have \[503 - 2^{k-3} + 503 > 503 + 2^{k-3}\] \[1006 - 2^{k-3} > 503 + 2^{k-3}\] \[503 > 2^{k-2}\] \[9 > k-2\] \[k < 11\] Hence, the first triangle which does not exist in this sequence is $T_{11}$ .
Hence the perimeter is \[\frac{375}{128} + \frac{503}{128} + \frac{631}{128} = \boxed{\textbf{(D)} \frac{1509}{128}}\] .

## Solution 2
Proceeding similarly to the first solution, we have that sides of each triangle are of the form $a, a+1, a+2$ for some number $a$ . Also, note that the perimeter of each triangle is half of the previous one. In order for the triangle to not exist, it must not satisfy the triangle inequality, meaning that $a + a + 1 < a+2 \Rightarrow a<1$ . Then, the perimeter would be $a + a + 1 + a + 2 = 3a + 3 < 6$ . So, to have a proper triangle, we have $\frac{3018}{2^{k}} > 6 \Rightarrow 2^k < 503 \Rightarrow 2^{k} < 512$ . The first triangle to not work would have perimeter $\frac{3018}{256} = \frac{1509}{128}$ , thus the answer is $\boxed{\textbf{(D)} \frac{1509}{128}}$ .

## Solution 3
This problem is a PoP(Power of Point) Bash exercise. What I did to solve this problem was look at recursive perimeters. The first ever perimeter is $P_1 = 2011 + 2012 + 2013$ . Next, by PoP, inscribing the circle gives us three new lengths, namely $AD, BE, CF$ . Denote $AD$ as $x_1$ and homogeneously the others. Then, $x_1 + x_2 = 2011, x_2 + x_3 = 2012$ , and $x_1 + x_3 = 2013$ . If we add all these equations up and divide by $2$ , we get $x_1 + x_2 + x_3 = \frac{2011 + 2012 + 2013}{2}$ . Writing this with $P_1 = 2011 + 2012 + 2013$ , we get that our new perimeter, $P_2$ , is indeed equal to $\frac{P_1}{2}$ . Similarly, by the same concept, we get that $P_3 = \frac{P_1}{4}$ and the pattern keeps going. In general, I found that for each new perimeter $P_n$ , $P_n = \frac{P_1}{2^{n-1}}$ . Now, substituting in the numerical value of $P_1$ , we get that $P_n = \frac{2011 + 2012 + 2013}{2^{n-1}}$ . If you keep dividing the numerator and denominator by 2, I got that: $P_n = \frac{1509}{2^{n-3}}$ . This representation of a new perimeter in terms of $n$ looks very similar to the option choices, so we're on the right path. Now, all we need to do is find out the last value of $n$ when the sequence stops working. By the Triangular Inequality, we may be able to finish this off. Now, I won't go into depths here, but listing out terms and using the Triangular Inequality gives us: First Sequence: $x_1 < 2012$
$x_2 < 2013$
$x_3 < 2011$ . The ordered triple for this set of $(x_1, x_2, x_3)$ is $(1005, 1006, 1007)$ if you solve the PoP system of equations we got earlier. If you keep listing out terms, we can come up with the general form, and that is: $x_1 < \frac{503}{2^{n-4}}$
$x_2 < \frac{503}{2^{n-4}} + 1$
$x_3 < \frac{503}{2^{n-4}} - 1$ . The ordered triple for this set of $(x_1, x_2, x_3)$ is $(\frac{503}{2^{n-4}}, \frac{503}{2^{n-4}} - 1, \frac{503}{2^{n-4}} + 1)$ . Now, if we plug in these values of $x_1, x_2$ , and $x_3$ into the inequalities, we see that the first two are always satisfied, but the last one is only satisfied when: $2^{n-2} < 503$ (You will get this if you simplify the last inequality). The last $n$ for this to be satisfied is when $n = 10$ . If we go up to our general representation of $P_n$ , we see that $P_n = \frac{1509}{2^{n-3}}$ . Plugging in $10$ because this is the last $n$ (and also the last triangle), we our final answer of $\frac{1509}{2^{7}} = \boxed{\frac{1509}{128}}$ or $\boxed{D}$ .
~ilikemath247365
### See Also
Identical problem to the 2011 AMC 12B Problems/Problem 22 .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
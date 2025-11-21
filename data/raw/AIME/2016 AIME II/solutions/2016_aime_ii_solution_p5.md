# 2016 AIME II Problem 5

## Problem

Triangle $ABC_0$ has a right angle at $C_0$ . Its side lengths are pairwise relatively prime positive integers, and its perimeter is $p$ . Let $C_1$ be the foot of the altitude to $\overline{AB}$ , and for $n \geq 2$ , let $C_n$ be the foot of the altitude to $\overline{C_{n-2}B}$ in $\triangle C_{n-2}C_{n-1}B$ . The sum $\sum_{n=2}^\infty C_{n-2}C_{n-1} = 6p$ . Find $p$ .

## Solution 1
Do note that by counting the area in 2 ways, the first altitude is $x = \frac{ab}{c}$ . By similar triangles, the common ratio is $\rho = \frac{a}{c}$ for each height, so by the geometric series formula, we have \begin{align} 6p=\frac{x}{1-\rho} = \frac{ab}{c-a}. \end{align} Writing $p=a+b+c$ and clearing denominators, we get \[13a=6p .\] Thus $p=13q$ , $a=6q$ , and $b+c=7q$ , i.e. $c=7q-b$ . Plugging these into $(1)$ , we get $78q(q-b)=6bq$ , i.e., $14b=13q$ . Thus $q=14r$ and $p=182r$ , $b=13r$ , $a=84r$ , $c=85r$ . Taking $r=1$ (since $a,b,c$ are relatively prime) we get $p=\boxed{182}$ .
Note this solution seems to have some serious errors

## Solution 2
Note that by counting the area in 2 ways, the first altitude is $\dfrac{ab}{c}$ . By similar triangles, the common ratio is $\dfrac{a}{c}$ for reach height, so by the geometric series formula, we have $6p=\dfrac{\dfrac{ab}{c}}{1-\dfrac{a}{c}}$ . Multiplying by the denominator and expanding, the equation becomes $\dfrac{ab}{c}=6a+6b+6c-\dfrac{6a^2}{c}-\dfrac{6ab}{c}-6a$ . Cancelling $6a$ and multiplying by $c$ yields $ab=6bc+6c^2-6a^2-6ab$ , so $7ab = 6bc+6b^2$ and $7a=6b+6c$ . Checking for Pythagorean triples gives $13,84,$ and $85$ , so $p=13+84+85=\boxed{182}$
Note: a more rigorous solution instead of checking for triples would be to substitute $c = \sqrt{a^2 + b^2}$ and heavily simplifying the equation. Eventually we are left with $13a = 84b,$ and since $a, b$ are relatively prime, we know $a = 84$ and $b = 13.$ From here we can note that $(13, 84, 85)$ is a pythagorean triple or again use the Pythagorean Theorem to find $c = 85.$ Thus, the answer is $\boxed{182}.$
Solution modified/fixed from Shaddoll's solution.

## Solution 3
We start by splitting the sum of all $C_{n-2}C_{n-1}$ into two parts: those where $n-2$ is odd and those where $n-2$ is even.
First consider the sum of the lengths of the segments for which $n-2$ is odd for each $n\geq2$ . The perimeters of these triangles can be expressed using $p$ and ratios that result because of similar triangles. Considering triangles where $n-2$ is odd, we find that the perimeter for each such $n$ is $p\left(\frac{C_{n-1}C_{n}}{C_{0}B}\right)$ . Thus,
$p\sum_{n=1}^{\infty}\frac{C_{2n-1}C_{2n}}{C_{0}B}=6p+C_{0}B$ .
Simplifying,
$\sum_{n=1}^{\infty}C_{2n-1}C_{2n}=6C_{0}B + \frac{(C_{0}B)^2}{p}=C_{0}B\left(6+\frac{C_{0}B}{p}\right)$ . (1)
Continuing with a similar process for the sum of the lengths of the segments for which $n-2$ is even,
$p\sum_{n=1}^{\infty}\frac{C_{2n-2}C_{2n-1}}{C_{0}B}=6p+C_{0}A+AB=7p-C_{0}B$ .
Simplifying,
$\sum_{n=1}^{\infty}C_{2n-2}C_{2n-1}=C_{0}B\left(7-\frac{C_{0}B}{p}\right)$ . (2)
Adding (1) and (2) together, we find that
$6p=13C_{0}B \Rightarrow p=\frac{13C_{0}B}{6}=C_{0}B+C_{0}A+AB \Rightarrow \frac{7C_{0}B}{6}=C_{0}A+AB \Rightarrow 7C_{0}B=6C_{0}A + 6AB$ .
Setting $a=C_{0}B$ , $b=C_{0}A$ , and $c=AB$ , we can now proceed as in Shaddoll's solution, and our answer is $p=13+84+85=\boxed{182}$ .

## Solution 4
[asy] size(10cm); // Setup pair A, B; pair C0, C1, C2, C3, C4, C5, C6, C7, C8; A = (5, 0); B = (0, 3); C0 = (0, 0); C1 = foot(C0, A, B); C2 = foot(C1, C0, B); C3 = foot(C2, C1, B); C4 = foot(C3, C2, B); C5 = foot(C4, C3, B); C6 = foot(C5, C4, B); C7 = foot(C6, C5, B); C8 = foot(C7, C6, B); // Labels label("$A$", A, SE); label("$B$", B, NW); label("$C_0$", C0, SW); label("$C_1$", C1, NE); label("$C_2$", C2, W); label("$C_3$", C3, NE); label("$C_4$", C4, W); label("$a$", (B+C0)/2, W); label("$b$", (A+C0)/2, S); label("$c$", (A+B)/2, NE); // Drawings draw(A--B--C0--cycle); draw(C0--C1--C2, red); draw(C2--C3--C4--C5--C6--C7--C8); draw(C0--C2, blue); [/asy]
Let $a = BC_0$ , $b = AC_0$ , and $c = AB$ . Note that the total length of the red segments in the figure above is equal to the length of the blue segment times $\frac{a+c}{b}$ .
The desired sum is equal to the total length of the infinite path $C_0 C_1 C_2 C_3 \cdots$ , shown in red in the figure below. Since each of the triangles $\triangle C_0 C_1 C_2, \triangle C_2 C_3 C_4, \dots$ on the left are similar, it follows that the total length of the red segments in the figure below is equal to the length of the blue segment times $\frac{a+c}{b}$ . In other words, we have that $a\left(\frac{a+c}{b}\right) = 6p$ .
Guessing and checking Pythagorean triples reveals that $a = 84$ , $b=13$ , $c = 85$ , and $p = a + b + c = \boxed{182}$ satisfies this equation.
[asy] size(10cm); // Setup pair A, B; pair C0, C1, C2, C3, C4, C5, C6, C7, C8; A = (5, 0); B = (0, 3); C0 = (0, 0); C1 = foot(C0, A, B); C2 = foot(C1, C0, B); C3 = foot(C2, C1, B); C4 = foot(C3, C2, B); C5 = foot(C4, C3, B); C6 = foot(C5, C4, B); C7 = foot(C6, C5, B); C8 = foot(C7, C6, B); // Labels label("$A$", A, SE); label("$B$", B, NW); label("$C_0$", C0, SW); label("$a$", (B+C0)/2, W); label("$b$", (A+C0)/2, S); label("$c$", (A+B)/2, NE); // Drawings draw(A--B--C0--cycle); draw(C0--C1--C2--C3--C4--C5--C6--C7--C8, red); draw(C0--B, blue); [/asy]

## Solution 5
This solution proceeds from $\frac{\frac{ab}{c}}{1-\frac{a}{c}} = \frac{\frac{ab}{c}}{\frac{c-a}{c}} = \frac{ab}{c-a} = 6(a+b+c)$ . Note the general from for a primitive pythagorean triple, $m^2-n^2, 2mn, m^2+n^2$ and after substitution, letting $a = m^2-n^2, b = 2mn, c = m^2+n^2$ into the previous equation simplifies down very nicely into $m = 13n$ . Thus $a = 168n^2, b = 26n^2, c = 170n^2$ . Since we know all three side lengths are relatively prime, we must divide each by 2 and let n = 1 giving $a = 84, b = 13, c = 85$ yielding $p = a + b + c = \boxed{182}$ .
Alternate way to find a, b, and c (from VarunGotem) : $7a=6b+6c$ implies that $6b=7a-6c$ . Because $a^2+b^2=c^2$ , $36a^2+(6b)^2=36c^2$ . Plugging in gives $85a^2-84ac+36c^2=36c^2$ . Simplifying gives $85a-84c=0$ , and since $a$ and $c$ are relatively prime, $a=84$ and $c=85$ . This means $b=13$ and $p=13+84+85=\boxed{182}$ .

## Solution 6
For this problem, first notice that its an infinite geometric series of $6(a+b+c)=\frac{ab}{c-b}$ if $c$ is the hypotenuse. WLOG $a<b$ , we can generalize a pythagorean triple of $x^2-y^2, 2xy, x^2+y^2$ . Let $b=2xy$ , then this generalization gives $6(a+b+c)(c-b)=ab$ \[(x^2-y^2)2xy=6(2x^2+2xy)(x-y)^2\] \[(x+y)xy=6(x^2+xy)(x-y)\] \[xy=6x(x-y)\] \[7xy=6x^2\] \[y=\frac{6}{7}x\]
Now this is just clear. Let $x=7m$ and $y=6m$ for $m$ to be a positive integer, the pythagorean triple is $13-84-85$ which yields $\boxed{182}$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
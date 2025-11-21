# 2006 AIME II Problem 6

## Problem

Square $ABCD$ has sides of length 1. Points $E$ and $F$ are on $\overline{BC}$ and $\overline{CD},$ respectively, so that $\triangle AEF$ is equilateral. A square with vertex $B$ has sides that are parallel to those of $ABCD$ and a vertex on $\overline{AE}.$ The length of a side of this smaller square is $\frac{a-\sqrt{b}}{c},$ where $a, b,$ and $c$ are positive integers and $b$ is not divisible by the square of any prime. Find $a+b+c.$

## Solution 1
[asy] unitsize(32mm); defaultpen(linewidth(.8pt)+fontsize(10pt)); dotfactor=3; pair B = (0, 0), C = (1, 0), D = (1, 1), A = (0, 1); pair Ep = (2 - sqrt(3), 0), F = (1, sqrt(3) - 1); pair Ap = (0, (3 - sqrt(3))/6); pair Cp = ((3 - sqrt(3))/6, 0); pair Dp = ((3 - sqrt(3))/6, (3 - sqrt(3))/6); pair[] dots = {A, B, C, D, Ep, F, Ap, Cp, Dp}; draw(A--B--C--D--cycle); draw(A--F--Ep--cycle); draw(Ap--B--Cp--Dp--cycle); dot(dots); label("$A$", A, NW); label("$B$", B, SW); label("$C$", C, SE); label("$D$", D, NE); label("$E$", Ep, SE); label("$F$", F, E); label("$A'$", Ap, W); label("$C'$", Cp, SW); label("$D'$", Dp, E); label("$s$", Ap--B, W); label("$1$", A--D, N); [/asy] Call the vertices of the new square A', B', C', and D', in relation to the vertices of $ABCD$ , and define $s$ to be one of the sides of that square. Since the sides are parallel , by corresponding angles and AA~ we know that triangles $AA'D'$ and $D'C'E$ are similar. Thus, the sides are proportional: $\frac{AA'}{A'D'} = \frac{D'C'}{C'E} \Longrightarrow \frac{1 - s}{s} = \frac{s}{1 - s - CE}$ . Simplifying, we get that $s^2 = (1 - s)(1 - s - CE)$ .
$\angle EAF$ is $60$ degrees, so $\angle BAE = \frac{90 - 60}{2} = 15$ . Thus, $\cos 15 = \cos (45 - 30) = \frac{\sqrt{6} + \sqrt{2}}{4} = \frac{1}{AE}$ , so $AE = \frac{4}{\sqrt{6} + \sqrt{2}} \cdot \frac{\sqrt{6} - \sqrt{2}}{\sqrt{6} - \sqrt{2}} = \sqrt{6} - \sqrt{2}$ . Since $\triangle AEF$ is equilateral , $EF = AE = \sqrt{6} - \sqrt{2}$ . $\triangle CEF$ is a $45-45-90 \triangle$ , so $CE = \frac{AE}{\sqrt{2}} = \sqrt{3} - 1$ . Substituting back into the equation from the beginning, we get $s^2 = (1 - s)(2 - \sqrt{3} - s)$ , so $(3 - \sqrt{3})s = 2 - \sqrt{3}$ . Therefore, $s = \frac{2 - \sqrt{3}}{3 - \sqrt{3}} \cdot \frac{3 + \sqrt{3}}{3 + \sqrt{3}} = \frac{3 - \sqrt{3}}{6}$ , and $a + b + c = 3 + 3 + 6 = \boxed{12}$ .
Here's an alternative geometric way to calculate $AE$ (as opposed to trigonometric ): The diagonal $\overline{AC}$ is made of the altitude of the equilateral triangle and the altitude of the $45-45-90 \triangle$ . The former is $\frac{AE\sqrt{3}}{2}$ , and the latter is $\frac{AE}{2}$ ; thus $\frac{AE\sqrt{3} + AE}{2} = AC = \sqrt{2} \Longrightarrow AE= \sqrt{6}-\sqrt{2}$ . The solution continues as above.

## Solution 2
Since $\triangle AFE$ is equilateral, $\overline{AE} = \overline{AF}$ . It follows that $\overline{FC} = \overline{EC}$ . Let $\overline{FC} = x$ . Then, $\overline{EF} = x\sqrt{2}$ and $\overline{DF} = 1-x$ .
$\overline{AF} = \sqrt{1+(1-x)^2} = x\sqrt{2}$ .
Square both sides and combine/move terms to get $x^2+2x-2 = 0$ . Therefore $x = -1 + \sqrt{3}$ and $x = -1 - \sqrt{3}$ . The second solution is obviously extraneous, so $x = -1 + \sqrt{3}$ .
Now, consider the square ABCD to be on the Cartesian Coordinate Plane with $A = (0,0)$ . Then, the line containing $\overline{AF}$ has slope $\frac{1}{2-\sqrt{3}}$ and equation $y = \frac{1}{2-\sqrt{3}}x$ .
The distance from $\overline{DC}$ to $\overline{AF}$ is the distance from $y = 1$ to $y = \frac{1}{2-\sqrt{3}}x$ .
Similarly, the distance from $\overline{AD}$ to $\overline{AF}$ is the distance from $x = 0$ to $y = \frac{1}{2-\sqrt{3}}x$ .
For some value $x = s$ , these two distances are equal.
$(s-0) = (1 - (\frac{1}{2-\sqrt{3}})s)$
Solving for s, $s = \frac{3 - \sqrt{3}}{6}$ , and $a + b + c = 3 + 3 + 6 = 12$ .

## Solution 3
Suppose $\overline{AB} = \overline{AD} = x.$ Note that $\angle EAF = 60$ since the triangle is equilateral, and by symmetry, $\angle BAE = \angle DAF = 15.$ Note that if $\overline{AD} = x$ and $\angle BAE = 15$ , then $\overline{AA'}=\frac{x}{\tan(15)}.$ Also note that \[AB = 1 = \overline{AA'} + \overline{A'B} = \frac{x}{\tan(15)} + x\] Using the fact $\tan(15) = 2-\sqrt{3}$ , this yields \[x = \frac{1}{3+\sqrt{3}} = \frac{3-\sqrt{3}}{6} \rightarrow 3 + 3 + 6 = \boxed{12}\]

## Elegant Solution
Why not solve in terms of the side $x$ only (single-variable beauty)? By similar triangles we obtain that $BE=\frac{x}{1-x}$ , therefore $CE=\frac{1-2x}{1-x}$ . Then $AE=\sqrt{2}*\frac{1-2x}{1-x}$ . Using Pythagorean Theorem on $\triangle{ABE}$ yields $\frac{x^2}{(1-x)^2} + 1 = 2 * \frac{(1-2x)^2}{(1-x)^2}$ . This means $6x^2-6x+1=0$ , and it's clear we take the smaller root: $x=\frac{3-\sqrt{3}}{6}$ . Answer: $\boxed{12}$ .

## Solution 5 (First part is similar to Solution 2)
Since $AEF$ is equilateral, $AE=EF$ . Let $BE=x$ . By the Pythagorean theorem , $1+x^2=2(1-x)^2$ . Simplifying, we get $x^2-4x+1=0$ . By the quadratic formula, the roots are $2 \pm \sqrt{3}$ . Since $x<1$ , we discard the root with the "+", giving $x=2-\sqrt{3}$ . [asy] real n; n=0.26794919243; real m; m=0.2113248654; draw((0,0)--(0,n)--(1,0)--(0,0)); draw((0,m)--(m,m)--(m,0)); label((0,0), "$B$",SW); label((0,n), "$E$",SW); label((0,m), "$M$",SW); label((1,0), "$A$",SW); label((m,0), "$N$",SW); label((m,m), "$K$",NE); [/asy] Let the side length of the square be s. Since $MEK$ is similar to $ABE$ , $s=\frac{2-\sqrt{3}-s}{2-\sqrt{3}}$ . Solving, we get $s=\frac{3-\sqrt{3}}{6}$ and the final answer is $\boxed{012}$ .
These problems are copyrighted © by the Mathematical Association of America.
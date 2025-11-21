# 2009 AIME I Problem 2

## Problem

There is a complex number $z$ with imaginary part $164$ and a positive integer $n$ such that

\[\frac {z}{z + n} = 4i.\]

Find $n$ .

## Solution 1
Let $z = a + 164i$ .
Then \[\frac {a + 164i}{a + 164i + n} = 4i\] and \[a + 164i = \left (4i \right ) \left (a + n + 164i \right ) = 4i \left (a + n \right ) - 656.\]
By comparing coefficients, equating the real terms on the leftmost and rightmost side of the equation,
we conclude that \[a = -656.\]
By equating the imaginary terms on each side of the equation,
we conclude that \[164i = 4i \left (a + n \right ) = 4i \left (-656 + n \right ).\]
We now have an equation for $n$ : \[4i \left (-656 + n \right ) = 164i,\]
and this equation shows that $n = \boxed{697}.$

## Solution 2
\[\frac {z}{z+n}=4i\]
\[1-\frac {n}{z+n}=4i\]
\[1-4i=\frac {n}{z+n}\]
\[\frac {1}{1-4i}=\frac {z+n}{n}\]
\[\frac {1+4i}{17}=\frac {z}{n}+1\]
Since their imaginary part has to be equal,
\[\frac {4i}{17}=\frac {164i}{n}\]
\[n=\frac {(164)(17)}{4}=697\]
\[n = \boxed{697}.\]

## Solution 3 (Not Highly Recommended)
Below is an image of the complex plane. Let $\operatorname{Im}(z)$ denote the imaginary part of a complex number $z$ . [asy] unitsize(1cm); xaxis("Re",Arrows); yaxis("Im",Arrows); real f(real x) {return 164;} pair F(real x) {return (x,f(x));} draw(graph(f,-700,100),red,Arrows); label("Im$(z)=164$",F(-330),N); pair z = (-656,164); dot(Label("$z$",align=N),z); dot(Label("$z+n$",align=N),z+(697,0)); draw(Label("$4x$"),z--(0,0)); draw(Label("$x$"),(0,0)--z+(697,0)); markscalefactor=2; draw(rightanglemark(z,(0,0),z+(697,0))); [/asy] $z$ must lie on the line $\operatorname{Im}(z)=164$ . $z+n$ must also lie on the same line, since $n$ is real and does not affect the imaginary part of $z$ .
Consider $z$ and $z+n$ in terms of their magnitude (distance from the origin) and phase (angle formed by the point, the origin, and the positive real axis, measured counterclockwise from said axis). When multiplying/dividing two complex numbers, you can multiply/divide their magnitudes and add/subtract their phases to get the magnitude and phase of the product/quotient. Expressed in a formula, we have $z_1z_2 = r_1\angle\theta_1 \cdot r_2\angle\theta_2 = r_1r_2\angle(\theta_1+\theta_2)$ and $\frac{z_1}{z_2} = \frac{r_1\angle\theta_1}{r_2\angle\theta_2} = \frac{r_1}{r_2}\angle(\theta_1-\theta_2)$ , where $r$ is the magnitude and $\theta$ is the phase, and $z_n=r_n\angle\theta_n$ .
Since $4i$ has magnitude $4$ and phase $90^\circ$ (since the positive imaginary axis points in a direction $90^\circ$ counterclockwise from the positive real axis), $z$ must have a magnitude $4$ times that of $z+n$ . We denote the length from the origin to $z+n$ with the value $x$ and the length from the origin to $z$ with the value $4x$ . Additionally, $z$ , the origin, and $z+n$ must form a right angle, with $z$ counterclockwise from $z+n$ .
This means that $z$ , the origin, and $z+n$ form a right triangle. The hypotenuse is the length from $z$ to $z+n$ and has length $n$ , since $n$ is defined to be a positive integer. The area of the triangle can be expressed using the two legs, as $\frac{x \cdot 4x}{2}$ , or using the hypotenuse and its corresponding altitude, as $\frac{164n}{2}$ , so $\frac{x \cdot 4x}{2} = \frac{164n}{2} \implies x^2 = 41n$ . By Pythagorean Theorem, $x^2+(4x)^2 = n^2 \implies 17x^2 = n^2$ . Substituting out $x^2$ using the earlier equation, we get $17\cdot41n = n^2 \implies n = \boxed{697}$ . ~ emerald_block

## Solution 4 (fast)
Taking the reciprocal of our equation gives us $1 + \frac{n}{z} = \frac{1}{4i}.$ Therefore, \[\frac{n}{z} = \frac{1-4i}{4i} = \frac{17}{-16+4i}.\] Since $z$ has an imaginary part of $164$ , we must multiply both sides of our RHS fraction by $\frac{164}{4} = 41$ so that its denominator's imaginary part matches the LHS fraction's denominator's imaginary part. That looks like this: \[\frac{n}{z} = \frac{697}{-656 + 164i}.\] Therefore, we can conclude the real part of $z$ is $-656$ and $n = \boxed{697}.$ (it wasn't necessary to find the real part)
~Maximilian113

## Video Solution
https://youtu.be/NL79UexadzE
~IceMatrix

## Video Solution
https://www.youtube.com/watch?v=P00iOJdQiL4
~Shreyas S
These problems are copyrighted © by the Mathematical Association of America.
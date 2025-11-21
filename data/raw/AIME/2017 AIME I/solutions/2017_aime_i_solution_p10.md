# 2017 AIME I Problem 10

## Problem

Let $z_1=18+83i,~z_2=18+39i,$ and $z_3=78+99i,$ where $i=\sqrt{-1}.$ Let $z$ be the unique complex number with the properties that $\frac{z_3-z_1}{z_2-z_1}~\cdot~\frac{z-z_2}{z-z_3}$ is a real number and the imaginary part of $z$ is the greatest possible. Find the real part of $z$ .

## Solution 1 (Coordinates, Geometry)
This problem is pretty obvious how to bash, and indeed many of the solutions below explain how to do that. But there’s no fun in that, and let’s see if we can come up with a slicker solution that will be more enjoyable.
Instead of thinking of complex numbers as purely a real plus a constant times $i$ , let’s graph them and hope that the geometric visualization adds insight to the problem.
[asy] size(1200,300); real xMin = 0; real xMax = 100; real yMin = 0; real yMax = 120; draw((xMin,0)--(xMax,0),black+linewidth(1.5),EndArrow(5)); draw((0,yMin)--(0,yMax),black+linewidth(1.5),EndArrow(5)); label("$R$",(xMax,0),(2,0)); label("$Im$",(0,yMax),(0,2)); pair A,B,C,D; A = (18,83); B = (18,39); C = (78,99); D = (56, 104.908997); dot(A); dot(B); dot(C); dot(D); label("$Z_1$", A, N); label("$Z_2$", B, S); label("$Z_3$", C, N); label("$Z$", D, N); [/asy]
Note that when we subtract two vectors, the geometric result is the line segment between the two endpoints of the vectors. Thus we can fill in $z_3 - z_1, z_2 - z_1, z-z_2$ and $z-z_3$ as so;
[asy] size(1200,300); real xMin = 0; real xMax = 100; real yMin = 0; real yMax = 120; draw((xMin,0)--(xMax,0),black+linewidth(1.5),EndArrow(5)); draw((0,yMin)--(0,yMax),black+linewidth(1.5),EndArrow(5)); label("$R$",(xMax,0),(2,0)); label("$Im$",(0,yMax),(0,2)); pair A,B,C,D; A = (18,83); B = (18,39); C = (78,99); D = (56, 104.908997); dot(A); dot(B); dot(C); dot(D); draw(A--C); draw(A--B); draw(D--C); draw(D--B); label("$Z_1$", A, N); label("$Z_2$", B, S); label("$Z_3$", C, N); label("$Z$", D, N); [/asy]
$\angle Z_3Z_1Z_2$ looks similar to $\angle Z_3ZZ_2$ , so let’s try to prove that they are congruent. We can show this in two ways;

## Solution 1.1
Let’s look back at the information given to us. The problem states that $\frac{z_3-z_1}{z_2-z_1}~\cdot~\frac{z-z_2}{z-z_3}$ is a real number. Let the real number be some constant, $c$ . Rearranging yields $\frac{z_3-z_1}{z_2-z_1} = c~\cdot~\frac{z-z_3}{z-z_2}$ . But how do we relate this expression to our angles? Well, let’s take a look at the divisions themselves.
The subtraction of two vectors yields a vector, and we can write any vector division as $\frac{V_1}{V_2}= X$ where $X$ is a complex number, as the division of two vectors also yields a vector. We can rewrite this as $V_1 = V_2 \cdot X$ . We can think of this expression as transforming $V_2$ directly on to $V_1$ , and $X$ is the transformation function. However, this transformation must be some kind of rotation, which means that the degree measure of $X$ is equal to the angle between the two vectors since we need to rotate by that angle to lay $V_2$ flat on $V_1$ .
Thus we can rewrite our previous equation as $X_1 = c \cdot X_2$ , where the angle of $X_1$ equals the angle between $z_3-z_1$ and $z_2-z_1$ and likewise for $X_2$ . More precisely, we can write $X_1, X_2$ as $r_1 \cdot e^{i \theta_1}$ and $r_2 \cdot e^{i\theta_2}$ , respectively by Euler’s formula. Then $\theta_1= \theta_2$ is the claim we wish to prove.
We can now do some simple algebra to prove this;
$r_1 \cdot e^{i \theta_1} = c \cdot r_2 \cdot e^{i\theta_2} \implies \frac{c \cdot r_2}{r_1} = e^{i(\theta_1-\theta_2)} = \cos{(\theta_1-\theta_2)} + i \cdot \sin{(\theta_1-\theta_2)}$
$\frac{c \cdot r_2}{r_1}$ is obviously real, so $\cos{(\theta_1-\theta_2)} + i \cdot \sin{(\theta_1-\theta_2)}$ must be real as well. But the only way that can happen is if $\sin{(\theta_1-\theta_2)} = 0 \implies \theta_1-\theta_2 = 0 \implies \boxed{\theta_1 = \theta_2}$ .
Food For Thought: Let a, b, c, and d be pairwise distinct complex numbers. Then, a, b, c, and d are concyclic if and only if d-b/d-a : c-b/c-a is a real number. How can we use the above theorem to prove this?

## Solution 1.2
Let us write $\frac{z_3 - z_1}{z_2 - z_1}$ as some complex number with form $r_1 (\cos \theta_1 + i \sin \theta_1).$ Similarly, we can write $\frac{z-z_2}{z-z_3}$ as some $r_2 (\cos \theta_2 + i \sin \theta_2).$
The product must be real, so we have that $r_1 r_2 (\cos \theta_1 + i \sin \theta_1) (\cos \theta_2 + i \sin \theta_2)$ is real. $r_1 r_2$ is real by definition, so dividing the real number above by $r_1 r_2$ will still yield a real number. (Note that we can see that $r_1 r_2 \not= 0$ from the definitions of $z_1,$ $z_2,$ and $z_3$ ). Thus we have
\[(\cos \theta_1 + i \sin \theta_1) (\cos \theta_2 + i \sin \theta_2) = \cos \theta_1 \cos \theta_2 - \sin \theta_1 \sin \theta_2 + i(\cos \theta_1 \sin \theta_2 + \cos \theta_2 \sin \theta_1)\]
is real. The imaginary part of this is $(\cos \theta_1 \sin \theta_2 + \cos \theta_2 \sin \theta_1),$ which we recognize as $\sin(\theta_1 + \theta_2).$ This is only $0$ when $\theta_1 + \theta_2 = k\pi$ for some integer $k$ . Here $\theta_2$ represents the major angle $\angle Z_3ZZ_2$ , and the angle we want is the minor angle, so we can rewrite the equation as $\theta_1 + 2\pi - \theta_2 = k\pi \implies \theta_1 - \theta_2 = (k-2)\pi$ . We can see from the diagram that both $\theta_1$ and $\theta_2$ are obtuse, so therefore $\theta_1 - \theta_2 = 0 \implies \boxed{\theta_1 = \theta_2}$ .

## Solution 1 Rejoined
Now that we’ve proven this fact, we know that all four points lie on a circle (intuitively one can also observe this because $z=z_1$ and $z=z_2$ satisfy the property in the question, and $z=z_3$ techincally gives no imaginary part), so let’s draw that in;
[asy] size(1200,300); real xMin = 0; real xMax = 100; real yMin = 0; real yMax = 120; draw((xMin,0)--(xMax,0),black+linewidth(1.5),EndArrow(5)); draw((0,yMin)--(0,yMax),black+linewidth(1.5),EndArrow(5)); label("$R$",(xMax,0),(2,0)); label("$Im$",(0,yMax),(0,2)); pair A,B,C,D; A = (18,83); B = (18,39); C = (78,99); D = (56,104.908997); dot(A); dot(B); dot(C); dot(D); draw(A--C); draw(A--B); draw(D--C); draw(C--B); draw(D--B); label("$Z_1$", A, W); label("$Z_2$", B, W); label("$Z_3$", C, N); label("$Z$", D, N); draw(circle((56,61), 43.9089968)); [/asy]
While $Z_1, Z_2, Z_3$ are fixed, $Z$ can be anywhere on the circle because those are the only values of $Z$ that satisfy the problem requirements. However, we want to find the real part of the $Z$ with the maximum imaginary part. This Z would lie directly above the center of the circle, and thus the real part would be the same as the x-value of the center of the circle. So all we have to do is find this value and we’re done.
Consider the perpendicular bisectors of $Z_1Z_2$ and $Z_2Z_3$ . Since any chord can be perpendicularly bisected by a radius of a circle, these two lines both intersect at the center. Since $Z_1Z_2$ is vertical, the perpendicular bisector will be horizontal and pass through the midpoint of this line, which is (18, 61). Therefore the equation for this line is $y=61$ . $Z_2Z_3$ is nice because it turns out the differences in the x and y values are both equal (60) which means that the slope of the line is 1. The slope of the perpendicular bisector is therefore -1 and it passes through the midpoint, (48,69), so the equation of this line is $y=-x+117$ . Finally, equating the two yields \[61=-x+117 \implies x = \boxed{056}\]
~KingRavi
~Anonymous(Solution 1.2)

## Bashy Solution :)
We know that \[z_3-z_1 = (78+99i)-(18+83i) = 60 + 16i.\] \[z_2-z_1=(18+39i)-(18+83i) = -44i.\] Hence, \[\frac{z_3-z_1}{z_2-z_1} = \frac{60 + 16i}{-44i} = \frac{15i-4}{11} = \frac{c}{15i+4}\] where $c \in R$ . Let $z = a+bi$ . Then, \[\frac{z-z_2}{z-z_3} = \frac{(a+bi)-(18+39i)}{(a+bi)-(78+99i)} =\] \[\frac{z-z_2}{z-z_3} = \frac{(a-18)+i(b-39)}{(a-78)+i(b-99)} =\] \[\frac{z-z_2}{z-z_3} = \frac{((a-18)+i(b-39)((a-78)+i(99-b))}{((a-78)+i(b-99))((a-78)+i(99-b)} =\] \[\frac{z-z_2}{z-z_3} = \frac{((a-18)+i(b-39)((a-78)+i(99-b))}{k}\] The numerator is: \[(a-18)(a-78)-(b-39)(99-b)+i((b-39)(a-78) + (99-b)(a-18))=\] \[a^2+b^2-96a-138b+18 \cdot 78 + 39 \cdot 99 + i(60a - 60b + 39 \cdot 78 + 18 \cdot 99)\] The ratio of the imaginary part to the real part must be $\frac{15}{4}$ because $\frac{z_3-z_1}{z_2-z_1} = \frac{c}{15i+4}.$ Hence, \[\frac{60a - 60b + 39 \cdot 78 - 18 \cdot 99}{a^2+b^2-96a-138b+18 \cdot 78 + 39 \cdot 99} = \frac{15}{4} \implies\] \[\frac{4a-4b+84}{a^2+b^2-96a-138b+9(2 \cdot 78 + 39 \cdot 11)} = \frac{1}{4} \implies\] \[16a - 16b + 336 = a^2 + b^2 -96a - 138b +5265 \implies\] \[0 = a^2 + b^2 -112a-122b+4929.\] Evidently, $b$ is maximized when $112a-a^2$ is maximized or when $a = \boxed{056}.$
~AopsUser101
fixed a single wrong digit - ethanhansummerfun

## Solution 3
Algebra Bash
First we calculate $\frac{z_3 - z_1}{z_2 - z_1}$ , which becomes $\frac{15i-4}{11}$ .
Next, we define $z$ to be $a+bi$ for some real numbers $a$ and $b$ . Then, $\frac {z-z_2}{z-z_3}$ can be written as $\frac{(a-18)+(b-39)i}{(a-78)+(b-99)i}.$ Multiplying both the numerator and denominator by the conjugate of the denominator, we get:
$\frac {[(a-18)(a-78)+(b-39)(b-99)]+[(a-78)(b-39)-(a-18)(b-99)]i}{(a-78)^2+(b-99)^2}$
In order for the product to be a real number, since both denominators are real numbers, we must have the numerator of $\frac {z-z_2}{z-z_3}$ be a multiple of the conjugate of $15i-4$ , namely $-15i-4$ So, we have $(a-18)(a-78)+(b-39)(b-99) = -4k$ and $(a-78)(b-39)-(a-18)(b-99) = -15k$ for some real number $k$ .
Then, we get: $(a-18)(a-78)+(b-39)(b-99) = \frac{4}{15}[(a-78)(b-39)-(a-18)(b-99)]$
Expanding both sides and combining like terms, we get:
$a^2 - 112a +b^2 - 122b + 4929 = 0$
which can be rewritten as:
$(a-56)^2 + (b-61)^2 = 1928$
Now, common sense tells us that to maximize $b$ , we would need to maximize $(b-61)^2$ . Therefore, we must set $(a-56)^2$ to its lowest value, namely 0. Therefore, $a$ must be $\boxed{056}.$
You can also notice that the ab terms cancel out so all you need is the x-coordinate of the center and only expand the a parts of the equation.
~stronto

## Solution 4 (algebra but much cleaner)
We see that $\frac{z_3-z_1}{z_2-z_1}=\frac{60+16i}{-44i}=\frac{15i-4}{11}$ .
Now, let $z-z_3=a+bi$ , in which case $z=(a+78)+(b+99)i$ and $z-z_2=(a+60)+(b+60)i$ .
We now have that $\left(\frac{(a+60)+(b+60)i}{a+bi}\right)\left(\frac{15i-4}{11}\right)$ is real, meaning that: \[((a+60)+(b+60)i)\left(\frac{15i-4}{a+bi}\right)\] is also real.
We see that: \[\frac{15i-4}{a+bi}=\frac{(15i-4)(a-bi)}{a^2+b^2}=\frac{(15b-4a)+(15a+4b)i}{a^2+b^2},\] so therefore, $x=((a+60)+(b+60)i)((15b-4a)+(15a+4b)i)$ is real.
This means that $Im(x)=0$ , so we now have that: \[(a+60)(15a+4b)+(b+60)(15b-4a)=15a^2+15b^2+660a+1140b=0 \Rightarrow a^2+b^2+44a+76b=0.\]
This can be rewritten as: \[(a+22)^2+(b+38)^2=22^2+38^2.\] In order to maximize $Im(z)$ we want to maximize $b$ , and in order to maximize $b$ we want $a+22=0$ and $a=-22$ , so $Re(z)=a+78=-22+78=\boxed{056}$ . (Note: $Im(\omega)$ is the imaginary part of $\omega$ , and $Re(\omega)$ is the real part of $\omega$ ) ~Stormersyle

## Solution 5
We will just bash. Let $z=a+bi$ where $a,b\in\mathbb{R}$ . We see that $\frac{z_3-z_1}{z_2-z_1}=\frac{-4+15i}{11}$ after doing some calculations. We also see that $\frac{[(a-18)+(b-39)i][(a-78)-(b-99)i]}{\text{some real stuff}}.$ We note that $[(a-18)+(b-39)i][(a-78)-(b-99)i]$ is a multiple of $-4-15i$ because the numerator has to be real. Thus, expanding it out, we see that $(a-18)(a-78)+(b-39)(b-99)=-4k \\ (a-78)(b-39)-(a-18)(b-99)=-15k.$ Hence, $(a-18)(a-78)+(b-39)(b-99)=\frac{4}{15}[(a-78)(b-39)-(a-18)(b-99)] \implies a^2-96a+b^2-138b+5265=16a-16b+336 \\ (a-56)^2+(b-61)^2=1928.$ To maximize the imaginary part, $(a-56)^2$ must equal $0$ so hence, $a=\boxed{056}$ .

## Solution 6 (Euclidean geometry and coordinates)
If you've read Evan Chen's book EGMO (Euclidean Geometry in Mathematical Olympiads), you know that $\frac{z_3-z_1}{z_2-z_1}~\cdot~\frac{z-z_2}{z-z_3}$ is a real number is just a fancy way of saying that $z, z_1, z_2, z_3$ are points on a cyclic quadrilateral. The proof of this can be found in EGMO or other sources, and this is the key to the problem.
And the three given points already define the circle that circumscribes that cyclic quadrilateral. So all we need to do is get the equation for that circle in the Cartesian plane, and then maximize the y-coordinate of $z$ .
To find the center of the circumcircle, find the intersection of the perpendicular bisectors. One of them is just $y=61$ , and the second is $y=-x+117$ . So we have the point (56, 61) as the center of the circle. The distance from this point to all three points is $\sqrt{22^2+38^2}$ . The square of the radius of this circle is $22^2+38^2=1928$ . So the equation for the circle is $(x-56)^2+(y-61)^2=1928$ . To maximize the y-coordinate, which does not have to be a positive integer, but $x$ does (per AIME rules given it's the answer), by the trivial inequality $(x-56)^2 \geq 0$ , so $\boxed{056}$ is the answer.
~First

## Video Solution
2017 AIME I #10
MathProblemSolvingSkills.com
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
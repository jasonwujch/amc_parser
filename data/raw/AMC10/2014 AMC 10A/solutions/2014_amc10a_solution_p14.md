# 2014 AMC 10A Problem 14

## Problem

The $y$ -intercepts, $P$ and $Q$ , of two perpendicular lines intersecting at the point $A(6,8)$ have a sum of zero. What is the area of $\triangle APQ$ ?

$\textbf{(A)}\ 45\qquad\textbf{(B)}\ 48\qquad\textbf{(C)}\ 54\qquad\textbf{(D)}\ 60\qquad\textbf{(E)}\ 72$

## Solution 1
[asy]//Needs refining (hmm I think it's fine --bestwillcui1) size(12cm); fill((0,10)--(6,8)--(0,-10)--cycle,rgb(.7,.7,.7)); for(int i=-2;i<=8;i+=1) draw((i,-12)--(i,12),grey); for(int j=-12;j<=12;j+=1) draw((-2,j)--(8,j),grey); draw((-3,0)--(9,0),linewidth(1),Arrows); //x-axis draw((0,-13)--(0,13),linewidth(1),Arrows); //y-axis dot((0,0)); dot((6,8)); draw((-2,10.66667)--(8,7.33333),Arrows); draw((7.33333,12)--(-0.66667,-12),Arrows); draw((6,8)--(0,8)); draw((6,8)--(0,0)); draw(rightanglemark((0,10),(6,8),(0,-10),20)); label("$A$",(6,8),NE); label("$a$", (0,5),W); label("$a$",(0,-5),W); label("$a$",(3,4),NW); label("$P$",(0,10),SW); label("$Q$",(0,-10),NW); // wanted to import graph and use xaxis/yaxis but w/e label("$x$",(9,0),E); label("$y$",(0,13),N); [/asy] Note that if the $y$ -intercepts have a sum of $0$ , the distance from the origin to each of the intercepts must be the same. Call this distance $a$ . Since the $\angle PAQ = 90^\circ$ , the length of the median to the midpoint of the hypotenuse is equal to half the length of the hypotenuse. Since the median's length is $\sqrt{6^2+8^2} = 10$ , this means $a=10$ , and the length of the hypotenuse is $2a = 20$ . Since the $x$ -coordinate of $A$ is the same as the altitude to the hypotenuse, $[APQ] = \dfrac{20 \cdot 6}{2} = \boxed{\textbf{(D)} \: 60}$ . ( https://math.stackexchange.com/questions/2098721/a-property-of-the-midpoint-of-the-hypotenuse-in-a-right-triangle )

## Solution 2
We can let the two lines be \[y=mx+b\] \[y=-\frac{1}{m}x-b\] This is because the lines are perpendicular, hence the $m$ and $-\frac{1}{m}$ , and the sum of the y-intercepts is equal to 0, hence the $b, -b$ .
Since both lines contain the point $(6,8)$ , we can plug this into the two equations to obtain \[8=6m+b\] and \[8=-6\frac{1}{m}-b\]
Adding the two equations gives \[16=6m+\frac{-6}{m}\] Multiplying by $m$ gives \[16m=6m^2-6\] \[\implies 6m^2-16m-6=0\] \[\implies 3m^2-8m-3=0\] Factoring gives \[(3m+1)(m-3)=0\]
Plugging $m=3$ into one of our original equations, we obtain \[8=6(3)+b\] \[\implies b=8-6(3)=-10\]
Since $\bigtriangleup APQ$ has hypotenuse $2|b|=20$ and the altitude to the hypotenuse is equal to the the x-coordinate of point $A$ , or 6, the area of $\bigtriangleup APQ$ is equal to \[\frac{20\cdot6}{2}=\boxed{\textbf{(D)}\ 60}\]

## Solution 3
Like Solution 2 but solving directly for intercepts (b):
1. Solve for m using: $8=6m+b$
\[m=\frac{8-b}{6}\]
2. Substitute into the other equation:
\[8=-6\cdot(\frac{1}{\frac{8-b}{6}})-b\]
Flip the inverse:
\[8=-6\cdot(\frac{6}{8-b})-b\]
Multiply $6$ 's:
\[8=-(\frac{36}{8-b})-b\]
3. Multiply through by $8-b$ (Watch distributing minus!)
\[64-8b=-36-8b+b^2\]
4. Add $36$ to both sides, and cancel $-8b$ by adding to both sides:
\[100=b^2\]
$b=10$ (or $-10$ )
The rest is as above.

## Solution 4(Heron's Formula)
Since their sum is $0$ , let the y intercepts be P $(0,a)$ and Q $(0,-a)$ . The slope of $AP$ is $\frac{8-a}{6}$ . The slope of AQ is $\frac{8+a}{6}$ . Since multiplying the slopes of perpendicular lines yields a product of $-1$ , we have $\frac{64-a^2}{36}=-1$ , which results in $a^2=100$ . We can use either the positive or negative solution because if we choose $10$ , then the other y-intercept is $-10$ ; but if we choose $-10$ , then the other y-intercept is $10$ . For simplicity, we choose that $a=10$ in this solution.
Now we have a triangle APQ with points A $(6,8)$ , P $(0,10)$ , and Q $(0,-10)$ . By the Pythagorean theorem, we have that $AP=\sqrt{6^2+2^2}=2\sqrt{10}$ , and that $AQ=\sqrt{6^2+18^2}=6\sqrt{10}$ . $PQ$ is obviously $10-(-10)=20$ since they have the same $x$ coordinate. Now using Heron's formula, we have $\sqrt{s(s-a)(s-b)(s-c)}=\sqrt{(4\sqrt{10}+10)(4\sqrt{10}-10)(10+2\sqrt{10})(10-2\sqrt{10})}=\sqrt{60^2}=60 \implies \boxed{D}$ .
~smartninja2000

## Solution 5 (point-slope)
Using point-slope form, the first line has the equation \[y-8=m\left(x-6\right) \longrightarrow y=mx-6m+8\] The second line has the equation \[y-8=-\frac{1}{m}\left(x-6\right) \longrightarrow y=-\frac{x}{m}+\frac{6}{m}+8\] At the y-intercept, the value of the x-coordinate is $0$ , hence: the first equation is $y=-6m+8$ and the second is $y=\frac{6}{m}+8$ . Since the y-intercepts sum to $0$ , they are opposites, so: \[-6m+8=-\left(\frac{6}{m}+8\right)=-\frac{6}{m}-8\] \[6m-\frac{6}{m}=16\] Multiply both sides by m: $6m^{2}-6=16m \longrightarrow 3m^{2}-8m-3=0$ . The solution to this quadratic, using the quadratic formula, is: $\frac{8\pm\sqrt{64-4\left(3\right)\left(-3\right)}}{6}=\frac{8\pm\sqrt{100}}{6}=\frac{8\pm10}{6}$ This yields $m=-\frac{1}{3}$ and $m=3$ . Plugging $m=3$ into the second equation, we get $y=\frac{6}{3}+8=10$ . Plugging $m=-\frac{1}{3}$ into the first equation, we get $y=-10$ So the base is $20$ and the height is $6$ , the area is $60 \Longrightarrow \boxed{\textbf{(D) } 60}$ .
~JH. L

## Solution 6 (Geometry only)
(Not to scale) [asy] unitsize(36); pair A = (0,0); pair B = (5,1); pair C = (13/5,13); pair D = C-B; pair E = (26/5,0); pair F = (0,26); pair G = intersectionpoints(C--D,A--F)[0]; draw(A--E--F--A--B--C--D--A,linewidth(1)); label(A,scale(2)*"A",dir(-135)); label(E,scale(2)*"E",dir(-45)); label(F,scale(2)*"F",dir(90)); label(B,scale(2)*"B",dir(45)); label(C,scale(2)*"C",dir(45)); label(D,scale(2)*"D",dir(180)); label(G,scale(2)*"G",dir(135)); [/asy] Long solution: By rotating the right triangle, we get the figure shown where \[CD\perp EF\] and CE=CF. We know AB=CD=6 and AD=BC=8. By the pythagorean theorem, we have AC=10, and since C is the midpoint of EF, CE=EF=10 also. By similar triangles, \[\frac{AD}{FC}=\frac{DG}{CG}~\text{so}~DG=\frac{8}{3}~\text{and}~CG=\frac{10}{3}\] Then, by more similar triangles, \[\frac{CG}{FG}=\frac{EA}{FA}=\frac{1}{3}~\text{so}~AF=3AE\] Then $AE=2\sqrt{10},~AE=6\sqrt{10}$ , and the area is \[\boxed{(D)~60}\] Short solution: By rotating the right triangle, we get the figure shown where \[CD\perp EF\] and CE=CF. We know AB=CD=6 and AD=BC=8. By the pythagorean theorem, we have AC=10, and since C is the midpoint of EF, CE=EF=10 also, so CF=20. \[A=\frac{bh}{2}=\frac{(EF)(AB)}{2}=\frac{(20)(6)}{2}=\frac{120}{2}=\boxed{(\textbf{D})~60}\] Afly ( talk )

## Video Solution
https://www.youtube.com/watch?v=AJdRK51xvos ~Mathematical Dexterity
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .
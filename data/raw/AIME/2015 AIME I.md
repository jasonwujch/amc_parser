Problem 1
The expressions $A$ = $1 \times 2 + 3 \times 4 + 5 \times 6 + \cdots + 37 \times 38 + 39$ and $B$ = $1 + 2 \times 3 + 4 \times 5 + \cdots + 36 \times 37 + 38 \times 39$ are obtained by writing multiplication and addition operators in an alternating pattern between successive integers. Find the positive difference between integers $A$ and $B$ .

Solution

Problem 2
The nine delegates to the Economic Cooperation Conference include $2$ officials from Mexico, $3$ officials from Canada, and $4$ officials from the United States. During the opening session, three of the delegates fall asleep. Assuming that the three sleepers were determined randomly, the probability that exactly two of the sleepers are from the same country is $\frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

Solution

Problem 3
There is a prime number $p$ such that $16p+1$ is the cube of a positive integer. Find $p$ .

Solution

Problem 4
Point $B$ lies on line segment $\overline{AC}$ with $AB=16$ and $BC=4$ . Points $D$ and $E$ lie on the same side of line $AC$ forming equilateral triangles $\triangle ABD$ and $\triangle BCE$ . Let $M$ be the midpoint of $\overline{AE}$ , and $N$ be the midpoint of $\overline{CD}$ . The area of $\triangle BMN$ is $x$ . Find $x^2$ .

Solution

Problem 5
In a drawer Sandy has $5$ pairs of socks, each pair a different color. On Monday, Sandy selects two individual socks at random from the $10$ socks in the drawer. On Tuesday Sandy selects $2$ of the remaining $8$ socks at random, and on Wednesday two of the remaining $6$ socks at random. The probability that Wednesday is the first day Sandy selects matching socks is $\frac{m}{n}$ , where $m$ and $n$ are relatively prime positive integers. Find $m+n$ .

Solution

Problem 6
Point $A,B,C,D,$ and $E$ are equally spaced on a minor arc of a circle. Points $E,F,G,H,I$ and $A$ are equally spaced on a minor arc of a second circle with center $C$ as shown in the figure below. The angle $\angle ABD$ exceeds $\angle AHG$ by $12^\circ$ . Find the degree measure of $\angle BAG$ .
[asy] pair A,B,C,D,E,F,G,H,I,O; O=(0,0); C=dir(90); B=dir(70); A=dir(50); D=dir(110); E=dir(130); draw(arc(O,1,50,130)); real x=2*sin(20*pi/180); F=x*dir(228)+C; G=x*dir(256)+C; H=x*dir(284)+C; I=x*dir(312)+C; draw(arc(C,x,200,340)); label("$A$",A,dir(0)); label("$B$",B,dir(75)); label("$C$",C,dir(90)); label("$D$",D,dir(105)); label("$E$",E,dir(180)); label("$F$",F,dir(225)); label("$G$",G,dir(260)); label("$H$",H,dir(280)); label("$I$",I,dir(315));[/asy]

Solution

Problem 7
In the diagram below, $ABCD$ is a square. Point $E$ is the midpoint of $\overline{AD}$ . Points $F$ and $G$ lie on $\overline{CE}$ , and $H$ and $J$ lie on $\overline{AB}$ and $\overline{BC}$ , respectively, so that $FGHJ$ is a square. Points $K$ and $L$ lie on $\overline{GH}$ , and $M$ and $N$ lie on $\overline{AD}$ and $\overline{AB}$ , respectively, so that $KLMN$ is a square. The area of $KLMN$ is 99. Find the area of $FGHJ$ .
[asy] pair A,B,C,D,E,F,G,H,J,K,L,M,N; B=(0,0); real m=7*sqrt(55)/5; J=(m,0); C=(7*m/2,0); A=(0,7*m/2); D=(7*m/2,7*m/2); E=(A+D)/2; H=(0,2m); N=(0,2m+3*sqrt(55)/2); G=foot(H,E,C); F=foot(J,E,C); draw(A--B--C--D--cycle); draw(C--E); draw(G--H--J--F); pair X=foot(N,E,C); M=extension(N,X,A,D); K=foot(N,H,G); L=foot(M,H,G); draw(K--N--M--L); label("$A$",A,NW); label("$B$",B,SW); label("$C$",C,SE); label("$D$",D,NE); label("$E$",E,dir(90)); label("$F$",F,NE); label("$G$",G,NE); label("$H$",H,W); label("$J$",J,S); label("$K$",K,SE); label("$L$",L,SE); label("$M$",M,dir(90)); label("$N$",N,dir(180)); [/asy]

Solution

Problem 8
For positive integer $n$ , let $s(n)$ denote the sum of the digits of $n$ . Find the smallest positive integer satisfying $s(n) = s(n+864) = 20$ .

Solution

Problem 9
Let $S$ be the set of all ordered triple of integers $(a_1,a_2,a_3)$ with $1 \le a_1,a_2,a_3 \le 10$ . Each ordered triple in $S$ generates a sequence according to the rule $a_n=a_{n-1}\cdot | a_{n-2}-a_{n-3} |$ for all $n\ge 4$ . Find the number of such sequences for which $a_n=0$ for some $n$ .

Solution

Problem 10
Let $f(x)$ be a third-degree polynomial with real coefficients satisfying \[|f(1)|=|f(2)|=|f(3)|=|f(5)|=|f(6)|=|f(7)|=12.\] Find $|f(0)|$ .

Solution

Problem 11
Triangle $ABC$ has positive integer side lengths with $AB=AC$ . Let $I$ be the intersection of the bisectors of $\angle B$ and $\angle C$ . Suppose $BI=8$ . Find the smallest possible perimeter of $\triangle ABC$ .

Solution

Problem 12
Consider all 1000-element subsets of the set $\{ 1, 2, 3, ... , 2015 \}$ . From each such subset choose the least element. The arithmetic mean of all of these least elements is $\frac{p}{q}$ , where $p$ and $q$ are relatively prime positive integers. Find $p + q$ .

Solution

Problem 13
With all angles measured in degrees, the product $\prod_{k=1}^{45} \csc^2(2k-1)^\circ=m^n$ , where $m$ and $n$ are integers greater than 1. Find $m+n$ .

Solution

Problem 14
For each integer $n \ge 2$ , let $A(n)$ be the area of the region in the coordinate plane defined by the inequalities $1\le x \le n$ and $0\le y \le x \left\lfloor \sqrt x \right\rfloor$ , where $\left\lfloor \sqrt x \right\rfloor$ is the greatest integer not exceeding $\sqrt x$ . Find the number of values of $n$ with $2\le n \le 1000$ for which $A(n)$ is an integer.

Solution

Problem 15
A block of wood has the shape of a right circular cylinder with radius $6$ and height $8$ , and its entire surface has been painted blue. Points $A$ and $B$ are chosen on the edge of one of the circular faces of the cylinder so that $\overarc{AB}$ on that face measures $120^\text{o}$ . The block is then sliced in half along the plane that passes through point $A$ , point $B$ , and the center of the cylinder, revealing a flat, unpainted face on each half. The area of one of these unpainted faces is $a\cdot\pi + b\sqrt{c}$ , where $a$ , $b$ , and $c$ are integers and $c$ is not divisible by the square of any prime. Find $a+b+c$ .
[asy] import three; import solids; size(8cm); currentprojection=orthographic(-1,-5,3); picture lpic, rpic; size(lpic,5cm); draw(lpic,surface(revolution((0,0,0),(-3,3*sqrt(3),0)..(0,6,4)..(3,3*sqrt(3),8),Z,0,120)),gray(0.7),nolight); draw(lpic,surface(revolution((0,0,0),(-3*sqrt(3),-3,8)..(-6,0,4)..(-3*sqrt(3),3,0),Z,0,90)),gray(0.7),nolight); draw(lpic,surface((3,3*sqrt(3),8)..(-6,0,8)..(3,-3*sqrt(3),8)--cycle),gray(0.7),nolight); draw(lpic,(3,-3*sqrt(3),8)..(-6,0,8)..(3,3*sqrt(3),8)); draw(lpic,(-3,3*sqrt(3),0)--(-3,-3*sqrt(3),0),dashed); draw(lpic,(3,3*sqrt(3),8)..(0,6,4)..(-3,3*sqrt(3),0)--(-3,3*sqrt(3),0)..(-3*sqrt(3),3,0)..(-6,0,0),dashed); draw(lpic,(3,3*sqrt(3),8)--(3,-3*sqrt(3),8)..(0,-6,4)..(-3,-3*sqrt(3),0)--(-3,-3*sqrt(3),0)..(-3*sqrt(3),-3,0)..(-6,0,0)); draw(lpic,(6*cos(atan(-1/5)+3.14159),6*sin(atan(-1/5)+3.14159),0)--(6*cos(atan(-1/5)+3.14159),6*sin(atan(-1/5)+3.14159),8)); size(rpic,5cm); draw(rpic,surface(revolution((0,0,0),(3,3*sqrt(3),8)..(0,6,4)..(-3,3*sqrt(3),0),Z,230,360)),gray(0.7),nolight); draw(rpic,surface((-3,3*sqrt(3),0)..(6,0,0)..(-3,-3*sqrt(3),0)--cycle),gray(0.7),nolight); draw(rpic,surface((-3,3*sqrt(3),0)..(0,6,4)..(3,3*sqrt(3),8)--(3,3*sqrt(3),8)--(3,-3*sqrt(3),8)--(3,-3*sqrt(3),8)..(0,-6,4)..(-3,-3*sqrt(3),0)--cycle),white,nolight); draw(rpic,(-3,-3*sqrt(3),0)..(-6*cos(atan(-1/5)+3.14159),-6*sin(atan(-1/5)+3.14159),0)..(6,0,0)); draw(rpic,(-6*cos(atan(-1/5)+3.14159),-6*sin(atan(-1/5)+3.14159),0)..(6,0,0)..(-3,3*sqrt(3),0),dashed); draw(rpic,(3,3*sqrt(3),8)--(3,-3*sqrt(3),8)); draw(rpic,(-3,3*sqrt(3),0)..(0,6,4)..(3,3*sqrt(3),8)--(3,3*sqrt(3),8)..(3*sqrt(3),3,8)..(6,0,8)); draw(rpic,(-3,3*sqrt(3),0)--(-3,-3*sqrt(3),0)..(0,-6,4)..(3,-3*sqrt(3),8)--(3,-3*sqrt(3),8)..(3*sqrt(3),-3,8)..(6,0,8)); draw(rpic,(-6*cos(atan(-1/5)+3.14159),-6*sin(atan(-1/5)+3.14159),0)--(-6*cos(atan(-1/5)+3.14159),-6*sin(atan(-1/5)+3.14159),8)); label(rpic,"$A$",(-3,3*sqrt(3),0),W); label(rpic,"$B$",(-3,-3*sqrt(3),0),W); add(lpic.fit(),(0,0)); add(rpic.fit(),(1,0)); [/asy]

Solution
